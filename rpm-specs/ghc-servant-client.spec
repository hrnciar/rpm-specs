# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name servant-client
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.16.0.1
Release:        1%{?dist}
Summary:        Automatic derivation of querying functions for servant

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-media-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-kan-extensions-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-servant-prof
BuildRequires:  ghc-servant-client-core-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-compat-prof
# End cabal-rpm deps

%description
This library lets you derive automatically Haskell functions that let you query
each endpoint of a <http://hackage.haskell.org/package/servant servant>
webservice.

See <http://docs.servant.dev/en/stable/tutorial/Client.html the client section
of the tutorial>.

<https://github.com/haskell-servant/servant/blob/master/servant-client/CHANGELOG.md
CHANGELOG>.


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
%doc CHANGELOG.md README.lhs README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.16.0.1-1
- update to 0.16.0.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.15-1
- update to 0.15

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.14-1
- update to 0.14

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.13.0.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.13.0.1-1
- update to 0.13.0.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Jens Petersen <petersen@redhat.com> - 0.12.0.1-2
- rebuild

* Thu Nov 16 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.12.0.1-1
- spec file generated by cabal-rpm-0.11.2
