%{?mingw_package_header}

%global pkgname cfitsio

Name:          mingw-%{pkgname}
Version:       3.470
Release:       4%{?dist}
Summary:       MinGW Windows CFITSIO library

License:       MIT
BuildArch:     noarch
URL:           http://heasarc.gsfc.nasa.gov/fitsio/
Source0:       ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/%{pkgname}-%(v=%{version}; echo $v | sed 's|0$||').tar.gz

# CMakeLists fixes, unbundle zlib, fix pkgconfig file
Patch0:        cfitsio_build.patch
# Disable curl support, otherwise a collision between #define TBYTE in fitsio.h and typedef TBYTE in tchar.h occurs
Patch1:        disable-curl-mingw.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib


%description
MinGW Windows CFITSIO library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows CFITSIO library

%description -n mingw32-%{pkgname}
MinGW Windows CFITSIO library.


%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library

%description -n mingw32-%{pkgname}-tools
MinGW Windows CFITSIO library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows CFITSIO library

%description -n mingw64-%{pkgname}
MinGW Windows CFITSIO library.


%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library

%description -n mingw64-%{pkgname}-tools
MinGW Windows CFITSIO library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%(v=%{version}; echo $v | sed 's|0$||')

# remove bundled zlib
# not all the files inside zlib belong to zlib
find zlib -type f \
    -not -name zcompress.? \
    -and -not -name zuncompress.? \
    -and -not -name zutil.? \
    -exec rm {} \;


%build
%mingw_cmake .
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license License.txt
%{mingw32_bindir}/libcfitsio-3.dll
%{mingw32_libdir}/libcfitsio.dll.a
%{mingw32_libdir}/pkgconfig/cfitsio.pc
%{mingw32_includedir}/cfitsio/

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/FPack.exe
%{mingw32_bindir}/Funpack.exe

%files -n mingw64-%{pkgname}
%license License.txt
%{mingw64_bindir}/libcfitsio-3.dll
%{mingw64_libdir}/libcfitsio.dll.a
%{mingw64_libdir}/pkgconfig/cfitsio.pc
%{mingw64_includedir}/cfitsio/

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/FPack.exe
%{mingw64_bindir}/Funpack.exe

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.470-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.470-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 3.470-2
- Fix broken pkgconfig file

* Fri Aug 02 2019 Sandro Mani <manisandro@gmail.com> - 3.470-1
- Update to 3.470

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.450-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.450-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Sandro Mani <manisandro@gmail.com> - 3.450-1
- Updateto 3.450

* Mon Mar 12 2018 Sandro Mani <manisandro@gmail.com> - 3.430-1
- Update to 3.430

* Fri Feb 23 2018 Sandro Mani <manisandro@gmail.com> - 3.420-1
- Update to 3.420

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.410-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 3.410-1
- Update to 3.410

* Thu Apr 23 2015 Sandro Mani <manisandro@gmail.com> - 3.370-1
- Initial package
