Summary:           Program for managing links into a DRBD shared partition
Name:              drbdlinks
Version:           1.29
Release:           3%{?dist}
License:           GPLv2
URL:               https://www.tummy.com/software/drbdlinks/
Source0:           https://github.com/linsomniac/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:           drbdlinksclean
Source2:           drbdlinks.logrotate
Source3:           drbdlinksclean.service
Source4:           drbdlinksclean-wrapper
%if 0%{?rhel} >= 8 || 0%{?fedora}
Requires:          python3
BuildRequires:     python3-devel
%else
Requires:          python2
BuildRequires:     python2
%endif
%if 0%{?rhel} > 6 || 0%{?fedora}
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
BuildRequires:     systemd
%else
Requires(post):    /sbin/chkconfig
Requires(preun):   /sbin/chkconfig
%endif
BuildArch:         noarch

%description
The drbdlinks program manages links into a DRBD partition which is shared
among several machines. A simple configuration file, "/etc/drbdlinks.conf",
specifies the links. This can be used to manage e.g. links for /etc/httpd,
/var/lib/pgsql and other system directories that need to appear as if they
are local to the system when running applications after the drbd shared
partition has been mounted.

When running drbdlinks with "start" as the mode, drbdlinks will rename the
existing files/directories and then make symbolic links into the DRBD
partition, "stop" does the reverse. By default, rename appends ".drbdlinks"
to the name, but this can be overridden.

An init script is included which runs "stop" before heartbeat starts, and
after heartbeat stops. This is done to try to ensure that when the shared
partition isn't mounted, the links are in their normal state.

%prep
%setup -q -n %{name}-release-%{version}

%build

%install
install -D -p -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
%if 0%{?rhel} >= 8 || 0%{?fedora}
sed -e '1 s|^#!.*python|#!%{__python3}|g' -i $RPM_BUILD_ROOT%{_sbindir}/%{name}
%else
sed -e '1 s|^#!.*python|#!%{__python}|g' -i $RPM_BUILD_ROOT%{_sbindir}/%{name}
%endif
touch -c -r %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/{%{name}.d,ha.d/resource.d},/usr/lib/ocf/resource.d/tummy}
ln -s ../../..%{_sbindir}/%{name} $RPM_BUILD_ROOT%{_sysconfdir}/ha.d/resource.d/%{name}
ln -s ../../../../..%{_sbindir}/%{name} $RPM_BUILD_ROOT/usr/lib/ocf/resource.d/tummy/%{name}
install -D -p -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
%if 0%{?rhel} > 6 || 0%{?fedora}
install -D -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/drbdlinksclean.service
install -D -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/drbdlinksclean
%else
install -D -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/drbdlinksclean
%endif
install -D -p -m 644 %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/configs-to-clean

mv -f README.markdown README

%check
make -C tests DRBDLINKS=$RPM_BUILD_ROOT%{_sbindir}/%{name}

%post
%if 0%{?rhel} > 6 || 0%{?fedora}
%systemd_post drbdlinksclean.service
%else
/sbin/chkconfig --add drbdlinksclean
%endif

%preun
%if 0%{?rhel} > 6 || 0%{?fedora}
%systemd_preun drbdlinksclean.service
%else
if [ $1 -eq 0 ]; then
  /sbin/service drbdlinksclean stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del drbdlinksclean
fi
%endif

%if 0%{?rhel} > 6 || 0%{?fedora}
%postun
%systemd_postun drbdlinksclean.service
%endif

%files
%license LICENSE
%doc README WHATSNEW
%if 0%{?rhel} > 6 || 0%{?fedora}
%{_unitdir}/drbdlinksclean.service
%{_libexecdir}/drbdlinksclean
%else
%{_sysconfdir}/rc.d/init.d/drbdlinksclean
%endif
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.d/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/%{name}
%{_sysconfdir}/ha.d/
/usr/lib/ocf/resource.d/tummy/
%{_mandir}/man8/%{name}.8*
%{_localstatedir}/lib/%{name}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Robert Scheck <robert@fedoraproject.org> 1.29-1
- Upgrade to 1.29

* Sat Aug 10 2019 Robert Scheck <robert@fedoraproject.org> 1.28-7
- Added patch for python 3 support (#1737964)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Robert Scheck <robert@fedoraproject.org> 1.28-3
- Update python 2 dependency declarations to new packaging standards,
  see https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Robert Scheck <robert@fedoraproject.org> 1.28-1
- Upgrade to 1.28

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Robert Scheck <robert@fedoraproject.org> 1.27-3
- Provide native systemd service

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 08 2014 Robert Scheck <robert@fedoraproject.org> 1.27-1
- Upgrade to 1.27

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Robert Scheck <robert@fedoraproject.org> 1.26-1
- Upgrade to 1.26

* Sun Oct 13 2013 Robert Scheck <robert@fedoraproject.org> 1.25-1
- Upgrade to 1.25

* Sun Aug 04 2013 Robert Scheck <robert@fedoraproject.org> 1.23-1
- Upgrade to 1.23

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Robert Scheck <robert@fedoraproject.org> 1.22-1
- Upgrade to 1.22

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 13 2011 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Sun Jul 17 2011 Robert Scheck <robert@fedoraproject.org> 1.19-2
- Handle visible SELinux range label if mcstrans is not used
- Added configuration file for tmpfiles handling (#656578)
- Added logrotate configuration to ignore possible *.drbdlinks

* Mon May 16 2011 Robert Scheck <robert@fedoraproject.org> 1.19-1
- Upgrade to 1.19

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Robert Scheck <robert@fedoraproject.org> 1.18-1
- Upgrade to 1.18

* Mon May 18 2009 Robert Scheck <robert@fedoraproject.org> 1.17-1
- Upgrade to 1.17

* Sun May 17 2009 Robert Scheck <robert@fedoraproject.org> 1.16-1
- Upgrade to 1.16

* Sat May 16 2009 Robert Scheck <robert@fedoraproject.org> 1.15-1
- Upgrade to 1.15
- Initial spec file for Fedora and Red Hat Enterprise Linux
