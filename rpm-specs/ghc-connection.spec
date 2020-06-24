# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name connection
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Simple and easy network connections API

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
BuildRequires:  ghc-basement-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-socks-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-x509-prof
BuildRequires:  ghc-x509-store-prof
BuildRequires:  ghc-x509-system-prof
BuildRequires:  ghc-x509-validation-prof
# End cabal-rpm deps

%description
Simple network library for all your connection need.

Features: Really simple to use, SSL/TLS, SOCKS.

This library provides a very simple api to create sockets to a destination with
the choice of SSL/TLS, and SOCKS.


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
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- update to 0.3.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.2.8-10
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.2.8-8
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.2.8-6
- rebuild

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-5
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.2.8-2
- rebuild

* Tue Sep 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.8-1
- Update to latest spec template.
- Update to latest version.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.5-5
- Bump for Fedora 26.

* Sat Dec 17 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-4
- spec file generated by cabal-rpm-0.10.0
- Update release to be newer than previous builds

* Sun May 01 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-3
- Bump to rebuild against new dependencies

* Mon Apr 25 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-2
- Bump to rebuild with new dependencies

* Sun Aug 23 2015 Ben Boeckel <mathstuf@gmail.com> - 0.2.5-1
- initial package
