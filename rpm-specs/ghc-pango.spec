# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name pango
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.13.8.1
Release:        4%{?dist}
Summary:        Binding to the Pango text rendering engine

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-cairo-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-glib-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-text-prof
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
# End cabal-rpm deps

%description
This package provides a wrapper around the Pango C library that allows
high-quality rendering of Unicode text. It can be used either with Cairo to
output text in PDF, PS or other documents or with Gtk+ to display text
on-screen.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
# End cabal-rpm deps

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

# demo files
rm -r %{buildroot}%{_datadir}/%{pkgver}


%files -f %{name}.files
# Begin cabal-rpm files:
%license COPYING
# End cabal-rpm files


%files devel -f %{name}-devel.files


%if %{with haddock}
%files doc -f %{name}-doc.files
%license COPYING
%endif
%doc demo


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jens Petersen <petersen@redhat.com> - 0.13.8.1-2
- re-enable ppc64le

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 0.13.8.1-1
- update to 0.13.8.1

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.13.8.0-1
- update to 0.13.8.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Jens Petersen <petersen@redhat.com> - 0.13.6.0-1
- update to 0.13.6.0
- exclude ppc64le because of #1737587
- move demo to doc subpkg

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.13.5.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.13.5.0-1
- update to 0.13.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.13.4.0-1
- update to 0.13.4.0

* Mon Aug 14 2017 Jens Petersen <petersen@redhat.com> - 0.13.3.1-4
- reenable i686 (#1427000)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.13.3.1-1
- update to 0.13.3.1
- exclude i686 due to gcc7 __float128

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 0.13.1.1-1
- update to 0.13.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Jens Petersen <petersen@redhat.com> - 0.13.1.0-1
- update to 0.13.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.13.0.5-1
- update to 0.13.0.5

* Tue Sep 16 2014 Jens Petersen <petersen@redhat.com> - 0.13.0.0-1
- update to 0.13.0.0
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Jens Petersen <petersen@redhat.com> - 0.12.5.0-1
- update to 0.12.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.12.4-4
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Jens Petersen <petersen@redhat.com> - 0.12.4-2
- rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.12.4-1
- update to 0.12.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.12.3-3
- change prof BRs to devel

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.12.3-2
- rebuild

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 0.12.3-1
- update to 0.12.3

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 0.12.2-1
- update to 0.12.2 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12.1-1.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12.1-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.12.1-1.1
- rebuild with new gmp

* Tue Sep 20 2011 Jens Petersen <petersen@redhat.com> - 0.12.1-1
- update to 0.12.1
- add _isa suffix to gtk2-devel depends (see #723558)

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-5
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.12.0-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 0.12.0-2
- update to cabal2spec-0.22.4

* Tue Nov 30 2010 Jens Petersen <petersen@redhat.com> - 0.12.0-1
- update to 0.12.0

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-3
- fix build with Cabal-1.10: add ghc7-Gtk2HsSetup-Cabal-1.10.patch

* Tue Sep  7 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-2
- rebuild against ghc-glib-0.11.2

* Wed Sep  1 2010 Jens Petersen <petersen@redhat.com> - 0.11.2-1
- update to 0.11.2
- move demo into devel doc

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 0.11.0-2
- use ghc-rpm-macros-0.8.1 so devel provides doc

* Tue Jul 13 2010 Jens Petersen <petersen@redhat.com> - 0.11.0-1
- license is LGPLv2+
- description
- depends on ghc-glib-devel, ghc-cairo-devel, and pango-devel
- BR gtk2hs-buildtools
- support hscolour

* Tue Jul 13 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.11.0-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.1
