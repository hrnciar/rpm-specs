# generated by cabal-rpm-2.0.2 --subpackage
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name generics-sop
%global pkgver %{pkg_name}-%{version}

%global sopcore sop-core-0.4.0.0
%global subpkgs %{sopcore}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.4.0.1
# can only be reset when all subpkgs bumped
Release:        2%{?dist}
Summary:        Generic Programming using True Sums of Products

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{sopcore}/%{sopcore}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-base-prof
#BuildRequires:  ghc-sop-core-prof
BuildRequires:  ghc-template-haskell-prof
# for missing dep 'sop-core':
BuildRequires:  ghc-deepseq-prof
# End cabal-rpm deps

%description
A library to support the definition of generic functions. Datatypes are viewed
in a uniform, structured way: the choice between constructors is represented
using an n-ary sum, and the arguments of each constructor are represented using
an n-ary product.

The module "Generics.SOP" is the main module of this library and contains more
detailed documentation.

Since version 0.4.0.0, this package is now based on
'<https://hackage.haskell.org/package/sop-core sop-core>'. The core package
contains all the functionality of n-ary sums and products, whereas this package
provides the datatype-generic programming support on top.

Examples of using this library are provided by the following packages:

* '<https://hackage.haskell.org/package/basic-sop basic-sop>' basic examples,

* '<https://hackage.haskell.org/package/pretty-sop pretty-sop>' generic pretty
printing,

* '<https://hackage.haskell.org/package/lens-sop lens-sop>' generically
computed lenses,

* '<https://hackage.haskell.org/package/json-sop json-sop>' generic JSON
conversions.

A detailed description of the ideas behind this library is provided by the
paper:

* Edsko de Vries and Andres Löh.
<http://www.andres-loeh.de/TrueSumsOfProducts True Sums of Products>.
Workshop on Generic Programming (WGP) 2014. .


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


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage %{sopcore}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%ghc_fix_rpath %{pkgver}
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
%doc CHANGELOG.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.4.0.1-1
- update to 0.4.0.1
- subpackage sop-core

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.3.2.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.3.2.0-1
- update to 0.3.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.3.1.0-2
- rebuild

* Thu Nov 16 2017 David Shea <dshea@redhat.com> - 0.3.1.0-2
- Move the API docs to a separate package
- spec file generated by cabal-rpm-0.11.2