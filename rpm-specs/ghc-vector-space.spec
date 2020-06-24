# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name vector-space
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.16
Release:        1%{?dist}
Summary:        Vector and affine spaces, linear maps, and derivatives

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Boolean-prof
BuildRequires:  ghc-MemoTrie-prof
BuildRequires:  ghc-NumInstances-prof
BuildRequires:  ghc-base-prof
# End cabal-rpm deps

%description
Classes and generic operations for vector spaces and affine spaces.
It also defines a type of infinite towers of generalized derivatives.
A generalized derivative is a linear transformation rather than one of
the common concrete representations (scalars, vectors, matrices, ...).


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
%license COPYING
# End cabal-rpm files


%files devel -f %{name}-devel.files


%if %{with haddock}
%files doc -f %{name}-doc.files
%license COPYING
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.16-1
- update to 0.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.15-1
- update to 0.15

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.13-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.13-1
- update to 0.13

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.12-1
- update to 0.12

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 0.10.4-1
- update to 0.10.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 0.10.3-1
- update to 0.10.3

* Tue May 24 2016 Ben Boeckel <mathstuf@gmail.com> - 0.10.2-3
- Rebuild for ghc-MemoTrie
- doc -> license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Jens Petersen <petersen@redhat.com> - 0.10.2-1
- update to 0.10.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.8.6-6
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-2
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-1
- update to 0.8.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 0.8.4-1
- update to 0.8.4

* Mon Aug 06 2012 Ben Boeckel <mathstuf@gmail.com> - 0.8.2-1
- Update to 0.8.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-4
- change prof BRs to devel

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-3
- add license to ghc_files

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-2
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.6-1.1
- rebuild with new gmp without compat lib

* Mon Oct  3 2011 Jens Petersen <petersen@redhat.com> - 0.7.6-1
- update to 0.7.6

* Sat Jul 09 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7.3-2
- Update to cabal2spec-0.24

* Mon Jun 20 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Sat Sep 04 2010 Ben Boeckel <mathstuf@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri Sep 03 2010 Ben Boeckel <mathstuf@gmail.com> - 0.5.9-1
- Initial package

* Fri Sep  3 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.5.9-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
