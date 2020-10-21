%undefine __cmake_in_source_build
%global abiversion 4.3

Name:           stage
Version:        4.3.0
Release:        4%{?dist}
Summary:        A 2.5D multi-robot simulator

License:        GPLv2+
URL:            http://playerproject.github.io
Source0:        https://github.com/rtv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This patch installs the Player plugin to libdir/player instead of libdir
Patch0:         Stage-4.0.0.plugininstall.patch
Patch5:         stage-4.3.0-libdir.patch
Patch6:         stage-4.3.0-printf.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fltk-devel
BuildRequires:  graphviz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libXext-devel
BuildRequires:  libX11-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  player-devel >= 3.1.0

%description
Stage is a fast and scalable 2.5D multiple robot simulator from the Player
project.  Stage can be used to simulate sensors and actuators in a
low-fidelity bit-mapped environment.  Stage models can be controlled with
the Stage C API, or through the Player server via a Player plug-in library.

%package devel
Summary: Header files and libraries for Stage
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fltk-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libGL-devel
Requires: libGLU-devel

%description devel
This package contains the header files and libraries
for Stage. If you want to develop programs using the libstage
API, you will need to install stage-devel.

%package -n player-%{name}
Summary: Plug-in to add Stage support to Player
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: player%{?_isa} >= 3.1.0
# until f28
Obsoletes: %{name}-playerplugin < 4.1.1-15
Provides:  %{name}-playerplugin%{_isa} = %{version}-%{release}

%description -n player-%{name}
This package contains the Stage plug-in library for the Player server.
stage-playerplugin allows Stage models to be exposed as Player interfaces,
and manipulated through the Player server.

%prep
%setup -q -n Stage-%{version}
%patch0 -p0
%patch5 -p1 -b .libdir
%patch6 -p1 -b .printf

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

# Documentation builds separately
pushd docsrc
make
mv stage html
popd

%install
%cmake_install
chmod +x %{buildroot}%{_datadir}/stage/worlds/*.sh

# These config files are broken, remove them
rm %{buildroot}%{_datadir}/stage/worlds/uoa*
rm %{buildroot}%{_datadir}/stage/worlds/large.world
rm -rf %{buildroot}%{_datadir}/stage/worlds/wifi*

%ldconfig_scriptlets

%files
%license COPYING.txt
%doc DESCRIPTION.txt README.md RELEASE.txt AUTHORS.txt
%{_bindir}/stage
%{_libdir}/*.so.*
%{_datadir}/stage
%{_libdir}/Stage-%{abiversion}

%files -n player-%{name}
%{_libdir}/player-3.1/*.so

%files devel
%doc docsrc/html
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Stage
%{_includedir}/Stage-%{abiversion}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Rich Mattes <richmattes@gmail.com> - 4.3.0-1
- Update to release 4.3.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.1.1-21
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 4.1.1-16
- Rebuild for player-3.1.0
- Clean up specfile
- Rename player plugin package

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 03 2016 Rich Mattes <richmattes@gmail.com> - 4.1.1-14
- Fix gcc6 FTBFS (rhbz#1308151)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.1-12
- Fix all 64 bit arches with single patch (s390x, aarch64, ppc64le)

* Wed Apr 29 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 4.1.1-11
- AArch64 is 64bit too

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.1.1-10
- rebuild (fltk)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 4.1.1-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.1.1-4
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Rich Mattes <richmattes@gmail.com> - 4.1.1-1
- Update to release 4.1.1
- Cleanup old patches

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2.0e7f6agit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 29 2011 Rich Mattes <richmattes@gmail.com> - 4.0.1-1.0e7f6agit
- Latest git snapshot

* Sun May 29 2011 Rich Mattes <richmattes@gmail.com> - 4.0.0-4
- Rebuild for FLTK

* Wed May 04 2011 Dan Horák <dan[at]danny.cz> - 4.0.0-3
- Fix typos causing s390x build to fail

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Rich Mattes <richmattes@gmail.com> - 4.0.0-1
- New release: Stage 4.0.0

* Sun Mar 14 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-7
- Merged -doc subpackage into -devel
- Added Requires pkgconfig entries

* Wed Mar 10 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-6
- Remove conflicting compiler flags

* Tue Mar 9 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-5
- Remove broken world files

* Sun Feb 28 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-4
- Fixed DSO link errors for F13
- Added necessary requires for -devel package
- Corrected Sourceforge download link

* Thu Feb 4 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-3
- More specfile cleanup

* Mon Jan 18 2010 Rich Mattes <richmattes@gmail.com> - 3.2.2-2
- Spec file cleanup
- License fixed

* Wed Sep 23 2009 Rich Mattes <richmattes@gmail.com> - 3.2.2-1
- First build
