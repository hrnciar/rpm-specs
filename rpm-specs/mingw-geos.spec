%{?mingw_package_header}

%global pkgname geos

Name:          mingw-%{pkgname}
Version:       3.8.1
Release:       2%{?dist}
Summary:       MinGW Windows GEOS library
License:       LGPLv2+
BuildArch:     noarch
URL:           http://trac.osgeo.org/geos/
Source0:       http://download.osgeo.org/%{pkgname}/%{pkgname}-%{version}.tar.bz2

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows GEOS library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GEOS library

%description -n mingw32-%{pkgname}
MinGW Windows GEOS library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GEOS library

%description -n mingw64-%{pkgname}
MinGW Windows GEOS library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_configure --disable-static --disable-inline
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/%{mingw32_target}-geos-config
%{mingw32_bindir}/libgeos-3-8-1.dll
%{mingw32_bindir}/libgeos_c-1.dll
%{mingw32_includedir}/geos/
%{mingw32_includedir}/geos.h
%{mingw32_includedir}/geos_c.h
%{mingw32_libdir}/libgeos.dll.a
%{mingw32_libdir}/libgeos_c.dll.a

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/%{mingw64_target}-geos-config
%{mingw64_bindir}/libgeos-3-8-1.dll
%{mingw64_bindir}/libgeos_c-1.dll
%{mingw64_includedir}/geos/
%{mingw64_includedir}/geos.h
%{mingw64_includedir}/geos_c.h
%{mingw64_libdir}/libgeos.dll.a
%{mingw64_libdir}/libgeos_c.dll.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Sandro Mani <manisandro@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.7.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Sandro Mani <manisandro@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Tue Apr 14 2015 Sandro Mani <manisandro@gmail.com> - 3.4.2-1
- Initial package
