Name:           wicd-kde
Version:        0.3.1
Release:        17%{?dist}
License:        GPLv3+
Summary:        A Wicd client built on the KDE Development Platform
URL:            https://projects.kde.org/projects/extragear/network/wicd-kde
Source:         http://kde-apps.org/CONTENT/content-files/132366-wicd-kde-0.3.1.tar.gz
Requires:       wicd

BuildRequires:  qt4-devel
BuildRequires:  kdelibs4-devel
BuildRequires:  gettext

%description
A Wicd client built on the KDE Development Platform.

%prep
%setup -qn %{name}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform} 

%install
make install/fast DESTDIR=${RPM_BUILD_ROOT} -C %{_target_platform}

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING TODO
%config(noreplace) %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.wicdclient.scripts.conf
%{_kde4_libdir}/kde4/*
%{_kde4_libexecdir}/wicdclient_scripts_helper
%{_kde4_datadir}/dbus-1/system-services/org.kde.wicdclient.scripts.service
%{_kde4_appsdir}/%{name}
%{_kde4_appsdir}/plasma/services/wicd.operations
%{_datadir}/kde4/services/*
%{_kde4_datadir}/polkit-1/actions/org.kde.wicdclient.scripts.policy

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.1-9
- Rebuilt for new wicd + spec clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Minh Ngo <minh@fedoraproject.org> - 0.3.1-2
- removing a patch (have fixed in the current release)

* Wed Feb 13 2013 Minh Ngo <minh@fedoraproject.org> - 0.3.1-1
- New version

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-4
- Bump build

* Tue Apr  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-3
- Add debian patch to fix FTBFS on ARM

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 10 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.0-1
- Wicd 1.7.1 compatibility
- Port to Plasma

* Thu Nov 10 2011 Minh Ngo <nlminhtl@gmail.com> 0.2.3-3
- fixing make install command

* Fri Oct 28 2011 Minh Ngo <nlminhtl@gmail.com> 0.2.3-2
- fixing the warning conffile-without-noreplace-flag
- removing kcm_wicd.desktop changes

* Wed Oct 12 2011 Minh Ngo <nlminhtl@gmail.com> 0.2.3-1
- Updating to the new version
- kcm_wicd.desktop fix

* Wed Jun 08 2011 Minh Ngo <nlminhtl@gmail.com> 0.2.2-2
- desktop-file-install for desktop files
- KDE-specific macros
- macro %%make_install fixed

* Tue Jun 07 2011 Minh Ngo <nlminhtl@gmail.com> 0.2.2-1
- initial build 
