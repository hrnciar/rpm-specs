# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hadolint
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           %{pkg_name}
Version:        1.18.0
Release:        1%{?dist}
Summary:        Dockerfile linter, validate inline bash

License:        GPLv3+
URL:            https://github.com/%{pkg_name}/%{pkg_name}/
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-HsYAML-prof
BuildRequires:  ghc-ShellCheck-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-gitrev-prof
BuildRequires:  ghc-language-docker-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-void-prof
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
A smarter Dockerfile linter that helps you build best practice Docker
images. The linter is parsing the Dockerfile into an AST and performs rules on
top of the AST. It is standing on the shoulders of ShellCheck to lint the Bash
code inside RUN instructions.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q
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


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md
%{_bindir}/%{name}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Thu Sep 03 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.18.0-1
- Initial RPM release, from spec file generated by cabal-rpm-2.0.6
