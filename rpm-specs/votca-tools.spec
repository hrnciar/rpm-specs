Name:           votca-tools
Version:        1.6.2
%global         uversion %{version}
%global         sover 6
Release:        1%{?dist}
Summary:        VOTCA tools library
License:        ASL 2.0
URL:            http://www.votca.org
Source0:        https://github.com/votca/tools/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  eigen3-devel
BuildRequires:  boost-devel

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the basic tools library of VOTCA.


%package devel
Summary:        Development headers and libraries for votca-tools
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}
# Programs that build against votca need also these
Requires:       boost-devel
Requires:       expat-devel
Requires:       fftw-devel

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains development headers and libraries for votca-tools.


%prep
%setup -qn tools-%{uversion}

%build
%{cmake} -DCMAKE_BUILD_TYPE=Release -DWITH_RC_FILES=OFF -DENABLE_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets

%files
%license LICENSE
%doc NOTICE CHANGELOG.md README.md
%{_bindir}/votca_*
%{_libdir}/libvotca_tools.so.%{sover}
%{_mandir}/man1/votca_property.*
%{_mandir}/man7/votca-tools.7*

%files devel
%{_includedir}/votca/
%{_libdir}/libvotca_tools.so
%{_libdir}/cmake/VOTCA_TOOLS

%changelog
* Sat Aug 22 2020 Christoph Junghans <junghans@votca.org> - 1.6.2-1
- Version bump to v1.6.2 (bug #1871342)

* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 1.6.1-4
- Fix out-of-source build on F33 (bug#1865610)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Christoph Junghans <junghans@votca.org> - 1.6.1-1
- Version bump to v1.6.1

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.6-2
- Rebuilt for Boost 1.73

* Sat Apr 18 2020 Christoph Junghans <junghans@votca.org> - 1.6-1
- Version bump to v1.6 (bug #1825474)

* Mon Feb 10 2020 Christoph Junghans <junghans@votca.org> - 1.6~rc2-1
- Version bump to 1.6~rc2
- Drop 196.patch, 197.patch and  199.patch - merged upstream

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-0.4rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.3rc1
- Added upstream 196.patch to failing table test
- Added upstream 199.patch to fix 32bit builds

* Thu Dec 05 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.2rc1
- Added upstream 197.patch to fix CMake files

* Thu Dec 05 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.1rc1
- Version bump to 1.6_rc1 (bug #1779862)

* Fri Nov 22 2019 Christoph Junghans <junghans@votca.org> - 1.5.1-2
- Fix python3 shebang

* Thu Nov 21 2019 Christoph Junghans <junghans@votca.org> - 1.5.1-1
- Version bump to 1.5.1 (bug #1774849)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Christoph Junghans <junghans@votca.org> - 1.5-1
- Version bump to v1.5

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-1.4
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-1.1
- Rebuilt for Boost 1.66

* Sun Sep 03 2017 Christoph Junghans <junghans@votca.org> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.4-1.6
- Rebuild with binutils fix for ppc64le (#1475636)

* Tue Jul 25 2017 Christoph Junghans <junghans@votca.org> - 1.4-1.5
- Rebuild for gsl 2.4

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.4-1.4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4-1.1
- Rebuilt for Boost 1.63

* Sun Oct 30 2016 Christoph Junghans <junghans@votca.org> - 1.4-1
- Update to 1.4

* Mon Oct 03 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.2rc1
- clean up, don't install RC files

* Wed Sep 28 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.1rc1
- Update to 1.4_rc1

* Mon Aug 22 2016 Christoph Junghans <junghans@votca.org> - 1.3.1-1
- Update to 1.3.1
- Drop obsolete patch

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3-1.2
- Rebuild for gsl 2.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Thomas Spura <tomspur@fedoraproject.org> - 1.3-1
- Update to 1.3
- cleanup spec
- Add patch to add shebangs to scripts

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.3-0.2rc1
- Rebuilt for Boost 1.60

* Mon Nov 09 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.3-0.1.rc1
- update to 1.3_rc1
- cleanup spec

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.4-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.4-6
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-4
- Rebuilt with new gcc

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2.4-3
- Rebuild for boost 1.57.0

* Sun Sep  7 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-2
- correct source url

* Fri Sep 05 2014 Christoph Junghans <junghans@votca.org> - 1.2.4-1
- Update to 1.2.4
- Drop obsolete patch

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.2.3-4
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.2.3-2
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3, fix build in rawhide.

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.2.1-6.1
- Rebuild for Boost-1.53.0

* Tue Aug 14 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-5.1
- Bump due to boost update.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3.1
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-1.1
- Bump due to boost update.

* Thu Aug 25 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Fri Jul 22 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-3
- Bump spec due to new boost.

* Wed Apr 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-2
- Bump spec due to Boost upgrade.

* Sun Feb 20 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-1
- Update to 1.1.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.0.1-4
- rebuild for new boost

* Sun Dec 26 2010 Dan Horák <dan[at]danny.cz> - 1.0.1-3
- fix build on non-x86 64-bit architectures (ax_boost_base.m4 is wrong)

* Tue Dec 14 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-2
- Preserve timestamps on install.
- Added Requires: pkgconfig in -devel for EPEL support.

* Tue Dec 07 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- Drop bash completion (moved to votca-csg).
- Disable rc files.
- Added expat-devel and boost-devel as Requires in -devel.

* Thu Nov 25 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- First release.
