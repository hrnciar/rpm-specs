# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name websockets
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.12.7.0
Release:        1%{?dist}
Summary:        A sensible and clean way to write WebSocket-capable servers in Haskell

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
#BuildRequires:  ghc-bytestring-builder-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-entropy-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-prof
# End cabal-rpm deps

%description
This library allows you to write WebSocket-capable servers.

An example server:
<https://github.com/jaspervdj/websockets/blob/master/example/server.lhs>

An example client:
<https://github.com/jaspervdj/websockets/blob/master/example/client.hs>

See also:

* The specification of the WebSocket protocol:
<http://www.whatwg.org/specs/web-socket-protocol/>

* The JavaScript API for dealing with WebSockets:
<http://www.w3.org/TR/websockets/>.


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
cabal-tweak-drop-dep bytestring-builder


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
%license LICENCE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG example


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENCE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.12.7.0-1
- update to 0.12.7.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.12.5.3-1
- update to 0.12.5.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr  5 2019 Jens Petersen <petersen@redhat.com> - 0.12.5.2-1
- spec file generated by cabal-rpm-0.13.1
- exclude deprecated bytestring-builder