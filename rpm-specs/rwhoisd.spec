# Disable TCP Wrappers connection filter
%bcond_with rwhoisd_enables_tcpwrappers

Name:       rwhoisd 
Version:    1.5.9.6
Release:    18%{?dist}
Summary:    ARIN's Referral WHOIS server
# tools/tcpd_wrapper/DISCLAIMER:    BSD (tcp_wrappers variant)
# tools/tcpd_wrapper/strcasecmp.c:  BSD
# regexp/COPYRIGHT:                 zlib
# mkdb/metaphon.c:                  Public Domain
# mkdb/y.tab.c:                     (GPLv2+ or FSFUL)
# LICENSE:                          GPLv2+
# common/strerror.c:                GPLv2+ (libiberty)
# configure:                        FSFUL
License:    Public Domain and zlib and GPLv2+
URL:        http://projects.arin.net/rwhois/
Source0:    %{url}ftp/%{name}-%{version}.tar.gz
Source1:    %{name}.service
# Install database to /var
Patch0:     %{name}-1.5.9.6-Install-database-to-var.patch
# Fix configure script
Patch1:     %{name}-1.5.9.5-Use-configure-options-instead-of-GCC-test.patch
# Fix configure script
Patch2:     %{name}-1.5.9.5-Use-AC_SYS_LARGEFILE-for-large-file-support-check.patch
# Fix configure script
Patch3:     %{name}-1.5.9.5-Respect-without-local-libwrap.patch
# Use system tcpd.h
Patch4:     %{name}-1.5.9.5-Do-not-include-bundled-tcpd.h.patch
# GNU sort requires new syntax
Patch5:     %{name}-1.5.9.5-Select-which-way-to-call-sort.patch
# Change default configuration
Patch6:     %{name}-1.5.9.5-Adjust-sample-configuration.patch
# Disable TCP wrappers, bug #1518781
Patch7:     %{name}-1.5.9.6-Allow-disabling-TCP-wrappers.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
%if %{with rwhoisd_enables_tcpwrappers}
BuildRequires:  tcp_wrappers-devel
%endif
BuildRequires:  systemd
# cat executed by rwhois_repack
Requires:       %{_bindir}/cat
# sort executed by rwhois_indexer
Requires:       %{_bindir}/sort
Requires(pre):      shadow-utils
%{?systemd_requires}

%description
This server is a reference implementation of the server side of the RWhois
protocol, first described in RFC 1714.  This server attempts to implement
concepts and practices in accordance with version 1.5 of the protocol,
described in RFC 2167.

%package example
License:    GPLv2+
Summary:    Sample data for %{name} WHOIS server
BuildArch:  noarch
Requires:   %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description example
This package delivers example configuration and data for %{name} WHOIS server.
Recommended how-to is <http://www.unixadmin.cc/rwhois/>.


%prep
%setup -q
%patch0 -p1 -b .destdir
%patch1 -p1 -b .config_gcc
%patch2 -p1 -b .config_lfs
%patch3 -p1 -b .config_libwrap
%patch4 -p1 -b .system_tcp
%patch5 -p1 -b .sort
%patch6 -p1 -b .config
%patch7 -p1 -b .tcpwrappers
# Remove bundled tcp_wrappers for sure
find tools/tcpd_wrapper -depth -mindepth 1 \! -name Makefile.in -exec rm {} +
# Keep System V8 regexp library
# TODO: port to GNU glibc
autoreconf

%build
%global _hardened_build 1
%configure \
    --disable-gcc-debug \
    --disable-gprof \
    --enable-ipv6 \
    --enable-largefile \
    --enable-newsort \
    --enable-syslock \
%if %{with rwhoisd_enables_tcpwrappers}
    --enable-tcpwrappers \
%else
    --disable-tcpwrappers \
%endif
    --enable-warnings \
    --without-local-libwrap

# Does not support parallel build
make

%install
make install DESTDIR='%{buildroot}'
install -d '%{buildroot}%{_mandir}/man8'
install -m 0644 -t '%{buildroot}%{_mandir}/man8' doc/*.8
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'
# Default empty configuration
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.conf
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.x.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.root
install -m 0644 -t '%{buildroot}%{_localstatedir}/%{name}/' \
    sample.data/rwhoisd.auth_area
install -d -m 0775 "%{buildroot}%{_localstatedir}/%{name}/register-spool"

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/%{name} -s /sbin/nologin \
    -c "rwhoisd daemon" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%license LICENSE
%doc doc/operations_guide.txt doc/security.txt doc/TODO doc/UPGRADE README
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.dir
%config(noreplace) %{_sysconfdir}/%{name}.x.dir
%config(noreplace) %{_sysconfdir}/%{name}.root
%dir %{_localstatedir}/%{name}
%config(noreplace) %{_localstatedir}/%{name}/%{name}.auth_area
%attr(775,root,%{name}) %dir %{_localstatedir}/%{name}/register-spool

%files example
%{_localstatedir}/%{name}/samples


%changelog
* Mon Feb 10 2020 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-18
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.9.6-14
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-12
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.5.9.6-10
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-9
- Disable TCP wrappers (bug #1518781)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-1
- 1.5.9.6 bump

* Thu Oct 03 2013 Petr Pisar <ppisar@redhat.com> - 1.5.9.5-1
- 1.5.9.5 version packaged
