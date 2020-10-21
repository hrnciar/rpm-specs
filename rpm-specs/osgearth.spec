%global osg_ver 3.4.1

Name:           osgearth
Version:        2.7
Release:        27%{?dist}
Summary:        Dynamic map generation toolkit for OpenSceneGraph

License:        LGPLv3 with exceptions
URL:            http://osgearth.org/
Source0:        https://github.com/gwaldron/osgearth/archive/%{name}-%{version}.tar.gz
# Fix build failure
Patch0:         osgearth_build.patch
# Add fast path for gdal heightfield nearest neighbor sampling
# Backport of upstream b55ee29ed4a3209726a9e067cde0d1a89dbf2c4b
Patch1:         osgearth_gdalperformance.patch
# GEOS-3.6+ compatibility
Patch2:         osgearth_geos.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  OpenSceneGraph = %{osg_ver}
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  OpenSceneGraph-qt-devel
BuildRequires:  python3-sphinx
BuildRequires:  qt4-devel
BuildRequires:  tinyxml-devel

Requires:       OpenSceneGraph = %{osg_ver}

%description
osgEarth is a C++ terrain rendering SDK. Just create a simple XML file, point
it at your imagery, elevation, and vector data, load it into your favorite
OpenSceneGraph application, and go! osgEarth supports all kinds of data and
comes with lots of examples to help you get up and running quickly and easily.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       OpenSceneGraph-devel
Requires:       OpenSceneGraph-qt-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        %{name} viewers and tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools contains viewers and data manipulation tools for %{name}.


%package        examples
Summary:        %{name} example applications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-examples-data = %{version}-%{release}

%description    examples
The %{name}-examples contains %{name} example applications.


%package        examples-data
Summary:        Data for %{name} example applications
BuildArch:      noarch
Requires:       %{name}-examples = %{version}-%{release}

%description    examples-data
The %{name}-examples-data contains data for the %{name} example
applications.


%package doc
Summary:        Documentation files for %{name}
Provides:       bundled(jquery)
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation files for developing
applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Fix spurious-executable-perm and script-without-shebang
chmod -x data/boxman.osg
chmod -x src/osgEarth/TextureCompositor.cpp
chmod -x src/osgEarthAnnotation/AnnotationUtils.cpp
chmod -x src/osgEarthUtil/Controls.cpp
chmod -x src/osgEarth/OverlayDecorator.cpp
chmod -x src/osgEarth/ShaderFactory.cpp

# Remove bundled sources just to be sure
rm -f osgEarth/tiny*

# Remove non-free content
rm -rf data/loopix


%build
%cmake -DWITH_EXTERNAL_TINYXML=True
%cmake_build
make -C docs html


%ldconfig_scriptlets


%install
%cmake_install
install -Dd %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data
cp -a tests %{buildroot}%{_datadir}/%{name}/tests

# Remove unnecessary files
rm -f docs/build/html/.buildinfo


%files
%license LICENSE.txt
%{_libdir}/libosgEarth*.so.*
%{_libdir}/osgPlugins-%{osg_ver}/osgdb_*.so

%files devel
%{_includedir}/osgEarth*/
%{_libdir}/libosgEarth*.so

%files tools
%{_bindir}/osgearth_atlas
%{_bindir}/osgearth_backfill
%{_bindir}/osgearth_boundarygen
%{_bindir}/osgearth_cache
%{_bindir}/osgearth_conv
%{_bindir}/osgearth_featureinfo
%{_bindir}/osgearth_package
%{_bindir}/osgearth_package_qt
%{_bindir}/osgearth_qt
%{_bindir}/osgearth_shadergen
%{_bindir}/osgearth_tfs
%{_bindir}/osgearth_tileindex
%{_bindir}/osgearth_version
%{_bindir}/osgearth_viewer

%files examples
%{_bindir}/osgearth_annotation
%{_bindir}/osgearth_cache_test
%{_bindir}/osgearth_createtile
%{_bindir}/osgearth_city
%{_bindir}/osgearth_clamp
%{_bindir}/osgearth_clipplane
%{_bindir}/osgearth_colorfilter
%{_bindir}/osgearth_controls
%{_bindir}/osgearth_demo
%{_bindir}/osgearth_elevation
%{_bindir}/osgearth_featureeditor
%{_bindir}/osgearth_featurefilter
%{_bindir}/osgearth_featurequery
%{_bindir}/osgearth_features
%{_bindir}/osgearth_fog
%{_bindir}/osgearth_graticule
%{_bindir}/osgearth_imageoverlay
%{_bindir}/osgearth_los
%{_bindir}/osgearth_manip
%{_bindir}/osgearth_map
%{_bindir}/osgearth_measure
%{_bindir}/osgearth_minimap
%{_bindir}/osgearth_mrt
%{_bindir}/osgearth_pick
%{_bindir}/osgearth_occlusionculling
%{_bindir}/osgearth_overlayviewer
%{_bindir}/osgearth_qt_simple
%{_bindir}/osgearth_qt_windows
%{_bindir}/osgearth_sequencecontrol
%{_bindir}/osgearth_shadercomp
%{_bindir}/osgearth_sharedlayer
%{_bindir}/osgearth_terrainprofile
%{_bindir}/osgearth_tilesource
%{_bindir}/osgearth_toc
%{_bindir}/osgearth_tracks
%{_bindir}/osgearth_transform

%files examples-data
%{_datadir}/%{name}

%files doc
%license LICENSE.txt
%doc docs/build/html


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 2.7-26
- Rebuild (gdal)

* Wed May 06 2020 Sandro Mani <manisandro@gmail.com> - 2.7-25
- Rebuild (geos)

* Mon Mar 09 2020 Sandro Mani <manisandro@gmail.com> - 2.7-24
- Update geos patch

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 2.7-23
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Sandro Mani <manisandro@gmail.com> - 2.7-20
- Fix build against GEOS-3.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.coM> - 2.7-17
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-15
- Rebuild for OSG-3.4.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 2.7-11
- Rebuild (geos)

* Thu Jun 23 2016 Sandro Mani <manisandro@gmail.com> - 2.7-10
- Add osgearth_gdalperformance.patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 2.7-8
- Rebuild (GEOS)

* Tue Oct 13 2015 Sandro Mani <manisandro@gmail.com> - 2.7-7
- osgearth-devel: Requires: OpenSceneGraph-devel, OpenSceneGraph-qt-devel

* Fri Sep 11 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-6
- Rebuild for OSG-3.4.0.

* Fri Aug 28 2015 Sandro Mani <manisandro@gmail.com> - 2.7-5
- Rebuild (gdal)

* Mon Aug 17 2015 Sandro Mani <manisandro@gmail.com> - 2.7-4
- Rebuild (OpenSceneGraph)

* Sun Aug 09 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-3
- Rebuild for OSG-3.2.2.

* Mon Jul 27 2015 Sandro Mani <manisandro@gmail.com> - 2.7-2
- Rebuild (gdal)

* Fri Jul 24 2015 Sandro Mani <manisandro@gmail.com> - 2.7-1
- Update to 2.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 18 2015 Sandro Mani <manisandro@gmail.com> - 2.6-4
- Add patch to fix FTBFS (#1213049)

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 2.6-3
- Parallel build for docs
- Noarch data subpackage

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 2.6-2
- Add explicit Requires: OpenSceneGraph = %%{osg_ver}
- Add Provides: bundled(jquery) to -doc
- Use %%license for license
- Use system tinyxml, remove bundled sources
- Remove non-free loopix data
- Remove html/.buildinfo
- Add -Wl,--as-needed
- Improve descriptions
- Rename package data -> examples, put example binaries in that package

* Thu Nov 20 2014 Sandro Mani <manisandro@gmail.com> - 2.6-1
- Initial package
