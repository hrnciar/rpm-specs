%{?mingw_package_header}

%global pkgname gdal

# does not support out-of-tree builds
%global w64_dir %{_builddir}/mingw64-%{pkgname}-%{version}-%{release}

Name:          mingw-%{pkgname}
Version:       3.1.3
Release:       2%{?dist}
Summary:       MinGW Windows GDAL library

BuildArch:     noarch
License:       MIT
URL:           http://www.gdal.org
# Source0:      http://download.osgeo.org/gdal/%%{version}/gdal-%%{version}.tar.xz
# See PROVENANCE.TXT-fedora and the cleaner script for details!
Source0:       %{pkgname}-%{version}-fedora.tar.xz

# Fix MinGW build
Patch0:        gdal_mingw.patch
# Adapt to jasper 2.0.21
# See https://github.com/OSGeo/gdal/commit/9ef8e16e27c5fc4c491debe50bf2b7f3e94ed334
Patch1:        gdal_jasper.patch
# Assume numpy is present since build-time detection does not work
# (numpy attempts to load binary modules, which does clearly not work for
# cross-compiled modules)
Patch2:        gdal_assume-numpy.patch


BuildRequires: automake autoconf libtool

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-cfitsio
BuildRequires: mingw32-curl
BuildRequires: mingw32-expat
BuildRequires: mingw32-freexl
BuildRequires: mingw32-geos
BuildRequires: mingw32-giflib
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libgta
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libkml
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libgeotiff
BuildRequires: mingw32-libspatialite
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-openjpeg2
BuildRequires: mingw32-pcre
BuildRequires: mingw32-postgresql
BuildRequires: mingw32-proj
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-numpy
BuildRequires: mingw32-python3-setuptools
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-xerces-c
BuildRequires: mingw32-xz-libs
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-cfitsio
BuildRequires: mingw64-curl
BuildRequires: mingw64-expat
BuildRequires: mingw64-freexl
BuildRequires: mingw64-geos
BuildRequires: mingw64-giflib
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libgta
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libkml
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libgeotiff
BuildRequires: mingw64-libspatialite
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-openjpeg2
BuildRequires: mingw64-pcre
BuildRequires: mingw64-postgresql
BuildRequires: mingw64-proj
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-numpy
BuildRequires: mingw64-python3-setuptools
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-xerces-c
BuildRequires: mingw64-xz-libs
BuildRequires: mingw64-zlib

# TODO
# BuildRequires: armadillo-devel
# BuildRequires: hdf-devel
# BuildRequires: hdf5-devel
# BuildRequires: netcdf-devel
# BuildRequires: libdap-devel
# BuildRequires: librx-devel
# BuildRequires: mysql-devel
# BuildRequires: ogdi-devel
# BuildRequires: unixODBC-devel



%description
MinGW Windows GDAL library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GDAL library
# GDAL bundles a modified copy of g2clib and degrib
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14

%description -n mingw32-%{pkgname}
MinGW Windows GDAL library.



%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 GDAL bindings

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 GDAL bindings.


%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows GDAL library tools

%description -n mingw32-%{pkgname}-tools
MinGW Windows GDAL library tools.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GDAL library
# GDAL bundles a modified copy of g2clib and degrib
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14

%description -n mingw64-%{pkgname}
MinGW Windows GDAL library.



%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 GDAL bindings

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 GDAL bindings.



%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows GDAL library tools

%description -n mingw64-%{pkgname}-tools
MinGW Windows GDAL library tools.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}-fedora

# Delete bundled libraries
rm -rf frmts/zlib
rm -rf frmts/png/libpng
rm -rf frmts/gif/giflib
rm -rf frmts/jpeg/libjpeg
rm -rf frmts/jpeg/libjpeg12
rm -rf frmts/gtiff/libgeotiff
rm -rf frmts/gtiff/libtiff


# http://ramblingfoo.blogspot.ch/2007/07/required-file-configrpath-not-found.html
touch config.rpath
autoreconf -ifv .

cp -a . %{w64_dir}


%build
%mingw32_configure \
    --without-bsb \
    --with-liblzma \
    --with-curl \
    --with-webp \
    --with-spatialite \
    --with-geos=%{mingw32_bindir}/%{mingw32_target}-geos-config \
    --with-libkml=%{mingw32_prefix} \
    --disable-static
%mingw32_make %{?_smp_mflags}

pushd swig/python
NUMPY_INCLUDEDIR=%{mingw32_python3_sitearch}/numpy/core/include %{mingw32_python3} setup.py build
popd

(
cd %{w64_dir}
%mingw64_configure \
    --without-bsb \
    --with-liblzma \
    --with-curl \
    --with-webp \
    --with-spatialite \
    --with-geos=%{mingw64_bindir}/%{mingw64_target}-geos-config \
    --with-libkml=%{mingw64_prefix} \
    --disable-static
%mingw64_make %{?_smp_mflags}

pushd swig/python
NUMPY_INCLUDEDIR=%{mingw64_python3_sitearch}/numpy/core/include %{mingw64_python3} setup.py build
popd
)


%install
%mingw32_make DESTDIR=%{buildroot} install
pushd swig/python
%{mingw32_python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd

(
cd %{w64_dir}
%mingw64_make DESTDIR=%{buildroot} install
pushd swig/python
%{mingw64_python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
)

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Delete empty gdalplugins dir
rmdir %{buildroot}%{mingw32_libdir}/gdalplugins
rmdir %{buildroot}%{mingw64_libdir}/gdalplugins

# Delete data
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-%{pkgname}
%license LICENSE.TXT
%{mingw32_bindir}/libgdal-27.dll
%{mingw32_bindir}/gdal-config
%{mingw32_libdir}/libgdal.dll.a
%{mingw32_libdir}/pkgconfig/gdal.pc
%{mingw32_includedir}/*.h

%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%{mingw32_python3_sitearch}/*
%{mingw32_bindir}/*.py

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.TXT
%{mingw64_bindir}/libgdal-27.dll
%{mingw64_bindir}/gdal-config
%{mingw64_libdir}/libgdal.dll.a
%{mingw64_libdir}/pkgconfig/gdal.pc
%{mingw64_includedir}/*.h

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%{mingw64_python3_sitearch}/*
%{mingw64_bindir}/*.py

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Fri Oct 16 21:27:12 CEST 2020 Sandro Mani <manisandro@gmail.com> - 3.1.3-2
- Rebuild (jasper)

* Mon Sep 07 2020 Sandro Mani <manisandro@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Mon Aug 17 2020 Sandro Mani <manisandro@gmail.com> - 3.1.2-3
- Add gdal_assume-numpy.patch

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 3.1.0-2
- Rebuild (python-3.9)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-16
- BR: mingw{32,64}-python3-setuptools

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-15
- Drop poppler, requires mingw*-xpdf-devel

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-14
- Rebuild to re-enable poppler, jasper support

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-13
- Backport fix for CVE-2019-17545

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-12
- Rebuild (Changes/Mingw32GccDwarf2)

* Sat Sep 28 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-11
- Bump for gdal_proj-libname.patch update

* Sat Sep 28 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-10
- Rebuild (proj, libspatialite, python 3.8)

* Fri Aug 02 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-9
- Drop python2 bindings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-7
- Add python3 subpackages

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-6
- Fix proj requires

* Tue Feb 12 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-5
- Really rebuild (proj, geos)

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-4
- Rebuild (proj, geos)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-2
- Rebuild (poppler)

* Wed Oct 03 2018 Sandro Mani <manisandro@gmail.com> - 2.3.2-1
- Update to 2.3.2

* Mon Aug 27 2018 Sandro Mani <manisandro@gmail.com> - 2.3.1-3
- Rebuild (openssl)

* Wed Aug 22 2018 Sandro Mani <manisandro@gmail.com> - 2.3.1-2
- Enable OpenJPEG2 support
- Add bundled provides

* Tue Aug 21 2018 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Tue Aug 14 2018 Sandro Mani <manisandro@gmail.com> - 2.2.4-6
- Rebuild (poppler)

* Tue Jul 24 2018 Pete Walter <pwalter@fedoraproject.org> - 2.2.4-5
- Rebuild for xerces-c 3.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Sandro Mani <manisandro@gmail.com> - 2.2.4-3
- Rebuild for libkml ABI change

* Wed Apr 11 2018 Sandro Mani <manisandro@gmail.com> - 2.2.4-2
- Rebuild (poppler)

* Tue Mar 27 2018 Sandro Mani <manisandro@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Thu Feb 15 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-3
- Rebuild (poppler)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Thu Nov 09 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-6
- Rebuild (libkml)

* Wed Nov 08 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-5
- Rebuild (poppler)

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-4
- Enable libkml support

* Tue Oct 24 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-3
- Add patch to fix incorrect libproj libname

* Mon Oct 09 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-2
- Rebuild (poppler)

* Wed Sep 27 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-6
- Rebuild (mingw-filesystem)

* Fri Sep 08 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-5
- Rebuild (gdal)

* Sun Sep 03 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-4
- Build python2 bindings

* Thu Aug 24 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-3
- Fix spatialite detection

* Sun Aug 06 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-2
- Rebuild (poppler)

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Sat Feb 04 2017 Sandro Mani <manisandro@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Wed Aug 05 2015 Sandro Mani <manisandro@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Tue May 12 2015 Sandro Mani <manisandro@gmail.com> - 1.11.2-1
- Initial package
