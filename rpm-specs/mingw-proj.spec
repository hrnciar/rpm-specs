%{?mingw_package_header}

%global pkgname proj

Name:          mingw-%{pkgname}
Version:       6.3.2
Release:       1%{?dist}
Summary:       Cartographic projection software (PROJ.4)

BuildArch:     noarch
License:       MIT
URL:           https://github.com/OSGeo/proj.4
Source0:       https://github.com/OSGeo/proj.4/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: sqlite

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-sqlite

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-sqlite


%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/


%package -n mingw32-%{pkgname}
Summary:       Cartographic projection software (PROJ.4)

%description -n mingw32-%{pkgname}
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/


%package -n mingw32-%{pkgname}-static
Summary:       Static libraries for mingw32-%{pkgname}
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static libraries for mingw32-%{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       Cartographic projection software (PROJ.4)

%description -n mingw64-%{pkgname}
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/


%package -n mingw64-%{pkgname}-static
Summary:       Static libraries for mingw64-%{pkgname}
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static libraries for mingw64-%{pkgname}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n PROJ-%{version}


%build
./autogen.sh

%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# Remove libtool archives
find %{buildroot} -type f -name '*.la' -delete

# Remove unneeded files
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libproj-15.dll
%{mingw32_bindir}/*.exe
%{mingw32_libdir}/libproj.dll.a
%{mingw32_libdir}/pkgconfig/proj.pc
%{mingw32_includedir}/*.h
%{mingw32_includedir}/proj/

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libproj.a

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libproj-15.dll
%{mingw64_bindir}/*.exe
%{mingw64_libdir}/libproj.dll.a
%{mingw64_libdir}/pkgconfig/proj.pc
%{mingw64_includedir}/*.h
%{mingw64_includedir}/proj/

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libproj.a


%changelog
* Sun May 03 2020 Sandro Mani <manisandro@gmail.com> - 6.3.2-1
- Update to 6.3.2

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 6.2.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 5.2.0-1
- Update to 5.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 4.9.3-1
- Update to 4.9.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Sandro Mani <manisandro@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Sandro Mani <manisandro@gmail.com> - 4.8.0-1
- Update to 4.8.0
- Remove upstreamed patch
- Also build mingw64 packages
- Add static subpackage
- Modernize spec file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 4.6.1-8
- Renamed the source package to mingw-proj (#801017)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.6.1-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 15 2009 David Ludlow <dave@adsllc.com> - 4.6.1-4
- Don't remove build executables

* Thu Oct 15 2009 David Ludlow <dave@adsllc.com> - 4.6.1-3
- Updates for Fedora packaging

* Wed Sep 9 2009 David Ludlow <dave@adsllc.com> - 4.6.1-2
- Initial creation of mingw32 package
