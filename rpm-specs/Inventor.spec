#
# Copyright (c) 2004-2019 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           Inventor
Version:        2.1.5
Release:        73%{?dist}

Summary:        SGI Open Inventor (TM)

License:        LGPLv2+
URL:            http://oss.sgi.com/projects/inventor/
Source0:        ftp://oss.sgi.com/projects/inventor/download/inventor-2.1.5-10.src.tar.gz

Patch1:         0001-Inventor-2.1.5-30.patch
Patch2:         0002-Inventor-2.1.5-30-31.patch
# GCC44 compatibility hacks
Patch3:         0003-Inventor-2.1.5-31-32.patch
# Misc C++ modernization stuff
Patch4:         0004-Inventor-2.1.5-32-33.patch
# s390x, aarch64 fixes
Patch5:         0005-Import-Inventor-2.1.5-s390x.patch
# Indirect linkage fixes
Patch6:         0006-Inventor-2.1.5-33-38.patch
# DSO loader fix.
Patch7:         0007-Address-RH-BZ-433154.patch
# GCC-4.7 FTBFS hacks
Patch8:         0008-GCC-4.7-FTBFS-hacks.patch
# GCC-6.0 FTBFS hacks
Patch9:         0009-Use-fabs-instead-of-abs-macros.patch
# freetype > 2.6.3 compatibility hacks
Patch10:        0010-freetype-2.6.3-compatibility-hacks.patch
# Add aarch64, remove USE_64BIT_HACKS
Patch11:        0011-Add-aarch64.patch


# Inventor is not aliasing-safe.
# Inventor presumes unsigned chars.
%global hackcxxflags -O2 -fno-strict-aliasing -funsigned-char

BuildRequires:  libGLU-devel
BuildRequires:  libGLw-devel
# FIXME: Why is libXi required?
BuildRequires:  libXi-devel

BuildRequires:  gcc-c++

BuildRequires:  motif-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  bison
BuildRequires:  /bin/csh
BuildRequires:  /usr/bin/xdg-open

%if 0%{fedora} > 30
%define fontserif -serif
%define fontsans  -sans
%define fontmono  -mono
%else
%define fontserif %{nil}
%define fontsans  %{nil}
%define fontmono  %{nil}
%endif

# fonts
BuildRequires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Regular.ttf
BuildRequires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Bold.ttf
BuildRequires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Italic.ttf
BuildRequires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-BoldItalic.ttf
BuildRequires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Regular.ttf
BuildRequires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Bold.ttf
BuildRequires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Italic.ttf
BuildRequires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-BoldItalic.ttf
BuildRequires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Regular.ttf
BuildRequires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Bold.ttf
BuildRequires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Italic.ttf
BuildRequires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-BoldItalic.ttf

Requires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Regular.ttf
Requires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Bold.ttf
Requires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Italic.ttf
Requires: /usr/share/fonts/liberation%{fontserif}/LiberationSerif-BoldItalic.ttf
Requires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Regular.ttf
Requires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Bold.ttf
Requires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-Italic.ttf
Requires: /usr/share/fonts/liberation%{fontsans}/LiberationSans-BoldItalic.ttf
Requires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Regular.ttf
Requires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Bold.ttf
Requires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-Italic.ttf
Requires: /usr/share/fonts/liberation%{fontmono}/LiberationMono-BoldItalic.ttf

%description
SGI Open Inventor(TM) is an object-oriented 3D toolkit offering a
comprehensive solution to interactive graphics programming
problems. It presents a programming model based on a 3D scene database
that dramatically simplifies graphics programming. It includes a rich
set of objects such as cubes, polygons, text, materials, cameras,
lights, trackballs, handle boxes, 3D viewers, and editors that speed
up your programming time and extend your 3D programming capabilities.


%package        devel
Summary:        SGI Open Inventor (TM) development files
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libGLU-devel
Requires:       freetype-devel libjpeg-devel

%description    devel
SGI Open Inventor (TM) development files.

%package        -n InventorXt
Summary:        SGI Open Inventor (TM) Motif bindings
Requires:       %{name} = %{version}-%{release}
Requires:       %{_bindir}/xmessage
Requires:       /usr/bin/xdg-open

%description    -n InventorXt
SGI Open Inventor (TM) development files.

%package        -n InventorXt-devel
Summary:        SGI Open Inventor (TM) Motif bindings
Requires:       %{name} = %{version}-%{release}
Requires:       InventorXt = %{version}-%{release}
Requires:       Inventor-devel = %{version}-%{release}
Requires:       pkgconfig
Requires:       motif-devel

%description    -n InventorXt-devel
SGI Open Inventor (TM) development files.

%package        demos
Summary:        SGI Open Inventor (TM) Demos
Requires:       %{name}-data

%description    demos
SGI Open Inventor (TM) demos.

%package        data
Summary:        SGI Open Inventor (TM) data
BuildArch:      noarch

%description    data
SGI Open Inventor data files.

%package        examples
Summary:        SGI Open Inventor (TM) source code examples
# Should we once ship binary examples, this requirement can be dropped
Requires:       InventorXt-devel

%description    examples
SGI Open Inventor (TM) Source Examples from the Inventor books
"The Inventor Mentor" and "The Inventor Toolmaker".

%prep
%setup -q -n inventor
find -name CVS | xargs rm -rf
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

sed -i \
-e 's,^IVPREFIX =.*$,IVPREFIX = %{_prefix},' \
-e 's,^_BINDIR =.*$,_BINDIR = %{_bindir},' \
-e 's,^_LIBDIR =.*$,_LIBDIR = %{_libdir},' \
-e 's,^_HDRTOP =.*$,_HDRTOP = %{_includedir}/Inventor,' \
-e 's,^_MAN1DIR =.*$,_MAN1DIR = %{_mandir}/man1,' \
-e 's,^_MAN3DIR =.*$,_MAN3DIR = %{_mandir}/man3,' \
-e 's,^_FONTPATH =.*$,_FONTPATH = %{_datadir}/Inventor/fonts,' \
-e 's,^_HELPDIR =.*$,_HELPDIR = %{_datadir}/Inventor/help,' \
-e 's,^_DATADIR =.*$,_DATADIR = %{_datadir}/Inventor/data/models,' \
-e 's,^_MATERIALSDIR =.*$,_MATERIALSDIR = %{_datadir}/Inventor/data/materials,' \
-e 's,^_TEXTURESDIR =.*$,_TEXTURESDIR = %{_datadir}/Inventor/data/textures,' \
-e 's,^_DEMOBINDIR =.*$,_DEMOBINDIR = %{_libdir}/Inventor,' \
-e 's,^_DEMODATADIR =.*$,_DEMODATADIR = %{_datadir}/Inventor/data/demos,' \
-e 's,^OPTIMIZER = -O -DNDEBUG,OPTIMIZER = -DNDEBUG,' \
-e 's,(X11DIR)/lib,(X11DIR)/%_lib,g' \
-e 's,_PDFVIEWER = xpdf,_PDFVIEWER = /usr/bin/xdg-open,' \
make/ivcommondefs

for i in apps/demos/*/*.RUNME; do \
  sed -i \
    -e 's,/usr/share/inventor/,%{_datadir}/Inventor/,g' \
    -e 's,/usr/lib/inventor/,%{_libdir}/Inventor/,g' \
    $i
done

for i in *.pc.in; do
  sed \
    -e 's,@prefix@,%_prefix,g' \
    -e 's,@exec_prefix@,%_exec_prefix,g' \
    -e 's,@includedir@,%_includedir,g' \
    -e 's,@libdir@,%_libdir,g' \
    -e 's,X11R6/lib,X11R6/%_lib,g' \
    < $i > $(basename $i .in)
done

rm -f data/models/scenes/chesschairs.iv

chmod -x apps/examples/Toolmaker/08.Manips/README


%build
# Inventor's build system wants us to install and build everything at once.
export LD_LIBRARY_PATH=${RPM_BUILD_ROOT}%{_libdir}
export VCOPTS="${RPM_OPT_FLAGS} -D_REENTRANT"
export VCXXOPTS=$(echo "${RPM_OPT_FLAGS} -D_REENTRANT -D__STDC_FORMAT_MACROS" | sed -e 's,-O2,%{hackcxxflags},')
make all \
  FREETYPE=1 IVROOT=${RPM_BUILD_ROOT} \
  LSUBDIRS="libimage tools libFL"
make install \
  FREETYPE=1 IVROOT=${RPM_BUILD_ROOT}
  LSUBDIRS="lib libSoXt"
make all \
  FREETYPE=1 IVROOT=${RPM_BUILD_ROOT} BUILDMAN=1 \
  LSUBDIRS="doc apps data"

# convert Mentor and Toolmaker examples into a standalone package
rm -rf devel-docs
cp -a apps/examples devel-docs
cp -a make devel-docs
pushd devel-docs > /dev/null
find -name 'GNUmakefile*' | while read a; do \
  b=`echo $a | sed 's,GNUmakefile.*$,,;s,^\./,,;s,[^/]*/,../,g;s,\/$,,;s,^$,.,'`
  sed -i -e "s,^IVDEPTH = .*$,IVDEPTH = $b," $a
done
find -name '*.c++' | while read a; do \
  sed -i -e "s,/usr/share/src/Inventor/examples/data,%{_libdir}/Inventor/examples/data,g" $a
done
sed -i -e '/^IVLIBHDRDIRS.*/,/libSoXt\/include/c\
IVLIBHDRS = `pkg-config --cflags libInventorXt`' \
make/ivcommondefs
make clean
popd > /dev/null

%install
export LD_LIBRARY_PATH=${RPM_BUILD_ROOT}%{_libdir}
export VCOPTS="${RPM_OPT_FLAGS} -D_REENTRANT"
export VCXXOPTS="${RPM_OPT_FLAGS} -D_REENTRANT"
make install \
  FREETYPE=1 IVROOT=${RPM_BUILD_ROOT} BUILDMAN=1

install -d -m755 ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install -m644 libInventor.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install -m644 libInventorXt.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

install -d -m755 ${RPM_BUILD_ROOT}%{_libdir}/Inventor
mv devel-docs ${RPM_BUILD_ROOT}%{_libdir}/Inventor/examples

install -d -m755 ${RPM_BUILD_ROOT}%{_datadir}/Inventor/data/materials
install -d -m755 ${RPM_BUILD_ROOT}%{_datadir}/Inventor/data/textures
install -d -m755 ${RPM_BUILD_ROOT}%{_datadir}/Inventor/fonts

# Map Inventor's standard fonts
# Utopia, Helvetica and Courier to liberation-TTF fonts
# Times-Roman is being used by some examples
pushd ${RPM_BUILD_ROOT}%{_datadir}/Inventor/fonts > /dev/null
ln -s Utopia-Regular Times-Roman
ln -s /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Regular.ttf Utopia-Regular
ln -s /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Bold.ttf Utopia-Bold
ln -s /usr/share/fonts/liberation%{fontserif}/LiberationSerif-Italic.ttf Utopia-Italic
ln -s /usr/share/fonts/liberation%{fontserif}/LiberationSerif-BoldItalic.ttf Utopia-BoldItalic
ln -s /usr/share/fonts/liberation%{fontsans}/LiberationSans-Regular.ttf Helvetica
ln -s /usr/share/fonts/liberation%{fontsans}/LiberationSans-Bold.ttf Helvetica-Bold
ln -s /usr/share/fonts/liberation%{fontsans}/LiberationSans-Italic.ttf Helvetica-Oblique
ln -s /usr/share/fonts/liberation%{fontsans}/LiberationSans-BoldItalic.ttf Helvetica-BoldOblique
ln -s /usr/share/fonts/liberation%{fontmono}/LiberationMono-Regular.ttf Courier
ln -s /usr/share/fonts/liberation%{fontmono}/LiberationMono-Bold.ttf Courier-Bold
ln -s /usr/share/fonts/liberation%{fontmono}/LiberationMono-Italic.ttf Courier-Oblique
ln -s /usr/share/fonts/liberation%{fontmono}/LiberationMono-BoldItalic.ttf Courier-BoldOblique
popd > /dev/null

%ldconfig_scriptlets

%files
%doc README.FIRST KNOWN.BUGS FAQ.misc
%license COPYING
%{_bindir}/iv2toiv1
%{_bindir}/ivcat
%{_bindir}/ivdowngrade
%{_bindir}/ivfix
%{_bindir}/ivinfo
%{_bindir}/ivnorm
%{_bindir}/ivAddVP
%{_libdir}/libInventor.so.*
%dir %{_datadir}/Inventor
%{_datadir}/Inventor/fonts
%{_mandir}/man1/inventor.*
%{_mandir}/man1/iv2toiv1.*
%{_mandir}/man1/ivcat.*
%{_mandir}/man1/ivdowngrade.*
%{_mandir}/man1/ivfix.*
%{_mandir}/man1/ivinfo.*

%files devel
%dir %{_includedir}/Inventor
%{_includedir}/Inventor/[^X]*
%{_libdir}/libInventor.so
%{_libdir}/pkgconfig/libInventor.pc
%{_mandir}/man3/Sb*
%{_mandir}/man3/So[^X]*


%ldconfig_scriptlets -n InventorXt

%files -n InventorXt
%{_bindir}/SceneViewer
%{_bindir}/ivview
%{_bindir}/ivperf
%{_mandir}/man1/SceneViewer.*
%{_mandir}/man1/ivview.*
%{_libdir}/libInventorXt.so.*
%dir %{_datadir}/Inventor
# Used by libInventorXt
%{_datadir}/Inventor/help
# Used by SceneViewer
%dir %{_datadir}/Inventor/data
%dir %{_datadir}/Inventor/data/materials
%dir %{_datadir}/Inventor/data/textures

%files -n InventorXt-devel
%dir %{_includedir}/Inventor
%{_includedir}/Inventor/Xt
%{_libdir}/libInventorXt.so
%{_libdir}/pkgconfig/libInventorXt*.pc
%{_mandir}/man3/SoXt*

%files data
%license COPYING
%dir %{_datadir}/Inventor
%dir %{_datadir}/Inventor/data
%{_datadir}/Inventor/data/models
%{_datadir}/Inventor/data/materials
%{_datadir}/Inventor/data/textures

%files demos
%dir %{_datadir}/Inventor
%dir %{_datadir}/Inventor/data
%{_datadir}/Inventor/data/demos
%dir %{_libdir}/Inventor
%{_libdir}/Inventor/[^e]*

%files examples
%dir %{_libdir}/Inventor
%{_libdir}/Inventor/examples

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-71
- Reflect liberation fontpaths having changed (F31FTBS RHBZ#1734886).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-68
- Add BR: gcc-c++ (RHBZ#1603273).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-62
- Switch to using xdg-open instead of xpdf as PDFVIEWER.
- Spec cleanup.

* Wed Nov 16 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-61
- Add 0010-freetype-2.6.3-compatibility-hacks.patch (F25FTBFS, RHBZ#1372348).
- Add 0011-Add-aarch64.patch (F26FTBFS).

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-60
- Use fabs instead of abs (Fix F24FTBFS).
  Add 0009-Use-fabs-instead-of-abs-macros.patch.
- Rebase patches.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-58
- Add %%license.

* Sat Dec 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-57
- Eliminate %%define.

* Thu Oct 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-56
- Remove dnf hack.

* Tue Oct 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-55
- Remove openmotif.
- Add hack to work-around mock w/ dnf's brokenness.
  (RHBZ#1271053, https://fedorahosted.org/rel-eng/ticket/6276)

* Thu Oct 01 2015 Jon Ciesla <limburgher@gmail.com> - 2.1.5-54
- Move from lesstif to motif.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.5-52
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.1.5-50
- Fix FTBFS on aarch64

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-48
- Modernize spec.
- Fix bogus %%changelog dates.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.1.5-45
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.1.5-44
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 08 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-41
- Modernize spec file.
- Add -funsigned-char to CXXFLAGS.
- Add Inventor-2.1.5-41.patch (Address gcc-4.7 FTBFS).
- Add Inventor-2.1.5-bz433154.patch (Address BZ433154).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-39
- Make Inventor-data a noarch subpackage.
- Add COPYING to Inventor-data.

* Fri Feb 12 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-38
- Add Inventor-2.1.5-33-38.diff (Address indirect DSO linkage issues).

* Wed Nov 11 2009 Dennis Gilmore <dennis@ausil.us> - 2.1.5-37
- apply s390x patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-34
- Add Inventor-2.1.5-31-32.diff.
- Add Inventor-2.1.5-32-33.diff.

* Tue Jun 03 2008 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-33
- Add -fnostrict-aliasing to VCXXOPTS to work around GCC-4.3 breakage.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.5-32
- Autorebuild for GCC 4.3

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-31
- Spec file cleanup.
- Introduce --with openmotif.
- Add Inventor-2.1.5-30-31.diff.

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-30.1
- Add hard-coded deps on font files (BZ 388761).
- Switch to using liberation-fonts instead of dejavu-fonts.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-30
- Apply major hacks (*-30.diff) to address BZ: 245192.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-29
- Update license tag.

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-28
- ExcludeArch: ppc64 (BZ: 245192).

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-27
- Add *-27.patch.
- Remove _ia64 grep (Incorporated into *-27.diff).
- Add powerpc64 hack.

* Wed Mar 14 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-26
- Use dejavu-fonts as fonts.
- Attempt to fix BZ 232017.

* Tue Feb 13 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-25
- Specfile fixes.

* Tue Oct 03 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-24
- Specfile cosmetics.
- Use %%{_datadir}/Inventor instead of %%{_datadir}/%%{name}
- Fix dep on xmessage for FC4.
- Add %%{_datadir}/Inventor/data/materials.
- Add %%{_datadir}/Inventor/fonts.

* Mon Oct 02 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-23
- Add make-var _PDFVIEWER.
- Backport to FC4.
- Fix path to chessboard.iv in chesschairs.iv.

* Thu Sep 28 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-22
- Misc minor fixes.
- Add dep to xmessage.
- Use unified patch.
- Rebuild against lesscrap.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-21
- Mass rebuild.

* Sun Feb 19 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-20
- Rebuild.

* Fri Dec 30 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-19
- Don't BR: libXau-devel (#176313 reported to be fixed).

* Wed Dec 28 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-18
- Remove patch10 (#173879, #175251 are reported to be fixed).

* Thu Dec 22 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-17
- Remove BR: libX11-devel (#173712 reported to be fixed).
- Remove BR: libGL-devel (#175253 reported to be fixed).

* Wed Dec 14 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-16
- Remove BR: libXext-devel (Impl. R'd by openmotif-devel).
- Remove BR: xorg-x11-proto-devel (PR #175256).

* Thu Dec 8 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-15
- Further modular X fixes.
- Reflect modular X pkgconfigs.

* Thu Dec 8 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-14
- Attempt to build against modular X.
- Add Inventor-redhat-bugs patch.

* Tue Aug 02 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-13
- Let PPC use standard RPM_OPT_FLAGS.

* Tue Aug 02 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-12
- Add SoTempPath fix.

* Sun May 22 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-9
- Increment release in an attempt to please build system.

* Sun May 22 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-8
- Use BR: xorg-x11-* instead of *.so.1 to work around rpm's brain-dead
  SONAME handling.
- Add %%dist.
- Use sed -i to avoid temporary files.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 16 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.1.5-7
- Add specfile-patch from Andy Loening to fix build on x86_64 (rhb#147267)

* Mon Feb 14 2005 David Woodhouse <dwmw2 infradead org> - 2.1.5-6
- Work around gcc bug by backing down to -O1 on ppc

* Mon Sep 6 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.5
- Add ivAddVP ivnorm ivperf to Inventor rsp. InventorXt.
- Remove BuildRequires: tcsh.

* Sun Aug 8 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.4
- Split out InventorXt, InventorXt-devel, Inventor-examples
- make/ivcommondefs: Remove -O from $OPTIMIZER.
- Various changes to libInventor.pc and libInventorXt.pc.

* Wed Jul 7 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.3
- Remove Mesa-Requires.
- Add pkgconfig support.
- Add various Requires: to *devel.
- Add Provides: InventorXt and InventorXt-devel.

* Thu Jul 1 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.2
- Adopt portions of Michael Schwendt's patch.
- Fix hard-coded paths in apps/demos/*.RUNMEs.
- Use %%{_prefix}/lib instead of %%{_libdir} to install the demos into.
- Add make/ to devel docs.
- Hack devel docs to be buildable.

* Wed Jun 30 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.1
- Initial Fedora Extras RPM.
- Adopt Debian/Testing patches (Thanks to Steve M. Robbins for keeping
  Inventor alive).
