# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name resource-pool
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.2.3.2
Release:        20%{?dist}
Summary:        A high-performance striped resource pooling implementation

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
A high-performance striped pooling abstraction for managing flexibly-sized
collections of resources such as database connections.


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
%doc README.markdown


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.2.3.2-18
- refresh to cabal-rpm-2.0.6

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 0.2.3.2-17
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.2.3.2-15
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.2.3.2-13
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.2.3.2-11
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.2.3.2-8
- rebuild

* Mon Jul 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.3.2-7
- Re-add dist tag to release numbers.

* Mon Jul 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.3.2-6
- Bump for Fedora 26.

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3.2-5
- Bump to rebuild against new dependencies

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3.2-4
- Bump to rebuild against new dependencies

* Thu Dec 15 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3.2-3
- Update release to be newer than previous builds

* Thu Dec 15 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.3.2-1
- spec file generated by cabal-rpm-0.10.0
