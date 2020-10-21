# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name foundation
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.0.25
Release:        3%{?dist}
Summary:        Alternative prelude with batteries and no dependencies

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
# End cabal-rpm deps

%description
A custom prelude with no dependencies apart from base.

This package has the following goals:

* provide a base like sets of modules that provide a consistent set of features
and bugfixes across multiple versions of GHC (unlike base).

* provide a better and more efficient prelude than base's prelude.

* be self-sufficient: no external dependencies apart from base.

* provide better data-types: packed unicode string by default, arrays.

* Better numerical classes that better represent mathematical thing (No more
all-in-one Num).

* Better I/O system with less Lazy IO

* Usual partial functions distinguished through type system.


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


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.0.25-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.0.25-1
- update to 0.0.25

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.0.23-1
- update to 0.0.23

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.0.21-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Jens Petersen <petersen@redhat.com> - 0.0.21-1
- update to 0.0.21

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.20-1
- update to 0.0.20

* Fri Feb 23 2018 Jens Petersen <petersen@redhat.com> - 0.0.17-3
- unbundle basement

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.0.13-1
- update to 0.0.17
- subpackage basement

* Mon Aug 28 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.0.13-3
- Make documentation subpackage noarch.

* Sat Aug 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.0.13-2
- Split documentation into separate subpackage.
- Update to latest spec template.

* Sat Jul 22 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0.13-1
- spec file generated by cabal-rpm-0.11
