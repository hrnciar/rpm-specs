%global ntp_version 4.2.8p15

Name:		ntp-refclock
Version:	0.4
Release:	2%{?dist}
Summary:	Drivers for hardware reference clocks
# MIT is the primary license of ntp and ntp-refclock, but some drivers
# are licensed under BSD or BSD with advertising
License:	MIT and BSD and BSD with advertising
URL:		https://github.com/mlichvar/ntp-refclock
Source0:	https://github.com/mlichvar/ntp-refclock/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-%{ntp_version}.tar.gz

BuildRequires:	gcc pps-tools-devel

Requires(pre):	shadow-utils

# The drivers and some code they need are from ntp
Provides:	bundled(ntp) = %{ntp_version}

%description
ntp-refclock is a wrapper for reference clock drivers included in the ntpd
daemon, which enables other NTP implementations to use the supported hardware
reference clocks for synchronization of the system clock.

It provides a minimal environment for the drivers to be able to run in a
separate process, measuring the offset of the system clock relative to the
reference clock and sending the measurements to another process controlling
the system clock.

%prep
%setup -q -a 1
ln -s ntp-%{ntp_version} ntp

# Refer to packaged documentation for drivers
sed -i 's|<https:.*refclock.html>|in %{_pkgdocdir}/drivers/|' ntp-refclock.8

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow"

pushd ntp

%configure \
	--enable-all-clocks \
	--enable-parse-clocks \
	--disable-ATOM \
	--disable-LOCAL-CLOCK \
	--without-crypto \
	--without-threads \
	--without-sntp

# Build only objects that may be linked with ntp-refclock
%make_build -C libntp
%make_build -C libparse
cd ntpd
%make_build $(echo *refclock*.c | sed 's|\.c|\.o|g')

popd

%make_build \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="$RPM_LD_FLAGS" \
	DEFAULT_USER=%{name} \
	DEFAULT_ROOTDIR=/usr/share/empty

%install
%make_install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	useradd -r -g %{name} -d / -s /sbin/nologin \
		-c "Reference clock driver" %{name}
:

%files
%license COPYRIGHT*
%doc README NEWS ntp/html/drivers
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Miroslav Lichvar <mlichvar@redhat.com> 0.4-1
- update ntp-refclock to 0.4 and ntp to 4.2.8p15

* Mon Mar 09 2020 Miroslav Lichvar <mlichvar@redhat.com> 0.3-1
- update ntp-refclock to 0.3 and ntp to 4.2.8p14
- enable SHM driver for testing

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Miroslav Lichvar <mlichvar@redhat.com> 0.2-5
- update ntp to 4.2.8p13

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.2-3
- update ntp to 4.2.8p12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.2-1
- update ntp-refclock to 0.2 and ntp to 4.2.8p11
- add gcc to build requirements

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.1-2
- provide bundled(ntp)
- don't duplicate _smp_mflags in CFLAGS

* Fri Jan 19 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.1-1.ntp4.2.8p10
- initial release
