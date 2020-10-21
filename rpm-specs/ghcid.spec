# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name ghcid
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           %{pkg_name}
Version:        0.8.7
Release:        3%{?dist}
Summary:        GHCi based bare bones IDE

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-cmdargs-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-fsnotify-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-terminal-size-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-prof
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps
Requires:       cabal-install
Requires:       ghc-compiler

%description
Either "GHCi as a daemon" or "GHC + a bit of an IDE". A very simple Haskell
development tool which shows you the errors in your project and updates them
whenever you save. Run 'ghcid --command=ghci', where '--command' is the
command to start GHCi on your project (defaults to 'ghci' if you have a '.ghci'
file, or else to 'cabal repl').


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q
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


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGES.txt README.md
%{_bindir}/%{name}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.txt README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.8.7-1
- update to 0.8.7

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.7.7-1
- update to 0.7.7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.7.4-1
- update to 0.7.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Jens Petersen <petersen@redhat.com> - 0.7.1-4
- requires ghc-compiler and cabal-install

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.7.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.7.1-1
- spec file generated by cabal-rpm-0.12.5
