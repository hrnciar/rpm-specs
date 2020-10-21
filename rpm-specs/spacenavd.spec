Name:           spacenavd
Version:        0.7.1
Release:        2%{?dist}
Summary:        A free, compatible alternative for 3Dconnexion's input drivers

License:        GPLv3+
URL:            http://spacenav.sourceforge.net/
Source0:        http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz
# systemd unit files, for fedora
Source1:        spacenavd.service
# systemV init script, for el6
Source2:        spacenavd

BuildRequires:  gcc libX11-devel

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  systemd
%{?systemd_requires}
%else
Requires(post): /sbin/chkconfig
Requires(post): /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
%endif


%description
Spacenavd, is a free software replacement user-space driver (daemon), for
3Dconnexion's space-something 6dof input devices. It's compatible with the
original 3dxsrv proprietary daemon provided by 3Dconnexion, and works
perfectly with any program that was written for the 3Dconnexion driver.


%prep
%autosetup


%build
%configure
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile

%make_build


%install
%make_install

%if 0%{?fedora} || 0%{?rhel} >= 7
# Install systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}
%else
# Install systemV init script
mkdir -p %{buildroot}%{_initrddir}
install -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}
%endif


%post
%if 0%{?fedora} || 0%{?rhel} >= 7
    %systemd_post spacenavd.service
%else
    if [ $1 -eq 1 ] ; then 
        /sbin/chkconfig --add spacenavd &> /dev/null || :
    fi
%endif

%preun
%if 0%{?fedora} || 0%{?rhel} >= 7
    %systemd_preun spacenavd.service
%else
    if [ $1 -eq 0 ] ; then
        /sbin/service spacenavd stop &> /dev/null
        /sbin/chkconfig --del spacenavd &> /dev/null || :
    fi
%endif

%postun
%if 0%{?fedora} || 0%{?rhel} >= 7
    %systemd_postun_with_restart spacenavd.service
%else
    if [ $1 -ge 1 ] ; then
        /bin/service restart spacenavd &> /dev/null || :
    fi
%endif


%files
%doc AUTHORS doc/* README.md
%license COPYING
%{_bindir}/*
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Richard Shaw <hobbes1069@gmail.com> - 0.7.1-1
- Update to 0.7.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Richard Shaw <hobbes1069@gmail.com> - 0.6-1
- Update to latest upstream release.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.5-5
- Update package for systemd macros in F18+.

* Tue Oct 16 2012 John Morris <john@zultron.com> - 0.5-4
- Re-add sysv init file for el6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.5-3
- Rebuild for GCC 4.7.0.

* Thu Aug 16 2011 Richard Shaw <hobbes1069@gmail.com> - 0.5-2
- Use systemd unit file instead of sysv init file.

* Tue Aug 16 2011 Richard Shaw <hobbes1069@gmail.com> - 0.5-1
- Initial Release.
