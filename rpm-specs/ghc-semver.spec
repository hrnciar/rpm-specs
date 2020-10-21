# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name semver
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.3.4
Release:        6%{?dist}
Summary:        Representation, manipulation, and de/serialisation of Semantic Versions

License:        MPLv2.0
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-text-prof
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps

%description
Representation, manipulation, and de/serialisation of a Version type following
the Semantic Versioning specification.

For more information see: <http://semver.org>.


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
chmod a-x README.md
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


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.3.4-4
- refresh to cabal-rpm-2.0.6

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 0.3.4-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.3.4-1
- update to 0.3.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.3.3.1-7
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.3.3.1-5
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.3.3.1-2
- rebuild

* Wed Nov 15 2017 David Shea <dshea@redhat.com> - 0.3.3.1-2
- spec file generated by cabal-rpm-0.11.2
- Fix the License field
