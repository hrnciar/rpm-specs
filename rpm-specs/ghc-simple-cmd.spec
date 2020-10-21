# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name simple-cmd
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        3%{?dist}
Summary:        Simple String-based process commands

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-unix-prof
# End cabal-rpm deps
# for Rpm.rpmspec
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     rpm-build
%endif

%description
Simple wrappers over System.Process (readProcess, readProcessWithExitCode,
rawSystem, and createProcess). The idea is to provide some common idioms for
calling out to commands from programs. For more advanced shell-scripting or
streaming use turtle, shelly, command, etc.


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
%doc ChangeLog.md README.md TODO


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 0.2.2-1
- update to 0.2.2

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.2.1-1
- update to 0.2.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Jens Petersen <petersen@redhat.com> - 0.2.0.1-3
- bring back scripts for ghc_pkg_recache

* Sun Dec 22 2019 Jens Petersen <petersen@redhat.com> - 0.2.0.1-2
- refresh to cabal-rpm-1.0.3:
- noarch doc and include license
- prof supplements devel
- f30 packaging compatibility

* Sat Jul 27 2019 Jens Petersen <petersen@redhat.com> - 0.2.0.1-1
- update to 0.2.0.1

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.1.4-1
- update to 0.1.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Jens Petersen <petersen@redhat.com> - 0.1.3.1-1
- update to 0.1.3.1
- better sudo

* Sun Feb 24 2019 Jens Petersen <petersen@redhat.com> - 0.1.3-1
- update to 0.1.3

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.1.2-1
- update to 0.1.2

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.1.1-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Jens Petersen <petersen@redhat.com> - 0.1.1-1
- https://hackage.haskell.org/package/simple-cmd-0.1.1/changelog

* Thu Sep 13 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.0.0-1
- spec file generated by cabal-rpm-0.12.6
