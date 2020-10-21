Name:		libinstpatch
Summary:	MIDI instrument patch library
Version:	1.0.0
Release:	22.20110806svn386%{?dist}
URL:		http://www.swamiproject.org/
License:	LGPLv2+
# Fetch source via
# sh libinstpatch-snapshot.sh 386
Source0:	libinstpatch-%{version}-svn386.tar.bz2
# script to download sources and make tarball from svn
Source1:	libinstpatch-snapshot.sh
# .pc file fixes. Patch sent upstream via their mailing list
Patch0:		libinstpatch-cmake-fixes.patch

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	libsndfile-devel
 

%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument "patch" files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.


%package devel
Summary:	Development package for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	libsndfile-devel

%description devel
This package includes the development libraries and header files for
%{name}.


%prep
%setup -q
%patch0 -p1 -b .pkgconfig


%build
%cmake
%cmake_build

%install
%cmake_install
%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}*.so.*


%files devel
%doc examples/create_sf2.c
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc


%changelog
* Mon Aug 03 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.0.0-22.20110806svn386
- Fix for new cmake macros
- Resolves: #1864003

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21.20110806svn386
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-3.20110806svn386
- Include the COPYING file. oops.
- Fix main package Requires of the devel package

* Sat Aug 06 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-2.20110806svn386
- Update to svn after upstream accepted our build patches, switched to cmake and fixed the licensing
- Prepare for submission for review

* Wed Oct 27 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-1
- Update to 1.0.0

* Thu Mar 26 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-0.1.297svn
- Initial Fedora build
