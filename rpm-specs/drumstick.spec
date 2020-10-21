%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Summary: C++/Qt5 wrapper around multiple MIDI interfaces
Name:    drumstick
Version: 1.1.3
Release: 5%{?dist}

License: GPLv2+
URL:     http://drumstick.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/drumstick/%{version}%{?svn}/drumstick-%{version}%{?svn}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.1
BuildRequires: alsa-lib-devel desktop-file-utils
BuildRequires: qt5-qtbase-devel >= 5.7
BuildRequires: qt5-qtsvg-devel
BuildRequires: fluidsynth-devel
BuildRequires: pulseaudio-libs-devel
# For building manpages
BuildRequires: docbook-style-xsl /usr/bin/xsltproc
# For building API documents
BuildRequires: doxygen

Obsoletes: aseqmm < %{version}-%{release}
Provides: aseqmm = %{version}-%{release}

%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt5 objects, idioms and style. OSS, network and Fluidsynth
interfaces are also supported by this library.

%package devel
Summary: Developer files for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: aseqmm-devel < %{version}-%{release}
Provides: aseqmm-devel = %{version}-%{release}
%description devel
%{summary}.

%package examples
Summary: Example programs for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: aseqmm-examples < %{version}-%{release}
Provides: aseqmm-examples = %{version}-%{release}
%description examples
This package contains the test/example programs for %{name}.

%package drumgrid
Summary: Drum Grid application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description drumgrid
This package contains the drumgrid application.

%package guiplayer
Summary: MIDI player from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description guiplayer
This package contains the guiplayer application.

%package vpiano
Summary: Virtual piano application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description vpiano
This package contains the vpiano application.


%prep
%setup -q -n %{name}-%{version}%{?svn}

%build
%cmake

%cmake_build
doxygen %{_target_platform}/Doxyfile


%install
%cmake_install
for i in $RPM_BUILD_ROOT%{_datadir}/applications/* ; do
  desktop-file-validate $i
done

%check
# Tests require an alsa system, which may not be available within the mock env
#make %{?_smp_mflags} -C %{_target_platform} test

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/libdrumstick-file.so.*
%{_libdir}/libdrumstick-alsa.so.*
%{_libdir}/libdrumstick-rt.so.*
%{_libdir}/drumstick/
%{_datadir}/mime/packages/%{name}.xml

%files devel
%doc doc/html/*
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/pkgconfig/drumstick-file.pc
%{_libdir}/pkgconfig/drumstick-alsa.pc
%{_libdir}/pkgconfig/drumstick-rt.pc
%{_datadir}/%{name}
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%files examples
%{_bindir}/drumstick-dumpmid
%{_bindir}/drumstick-dumpove
%{_bindir}/drumstick-dumpsmf
%{_bindir}/drumstick-dumpwrk
%{_bindir}/drumstick-metronome
%{_bindir}/drumstick-playsmf
%{_bindir}/drumstick-sysinfo
%{_datadir}/icons/hicolor/16x16/apps/drumstick.png
%{_datadir}/icons/hicolor/32x32/apps/drumstick.png
%{_datadir}/icons/hicolor/48x48/apps/drumstick.png
%{_datadir}/icons/hicolor/64x64/apps/drumstick.png
%{_datadir}/icons/hicolor/scalable/apps/drumstick.svgz
%{_datadir}/man/man1/drumstick-dumpmid.1.gz
%{_datadir}/man/man1/drumstick-dumpove.1.gz
%{_datadir}/man/man1/drumstick-dumpsmf.1.gz
%{_datadir}/man/man1/drumstick-dumpwrk.1.gz
%{_datadir}/man/man1/drumstick-metronome.1.gz
%{_datadir}/man/man1/drumstick-playsmf.1.gz
%{_datadir}/man/man1/drumstick-sysinfo.1.gz

%files drumgrid
%{_bindir}/drumstick-drumgrid
%{_datadir}/applications/drumstick-drumgrid.desktop
%{_datadir}/man/man1/drumstick-drumgrid.1.gz

%files guiplayer
%{_bindir}/drumstick-guiplayer
%{_datadir}/applications/drumstick-guiplayer.desktop
%{_datadir}/man/man1/drumstick-guiplayer.1.gz

%files vpiano
%{_bindir}/drumstick-vpiano
%{_datadir}/applications/drumstick-vpiano.desktop
%{_datadir}/man/man1/drumstick-vpiano.1.gz

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1.3-3
- Rebuild against fluidsynth2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.3-1
- Release 1.1.3

* Mon Jul 29 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.2-2
- Fix build for Fedora 31

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (BZ#1548773)
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 30 2016 Robin Lee <cheeselee@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (BZ#1380040)
- Requires pulseaudio-libs-devel for the eassynth backend
- Dropped drumstick-1.0.2-gcc6.patch
- Filtered auto-provides for plugin shared libraries

* Tue Feb 16 2016 Robin Lee <cheeselee@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (BZ#1294720)
- Fix FTBFS with GCC 6 (BZ#1307433)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Oct 17 2014 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-9
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Richard Hughes <richard@hughsie.com> - 0.5.0-7
- Split out the three applications as seporate packages so they are installable
  in the software center.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-1
- update to 0.5.0
- drumstick-0.3.1-sysinfo-#597354.patch removed
- drumstick-0.3.1-fix-implicit-linking.patch updated to
  drumstick-0.5.0-fix-implicit-linking.patch
- build the manpages and API documents, BR: docbook-style-xsl /usr/bin/xsltproc
  doxygen

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-2
- sysinfo: don't crash when no timer module available (#597354, upstream patch)

* Fri May 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-1
- update to 0.3.1
- fix FTBFS due to the strict ld in Fedora >= 13

* Mon Mar 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.0-1
- update to 0.3.0 release

* Mon Feb 08 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.3.svn20100208
- update from SVN for KMid2 0.2.1

* Sun Jan 31 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.2.svn20100107
- put the alphatag before the disttag

* Fri Jan 29 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.1.svn20100107
- update to 0.2.99svn tarball
- renamed from aseqmm to drumstick by upstream

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-2
- require the main package with exact version-release in -examples

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-1
- First Fedora package
