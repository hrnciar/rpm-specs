Name:           appmenu-qt
Version:        0.2.7+14.04.20140305
Release:        9%{?dist}
Summary:        Global application menu to Qt

License:        LGPLv2 with exceptions and GPLv3
URL:            http://launchpad.net/%{name}
Source0:        http://archive.ubuntu.com/ubuntu/pool/main/a/%{name}/%{name}_%{version}.orig.tar.gz

BuildRequires:  kde-workspace-devel
BuildRequires:  pkgconfig(dbusmenu-qt)

%description
This package allows Qt to export its menus over DBus.


%prep
%autosetup


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
%make_build
popd


%install
%make_install -C %{_target_platform}


%files
%license COPYING COPYING.LGPL-2.1 LGPL_EXCEPTION.txt
%doc NEWS README
%{_qt4_plugindir}/menubar/libappmenu-qt.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7+14.04.20140305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Björn Esser <fedora@besser82.io> - 0.2.7+14.04.20140305-1
- Update to v0.2.7+14.04.20140305
- Change Source0 to official release-tarball location
- Use %%autosetup and %%make_{build,install} macros
- Move licensing-files to %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.6-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jan 29 2013 Rex Dieter <rdieter@fedoraproject.org> 0.2.6-3
- cosmetics

* Sat Dec 08 2012 Mario Blättermann <mariobl@fedoraproject.org> - 0.2.6-2
- Spec cleanup: Use %%{_qt4_plugindir} instead of hardcoded path

* Sat Dec 01 2012 Mario Blättermann <mariobl@fedoraproject.org> - 0.2.6-1
- Initial package

