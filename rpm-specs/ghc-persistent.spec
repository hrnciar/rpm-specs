# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name persistent
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        2.9.2
Release:        3%{?dist}
Summary:        Type-safe, multi-backend data serialization

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-http-api-data-prof
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-path-pieces-prof
BuildRequires:  ghc-resource-pool-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-silently-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-void-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-monad-control-devel
%endif
# End cabal-rpm deps

%description
Persistent allows us to choose among existing databases that are highly tuned
for different data storage use cases, interoperate with other programming
languages, and to use a safe and productive query interface, while still
keeping the type safety of Haskell datatypes.

Persistent follows the guiding principles of type safety and concise,
declarative syntax. Other nice features are database-independence, convenient
data modeling, and automatic database migrations.


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
* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 2.9.2-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 2.9.2-1
- update to 2.9.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 2.8.2-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 2.8.2-3
- revise .cabal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.2-1
- update to 2.8.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 2.7.1-3
- rebuild

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.1-2
- rebuilt

* Sat Nov 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.1-1
- Update to latest version.

* Mon Oct 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.0-4
- rebuilt

* Mon Sep 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.7.0-3
- Split docs into subpackage.

* Sun Sep 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.7.0-2
- Add a real description.
- Update to latest spec template.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.7.0-1
- Update to latest version.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.2.4.1-6
- Bump for Fedora 26.

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.4.1-5
- Bump to rebuild against new dependencies

* Thu Dec 15 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.4.1-4
- Update release to be newer than previous builds

* Thu Dec 15 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.2.4.1-1
- spec file generated by cabal-rpm-0.10.0
