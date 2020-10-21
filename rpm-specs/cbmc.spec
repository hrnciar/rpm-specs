%undefine __cmake_in_source_build

%define utils_version 1.0
# FIXME: report to upstream
%define _lto_cflags %{nil} 

Name:           cbmc
Version:        5.15.0
Release:        1%{?dist}
Summary:        Bounded Model Checker for ANSI-C and C++ programs

License:        BSD with advertising
URL:            http://www.cprover.org/cbmc/

Source0:        https://github.com/diffblue/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/vmihalko/%{name}-utils/archive/v%{utils_version}/%{name}-utils-%{utils_version}.tar.gz

# Adapt to recent versions of glpk
Patch0:         %{name}-5.9-glpk.patch
# Regression test regression/cpp/virtual0 is failing - hotfix
%if 0%{?fedora} > 32
Patch1:         %{name}-5.12-fix-f33.patch
%endif
# Fedora-specific patch: python => python3 in one test case
Patch2:         %{name}-5.12.6-fix-f33+.patch
# Use minisat from Fedora
Patch3:         %{name}-minisat.patch
Patch4:         %{name}-32bit-arch-fix.patch
Patch5:         %{name}-signed-char.patch


BuildRequires:  bash
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen-latex
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glpk-devel
BuildRequires:  graphviz
BuildRequires:  minisat2-devel
BuildRequires:  zlib-devel

Requires:       gcc-c++
Requires:       sed

%description
CBMC generates traces that demonstrate how an assertion can be violated, or
proves that the assertion cannot be violated within a given number of loop
iterations.

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%package utils
Summary:        Output conversion utilities for CBMC 

%description utils
Output conversion utilities for CBMC (gcc like format) 

%prep
%setup -T -q -b 1 -n %{name}-utils-%{utils_version}
%autosetup -p0  

%build
%cmake -DWITH_JBMC=OFF -DWITH_SYSTEM_SAT_SOLVER=ON -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

# Build the documentation, TODO: build the doc with cmake
make -C src doc

%install
%cmake_install

# Remove useless manpages
rm %{buildroot}%{_mandir}/man1/j{bmc,analyzer,diff}.1 

install -p -m 0755 "%{_builddir}/%{name}-utils-%{utils_version}/cbmc_utils/formatCBMCOutput.py" %{buildroot}%{_bindir}/%{name}-convert-output

# Feed the debuginfo generator
ln -s xml_y.tab.h src/xmllang/xml_y.tab.hpp

%ifarch x86_64
%check
# The tests were written with the assumption that they would be executed on
# an x86_64.  Other platforms suffer a large number of spurious test failures.
%ctest --label-regex CORE
%ctest --tests-regex unit-xfail
%endif

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/{cbmc,goto-{analyzer,cc,diff,instrument,gcc,harness,ld}}
%{_mandir}/man1/*

%files doc
%doc doc/html
%license LICENSE

%files utils
%license ../%{name}-utils-%{utils_version}/LICENSE
%{_bindir}/%{name}-convert-output


%changelog
* Tue Oct 08 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.15.0-1
- New upstream release

* Wed Sep 30 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.14.3-1
- New upstream release

* Tue Sep 29 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.13.1-1
- New upstream release
- Use CMake instead of plain Makefiles
- Add cbmc-utils subpackage 

* Tue Sep 01 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.13.0-1
- New upstream release

* Wed Aug 12 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.12.6-1
- Replace custom goto-cc.1 with symlinks to cbmc.1
- Enable full cbmc testsuite
- python to python3 fix in one test case

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 9  2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.12-1
- New upstream release. Skipping some of regression tests - temporary f33 build fix

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Jerry James <loganjerry@gmail.com> - 5.11-4
- Drop cudd support due to impending cudd retirement

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Jerry James <loganjerry@gmail.com> - 5.11-2
- Fix man page links (bz 1718287)

* Thu Jan 31 2019 Jerry James <loganjerry@gmail.com> - 5.11-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Jerry James <loganjerry@gmail.com> - 5.10-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Jerry James <loganjerry@gmail.com> - 5.9-1
- New upstream release
- Drop upstreamed -float128 and -vec patches
- Musketeer and symex have been removed; do not try to build them

* Mon Jun 11 2018 Jerry James <loganjerry@gmail.com> - 5.8-4
- Fix out of bounds vector accesses

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 5.8-3
- Rebuild for glpk 4.65

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Jerry James <loganjerry@gmail.com> - 5.8-1
- New upstream release
- Drop upstreamed -musketeer patch
- Add -doc subpackage to hold doxygen-generated content

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr  6 2017 Jerry James <loganjerry@gmail.com> - 5.7-1
- New upstream release

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 5.6-3
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Jerry James <loganjerry@gmail.com> - 5.6-1
- New upstream release

* Fri Sep 16 2016 Jerry James <loganjerry@gmail.com> - 5.5-2
- Fix two tests that fail on big endian architectures (bz 1371894)

* Sat Aug 27 2016 Jerry James <loganjerry@gmail.com> - 5.5-1
- New upstream release

* Thu Mar 17 2016 Jerry James <loganjerry@gmail.com> - 5.4-1
- New upstream release

* Sat Mar 12 2016 Jerry James <loganjerry@gmail.com> - 5.3-5
- Rebuild for glpk 4.59

* Fri Feb 19 2016 Jerry James <loganjerry@gmail.com> - 5.3-4
- Rebuild for glpk 4.58

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Jerry James <loganjerry@gmail.com> - 5.3-2
- Rebuild for cudd 3.0.0

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 5.3-1
- New upstream release

* Wed Oct  7 2015 Jerry James <loganjerry@gmail.com> - 5.2-1
- New upstream release

* Fri Oct  2 2015 Jerry James <loganjerry@gmail.com> - 5.1-3
- Rebuild for cudd 2.5.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Jerry James <loganjerry@gmail.com> - 5.1-1
- New upstream release
- Drop upstreamed -messaget patch

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream release
- Drop upstreamed ppc64le patch
- Add -messaget patch to fix a build failure

* Mon Sep 15 2014 Jerry James <loganjerry@gmail.com> - 4.9-1
- New upstream release
- Drop upstreamed patches

* Wed Sep  3 2014 Jerry James <loganjerry@gmail.com> - 4.7-3
- Add patch to fix the ppc64le build (bz 1133066)
- Add man page links for goto-cc and goto-instrument
- Fix license handling

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Jerry James <loganjerry@gmail.com> - 4.7-1
- New upstream release
- Build with CUDD support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2.20131201svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec  1 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.6-1.20131201svn
- Updated to upstream 4.6 release

* Tue Sep 10 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-7.20130515svn
- Fix build with unversioned docdir using _pkgdocdir (#992043)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-6.20130515svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Dan Horák <dan[at]danny.cz> - 4.3-5.20130515svn
- fix build on s390x

* Mon Jul  8 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-4.20130515svn
- Fixed changelog date

* Sun Jun 30 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-3.20130515svn
- Updated license
- Fixed doc and manual page directories

* Tue Jun 25 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-2.20130515svn
- Updated release

* Wed May 15 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-1.20130515svn
- First release
