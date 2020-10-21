Name:           permlib
Version:        0.2.9
Release:        13%{?dist}
Summary:        Library for permutation computations

License:        BSD
URL:            https://github.com/tremlin/PermLib
Source0:        https://github.com/tremlin/PermLib/archive/v%{version}/%{name}-%{version}.tar.gz
# Doxygen config file written by Jerry James <loganjerry@gmail.com>
Source1:        %{name}-Doxyfile
# Fix gcc 6 build failure
Patch0:         %{name}-0.2.8-gcc6.patch
# Adapt to changes in recent versions of boost
Patch1:         %{name}-0.2.9-boost.patch
BuildArch:      noarch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dvipng
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  tex(newunicodechar.sty)

%description
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

%package devel
Summary:        Header files for developing programs that use PermLib
Requires:       boost-devel
Provides:       bundled(jquery)

%description devel
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

This package contains header files for developing programs that use
PermLib.

%prep
%autosetup -p0 -n PermLib-%{version}
sed "s/@VERSION@/%{version}/" %{SOURCE1} > Doxyfile

%build
%cmake
%cmake_build

# Build the documentation
mkdir doc
doxygen
rm -f doc/html/installdox

%install
# No install target is generated in the makefile, and
# DESTDIR=$RPM_BUILD_ROOT cmake -P cmake_install.cmake
# does nothing, so we do it by hand.

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include/%{name} $RPM_BUILD_ROOT%{_includedir}

%check
%ctest

%files devel
%doc AUTHORS CHANGELOG doc/html
%license LICENSE
%{_includedir}/permlib

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Jerry James <loganjerry@gmail.com> - 0.2.9-10
- Add -boost patch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.9-8
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-5
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-4
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-2
- Rebuilt for Boost 1.63
- Make build reproducible by removing %%{?_isa} on Requires.

* Wed Jul 20 2016 Jerry James <loganjerry@gmail.com> - 0.2.9-1
- New upstream release
- Update Doxyfile
- Drop upstreamed boost patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-14
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.8-12
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.2.8-10
- Update URLs
- Note bundled jquery
- Use license macro

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.2.8-9
- Rebuild for boost 1.57.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.8-7
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.2.8-5
- Rebuild for boost 1.54.0
- Remove -mt suffix from boost_unit_testing_framework DSO
  (permlib-0.2.8-boost_mt.patch)

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-3
- Rebuild for Boost-1.53.0

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 0.2.8-2
- Adjust BRs for TeXLive 2012

* Thu Sep 27 2012 Jerry James <loganjerry@gmail.com> - 0.2.8-1
- New upstream release
- Drop upstreamed patch

* Wed Sep 26 2012 Jerry James <loganjerry@gmail.com> - 0.2.7-1
- New upstream release
- Update Doxyfile
- Add -test patch to fix two test failures

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-4
- Rebuild for boost 1.50
- Update Doxyfile

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- BR gmp-devel
- Add comment on origin of Doxyfile

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
