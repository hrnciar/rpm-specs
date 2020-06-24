%global vcglibver 1.0.1

Summary:	A system for processing and editing unstructured 3D triangular meshes
Name:		meshlab
Version:	2016.12
Release:	12%{?dist}
URL:		http://meshlab.sourceforge.net/
License:	GPLv2+ and BSD and Public Domain

# https://bugzilla.redhat.com/show_bug.cgi?id=1472375
ExcludeArch:	ppc64 ppc64le s390x

Source0:	https://github.com/cnr-isti-vclab/meshlab/archive/v%{version}.tar.gz
Source1:	meshlab-48x48.xpm
# Matches 2016.12.
# Probably belongs in its own package, but nothing else seems to depend on it.
Source2:	https://github.com/cnr-isti-vclab/vcglib/archive/v%{vcglibver}.tar.gz
Provides:	bundled(vcglib) = %{vcglibver}

# Fedora-specific patches to use shared libraries, and to put plugins and
# shaders in appropriate directories
Patch0:		meshlab-2016.12-sharedlib.patch
Patch1:		meshlab-2016.12-plugin-path.patch
Patch2:		meshlab-2016.12-shader-path.patch

# Patch to fix FTBFS due to missing include of <cstddef>
# from Teemu Ikonen <tpikonen@gmail.com>
# Also added a missing include of <unistd.h>
Patch3:		meshlab-2016.12-cstddef.patch

# Patch to fix reading of .ply files in comma separator locales
# from Teemu Ikonen <tpikonen@gmail.com>
Patch4:		meshlab-2016.12-ply-numeric.patch

# Add #include <GL/glu.h> to various files
Patch5:		meshlab-2016.12-glu.patch

# Disable io_ctm until openctm is packaged
Patch6:		meshlab-2016.12-noctm.patch

# Include paths shouldn't have consecutive double slashes.  Causes
# a problem for debugedit, used by rpmbuild to extract debuginfo.
Patch11:	meshlab-2016.12-include-path-double-slash.patch

# FTBFS fixes
Patch12:	meshlab-2016.12-readheader.patch
Patch13:	meshlab-2016.12-stdmin.patch
Patch14:	meshlab-2016.12-format-security.patch

# Fix broken .pro file
Patch15:	meshlab-2016.12-fix-broken-pro-file.patch

# If you assign negative numbers to a char, it needs to be a signed char
# Otherwise, stuff breaks on arm architectures.
Patch16:	meshlab-2016.12-arm-signed-char-fix.patch

# Fix Screened Poisson Surface Reconstruction filter by copying around XML files
# https://github.com/cnr-isti-vclab/meshlab/issues/97
# https://github.com/cnr-isti-vclab/meshlab/commit/19148325122ac70a2cc3f6e2feb4b786c2e073cf
# https://github.com/cnr-isti-vclab/meshlab/commit/612388c42d00ab8eba1d9626a7da33a18c724d76
# https://bugzilla.redhat.com/show_bug.cgi?id=1559137
Patch17:	meshlab-2016.12-xml-filter.patch

# qPrintable doesn't take ints, just print regular ints
# already fixed (teh file has changed a lot) in upstream master
# https://bugzilla.redhat.com/show_bug.cgi?id=1604819
Patch18:	meshlab-2016.12-qprintable.patch

# Add missing includes for QLineEdit and QSlider
# https://github.com/cnr-isti-vclab/meshlab/pull/353
# https://bugzilla.redhat.com/show_bug.cgi?id=1604819
Patch19:	meshlab-2016.12-qt-includes.patch

BuildRequires:	bzip2-devel
BuildRequires:	glew-devel
BuildRequires:	levmar-devel
BuildRequires:	lib3ds-devel
BuildRequires:	muParser-devel
BuildRequires:	qhull-devel
BuildRequires:	qt5-qtbase-devel qt5-qtxmlpatterns-devel qt5-qtscript-devel
BuildRequires:	qtsoap5-devel
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	mpir-devel

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -q -c -n %{name} -a 2
%patch0 -p0 -b .sharedlib
%patch1 -p0 -b .plugin-path
%patch2 -p0 -b .shader-path
%patch3 -p0 -b .cstddef
%patch4 -p0 -b .ply-numeric
%patch5 -p0 -b .glu
%patch6 -p0 -b .noctm
%patch11 -p0 -b .include-path-double-slash
%patch12 -p0 -b .readheader
%patch13 -p0 -b .stdmin	
%patch14 -p0 -b .format-security
%patch15 -p0 -b .fix-broken-pro-file
%patch16 -p0 -b .armfix
%patch17 -p0 -b .xml-filter
%patch18 -p0 -b .qprintable
%patch19 -p0 -b .qt-includes

# Turn of execute permissions on source files to avoid rpmlint
# errors and warnings for the debuginfo package
find . \( -name *.h -o -name *.cpp -o -name *.inl \) -a -executable \
	-exec chmod -x {} \;

mv vcglib-%{vcglibver} vcglib
mv meshlab-%{version}/src/plugins_experimental/io_TXT/io_txt.pro meshlab-%{version}/src/plugins_experimental/io_TXT/io_TXT.pro

# Remove bundled library sources, since we use the Fedora packaged
# libraries
rm -rf vcglib/wrap/system/multithreading vcglib/wrap/system/*getopt* vcglib/wrap/system/time
rm -rf meshlab-%{version}/src/external/{ann*,bzip2*,glew*,levmar*,lib3ds*,muparser*,ode*,qhull*,qtsoap*}
rm -rf meshlab-%{version}/src/external/lib/linux-g++/*

%if 0%{?fedora} > 24
# Reflect qhull-2015.2 changes
sed -i \
  -e 's,#include <qhull/,#include <libqhull/,' \
  -e 's,/qhull.h>,/libqhull.h>,' \
  meshlab-%{version}/src/meshlabplugins/filter_qhull/qhull_tools.h
%endif

echo 'linux-g++:QMAKE_CXXFLAGS   +=  -fpermissive' >> meshlab-%{version}/src/general.pri
echo "linux-g++:DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x000000" >> meshlab-%{version}/src/general.pri
echo "linux-g++:DEFINES += __DISABLE_AUTO_STATS__" >> meshlab-%{version}/src/general.pri

sed -i 's|PLUGIN_DIR|QString("%{_libdir}/%{name}")|g'  meshlab-%{version}/src/common/pluginmanager.cpp

%build
# Build instructions from the wiki:
#   http://meshlab.sourceforge.net/wiki/index.php/Compiling_V122
# Note that the build instructions in README.linux are out of date.

cd meshlab-%{version}/src/external
%{qmake_qt5} -recursive external.pro
# Note: -fPIC added to make jhead link properly; don't know why this wasn't
# also an issue with structuresynth
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"
cd ..
%{qmake_qt5} -recursive meshlab_full.pro || :
make %{?_smp_mflags} CFLAGS="%{optflags} -fpermissive"
# DEFINES="-DMESHLAB_SCALAR=float -DQT_DISABLE_DEPRECATED_BEFORE=0x000000 -D__DISABLE_AUTO_STATS__ -DPLUGIN_DIR=\\\"%{_libdir}/%{name}\\\""

# process icon
convert %{SOURCE1} meshlab.png

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;
EOF

%install
# The QMAKE_RPATHDIR stuff puts in the path to the compile-time location
# of libcommon, which won't work at runtime, so we change the rpath here.
# The use of rpath will cause an rpmlint error, but the Fedora Packaging
# Guidelines specifically allow use of an rpath for internal libraries:
# http://fedoraproject.org/wiki/Packaging:Guidelines#Rpath_for_Internal_Libraries
# Ideally upstream would rename the library to libmeshlab, libmeshlabcommon,
# or the like, so that we could put it in the system library directory
# and avoid rpath entirely.
chrpath -r %{_libdir}/meshlab meshlab-%{version}/src/distrib/{meshlab,meshlabserver}

install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 meshlab-%{version}/src/distrib/meshlab \
		  meshlab-%{version}/src/distrib/meshlabserver \
		  %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 meshlab-%{version}/docs/meshlab.1 \
		  meshlab-%{version}/docs/meshlabserver.1 \
		  %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_libdir}/meshlab
install -p -m 755 meshlab-%{version}/src/distrib/libcommon.so.1.0.0 \
		  %{buildroot}%{_libdir}/meshlab
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so.1.0
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so.1
ln -s libcommon.so.1.0.0 %{buildroot}%{_libdir}/meshlab/libcommon.so

install -d -m 755 %{buildroot}%{_libdir}/meshlab/plugins
install -p -m 755 meshlab-%{version}/src/distrib/plugins/*.{so,xml} \
		  %{buildroot}%{_libdir}/meshlab/plugins

install -d -m 755 %{buildroot}%{_datadir}/meshlab/shaders
install -p -m 644 meshlab-%{version}/src/distrib/shaders/*.{frag,gdp,vert} \
		  %{buildroot}%{_datadir}/meshlab/shaders

install -d -m 755 %{buildroot}%{_datadir}/meshlab/shaders/shadersrm
install -p -m 644 meshlab-%{version}/src/distrib/shaders/shadersrm/*.rfx \
		  %{buildroot}%{_datadir}/meshlab/shaders/shadersrm

install -d -m 755 %{buildroot}%{_datadir}/meshlab/textures

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -p -m 644 meshlab-%{version}/src/meshlab.png \
		  %{buildroot}%{_datadir}/pixmaps

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 meshlab-%{version}/src/meshlab.desktop \
		  %{buildroot}%{_datadir}/applications

desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

%ldconfig_scriptlets

%files
%{_bindir}/meshlab
%{_bindir}/meshlabserver
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_mandir}/man1/*.1.*
%license meshlab-%{version}/LICENSE.txt
%doc meshlab-%{version}/README.md
%doc meshlab-%{version}/docs/meshlabserver.1.txt
%doc meshlab-%{version}/docs/meshlab.1.txt
%doc meshlab-%{version}/docs/privacy.txt
%doc meshlab-%{version}/docs/README.linux
%doc meshlab-%{version}/docs/readme.txt
%license meshlab-%{version}/src/distrib/shaders/3Dlabs-license.txt
%license meshlab-%{version}/src/distrib/shaders/LightworkDesign-license.txt
%license meshlab-%{version}/src/meshlabplugins/filter_poisson/license.txt
%license meshlab-%{version}/src/plugins_experimental/filter_segmentation/license.txt
%{_datadir}/applications/meshlab.desktop
%{_datadir}/pixmaps/meshlab.png

%changelog
* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 2016.12-12
- rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2016.12-8
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.12-6
- Fix Screened Poisson Surface Reconstruction filter (RHBZ#1559137) (again)

* Thu Mar 22 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.12-5
- Fix Screened Poisson Surface Reconstruction filter (RHBZ#1559137)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Tom Callaway <spot@fedoraproject.org> 2016.12-1
- update to 2016.12

* Tue Jul 18 2017 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-13
- Fix FTBFS (RHBZ#1423936, RHBZ#1439673), exclude ppc64 arches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-11
- Rebuild for glew 2.0.0

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.2-10
- Compile with -std=gnu++98 to work around c++14 incompatibilities
  (F24FTBFS, RHBZ#1305224).
- Rebuild for qhull-2015.2-1.

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-9
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.3.2-8
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.3.2-3
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Eric Smith <eric@brouhaha.com> - 1.3.2-1
- Update to upstream 1.3.2.
- Updated Patch0.
- Patch7 (argcref) no longer needed, fixed upstream.
- Patch8 (gcc47) no longer needed, mostly fixed upstream.
- Patch9 added, see Debian bug 667276, previously handled in patch8, but
  unclear whether it was correct.
- Patch10 by Miro Hrončok added to fix another incompatibility with GCC 4.7.
- Patch11 by Jon Ciesla to fix include paths to prevent debugedit complaints.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.3.1-8
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 1.3.1-7
- -Rebuild for new glew

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Eric Smith <eric@brouhaha.com> - 1.3.1-5
- Add new patch to resolve incompatibility with GCC 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Eric Smith <eric@brouhaha.com> - 1.3.1-2
- Add new patch to avoid crash due to mishandling of argc

* Fri Oct 21 2011 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-1
- Update to 1.3.1
- Rebase patches
- Add new patches to add needed includes and disable openctm support until
  openctm is packaged

* Wed Oct 05 2011 Eric Smith <eric@brouhaha.com> - 1.3.0a-2
- removed bundled qtsoap, use shared library from Fedora package
- fix rpath handling for internal-only library

* Wed Aug 03 2011 Eric Smith <eric@brouhaha.com> - 1.3.0a-1
- update to latest upstream release
- added patch from Teemu Ikonen to fix FTBFS
- added patch from Teemu Ikonen to fix reading of .ply files in comma
  separator locales

* Tue Oct 05 2010 jkeating - 1.2.2-5.1
- Rebuilt for gcc bug 634757

* Fri Sep 10 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-5
- Remove direct invocation of constructor to make GCC 4.5 happy

* Mon May  3 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-4
- in prep, remove bundled getopt library sources, to ensure
  that we're using the system library instead
- include doc tag for poisson filter license.txt
- add BSD to license tag
- correct typo in comment in spec

* Wed Apr  7 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-3
- updates based on pre-review comments by Jussi Lehtola

* Tue Apr  6 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-2
- updates based on pre-review comments by Martin Gieseking

* Tue Feb  2 2010 Eric Smith <eric@brouhaha.com> - 1.2.2-1
- initial version
