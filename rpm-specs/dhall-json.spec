# generated by cabal-rpm-2.0.7
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name dhall-json
%global pkgver %{pkg_name}-%{version}

# Union keys test fails
%bcond_with tests

Name:           %{pkg_name}
Version:        1.6.4
Release:        2%{?dist}
Summary:        Convert between Dhall and JSON or YAML

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-yaml-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-dhall-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps

%description
Use this package if you want to convert between Dhall expressions and JSON or
YAML. You can use this package as a library or an executable:

* See the "Dhall.JSON" or "Dhall.JSONToDhall" modules if you want to use this
package as a library

* Use the 'dhall-to-json', 'dhall-to-yaml', or 'json-to-dhall' programs from
this package if you want an executable

The "Dhall.JSON" and "Dhall.JSONToDhall" modules also contains instructions for
how to use this package.


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
cp -bp %{SOURCE1} %{name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/dhall-to-json --bash-completion-script dhall-to-json > %{buildroot}%{_datadir}/bash-completion/completions/dhall-to-json
%{buildroot}%{_bindir}/dhall-to-yaml --bash-completion-script dhall-to-yaml > %{buildroot}%{_datadir}/bash-completion/completions/dhall-to-yaml
%{buildroot}%{_bindir}/json-to-dhall --bash-completion-script json-to-dhall > %{buildroot}%{_datadir}/bash-completion/completions/json-to-dhall
# End cabal-rpm install


%check
%cabal_test


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/dhall-to-json
%{_bindir}/dhall-to-yaml
%{_bindir}/json-to-dhall
%{_datadir}/bash-completion/completions/dhall-to-json
%{_datadir}/bash-completion/completions/dhall-to-yaml
%{_datadir}/bash-completion/completions/json-to-dhall
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Sun Oct  4 2020 Jens Petersen <petersen@redhat.com> - 1.6.4-2
- enable bash completions and testsuite

* Tue Sep  1 2020 Jens Petersen <petersen@redhat.com> - 1.6.4-1
- spec file generated by cabal-rpm-2.0.6
