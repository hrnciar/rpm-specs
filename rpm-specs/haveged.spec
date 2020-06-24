Summary:        A Linux entropy source using the HAVEGE algorithm
Name:           haveged
Version:        1.9.12
Release:        1%{?dist}
License:        GPLv3+
URL:            https://github.com/jirka-h/haveged
Source0:        https://github.com/jirka-h/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

BuildRequires:  gcc
BuildRequires:  automake coreutils glibc-common systemd-units
Enhances:       apache2 gpg2 openssl openvpn php5 smtp_daemon systemd

%description
A Linux entropy source using the HAVEGE algorithm

Haveged is a user space entropy daemon which is not dependent upon the
standard mechanisms for harvesting randomness for the system entropy
pool. This is important in systems with high entropy needs or limited
user interaction (e.g. headless servers).
 
Haveged uses HAVEGE (HArdware Volatile Entropy Gathering and Expansion)
to maintain a 1M pool of random bytes used to fill /dev/random
whenever the supply of random bits in /dev/random falls below the low
water mark of the device. The principle inputs to haveged are the
sizes of the processor instruction and data caches used to setup the
HAVEGE collector. The haveged default is a 4kb data cache and a 16kb
instruction cache. On machines with a cpuid instruction, haveged will
attempt to select appropriate values from internal tables.

%package devel
Summary:   Headers and shared development libraries for HAVEGE algorithm
Requires:  %{name} = %{version}-%{release}

%description devel
Headers and shared object symbolic links for the HAVEGE algorithm

%prep
%setup -q

%build
#autoreconf -fiv
%configure
#SMP build is not working
#make %{?_smp_mflags}
make

%check
make check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

chmod 0644 COPYING README ChangeLog AUTHORS

#Install systemd service file
sed -e 's:@SBIN_DIR@:%{_sbindir}:g' -i init.d/service.fedora
install -Dpm 0644 init.d/service.fedora %{buildroot}%{_unitdir}/%{name}.service

# We don't ship .la files.
rm -rf %{buildroot}%{_libdir}/libhavege.*a

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -p COPYING README ChangeLog AUTHORS contrib/build/havege_sample.c %{buildroot}%{_defaultdocdir}/%{name}

%post
/sbin/ldconfig
%if 0%{?systemd_post:1}
%systemd_post haveged.service
%else
if [ $1 = 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif

%preun
%if 0%{?systemd_preun:1}
%systemd_preun haveged.service
%else
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable haveged.service >/dev/null 2>&1 || :
    /bin/systemctl stop haveged.service >/dev/null 2>&1 || :
fi
%endif

%postun
%if 0%{?systemd_postun_with_restart:1}
%systemd_postun_with_restart haveged.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart haveged.service >/dev/null 2>&1 || :
fi
%endif
/sbin/ldconfig

%files
%{_mandir}/man8/haveged.8*
%{_sbindir}/haveged
%{_unitdir}/haveged.service
%{_libdir}/*so.*
%{_defaultdocdir}/*

%files devel
%{_mandir}/man3/libhavege.3*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/havege.h
%doc contrib/build/havege_sample.c
%{_libdir}/*.so


%changelog
* Thu Jun 18 2020 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.12-1
 - Update to 1.9.12

* Fri Jun 12 2020 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.11-1
 - Update to 1.9.11

* Thu Jun 11 2020 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.10-1
 - Update to 1.9.10

* Thu Jun 11 2020 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.9-2
 - Fixed haveged.service file

* Tue Jun 09 2020 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.9-1
 - Update to 1.9.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.8-1
 - Update to 1.9.8

* Mon Aug 26 2019 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.6-1
 - Update to 1.9.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Jirka Hladky <hladky.jiri@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Sat Jan 04 2014 Jirka Hladky <hladky.jiri@gmail.com> - 1.8-1
- Unversioned docdir change, more info on 
  https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Fri Jan 03 2014 Jirka Hladky <hladky.jiri@gmail.com> - 1.8-0
- Updated to the version 1.8
- Improvement to systemd service file
- Fixed exit status

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Jirka Hladky <hladky.jiri@gmail.com> - 1.7-0
- Updated to the version 1.7
- Version 1.7 brings developement libraries
- Added devel package
* Sat Oct 13 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.5-2
- BZ 850144
- Introduce new systemd-rpm macros in haveged spec file
- Fedora 19 changes the way how to work with services in spec files. 
- It introduces new macros - systemd_post, systemd_preun and systemd_postun; 
- which replace scriptlets from Fedora 18 and older
- see https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd

* Tue Aug 14 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.5-1
- Update to the version 1.5
- Main new feature is a run time verification of the produced random numbers
- PIDFILE set to /run/haveged.pid
- converted README and man page to UTF-8. Informed the upstream to fix it.
* Wed Feb 15 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.4-3
- PIDFile should be stored at /run instead of the default location /var/run 
- There is  long term plan that directory /var/run will not further exist in the future Fedora versions
- Asked upstream to add -p <PID_FILE_location> switch to influence the location of the PID File
- Set PIDFile=/var/run/haveged.pid This is needed as long -p option is not implemented
- https://bugzilla.redhat.com/show_bug.cgi?id=770306#c10
* Wed Feb 15 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.4-2
- Updated systemd service file, https://bugzilla.redhat.com/show_bug.cgi?id=770306
* Tue Feb 14 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.4-1
- Update to the version 1.4
- Conversion to systemd, drop init script
* Sun Nov 06 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.3-2
- Fixed a bug on non x86 systems
* Sat Nov 05 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.3-1
- update from the upstream (1.3 stable)
* Mon Oct 03 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.3-0
-version 1.3 beta
* Fri Sep 30 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.2-4
- ppc64 build
* Mon Sep 26 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.2-3
- Cleaned spec file according to https://bugzilla.redhat.com/show_bug.cgi?id=739347#c11
* Sat Sep 24 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.2-2
- Added comment to explain why we need use Fedora specific start script
* Wed Sep 21 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.2-1
- Cleaned spec file according to https://bugzilla.redhat.com/show_bug.cgi?id=739347#c1
* Wed Sep 07 2011  Jirka Hladky <hladky.jiri@gmail.com> - 1.2-0
- Initial build