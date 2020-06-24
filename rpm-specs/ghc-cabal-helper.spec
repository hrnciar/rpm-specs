# generated by cabal-rpm-2.0.2 --subpackage
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name cabal-helper
%global pkgver %{pkg_name}-%{version}

%global cabalplan cabal-plan-0.4.0.0
%global subpkgs %{cabalplan}

# tests difficult
%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.8.2.0
# can only be reset when all subpkgs bumped
Release:        5%{?dist}
Summary:        Simple interface to some of Cabal's configuration state, mainly used by ghc-mod

License:        AGPLv3
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cabalplan}/%{cabalplan}.tar.gz
# End cabal-rpm sources

# build cabal-plan executable (in koji)
Patch1:         cabal-plan-exe-flag.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
#BuildRequires:  ghc-cabal-plan-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  cabal-install
%if %{with tests}
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-paths-devel
# tests/bkpregex.cabal
BuildRequires:  ghc-bytestring-devel
# tests/exeintlib.cabal
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
# tests/exelib.cabal
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
# tests/fliblib.cabal
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
%endif
# for missing dep 'cabal-plan':
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-optics-core-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-singleton-bool-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-topograph-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
Cabal's little helper provides access to build information gathered by 'cabal'
when configuring a project. Specifically we're interested in retrieving enough
information to bring up a compiler session, using the GHC API, which is similar
to running 'cabal repl' in a project.

While simple in principle this is complicated by the fact that the information
Cabal writes to disk is in an unstable format and only really accessible
through the Cabal API itself.

Since we do not want to bind the user of a development tool which utilises this
library to a specific version of Cabal we compile the code which interfaces
with the Cabal library's API on the user's machine, at runtime, against
whichever version of Cabal was used to write the on disk information for a
given project.

If this version of Cabal is not available on the users machine anymore, which
is fairly likely since cabal-install is usually linked statically, we have
support for compiling the Cabal library also. In this case the library is
installed into a private, isolated, package database in
'$XDG_CACHE_HOME/cabal-helper' so as to not interfere with the user's package
database.


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
%ghc_lib_subpackage %{cabalplan}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
cabal-tweak-dep-ver pretty-show '< 1.9' '< 1.10'

(
cd %{cabalplan}
cabal-tweak-dep-ver base '4.11' '4.12'
cabal-tweak-dep-ver containers '^>= 0.5.0' '^>= 0.6.0'
%patch1 -p1 -b .orig
)


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

echo %{_bindir}/cabal-plan >> %{cabalplan}/ghc-cabal-plan-devel.files


%check
# Don't add any servers to cabal config, so it
# doesn't try to download anything.
mkdir -p home/.cabal
echo > home/.cabal/config

# Cannot run build tests that use the network.
%global cabal_test_options ghc-session
HOME=$PWD/home %cabal_test


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
%doc README.md
%dir %{_libexecdir}/%{pkgver}
%{_libexecdir}/%{pkgver}/cabal-helper-wrapper


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 0.8.2.0-5
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.8.2.0-3
- update to 0.8.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Jens Petersen <petersen@redhat.com> - 0.8.1.2-1
- update to 0.8.1.2
- subpackage cabal-plan-0.4.0 dep

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.8.0.2-5
- revise .cabal
- run testsuite only on Intel archs (failing elsewhere)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.2-3
- Build with tests enabled

* Mon Apr 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.2-2
- Use macro-defined location for private executables (#1563863)

* Wed Apr  4 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.8.0.2-1
- spec file generated by cabal-rpm-0.12.1