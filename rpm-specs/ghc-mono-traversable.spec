# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name mono-traversable
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.0.15.1
Release:        1%{?dist}
Summary:        Type classes for mapping, folding, and traversing monomorphic containers

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vector-algorithms-prof
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-semigroups-devel
%endif
# End cabal-rpm deps

%description
Please see the README at <https://www.stackage.org/package/mono-traversable>.


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
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 1.0.15.1-1
- update to 1.0.15.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.0.11.0-1
- update to 1.0.11.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.0.10.0-1
- update to 1.0.10.0

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.0.8.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 1.0.8.1-1
- update to 1.0.8.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.0.7.0-1
- update to 1.0.7.0

* Thu Nov  9 2017 David Shea <dshea@redhat.com> - 1.0.2-3
- spec file generated by cabal-rpm-0.11.1
- Split the documentation into a separate package