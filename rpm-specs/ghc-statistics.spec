# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name statistics
%global pkgver %{pkg_name}-%{version}

%global denselinearalgebra dense-linear-algebra-0.1.0.0
%global subpkgs %{denselinearalgebra}

# testsuite missing deps: tasty-expected-failure

Name:           ghc-%{pkg_name}
Version:        0.15.2.0
# can only be reset when all subpkgs bumped
Release:        6%{?dist}
Summary:        A library of statistical types, data, and functions

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{denselinearalgebra}/%{denselinearalgebra}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-deepseq-prof
#BuildRequires:  ghc-dense-linear-algebra-prof
BuildRequires:  ghc-math-functions-prof
BuildRequires:  ghc-monad-par-prof
BuildRequires:  ghc-mwc-random-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vector-algorithms-prof
BuildRequires:  ghc-vector-binary-instances-prof
BuildRequires:  ghc-vector-th-unbox-prof
# End cabal-rpm deps

%description
This library provides a number of common functions and types useful in
statistics. We focus on high performance, numerical robustness, and use of good
algorithms. Where possible, we provide references to the statistical
literature.

The library's facilities can be divided into four broad categories:

* Working with widely used discrete and continuous probability distributions.
(There are dozens of exotic distributions in use; we focus on the most common.)

* Computing with sample data: quantile estimation, kernel density estimation,
histograms, bootstrap methods, significance testing, and regression and
autocorrelation analysis.

* Random variate generation under several different distributions.

* Common statistical tests for significant differences between samples.


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


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage %{denselinearalgebra}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
chmod a-x README.markdown changelog.md
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%ghc_fix_rpath %{pkgver}
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.markdown changelog.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.15.2.0-4
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.15.2.0-3
- update to 0.15.2.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.15.0.0-1
- update to 0.15.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.14.0.2-8
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.14.0.2-6
- revise .cabal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.14.0.2-3
- rebuild

* Mon Dec 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14.0.2-2
- Split documentation into separate subpackage.

* Sat Nov 18 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.14.0.2-1
- spec file generated by cabal-rpm-0.11.2
