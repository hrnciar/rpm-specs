# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name warp-tls
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        3.2.12
Release:        3%{?dist}
Summary:        HTTP over TLS support for Warp via the TLS package

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
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-tls-session-manager-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-prof
# End cabal-rpm deps

%description
SSLv1 and SSLv2 are obsoleted by IETF. We should use TLS 1.2 (or TLS 1.1 or TLS
1.0 if necessary). HTTP/2 can be negotiated by ALPN. API docs and the README
are available at <http://www.stackage.org/package/warp-tls>.


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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 3.2.12-1
- update to 3.2.12

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 3.2.9-1
- update to 3.2.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 3.2.7-1
- update to 3.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 3.2.4.3-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 3.2.4.3-1
- update to 3.2.4.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.4.2-1
- update to 3.2.4.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 3.2.4-2
- rebuild

* Thu Nov 16 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.2.4-1
- Update to latest version.

* Sun Jul 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.2.3-1
- Update to nearly-latest version.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.2.1-4
- Bump for Fedora 26.

* Sat Dec 17 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-3
- Update release to be newer than previous builds

* Sat Dec 17 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 3.2.1-1
- spec file generated by cabal-rpm-0.10.0
