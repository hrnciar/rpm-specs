%{?mingw_package_header}

%global pkgname qtkeychain

Name:           mingw-%{pkgname}
Version:        0.11.1
Release:        1%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        BSD
Url:            https://github.com/frankosterfeld/%{pkgname}
Source0:        https://github.com/frankosterfeld/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qttools-tools

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qttools-tools


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake \
    -DBUILD_WITH_QT4:BOOL=OFF
%mingw_make_build


%install
%mingw_make_install

%find_lang %{pkgname} --with-qt
grep %{mingw32_datadir}/qt5keychain/translations %{pkgname}.lang > mingw32_%{pkgname}-qt5.lang
grep %{mingw64_datadir}/qt5keychain/translations %{pkgname}.lang > mingw64_%{pkgname}-qt5.lang



%files -n mingw32-%{pkgname}-qt5 -f mingw32_%{pkgname}-qt5.lang
%license COPYING
%{mingw32_bindir}/libqt5keychain.dll
%{mingw32_includedir}/qt5keychain/
%{mingw32_libdir}/libqt5keychain.dll.a
%{mingw32_libdir}/cmake/Qt5Keychain
%{mingw32_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files -n mingw64-%{pkgname}-qt5 -f mingw64_%{pkgname}-qt5.lang
%license COPYING
%{mingw64_bindir}/libqt5keychain.dll
%{mingw64_includedir}/qt5keychain/
%{mingw64_libdir}/libqt5keychain.dll.a
%{mingw64_libdir}/cmake/Qt5Keychain
%{mingw64_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%changelog
* Tue Sep 15 2020 Sandro Mani <manisandro@gmail.com> - 0.11.1-1
- Update to 0.11.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Sandro Mani <manisandro@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.9.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Sandro Mani <manisandro@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Thu Apr 25 2019 Sandro Mani <manisandro@gmail.com> - 0.7.0-1
- Initial package
