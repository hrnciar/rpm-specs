%global apiversion 1.11

Name:           pcl
Version:        1.11.0
Release:        1%{?dist}
Summary:        Library for point cloud processing
License:        BSD
URL:            http://pointclouds.org/

# Source snapshots contain un-redistributable sources from nvidia
# create_tarball_pcl.sh provided to strip non-free sources
Source0:        %{name}-%{version}-fedora.tar.xz
Source1:        create_tarball_pcl.sh

# Only enable sse2, and only on x86_64
Patch0:         %{name}-1.11.0-sse2.patch
# Look for external metslib, not upstream
Patch1:         %{name}-1.11.0-metslib.patch
# Patch for PCLConfig.cmake to find pcl
Patch2:         %{name}-1.11.0-fedora.patch
# Exclude the "build" directory from doxygen processing.
Patch3:         %{name}-1.11.0-doxyfix.patch
# Split up explicit template instantiations so that builders don't run out of memory
Patch4:         %{name}-1.11.0-oom.patch
# Use a built-in sphinx documentation theme and disable doxylink plugin
Patch5:         %{name}-1.11.0-sphinx.patch

# For plain building
BuildRequires:  cmake, gcc-c++, boost-devel
# Documentation
BuildRequires:  doxygen, graphviz, /usr/bin/sphinx-build

# mandatory
BuildRequires:  eigen3-static, flann-devel, cminpack-devel, vtk-devel, gl2ps-devel, hdf5-devel, libxml2-devel, netcdf-cxx-devel, jsoncpp-devel, metslib-static, libXext-devel
# optional
BuildRequires:  qt5-qtbase-devel, qhull-devel, libusbx-devel, gtest-devel, qt5-qtwebkit-devel
%ifarch %{ix86} x86_64
BuildRequires:  openni-devel
%endif

%description
The Point Cloud Library (or PCL) is a large scale, open project for point
cloud processing.

The PCL framework contains numerous state-of-the art algorithms including
filtering, feature estimation, surface reconstruction, registration, model
fitting and segmentation. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       eigen3-devel, qhull-devel, cminpack-devel, flann-devel, vtk-devel
%ifarch %{ix86} x86_64
Requires:       openni-devel
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        Point cloud tools and viewers
Requires:       %{name} = %{version}-%{release}

%description    tools
This package contains tools for point cloud file processing and viewers
for point cloud files and live Kinect data.


%package        doc
Summary:        PCL API documentation
BuildArch:      noarch

%description    doc
The %{name}-doc package contains API documentation for the Point Cloud
Library.


%prep
%setup -qn %{name}-%{version}
%patch0 -p1 -b .sse2
%patch1 -p1 -b .metslib
%patch2 -p0 -b .fedora
%patch3 -p0 -b .doxyfix
%patch4 -p1 -b .oom
%patch5 -p1 -b .sphinx

# Just to make it obvious we're not using any of these
rm -fr recognition/include/pcl/recognition/3rdparty/metslib
rm -fr surface/src/3rdparty/opennurbs
rm -rf surface/include/pcl/surface/3rdparty/opennurbs

%build
mkdir build
pushd build
# try to reduce memory usage of compile process (can cause OOM errors
# esp. on ARM builders)
%global optflags %(echo %{optflags} | sed -e 's/-g /-g1 /' -e 's/-pipe //')

%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_DOCS=ON \
  -DWITH_CUDA=OFF \
  -DWITH_TUTORIALS=ON \
  -DBUILD_apps=ON \
  -DBUILD_global_tests=OFF \
  -DOPENNI_INCLUDE_DIR:PATH=/usr/include/ni \
  -DLIB_INSTALL_DIR=%{_lib} \
%ifarch x86_64
  -DPCL_ENABLE_SSE=ON \
%else
  -DPCL_ENABLE_SSE=OFF \
%endif
  -DPCL_PKGCONFIG_SUFFIX:STRING="" \
  -DBUILD_documentation=ON \
  -DCMAKE_SKIP_RPATH=ON \
  ..

# Don't use mflags, we're hitting out of memory errors on the koji builders
%make_build
popd

%install
pushd build
%make_install

# Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Just a dummy test
rm -f $RPM_BUILD_ROOT%{_bindir}/timed_trigger_test

# Remove installed documentation (will use %doc)
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Rename the documentation folders from "html"
mv doc/doxygen/html doc/doxygen/api
mv doc/tutorials/html doc/tutorials/tutorials
mv doc/advanced/html doc/advanced/advanced

cp -fr ../doc/advanced/content/files/* doc/advanced/advanced
cp -fr ../doc/tutorials/content/sources doc/tutorials/tutorials

rm -f doc/doxygen/api/_form*
popd

for f in $RPM_BUILD_ROOT%{_bindir}/{openni_image,pcd_grabber_viewer,pcd_viewer,openni_viewer,oni_viewer}; do
	if [ -f $f ]; then
		mv $f $RPM_BUILD_ROOT%{_bindir}/pcl_$(basename $f)
	fi
done
rm $RPM_BUILD_ROOT%{_bindir}/{openni_fast_mesh,openni_ii_normal_estimation,openni_voxel_grid} ||:

mkdir -p $RPM_BUILD_ROOT%{_libdir}/cmake/pcl
mv $RPM_BUILD_ROOT%{_datadir}/%{name}-*/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/pcl/
mv $RPM_BUILD_ROOT%{_datadir}/%{name}-*/Modules $RPM_BUILD_ROOT%{_libdir}/cmake/pcl/

%check
ARGS='-V' make -C build test || true

%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc AUTHORS.txt
%{_libdir}/*.so.*
%{_datadir}/%{name}-%{apiversion}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/pcl

%files tools
%{_bindir}/pcl_*
# There are no .desktop files because the GUI tools are rather examples
# to understand a particular feature of PCL.

%files doc
%doc build/doc/doxygen/api
%doc build/doc/tutorials/tutorials
%doc build/doc/advanced/advanced

%changelog
* Tue Jun 02 2020 Rich Mattes <richmattes@gmail.com> - 1.11.0-1
- Update to release 1.11.0

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.9.1-7
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.9.1-5
- Add patch to fix line fitting in SAC segmentation

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Rich Mattes <richmattes@gmail.com> - 1.9.1-3
- Fix cmake module installation

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 1.9.1-2
- Rebuild for vtk 8.2

* Thu Feb 14 2019 Rich Mattes <richmattes@gmail.com> - 1.9.1-1
- Update to release 1.9.1

* Sun Feb 03 2019 Volker Fröhlich <volker27@gmx.at> - 1.8.1-7
- Resolve build with Boost 1.69

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.8.1-5
- Rebuilt for Boost 1.69

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 1.8.1-4
- Rebuild for VTK 8.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Rich Mattes <richmattes@gmail.com> - 1.8.1-2
- Add patch to generate pcl-2d.pc

* Fri Feb 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.1-2
- Rebuild, minor spec cleanup

* Fri Feb 09 2018 Rich Mattes <richmattes@gmail.com> - 1.8.1-1
- Update to release 1.8.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-14
- Rebuilt for Boost 1.66

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.8.0-13
- Rebuilt for jsoncpp.so.20

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.8.0-12
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-9
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-8
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.0-5
- Rebuilt for Boost 1.63

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 1.8.0-4
- Rebuild for eigen3-3.3.1

* Wed Dec 7 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-3
- Rebuild for vtk 7.1

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 1.8.0-2
- Rebuilt for libjsoncpp.so.11

* Thu Sep 01 2016 Tim Niemueller <tim@niemueller.de> - 1.8.0-1
- Upgrade to 1.8.0 release

* Sat Apr 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.0-0.4.rc1
- Rebuild for qhull-2015.2-1.

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 1.8.0-0.3.rc1
- Rebuilt for libjsoncpp.so.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rich Mattes <richmattes@gmail.com> - 1.8.0-0.1.rc1
- Update to 1.8.0 release candidate (rhbz#1303049)

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-11
- Rebuild for boost 1.60

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-10
- Rebuild for vtk 6.3.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-9
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.2-7
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-4
- Rebuild for vtk 6.2.0

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.7.2-3
- Rebuild for boost 1.57.0
- Pass -DBOOST_NEXT_PRIOR_HPP_INCLUDED to qt4-moc in apps/CMakeLists.txt
  (pcl-0ddf-boost157.patch)

* Mon Dec 29 2014 Rich Mattes <richmattes@gmail.com> - 1.7.2-2
- Fix pkgconfig to require libopenni (rhbz#1177244)
- Disable latex doxygen documentation

* Tue Dec 16 2014 Rich Mattes <richmattes@gmail.com> - 1.7.2-1
- Update to release 1.7.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.7.1-3
- Rebuild for boost 1.55.0

* Fri Mar 21 2014 Rich Mattes <richmattes@gmail.com> - 1.7.1-2
- Rebuild for new eigen3
- Set PCL_ROOT to the CMAKE_INSTALL_PREFIX
- Fix usage of VTK_DEFINITIONS (rhbz#1079531)

* Sat Oct 26 2013 Rich Mattes <richmattes@gmail.com> - 1.7.1-1
- Update to release 1.7.1

* Sat Sep 14 2013 Rich Mattes <richmattes@gmail.com> - 1.7.0-4
- Add patch to remove openni-dev from pkgconfig files (rhbz#1007941)
- Add patch to generate pcl_geometry pkgconfig file again

* Sun Sep 08 2013 Rich Mattes <richmattes@gmail.com> - 1.7.0-3
- Fix hard-coded vtk library dependencies in PCLConfig.cmake

* Thu Aug 29 2013 Rich Mattes <richmattes@gmail.com> - 1.7.0-2
- Fix PCLConfig.cmake so PCL can discover itself

* Wed Aug 21 2013 Rich Mattes <richmattes@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Update vtk 6 patch for 1.7.0

* Sat Jul 27 2013 pmachata@redhat.com - 1.6.0-7
- Rebuild for boost 1.54.0

* Fri Jul 12 2013 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-6
- Rebuild for vtk 6.0.0
- Add patch for vtk 6 support

* Sat Jun 29 2013 Rich Mattes <richmattes@gmail.com> - 1.6.0-5
- Rebuild for new eigen3
- Change eigen3 BR to -static
- Add ARM support

* Fri Mar 08 2013 Karsten Hopp <karsten@redhat.com> 1.6.0-4
- more fixes for archs without openni

* Sun Feb 17 2013 Rich Mattes <richmattes@gmail.com> - 1.6.0-3
- Fixed bogus changelog dates
- Fixed build errors due to boost 1.53 and/or gcc 4.8

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.6.0-3
- Rebuild for Boost-1.53.0

* Tue Sep 25 2012 Rich Mattes <richmattes@gmail.com> - 1.6.0-2
- Disabled march=native flag in PCLConfig.cmake

* Mon Aug 06 2012 Rich Mattes <richmattes@gmail.com> - 1.6.0-1
- Update to release 1.6.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 1.5.1-3
- Rebuild for new vtk

* Thu Apr 19 2012 Tim Niemueller <tim@niemueller.de> - 1.5.1-2
- Pass proper LIB_INSTALL_DIR, install wrong cmake files otherwise

* Mon Apr 02 2012 Rich Mattes <richmattes@gmail.com> - 1.5.1-1
- Update to release 1.5.1
- Add new patch for gcc-4.7 fixes

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Rich Mattes <richmattes@gmail.com> - 1.4.0-1
- Update to release 1.4.0
- Add patch for gcc-4.7 fixes

* Mon Jan 16 2012 Tim Niemueller <tim@niemueller.de> - 1.3.1-5
- Update patch to fix PCLConfig.cmake

* Sat Jan 14 2012 Rich Mattes <richmattes@gmail.com> - 1.3.1-4
- Rebuild for gcc-4.7 and flann-1.7.1

* Sun Jan 08 2012 Dan Horák <dan[at]danny.cz> - 1.3.1-3
- openni is exclusive for x86

* Fri Dec 23 2011 Tim Niemueller <tim@niemueller.de> - 1.3.1-2
- Make sure documentation is not in main package

* Sun Dec 04 2011 Tim Niemueller <tim@niemueller.de> - 1.3.1-1
- Update to 1.3.1

* Tue Nov 22 2011 Tim Niemueller <tim@niemueller.de> - 1.3.0-1
- Update to 1.3.0

* Sat Oct 22 2011 Tim Niemueller <tim@niemueller.de> - 1.2.0-1
- Update to 1.2.0

* Tue Oct 04 2011 Tim Niemueller <tim@niemueller.de> - 1.1.1-2
- Change vtkWidgets to vtkRendering as import library flags to fix crash
  for binaries compiled with the installed PCL

* Tue Sep 20 2011 Tim Niemueller <tim@niemueller.de> - 1.1.1-1
- Update to 1.1.1

* Wed Jul 27 2011 Tim Niemueller <tim@niemueller.de> - 1.1.0-1
- Update to 1.1.0

* Wed Apr 06 2011 Tim Niemueller <tim@niemueller.de> - 1.0.0-0.1.svn366
- Initial package

