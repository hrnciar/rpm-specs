Name:		aqsis
Version:	1.8.2
Release:	36%{?dist}
Summary:	Open source 3D rendering solution adhering to the RenderMan standard

License:	GPLv2+ and LGPLv2+
URL:		http://www.aqsis.org
Source0:	http://downloads.sourceforge.net/aqsis/aqsis-%{version}.tar.gz

# fix build against ilmbase-2.x, kudos to arch linux
Patch1: imfinputfile-forward-declaration.diff
# Work-around boost-1.59 having dropped
# dropped boost/serialization/pfto.hpp
# and BOOST_MAKE_PFTO_WRAPPER
Patch2: aqsis-1.8.2-boost-1.59.patch
# Fix code to be C++11 compatible
# https://sourceforge.net/p/aqsis/bugs/433/
Patch3: aqsis-1.8.2-gcc6.patch

BuildRequires:  desktop-file-utils

BuildRequires:  bison >= 1.35.0
BuildRequires:  boost-devel >= 1.34.0
BuildRequires:  cmake >= 2.6.3
BuildRequires:  doxygen
BuildRequires:  flex >= 2.5.4
BuildRequires:  fltk-devel >= 1.1.0, fltk-fluid
BuildRequires:  libjpeg-devel >= 6
BuildRequires:  libtiff-devel >= 3.7.1
BuildRequires:  libpng-devel
BuildRequires:  libxslt
BuildRequires:  qt4-devel >= 4.6.2
#BuildRequires:  tinyxml-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  python3-sphinx
BuildRequires:  zlib-devel >= 1.1.4

Requires: qt4%{?_isa} >= %{_qt4_version}
Requires: aqsis-core = %{version}-%{release}
Requires: aqsis-data = %{version}-%{release}


%description
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains graphical utilities and desktop integration.


%package core
Requires:	%{name}-libs = %{version}-%{release}
Summary:	Command-line tools for Aqsis Renderer

%description core
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains a command-line renderer, a shader compiler
for shaders written using the RenderMan shading language, a texture
pre-processor for optimizing textures and a RIB processor.


%package libs
Summary:        Library files for Aqsis Renderer

%description libs
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains the shared libraries for Aqsis Renderer.


%package data
Requires:	%{name} = %{version}-%{release}
Summary:	Example content for Aqsis Renderer
BuildArch:      noarch

%description data
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains example content, including additional
scenes, procedurals and shaders.


%package devel
Requires:	%{name} = %{version}-%{release}
Requires:	aqsis-core = %{version}-%{release}
Requires:	aqsis-libs = %{version}-%{release}
Requires:	aqsis-data = %{version}-%{release}
Summary:	Development files for Aqsis Renderer

%description devel
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains various developer libraries to enable
integration with third-party applications.


%prep
%setup -q

%patch1 -p1 -b imfinputfile-forward-declaration
%patch2 -p1
%patch3 -p1

%build
## Do not Enable pdiff=yes Because it will conflict with Printdiff :
## /usr/bin/pdiff  from package	a2ps
rm -rf build
mkdir -p build
pushd build
%cmake \
  -DSYSCONFDIR:STRING=%{_sysconfdir}/%{name} \
  -DAQSIS_MAIN_CONFIG_NAME=aqsisrc-%{_lib} \
  -DLIBDIR=%{_lib} \
  -DPLUGINDIR=%{_lib}/%{name} \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DAQSIS_USE_RPATH:BOOL=OFF \
  -DAQSIS_BOOST_FILESYSTEM_LIBRARY_NAME=boost_filesystem-mt \
  -DAQSIS_BOOST_REGEX_LIBRARY_NAME=boost_regex-mt \
  -DAQSIS_BOOST_THREAD_LIBRARY_NAME=boost_thread-mt \
  -DAQSIS_BOOST_WAVE_LIBRARY_NAME=boost_wave-mt \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -DBOOST_FILESYSTEM_VERSION=3 -pthread" \
  -DAQSIS_USE_EXTERNAL_TINYXML:BOOL=OFF ..

make VERBOSE=1 %{?_smp_mflags}

popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

# Move aqsisrc
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc \
  $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc-%{_lib}

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsis.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsltell.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/eqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/piqsl.desktop


%ldconfig_scriptlets libs

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/eqsl
%{_bindir}/piqsl
%{_bindir}/ptview
# Do not use the name pdiff for PerceptualDiff
# It is used by PrintDiff in a2ps
#{_bindir}/pdiff
%{_datadir}/applications/aqsis.desktop
%{_datadir}/applications/aqsl.desktop
%{_datadir}/applications/aqsltell.desktop
%{_datadir}/applications/eqsl.desktop
%{_datadir}/applications/piqsl.desktop
%{_datadir}/pixmaps/aqsis.png
%{_datadir}/icons/hicolor/192x192/mimetypes/aqsis-doc.png
%{_datadir}/mime/packages/aqsis.xml


%files core
%{_bindir}/aqsis
%{_bindir}/aqsl
%{_bindir}/aqsltell
%{_bindir}/miqser
%{_bindir}/teqser


%files libs
%dir %{_sysconfdir}/%{name}
## Do not use noreplace with aqsis release
## This may definitly change in future releases.
%config %{_sysconfdir}/%{name}/aqsisrc-%{_lib}
%{_libdir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so.*
# Licensed under LGPLv2+
#{_libdir}/libaqsis_ri2rib.so.*


%files devel
%{_includedir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so
# Licensed under LGPLv2+
#{_libdir}/libaqsis_ri2rib.so


%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/plugins/
%{_datadir}/%{name}/scripts/
%{_datadir}/%{name}/shaders/



%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1.8.2-34
- Rebuild for OpenEXR 2.3.0.

* Sun Apr 07 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.2-33
- Append -pthread to CXXFLAGS (F30FTBS RHBZ#1674655).
- Build with python3-sphinx.
- Spec cosmetics.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.2-29
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-26
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-24
- Rebuilt for Boost 1.63

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-23
- Fix FTBFS with GCC 6 (#1307323)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.8.2-22
- Rebuilt for Boost 1.60

* Sun Sep 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.2-21
- Rebuild for boost 1.59 (Add aqsis-1.8.2-boost-1.59.patch).
- Add %%license.
- Modernize spec.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.8.2-19
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.2-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.2-16
- rebuild (fltk)

* Sat Feb 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.2-15
- Rebuild for boost 1.57.0 (Previous attempt had failed).
- Fix bogus %%changelog dates.

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.8.2-14
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.2-13
- rebuild (openexr)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.2-11
- optimize/update scriptlets

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.8.2-9
- Rebuild for boost 1.55.0

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.8.2-8
- rebuild (openexr)

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.2-7
- Rebuild for ilmbase related soname bumps

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.8.2-5
- Rebuild for boost 1.54.0

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.8.2-4
- rebuild (OpenEXR)

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.2-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.2-2
- Rebuild for Boost-1.53.0

* Thu Oct 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 1.8.1-3
- Rebuild for new boost, update boost filesystem to 3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Tue Mar 06 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-15
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-13
- Rebuilt for boost 1.48

* Sat Jul 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-12
- Rebuild for boost

* Fri May 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-11
- Rebuild for new fltk

* Sat Apr 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-9
- rebuilt

* Tue Mar 29 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.6.0-8
- Update to current bugfix
- Disable tinyxml

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Petr Machata <pmachata@redhat.com> - 1.6.0-6
- Rebuild for boost
  - Request v2 of boost::filesystem.  The new boost defaults to v3
  - Include <cstdlib> on a couple places

* Thu Jul 29 2010  Bill Nottingham <notting@redhat.com> - 1.6.0-5
- Rebuild for boost

* Sat Jan 16 2010  Nicolas Chauvet <kwizart@fedoraproject.org> - 1.6.0-4
- Rebuild for boost

* Mon Oct 19 2009  kwizart < kwizart at gmail.com > - 1.6.0-3
- Minor updates to SPEC file by Leon Tony Atkinson - <latkinson@aqsis.org> 

* Sat Oct 17 2009 kwizart < kwizart at gmail.com > - 1.6.0-1
- Update to 1.6.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 kwizart < kwizart at gmail.com > - 1.4.2-5
- Rebuild for boost on F-12

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 kwizart < kwizart at gmail.com > - 1.4.2-3
- Fix and Rebuild for gcc44

* Tue Feb  3 2009 kwizart < kwizart at gmail.com > - 1.4.2-2
- Backport piqsl problem with libtiff
- Fix unappropriate use of xdg-tools #481352

* Tue Jan 27 2009 kwizart < kwizart at gmail.com > - 1.4.2-1
- Update to 1.4.2

* Fri Dec 19 2008 kwizart < kwizart at gmail.com > - 1.4.1-6
- Improve -core summary - #477134

* Thu Dec 18 2008 kwizart < kwizart at gmail.com > - 1.4.1-5
- Rebuild for boost

* Tue Oct 28 2008 kwizart < kwizart at gmail.com > - 1.4.1-4
- Add Requires(post/preun): xdg-utils

* Wed Oct  8 2008 kwizart < kwizart at gmail.com > - 1.4.1-3
- backport gcc43 fix for bake.cpp

* Wed Oct  8 2008 kwizart < kwizart at gmail.com > - 1.4.1-2
- backport patch for intsize problem

* Mon Sep 29 2008 kwizart < kwizart at gmail.com > - 1.4.1-1
- Update to 1.4.1

* Fri Jul 25 2008 kwizart < kwizart at gmail.com > - 1.4.0-1
- Update to 1.4.0

* Mon Jan  7 2008 kwizart < kwizart at gmail.com > - 1.2.0-7
- Fix gcc43

* Mon Oct 15 2007 kwizart < kwizart at gmail.com > - 1.2.0-6
- Rebuild

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 1.2.0-5
- Update the license field to GPLv2

* Sun Mar  4 2007 kwizart < kwizart at gmail.com > - 1.2.0-4
- Fix ownership for /etc/aqsis directory

* Sun Mar  4 2007 kwizart < kwizart at gmail.com > - 1.2.0-3
- Make comments

* Fri Mar  2 2007 kwizart < kwizart at gmail.com > - 1.2.0-2
- Disable pdiff (PerceptualDiff) to prevent conflicts with a2ps (PrintDiff)

* Wed Feb 28 2007 kwizart < kwizart at gmail.com > - 1.2.0-1
- Update to final 1.2.0
- fix some libdir
- change aqsis config file to sysconfdir/aqsis
- Enable x86_64 build 
- Enable third-party pdiff utility

* Fri Jan 19 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.8.svn738
- Updated to the latest SVN

* Thu Jan 18 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.7.alpha2
- added modifications by kwizart < kwizart at gmail.com >
- fix x86_64 build (experimental)
- fix wrong-end of line encoding in debug
- fix script-without-shebang in debug

* Thu Jan 18 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.2.alpha2
- Excluded x86_64 for now

* Mon Jan 15 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.1.alpha2
- Moved mpanalyse.py to shared

* Sat Jan 13 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.4.alpha1
- Shared libs mod

* Sat Dec 23 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.3.alpha1
- More tuning to meet Fedora-Extras requirements

* Thu Dec 21 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.2.alpha1
- Some cleanup for a Fedora-only spec

* Thu Dec 14 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 1.2.0-0.1.alpha1
- More clean-up/optimisation..

* Mon Dec 11 2006 Leon Tony Atkinson <latkinson@aqsis.org> 1.1.0-3
- Added Fedora (Core 5 tested) and OpenSUSE (10.2 tested) support to SPEC file.
- Cleaned-up/optimised SPEC file.

* Sat Dec 09 2006 Leon Tony Atkinson <latkinson@aqsis.org> 1.1.0-2
- Added Mandriva (2006 tested) support to SPEC file.

* Wed Nov 22 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 1.1.0-1
- Initial RPM/SPEC.
