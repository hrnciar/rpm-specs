%{?mingw_package_header}

%global pkgname spatialindex

Name:          mingw-%{pkgname}
Version:       1.9.3
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library
BuildArch:     noarch

License:       MIT
URL:           http://libspatialindex.org
Source0:       https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2
# Fix mingw build
Patch0:        spatialindex_mingw.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-src-%{version}


%build
%mingw_cmake -DSIDX_BIN_SUBDIR=bin .
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_bindir}/lib%{pkgname}_c.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/lib%{pkgname}_c.dll.a
%{mingw32_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_bindir}/lib%{pkgname}_c.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/lib%{pkgname}_c.dll.a
%{mingw64_includedir}/%{pkgname}/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Sandro Mani <manisandro@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Wed Oct 23 2019 Sandro Mani <manisandro@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.8.5-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jun 24 2015 Sandro Mani <manisandro@gmail.com> - 1.8.5-1
- Initial package
