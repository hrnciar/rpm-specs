# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name regex-posix
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.96.0.0
Release:        3%{?dist}
Summary:        POSIX Backend for "Text.Regex" (regex-base)

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-regex-base-prof
# End cabal-rpm deps

%description
The POSIX regex backend for <//hackage.haskell.org/package/regex-base
regex-base>.

The main appeal of this backend is that it's very lightweight due to its
reliance on the ubiquitous
<https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/regex.h.html POSIX.2
regex> facility that is provided by the standard C library on most POSIX
platforms.

See also <https://wiki.haskell.org/Regular_expressions> for more information.


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
chmod a-x ChangeLog.md
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
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.96.0.0-1
- update to 0.96.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.95.2-45
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.95.2-42
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.95.2-39
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.95.2-36
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Jens Petersen <petersen@redhat.com>
- remove the C copy library in prep

* Mon Jan 26 2015 Jens Petersen <petersen@fedoraproject.org> - 0.95.2-32
- update urls

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan  7 2014 Jens Petersen <petersen@redhat.com> - 0.95.2-29
- update to 0.95.2 with cblrpm-0.8.7
- unsubpackage from haskell-platform

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 0.95.1-3
- rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Jens Petersen <petersen@redhat.com> - 0.95.1-1
- update to 0.95.1 for haskell-platform-2011.4.0.0
- cabal2spec-0.25.1

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.94.4-7.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.94.4-7.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.94.4-7.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.94.4-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 0.94.4-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 0.94.4-5
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94.4-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 0.94.4-2
- update to cabal2spec-0.22.4

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 0.94.4-1
- update to 0.94.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.94.2-2
- update url and drop -o obsoletes
- add hscolour

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 0.94.2-1
- update to 0.94.2 for haskell-platform-2010.2.0.0
- obsolete doc subpackage (ghc-rpm-macros-0.8.0)

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 0.94.1-4
- sync cabal2spec-0.22

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 0.94.1-3
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Fri Jan 15 2010 Jens Petersen <petersen@redhat.com> - 0.94.1-2
- BSD license
- depends on regexp-base

* Fri Jan 15 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.94.1-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
