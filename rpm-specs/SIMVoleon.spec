#
# Copyright (c) 2004-2015 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Summary: Volume rendering library for Coin
Name: SIMVoleon
Version: 2.0.3
Release: 5%{?dist}

License: GPLv2
URL: http://www.coin3d.org

Source: https://bitbucket.org/Coin3D/simvoleon/downloads/simvoleon-%{version}-src.zip

# bash-4 compatibility bugfix
Patch0: SIMVoleon-2.0.1-bash4.0.diff

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: Coin4-devel
BuildRequires: SoQt-devel
BuildRequires: doxygen

Provides: Coin4-SIMVoleon = %{version}-%{release}

%description
A volume rendering library for Coin.

%package devel
Summary: Development files for SIMVoleon
Requires: %{name} = %{version}-%{release}
Requires: Coin4-devel

Provides: Coin4-SIMVoleon-devel = %{version}-%{release}

%description devel
Development files for SIMVoleon.


%prep
%autosetup -p1 -n simvoleon

chmod +x cfg/doxy4win.pl


%build
mkdir build-%{_build_arch} && pushd build-%{_build_arch}
%cmake -DSIMVOLEON_BUILD_DOCUMENTATION=TRUE \
       -DSIMVOLEON_BUILD_TESTS=FALSE \
       -DSIMVOLEON_BUILD_DOC_MAN=TRUE \
       -S .. -B .

%make_build


%install
cd build-%{_build_arch}
%make_install


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_libdir}/libSIMVoleon*.so.*

%files devel
%{_docdir}/SIMVoleon/html/
%{_includedir}/VolumeViz/
%{_libdir}/libSIMVoleon.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_mandir}/man3/*.gz


%changelog
* Tue Aug 04 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.3-5
- Work around cmake madness (F33FTBFS, RHBZ#1863119).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Update to 2.0.3.
- Move from autotools to CMake based build.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-23
- Eliminate %%define.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-21
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-20
- Add Provides: Coin3-SIMVoleon, Coin3-SIMVoleon.

* Thu Feb 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-19
- Rebuild against Coin3.
- Modernise spec.
- Remove %%optflags and %%__global_ld_flags from *.cfg.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-15
- Modernize spec.
- Update config.{guess,sub} for aarch64 (RHBZ #926532).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-10
- Add SIMVoleon-2.0.1-pivy-hacks.diff, SIMVoleon-2.0.1-bash4.0.diff.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-8
- Rebuild for gcc43.
- Spec-file cosmetics.
- Update copyright.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-7
- Mass rebuild.
- Update license tag.

* Tue Feb 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-6
- Install simvoleon-default.cfg into %%{_prefix}/%%{_lib}

* Mon Feb 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-5
- Filter errant -L%%_libdir from soqt-config.cfg.
- Remove *.la.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-4
- Mass rebuild.

* Tue Feb 28  2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-3
- Rebuild.

* Mon Jan 16  2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-2
- Rebuild.
- Add gcc4.1 patch.
- Spec cleanup.

* Sat May 21  2005 Ralf Corsepius <ralf@links2linux.de> - 2.0.1-1
- FE submission candidate.

* Mon Oct 11  2004 Ralf Corsepius <ralf@links2linux.de> - 0:2.0.0-0.fdr.1
- Upstream update.

* Tue Jul 27  2004 Ralf Corsepius <ralf@links2linux.de> - 0:1.0.0-0.fdr.1
- Initial Fedora RPM.
