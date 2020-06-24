# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name aeson
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.4.6.0
Release:        1%{?dist}
Summary:        Fast JSON parsing and encoding

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uuid-types-prof
BuildRequires:  ghc-vector-prof
# End cabal-rpm deps

%description
A JSON parsing and encoding library optimized for ease of use and
high performance.  Aeson was the father of Jason in Greek mythology.


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
%doc README.markdown changelog.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sun Feb 09 2020 Jens Petersen <petersen@redhat.com> - 1.4.6.0-1
- update to 1.4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.4.2.0-1
- update to 1.4.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.3.1.1-1
- update to 1.3.1.1

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.2.4.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.2.4.0-1
- update to 1.2.4.0

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3.0-4
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.2.3.0-1
- update to 1.2.3.0

* Fri Jan 12 2018 Jens Petersen <petersen@redhat.com> - 1.0.2.1-8
- time-locale-compat is now packaged

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jens Petersen <petersen@redhat.com> - 1.0.2.1-5
- update to 1.0.2.1
- subpackage time-locale-compat

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0.2-3
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.2-1
- update to 0.8.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-2
- disable TH module on arch's without ghci

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-1
- update to 0.6.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-2
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-1
- update to 0.6.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-5
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-3
- rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-2
- rebuild

* Sun May  6 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-1
- update to 0.6.0.2
- build needs ghci

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-2
- depends on dlist for ghc > 7.2

* Mon Feb 27 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-1
- BSD license
- doc files

* Mon Feb 27 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
