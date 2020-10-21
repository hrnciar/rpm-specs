# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name chalmers-lava2000
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.6.1
Release:        15%{?dist}
Summary:        Hardware description EDSL

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Source1:        README.fedora

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
# End cabal-rpm deps

%description
A hardware description library in Haskell.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup
%{__install} -pm 644 %{SOURCE1} .


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install

rm %{buildroot}%{_datadir}/%{pkgver}/README
# End cabal-rpm install

# cleanup extra data files
%{__mv} %{buildroot}%{_datadir}/%{pkgver}/Doc/tutorial.pdf .
%{__rm} %{buildroot}%{_datadir}/%{pkgver}/INSTALL


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README README.fedora tutorial.pdf
%{_datadir}/%{pkgver}


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 1.6.1-14
- refresh to cabal-rpm-2.0.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 1.6.1-12
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.6.1-10
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 1.6.1-6
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 1.6.1-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 1.6.1-1
- update to 1.6.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Jens Petersen <petersen@redhat.com> - 1.4.1-1
- update to 1.4.1
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 1.3-4
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.3-2
- update with cabal-rpm
- include tutorial again and README files

* Sat Sep 29 2012 Shakthi Kannan <shakthimaan at fedoraproject dot org> - 1.3-1
- Updated to 1.3

* Mon Aug 13 2012 Shakthi Kannan <shakthimaan at fedoraproject dot org> - 1.2.0-1
- spec file template generated by cabal2spec-0.25.5
- Updated to 1.2.0

* Thu Dec 29 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.1.2-1
- Updated to use cabal2spec-0.24.1.
- Updated to 1.1.2.

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.1-12.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.1.1-12.1
- rebuild with new gmp

* Fri Jun 24 2011 Jens Petersen <petersen@redhat.com> - 1.1.1-12
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.1-11
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Jens Petersen <petersen@redhat.com> - 1.1.1-9
- update to cabal2spec-0.22.4

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-8
- bump base to 4 for ghc 7
- update url and drop -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-7
- add hscolour and doc obsolete (cabal2spec-0.22.2)

* Tue Jun 29 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-6
- update to cabal2spec-0.22.1

* Mon May 24 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-5
- Keep lava.vhd in datadir so users can find it easily (#546376)
- Improve summary and description

* Fri May 21 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-4
- Include the extra data files as doc files instead in the base package

* Tue Apr 13 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-3
- Removed INSTALL file.
- Gzip tutorial.ps and move it to docdir.
- Move Vhdl folder to docdir.
- Removed chalmers folder.

* Thu Apr 08 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-2
- Initial packaging for Fedora automatically generated by cabal2spec-0.21.3.
- Added BSD license.

* Sun Dec 20 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-1
- Added README.fedora, instead of using default README.
- Remove Scripts folder.
- Created patch to remove verification modules that use wrapper scripts.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.1.1

* Mon Dec 14 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.0-1
- Upstream fixed LAVADIR path as per recommendation.
- Upstream changed import Lava2000 to Lava.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.1.0

* Thu Dec 10 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.0.2-1
- Set LAVADIR path with sed.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.0.2
