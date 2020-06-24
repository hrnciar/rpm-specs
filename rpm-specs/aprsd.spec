%define uprel 15
Name: aprsd
Summary: Internet gateway and client access to amateur radio APRS packet data
Version: 2.2.5
Release: %{uprel}.6%{?dist}.23
License: GPLv2+
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}-%{uprel}.tar.gz
Source1: aprsd.conf
Source2: aprsd.service
Source3: INIT.TNC
Source4: user.deny
Source5: welcome.txt
Source6: RESTORE.TNC
Source7: aprsd.logrotate
Patch0: aprsd-2.2.5-15-compile.patch
Patch1: aprsd-2.2.5-15-gcc43-port.patch
Patch2: aprsd-2.2.5-15-sysconfdir.patch
URL: http://sourceforge.net/projects/aprsd/
BuildRequires:  gcc-c++
BuildRequires: libax25-devel
BuildRequires: systemd-units
#Requires (preun): /sbin/chkconfig
#Requires (preun): /sbin/service
#Requires (post): /sbin/chkconfig
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
APRSd is an APRS server program that uses amateur radio and internet
services to convey GPS mapping, weather, and positional data.
It has been developed by and for amateur radio enthusiasts to provide
real-time data in an easy to use package.

%prep
%setup -q -n %{name}-%{version}-%{uprel}
%patch0 -p1 -b compile
%patch1 -p1 -b gccport
%patch2 -p1 -b sysconfdir

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}" INSTALL="install -p"
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/aprsd
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/aprsd/aprsd.conf
install -m 755 %{SOURCE2} %{buildroot}%{_unitdir}/aprsd.service
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/aprsd/INIT.TNC
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/aprsd/user.deny
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/aprsd/welcome.txt
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/aprsd/RESTORE.TNC
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/aprsd
mkdir -p %{buildroot}%{_localstatedir}
mkdir -p %{buildroot}%{_localstatedir}/log/aprsd

%post
#/sbin/chkconfig --add aprsd
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
#if [ $1 = 0 ]; then
# /sbin/service aprsd stop > /dev/null 2>&1
# /sbin/chkconfig --del aprsd
#fi
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable aprsd.service > /dev/null 2>&1 || :
    /bin/systemctl stop aprsd.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart aprsd.service >/dev/null 2>&1 || :
fi

%triggerun -- aprsd < 2.2.5-15.6.3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply aprsd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save aprsd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del aprsd >/dev/null 2>&1 || :
/bin/systemctl try-restart aprsd.service >/dev/null 2>&1 || :



%files
%{_bindir}/aprsd
%{_bindir}/aprspass
%{_unitdir}/aprsd.service
%dir %{_sysconfdir}/aprsd
%dir %{_localstatedir}/log/aprsd
%config(noreplace) %{_sysconfdir}/aprsd/*
%config(noreplace) %{_sysconfdir}/logrotate.d/aprsd
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc README
%doc doc/aprsddoc.html
%doc doc/ports.html
%doc doc/q.html
%doc doc/qalgorithm.html

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.2.5-15.6.20
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.5-15.6.17
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.6.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.5-15.6.12
- Rebuild for updated libax25.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.5-15.6.10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.6.8
- fix build break - fixes #1105962
- fix bogus dates
- spec file cleanups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.5-15.6.3
- Migrate to systemd, BZ 754399.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.6
 - fix wrong version bumps
 - add patch from Alan Crosswell fix 'AX.25 sockets are not supported by this
 executable'

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-15.5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.5
- fix rh bug 458817

* Sat Aug  2 2008 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.4
- logrotate warning fixes

* Sat Mar  8 2008 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.3
- Patched to localstatedir
- Added logrotation support

* Fri Feb 22 2008 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.2
- Patched homedir to obey default sysconfdir
- Patched to compile for gcc-4.3
- Misc cleanups

* Thu Feb 21 2008 Lucian Langa <cooly@gnome.eu.org> - 2.2.5-15.1
- Initial spec file created

