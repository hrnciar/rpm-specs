%global qt_module qtaccountsservice

Name:           qt5-%{qt_module}
Summary:        Qt5 - AccountService addon
Version:        0.6.0
Release:        12%{?dist}

License:        LGPLv2+
URL:            https://github.com/hawaii-desktop/qtaccountsservice
Source0:        https://github.com/hawaii-desktop/qtaccountsservice/releases/download/v%{version}/%{qt_module}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%global __provides_exclude_from ^%{_kf5_qmldir}/QtAccountsService/.*\\.so$

%description
Qt-style API for freedesktop.org's AccountsService DBus service (see 
http://www.freedesktop.org/wiki/Software/AccountsService).


%package devel
Summary:    Development files for Qt Account Service Addon
Requires:   %{name}%{?isa} = %{version}-%{release}
Requires:   extra-cmake-modules
%description devel
Files for development using Qt Account Service Addon.


%prep
%autosetup -n %{qt_module}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

# please document why LINK= hack is needed -- rex
make %{?_smp_mflags} LINK='g++ -Wl,--as-needed' -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%ldconfig_scriptlets

%files
%{_libdir}/libQtAccountsService.so.*
%{_kf5_qmldir}/QtAccountsService/
%doc README.md
%license LICENSE.LGPL

%files devel
%{_includedir}/QtAccountsService/
%{_libdir}/cmake/QtAccountsService/
%{_libdir}/libQtAccountsService.so


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Rex Dieter <rdieter@math.unl.edu> - 0.6.0-4
- use new style __provides_exclude_from

* Mon Jan 02 2017 Rex Dieter <rdieter@math.unl.edu> - 0.6.0-3
- .spec cosmetics, use %%autosetup, filter qml provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.1.2-1
- Update to 0.1.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.1-1
- Rebase

* Tue Oct 15 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-3
- Own our directories (Christopher Meng, #1011501)
- Don't link to unused libraries (Christopher Meng, #1011501)

* Tue Sep 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Incorporate some review fixes (Christopher Meng, #1011501)

* Mon Sep 16 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging
