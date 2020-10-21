%{?mingw_package_header}

%global pkgname svg2svgt

Name:           mingw-%{pkgname}
Version:        0.9.6
Release:        8%{?dist}
Summary:        MinGW Windows %{pkgname} library

License:        LGPLv2+
BuildArch:      noarch
URL:            https://github.com/manisandro/svg2svgt
Source0:        https://github.com/manisandro/svg2svgt/archive/v%{version}/%{pkgname}-%{version}.tar.gz

# Add missing include
Patch0:         svg2svgt_includes.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools
BuildRequires: mingw32-qt5-qtsvg
BuildRequires: mingw32-qt5-qtxmlpatterns

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools
BuildRequires: mingw64-qt5-qtsvg
BuildRequires: mingw64-qt5-qtxmlpatterns


%description
MinGW Windows %{pkgname} library.

###############################################################################

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{?commit:%commit}%{!?commit:%version}


%build
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Delete data
rm -rf %{buildroot}%{mingw32_datadir}/{applications,icons,metainfo}/
rm -rf %{buildroot}%{mingw64_datadir}/{applications,icons,metainfo}/


%files -n mingw32-%{pkgname}
%license LICENSE.LGPL
%{mingw32_bindir}/%{pkgname}.exe
%{mingw32_bindir}/%{pkgname}-gui.exe
%{mingw32_bindir}/lib%{pkgname}-0.dll
%{mingw32_datadir}/%{pkgname}/
%{mingw32_includedir}/%{pkgname}/
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc

%files -n mingw64-%{pkgname}
%license LICENSE.LGPL
%{mingw64_bindir}/%{pkgname}.exe
%{mingw64_bindir}/%{pkgname}-gui.exe
%{mingw64_bindir}/lib%{pkgname}-0.dll
%{mingw64_datadir}/%{pkgname}/
%{mingw64_includedir}/%{pkgname}/
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6

* Tue Aug 29 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.1.git7a182a9
- Initial package
