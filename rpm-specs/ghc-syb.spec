# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name syb
%global pkgver %{pkg_name}-%{version}

# disable temporarily to build with only ghc
%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.7.1
Release:        2%{?dist}
Summary:        Scrap Your Boilerplate

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
%endif
# End cabal-rpm deps

%description
This package contains the generics system described in the "Scrap Your
Boilerplate" papers (see <http://www.cs.uu.nl/wiki/GenericProgramming/SYB>).
It defines the 'Data' class of types permitting folding and unfolding of
constructor applications, instances of this class for primitive types, and
a variety of traversals.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


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


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%cabal_test


%if 0%{?fedora} < 31 || 0%{?rhel} < 8
%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.7.1-1
- update to 0.7.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.7-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.7-1
- update to 0.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.6-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 14 2016 Jens Petersen <petersen@redhat.com> - 0.6-1
- update to 0.6

* Tue Jun  7 2016 Jens Petersen <petersen@redhat.com> - 0.5.1-1
- update to 0.5.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Jens Petersen <petersen@redhat.com> - 0.4.1-1
- update to 0.4.1
- tests fail on armv7

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.4.0-36
- update to cblrpm-0.8.11

* Fri Apr 18 2014 Jens Petersen <petersen@redhat.com> - 0.4.0-35
- bump over haskell-platform

* Tue Jan  7 2014 Jens Petersen <petersen@redhat.com> - 0.4.0-29
- update to 0.4.0
- unsubpackage from haskell-platform with cabal-rpm-0.8.7

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 0.3.6-1
- update to 0.3.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Jens Petersen <petersen@redhat.com> - 0.3.3-2
- move ghc_devel_package and ghc_devel_description to avoid srpm description

* Tue Dec 27 2011 Jens Petersen <petersen@redhat.com> - 0.3.3-1
- update to 0.3.3 for haskell-platform-2011.4.0.0
- update to cabal2spec-0.25.1
- add README to devel doc

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3-8
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.3-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 0.3-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Wed May 25 2011 Jens Petersen <petersen@redhat.com> - 0.3-5
- update to cabal2spec-0.22.7

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.3-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Jens Petersen <petersen@redhat.com> - 0.3-2
- update to cabal2spec-0.22.4

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 0.3-1
- update to 0.3

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.2.2-1
- BSD license
- summary and description

* Thu Nov 25 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.2.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
