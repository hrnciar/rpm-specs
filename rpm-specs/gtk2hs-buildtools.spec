# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name gtk2hs-buildtools
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        0.13.8.0
Release:        1%{?dist}
Summary:        Tools to build the Gtk2Hs suite of User Interface libraries

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashtables-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  alex
BuildRequires:  happy
Requires:       %{name}-common = %{version}-%{release}
# End cabal-rpm deps
ExcludeArch:    ppc64le

%description
This package provides a set of helper programs necessary to build the Gtk2Hs
suite of libraries. These tools include a modified c2hs binding tool that is
used to generate FFI declarations, a tool to build a type hierarchy that
mirrors the C type hierarchy of GObjects found in glib, and a generator for
signal declarations that are used to call back from C to Haskell.
These tools are not needed to actually run Gtk2Hs programs.


%package common
Summary:        %{name} common files
BuildArch:      noarch

%description common
This package provides the %{name} common data files.


%package -n ghc-%{name}
Summary:        Haskell %{name} library
Requires:       %{name}-common = %{version}-%{release}

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
mv %{buildroot}%{_ghcdocdir}{,-common}
# End cabal-rpm install


%if 0%{?fedora} < 31 || 0%{?rhel} < 8
%post -n ghc-%{name}-devel
%ghc_pkg_recache


%postun -n ghc-%{name}-devel
%ghc_pkg_recache
%endif


%files
# Begin cabal-rpm files:
%{_bindir}/gtk2hsC2hs
%{_bindir}/gtk2hsHookGenerator
%{_bindir}/gtk2hsTypeGen
# End cabal-rpm files


%files common
# Begin cabal-rpm files:
%license COPYING
%{_datadir}/%{pkgver}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license COPYING
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.13.8.0-1
- update to 0.13.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.13.5.0-1
- update to 0.13.5.0
- exclude ppc64le (#1737587)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Jens Petersen <petersen@redhat.com> - 0.13.4.0-4
- refresh to cabal-rpm-0.13.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Jens Petersen <petersen@redhat.com> - 0.13.4.0-2
- rebuild for static executable
- refresh to cabal-rpm-0.13

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.13.4.0-1
- update to 0.13.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.13.3.1-1
- update to 0.13.3.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul  6 2017 Jens Petersen <petersen@redhat.com> - 0.13.2.2-3
- add patch for i686 __float128 (#1427000)
  https://github.com/gtk2hs/gtk2hs/issues/200

* Sun Feb 26 2017 Jens Petersen <petersen@redhat.com> - 0.13.2.2-2
- datadir should live with library

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.13.2.2-1
- update to 0.13.2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 Jens Petersen <petersen@redhat.com> - 0.13.0.5-2
- rebuild

* Mon Mar 07 2016 Jens Petersen <petersen@redhat.com> - 0.13.0.5-1
- update to 0.13.0.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Jens Petersen <petersen@redhat.com> - 0.13.0.4-1
- update to 0.13.0.4
- remove aarch64 build-tools hacks
- use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Jens Petersen <petersen@redhat.com> - 0.13.0.3-2
- workaround build-tools version check failures on aarch64 (#1210323)

* Fri Jan 23 2015 Jens Petersen <petersen@redhat.com> - 0.13.0.3-1
- update to 0.13.0.3

* Wed Aug 27 2014 Jens Petersen <petersen@redhat.com> - 0.13.0.1-1
- update to 0.13.0.1
- refresh to cblrpm-0.9
- disable debuginfo since no files generated for c2hs_config.c

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Jens Petersen <petersen@redhat.com> - 0.12.5.1-1
- update to 0.12.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Jens Petersen <petersen@redhat.com> - 0.12.4-3
- update to cabal-rpm-0.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.12.4-1
- update to 0.12.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  9 2012 Jens Petersen <petersen@redhat.com> - 0.12.3.1-1
- update to 0.12.3.1

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.12.1-3
- depends on random
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12.1-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.12.1-1.1
- rebuild with new gmp

* Tue Sep 20 2011 Jens Petersen <petersen@redhat.com> - 0.12.1-1
- update to 0.12.1

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-6
- ghc_arches replaces ghc_excluded_archs

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-5
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.12.0-4
- Enable build on sparcv9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-2
- update to cabal2spec-0.22.4
- BR ghc-devel

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 0.12.0-1
- update to 0.12.0

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-2
- rebuild

* Mon Sep  6 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-1
- update to 0.11.2

* Thu Aug 19 2010 Jens Petersen <petersen@redhat.com> - 0.11.1-1
- update to 0.11.1

* Wed Jun 30 2010 Jens Petersen <petersen@redhat.com> - 0.9-2
- buildrequires alex and happy

* Wed Jun 30 2010 Jens Petersen <petersen@redhat.com> - 0.9-1
- summary, description, license, group, and filelist

* Wed Jun 30 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.9-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.1
