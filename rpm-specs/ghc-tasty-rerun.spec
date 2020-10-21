# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name tasty-rerun
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.1.17
Release:        4%{?dist}
Summary:        Rerun only tests which failed in a previous test run

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-transformers-prof
# End cabal-rpm deps

%description
This ingredient for <https://hackage.haskell.org/package/tasty tasty> testing
framework allows to filter a test tree depending on an outcome of the previous
run. This may be useful in many scenarios, especially when a test suite grows
large.


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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc Changelog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 1.1.17-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 1.1.17-1
- update to 1.1.17

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.1.14-1
- update to 1.1.14

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.1.13-1
- update to 1.1.13

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.1.12-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.1.12-3
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.12-1
- update to 1.1.12

* Fri Apr 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.10-1
- update to 1.1.10

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.1.8-1
- update to 1.1.8

* Wed Nov 15 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.1.7-1
- spec file generated by cabal-rpm-0.11.2
