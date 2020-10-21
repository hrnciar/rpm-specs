%{?mingw_package_header}

%global pkgname shapelib
#global pre RC1

Name:          mingw-%{pkgname}
Version:       1.5.0
Release:       5%{?pre:.%pre}%{?dist}
Summary:       MinGW Windows %{pkgname} library

# The core library is dual-licensed LGPLv2 or MIT.
# Some contributed files have different licenses:
# - contrib/csv2shp.c: GPLv2+
# - contrib/dbfinfo.c: Public domain
# - contrib/dbfcat.c:  Public domain
License:       (LGPLv2+ or MIT) and GPLv2+ and Public Domain
URL:           http://shapelib.maptools.org/
Source0:       http://download.osgeo.org/shapelib/%{pkgname}-%{version}%{?pre:%pre}.tar.gz
BuildArch:     noarch

BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-proj

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-proj

%description
%{summary}.


%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the  MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the  MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -n %{pkgname}-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%{mingw_make} install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libshp-2.dll
%{mingw32_includedir}/shapefil.h
%{mingw32_libdir}/libshp.dll.a
%{mingw32_libdir}/pkgconfig/shapelib.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libshp.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libshp-2.dll
%{mingw64_includedir}/shapefil.h
%{mingw64_libdir}/libshp.dll.a
%{mingw64_libdir}/pkgconfig/shapelib.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libshp.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.5.0-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Sandro Mani <manisandro@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 1.4.1-5
- Rebuild (proj)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Sandro Mani <manisandro@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 1.4.0-2
- Rebuild (proj)

* Sun Dec 11 2016 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Wed Dec 07 2016 Sandro Mani <manisandro@gmail.com> - 1.4.0-0.1.RC1
- Update to 1.4.0-RC1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Sandro Mani <manisandro@gmail.com> - 1.3.0-5
- Rebuild (proj)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Sandro Mani <manisandro@gmail.com> - 1.3.0-3
- Backport some fixes from the gdal bundled shapelib

* Thu Aug 08 2013 Sandro Mani <manisandro@gmail.com> - 1.3.0-2
- Add missing licenses

* Fri Jul 12 2013 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Initial Fedora package
