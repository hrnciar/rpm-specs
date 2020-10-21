Name:		dhcpd-pools
Version:	3.0
Release:	4%{?dist}
Summary:	ISC dhcpd lease analysis and reporting
# BSD: dhcpd-pools
# ASL 2.0: mustache templating (https://gitlab.com/jobol/mustach) src/mustach.[ch]
# GPLv3+: gnulib (https://www.gnu.org/software/gnulib/) lib/
License:	BSD and ASL 2.0 and GPLv3+
URL:		http://dhcpd-pools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:		dhcpd-pools-gnulib.patch

BuildRequires:	uthash-devel
BuildRequires:	gcc, automake, autoconf
%if ! 0%{?el6}
# EPEL 6 doesn't need gnulib update, can just use bundled
BuildRequires:	gnulib-devel
%endif
Provides:	bundled(gnulib)

%description
This is for ISC DHCP shared network and pool range usage analysis.  Purpose
of command is to count usage ratio of each IP range and shared network pool
which ISC dhcpd is in control of. Users of the command are most likely ISPs
and other organizations that have large IP space.

%prep
%setup -q

%if ! 0%{?el6}
# needed to handle gnulib/glibc compatibility
gnulib-tool --update
gnulib-tool --add-import

# handle http://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=commit;h=ba4b91abd5dbe486c71465b0968aa1a4a1198bd7
%patch0 -p1

autoreconf -fiv
%endif

%build
# configure to match OS install defaults
# add -std=c99 for gnulib on EPEL7
%configure \
    CC="%{__cc} -std=c99" \
    --with-dhcpd-conf=%{_sysconfdir}/dhcp/dhcpd.conf \
    --with-dhcpd-leases=%{_localstatedir}/lib/dhcpd/dhcpd.leases

make %{?_smp_mflags}

%install
%make_install
# make install installs docs, let rpmbuild handle it
rm -rf %{buildroot}%{_docdir}/%{name}

# original encoding appears to be ISO8859-1
iconv --from=ISO8859-1 --to=UTF-8 THANKS > THANKS.utf8
touch --reference=THANKS THANKS.utf8
mv THANKS.utf8 THANKS

%files
%license COPYING
%doc README THANKS TODO AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Chris Adams <linux@cmadams.net> - 3.0-3
- correct license tag and include info
- fix gnulib patch, add bundled provide
- convert THANKS character set
- add EPEL 6 support

* Mon Mar 09 2020 Chris Adams <linux@cmadams.net> - 3.0-2
- fix some notes from review request
- add patch for gnulib autoconf
- add -std=c99 for gnulib on EPEL7

* Mon Jan 27 2020 Chris Adams <linux@cmadams.net> - 3.0-1
- initial RPM

