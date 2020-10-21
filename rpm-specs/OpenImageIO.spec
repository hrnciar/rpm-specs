%undefine __cmake_in_source_build
%global sover 2.2

Name:           OpenImageIO
Version:        2.2.7.0
Release:        1%{?dist}
Summary:        Library for reading and writing images

License:        BSD and MIT
# The included fmtlib is MIT licensed
# src/include/OpenImageIO/fmt
URL:            https://sites.google.com/site/openimageio/home
Source0:        https://github.com/%{name}/oiio/archive/Release-%{version}/%{name}-%{version}.tar.gz
# Images for test suite
#Source1:        https://github.com/OpenImageIO/oiio-images/archive/master/oiio-images.tar.gz

# Needed until LibRaw is available on s390x and aarch64
%if 0%{?rhel} >= 8
ExclusiveArch:  x86_64 ppc64le
%endif

# Utilities
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  txt2man
BuildRequires:  /usr/bin/pathfix.py
# Libraries
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  bzip2-devel
# Not currently in RHEL/EPEL
%if ! 0%{?rhel}
BuildRequires:  dcmtk-devel
%endif
BuildRequires:  Field3D-devel
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  hdf5-devel
BuildRequires:  ilmbase-devel
BuildRequires:  jasper-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  LibRaw-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  opencv-devel
BuildRequires:  OpenEXR-devel ilmbase-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  openvdb-devel
BuildRequires:  pugixml-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  robin-map-devel
BuildRequires:  tbb-devel
BuildRequires:  zlib-devel

# WARNING: OpenColorIO and OpenImageIO are cross dependent.
# If an ABI incompatible update is done in one, the other also needs to be
# rebuilt.
BuildRequires:  OpenColorIO-devel


%description
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. Main features include:
- Extremely simple but powerful ImageInput and ImageOutput APIs for reading and
  writing 2D images that is format agnostic.
- Format plugins for TIFF, JPEG/JFIF, OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000,
  DPX, Cineon, FITS, BMP, ICO, RMan Zfile, Softimage PIC, DDS, SGI,
  PNM/PPM/PGM/PBM, Field3d.
- An ImageCache class that transparently manages a cache so that it can access
  truly vast amounts of image data.


%package -n python3-openimageio
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-openimageio}

%description -n python3-openimageio
Python bindings for %{name}.


%package utils
Summary:        Command line utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Command-line tools to manipulate and get information on images using the
%{name} library.


%package iv
Summary:        %{name} based image viewer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description iv
A really nice image viewer, iv, based on %{name} classes (and so will work
with any formats for which plugins are available).


%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       OpenEXR-devel

%description devel
Development files for package %{name}


%prep
%autosetup -p1 -n oiio-Release-%{version}

# Remove bundled pugixml
rm -f src/include/OpenImageIO/pugixml.hpp \
      src/include/OpenImageIO/pugiconfig.hpp \
      src/libutil/OpenImageIO/pugixml.cpp 

# Remove bundled tbb
rm -rf src/include/tbb

# Install test images
#mkdir ../oiio-images && pushd ../oiio-images
#tar --strip-components=1 -xzf %{SOURCE1}
#popd


%build
# CMAKE_SKIP_RPATH is OK here because it is set to FALSE internally and causes
# CMAKE_INSTALL_RPATH to be cleared, which is the desiered result.
mkdir build/linux && pushd build/linux
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DPYTHON_VERSION=%{python3_version} \
       -DBUILD_DOCS:BOOL=TRUE \
       -DINSTALL_DOCS:BOOL=FALSE \
       -DINSTALL_FONTS:BOOL=FALSE \
       -DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
       -DSTOP_ON_WARNING:BOOL=FALSE \
       -DJPEG_INCLUDE_DIR=%{_includedir} \
       -DOPENJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libopenjp2) \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DVERBOSE=TRUE

%cmake_build


%install
%cmake_install

# Move man pages to the right directory
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a src/doc/*.1 %{buildroot}%{_mandir}/man1


%check
# Not all tests pass on linux
#pushd build/linux && make test


%files
%doc CHANGES.md CREDITS.md README.md
%license LICENSE.md THIRD-PARTY.md
%{_libdir}/libOpenImageIO.so.%{sover}*
%{_libdir}/libOpenImageIO_Util.so.%{sover}*

%files -n python3-openimageio
%{python3_sitearch}/OpenImageIO.so

%files utils
%exclude %{_bindir}/iv
%{_bindir}/*
%exclude %{_mandir}/man1/iv.1.gz
%{_mandir}/man1/*.1.gz

%files iv
%{_bindir}/iv
%{_mandir}/man1/iv.1.gz

%files devel
%{_libdir}/libOpenImageIO.so
%{_libdir}/libOpenImageIO_Util.so
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/cmake/Modules/FindOpenImageIO.cmake
%{_includedir}/%{name}/


%changelog
* Thu Oct 01 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.7.0-1
- Update to 2.2.7.0.

* Wed Sep 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.6.1-1
- Update to 2.2.6.1.

* Thu Aug 20 2020 Simone Caronni <negativo17@gmail.com> - 2.1.18.1-2
- Rebuild for updated OpenVDB.

* Mon Aug 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.18.1-5
- Update to 2.1.18.1.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.17.0-3
- Rebuild for unannounced soname bump in libdc1394.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.17.0-1
- Update to 2.1.17.0.

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.1.16.0-3
- Rebuild for hdf5 1.10.6

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.16.0-2
- Rebuilt for OpenCV 4.3

* Tue Jun 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.16.0-1
- Update to 2.1.16.

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.15.0-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.15.0-3
- Rebuilt for Python 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.15.0-2
- Rebuild for new LibRaw

* Mon May 11 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.15.0-1
- Update to 2.1.15.0.
- Adds support for libRaw 0.20, fixes RHBZ#1833450.

* Sat May 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.14.0-1
- Update to 2.1.14.0.

* Sun Apr 12 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.13.0-2
- Rebuild for funky depdendency problem in Rawhide/33.

* Thu Apr 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.13.0-1
- Update to 2.1.13.

* Tue Mar 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.12.0-1
- Update to 2.1.12.0.

* Wed Feb 12 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.11.1-1
- Update to 2.1.11.0.

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.10.1-3
- Rebuild for OpenCV 4.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.10.1-1
- Update to 2.1.10.1.

* Fri Jan 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.10.0-1
- Update to 2.1.10.

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.0.13-2
- Rebuilt for opencv4

* Wed Dec 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.13-1
- Update to 2.0.13.

* Fri Nov 29 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.12-1
- Update to 2.0.12.
- Add proper attribution for bundled fmtlib.

* Wed Oct 02 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.11-1
- Update to 2.0.11.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.10-2
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.10-1
- Update to 2.0.10.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.9-1
- Update to 2.0.9.

* Sat May 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.8-1
- Update to 2.0.8.

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-3
- Rebuild for OpenEXR 2.3.0.

* Thu Apr 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-2
- Rebuild for OpenColorIO 1.1.1.

* Mon Apr 01 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-1
- Update to 2.0.7.

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Sun Mar 17 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.6-1
- Update to 2.0.6.

* Thu Mar 14 2019 Mohan Boddu <mboddu@bhujji.com> - 2.0.5-2
- Rebuilt for dcmtk 3.6.4

* Mon Feb 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.5-1
- Update to 2.0.5.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 2.0.4-2
- Rebuilt for Boost 1.69

* Sun Jan 06 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.4-1
- Update to 2.0.4:
  http://lists.openimageio.org/pipermail/oiio-dev-openimageio.org/2019-January/001391.html

* Sat Dec 08 2018 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Update to 2.0.3.

* Mon Dec 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.17-1
- Update to 1.8.17.

* Fri Nov 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.16-1
- Update to 1.8.16.

* Tue Oct 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.15-1
- Update to 1.8.15.

* Mon Sep 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-2
- Remove python2 module and replace with python3 module.

* Mon Sep 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-1
- Update to 1.8.14.

* Wed Jul 18 2018 Simone Caronni <negativo17@gmail.com> - 1.8.12-3
- Rebuild for LibRaw update.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.12-1
- Update to 1.8.12.

* Mon Apr 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.10-1
- Update to 1.8.10.

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 1.8.9-2
- Rebuild for opencv 3.4.1

* Thu Mar 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.9-1
- Update to 1.8.9

* Fri Feb 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.8-3
- Rebuild

* Tue Feb 13 2018 Sandro Mani <manisandro@gmail.com> - 1.8.8-2
- Rebuild (giflib)

* Fri Feb 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.8-1
- Update to 1.8.8.

* Thu Jan 18 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-3
- Add openjpeg2 to build dependencies.
- Re-enable dcmtk for 32bit arches.

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-2
- Rebuild for OpenColorIO 1.1.0.

* Wed Jan 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-1
- Update to latest upstream release.
- Disable building with dcmtk until fixed, see:
  https://github.com/OpenImageIO/oiio/issues/1841

* Thu Nov 02 2017 Richard Shaw <hobbes1069@gmail.com> - 1.8.6-1
- Update to latest upstream release.
- Add dcmtk to build to enable DICOM plugin.
