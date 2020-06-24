# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name vty
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        5.25.1
Release:        3%{?dist}
Summary:        A simple terminal UI library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-microlens-mtl-prof
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
Vty is terminal GUI library in the niche of ncurses. It is intended to be easy
to use, have no confusing corner cases, and good support for common terminal
types.

See the 'vty-examples' package as well as the program
'test/interactive_terminal_test.hs' included in the 'vty' package for examples
on how to use the library.

Import the "Graphics.Vty" convenience module to get access to the core parts of
the library.


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
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/vty-demo
%{_bindir}/vty-mode-demo


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 5.25.1-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 5.25.1-1
- update to 5.25.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jens Petersen <petersen@redhat.com> - 5.21-1
- spec file generated by cabal-rpm-1.0.0