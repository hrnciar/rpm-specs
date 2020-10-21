%{?mingw_package_header}

%global pkgname quazip

Name:          mingw-%{pkgname}
Version:       0.7.6
Release:       6%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
# Following files are zlib licensed:
#  - quazip/unzip.c
#  - quazip/unzip.h
#  - quazip/zip.c
#  - quazip/zip.h
# Rest is LGPLv2 with a static linking exception, see COPYING
License:       (LGPLv2+ with exceptions) and zlib
URL:           https://stachenov.github.io/quazip/
Source:        https://github.com/stachenov/quazip/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Fix library install directory, static library name and cmake modules installation directory
Patch0:        quazip_cmake.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-libzip

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-libzip

%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5-static
Summary:       Static version of the MinGW Windows Qt5 %{pkgname} library
Requires:      mingw32-%{pkgname}-qt5 = %{version}-%{release}

%description -n mingw32-%{pkgname}-qt5-static
Static version of the MinGW Windows Qt5 %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5-static
Summary:       Static version of the MinGW Windows Qt5 %{pkgname} library
Requires:      mingw64-%{pkgname}-qt5 = %{version}-%{release}

%description -n mingw64-%{pkgname}-qt5-static
Static version of the MinGW Windows Qt5 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
mkdir build_qt5
pushd build_qt5
%mingw_cmake -DBUILD_WITH_QT4=OFF -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make %{?_smp_mflags}
popd


%install
pushd build_qt5
%mingw_make install DESTDIR=%{buildroot}
popd


%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libquazip5.dll
%{mingw32_includedir}/quazip5/
%{mingw32_libdir}/libquazip5.dll.a
%{mingw32_datadir}/cmake/Modules/FindQuaZip5.cmake

%files -n mingw32-%{pkgname}-qt5-static
%{mingw32_libdir}/libquazip5.a

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libquazip5.dll
%{mingw64_includedir}/quazip5/
%{mingw64_libdir}/libquazip5.dll.a
%{mingw64_datadir}/cmake/Modules/FindQuaZip5.cmake

%files -n mingw64-%{pkgname}-qt5-static
%{mingw64_libdir}/libquazip5.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.7.6-4
- Rebuild (Changes/Mingw32GccDwarf2)
- Drop Qt4 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Sandro Mani <manisandro@gmail.com> - 0.7.3-5
- Fix cmake module install location

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-4
- Fix license

* Fri Aug 25 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-3
- Fix FindQuaZip5.cmake

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-2
- Align build with native package

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri Nov 01 2013 Sandro Mani <manisandro@gmail.com> - 0.5.1-1
- Initial package
