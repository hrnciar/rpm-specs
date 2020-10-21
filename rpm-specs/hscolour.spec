# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hscolour
%global pkgver %{pkg_name}-%{version}

# This default now for Fedora but keeping it for backcompat
# (link statically to Haskell libs for easier ghc version bootstrapping)
%global ghc_without_dynamic 1

# use following to bootstrap for a new arch:
#%%{?ghc_bootstrap}
#%%global ghc_bootstrapping 1
#%%global without_hscolour 1

Name:           %{pkg_name}
Version:        1.24.4
Release:        9%{?dist}
Summary:        Colorize Haskell code

# the source does not state intended GPL version
License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
Requires:       %{name}-common = %{version}-%{release}
# End cabal-rpm deps

%description
Hscolour is a Haskell tool to colorize Haskell code. It currently has
six output formats: ANSI terminal codes (optionally XTerm-256colour codes),
HTML 3.2 with <font> tags, HTML 4.01 with CSS, HTML 4.01 with CSS and mouseover
annotations, XHTML 1.0 with inline CSS styling, LaTeX, and mIRC chat codes.


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


%files
# Begin cabal-rpm files:
%{_bindir}/HsColour
# End cabal-rpm files


%files common
# Begin cabal-rpm files:
%license LICENCE-LGPL
%{_datadir}/%{pkgver}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENCE-LGPL
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 1.24.4-7
- refresh to cabal-rpm-2.0.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 1.24.4-5
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.24.4-3
- refresh to cabal-rpm-0.13

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 1.24.4-1
- update to 1.24.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.24.2-1
- update to 1.24.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 1.24.1-2
- rebuild

* Mon Feb 20 2017 Jens Petersen <petersen@redhat.com> - 1.24.1-1
- update to 1.24.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun  6 2016 Jens Petersen <petersen@redhat.com> - 1.23-1
- update to 1.23

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@fedoraproject.org> - 1.20.3-11
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Jens Petersen <petersen@redhat.com> - 1.20.3-8
- link executable to Haskell libs statically for easier ghc package bootstrapping

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Jens Petersen <petersen@redhat.com> - 1.20.3-6
- turn off bootstrap

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 1.20.3-5
- update to new simplified Haskell Packaging Guidelines
- bootstrap build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.20.3-3
- normal build

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.20.3-2
- bootstrap
- change license tag to GPL+ since no indication of version
- update with cabal-rpm

* Mon Sep 10 2012 Jens Petersen <petersen@redhat.com> - 1.20.3-1
- update to 1.20.3, which should build with ghc-7.6
- hscolour-1.20.2-non-ascii.patch is upstream

* Thu Jul 26 2012 Jens Petersen <petersen@redhat.com> - 1.20.2-3
- add upstream patch to workaround errors with unicode points > 255

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  9 2012 Jens Petersen <petersen@redhat.com> - 1.20.2-1
- update to 1.20.2

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.19-6
- normal full build

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.19-5
- bootstrap build
- drop the explicit containers BR

* Mon Jan 23 2012 Jens Petersen <petersen@redhat.com> - 1.19-4
- update to cabal2spec-0.25.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.19-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.19-2.1
- rebuild with new gmp

* Fri Jun 17 2011 Jens Petersen <petersen@redhat.com> - 1.19-2
- use ghc_arches (cabal-0.23.2)

* Fri Jun 17 2011 Jens Petersen <petersen@redhat.com> - 1.19-1
- update to 1.19
- use ghc_bootstrap from ghc-rpm-macros-0.13.5
- just depends on containers

* Thu May 05 2011 Jiri Skala <jskala@redhat.com> - 1.17-10
- enable source hscolour again

* Tue May 03 2011 Jiri Skala <jskala@redhat.com> - 1.17-9
- temporily disable hscolour for ghc-7.0.2 bootstrap on ppc64

* Thu Mar 10 2011 Jens Petersen <petersen@redhat.com> - 1.17-8
- enable source hscolour again

* Thu Mar 10 2011 Jens Petersen <petersen@redhat.com> - 1.17-7
- temporily disable hscolour for ghc-7.0.2 bootstrap

* Wed Feb 23 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.17-6
- enable build on sparcv9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jens Petersen <petersen@redhat.com> - 1.17-4
- rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 1.17-3
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 1.17-2
- rebuilt

* Mon Jul 19 2010 Jens Petersen <petersen@redhat.com> - 1.17-1
- 1.17 release
- use ghc-rpm-macros-0.8.1 macros: update to cabal2spec-0.22.1
- add hscolour and obsolete doc subpackage

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 1.16-3
- strip dynlinked files (cabal2spec-0.21.4)

* Mon Feb 15 2010 Conrad Meyer <konrad@tylerc.org> - 1.16-1
- Bump to 1.16

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.15-4
- update to ghc-rpm-macros-0.5.1 and cabal2spec-0.21.1:
- drop doc and prof bcond
- use common summary and common_description
- define pkg_name and use ghc_binlib_package

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.15-3
- devel package requires shared library not base

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.15-2
- update spec for ghc-6.12.1
- added shared library support: needs ghc-rpm-macros 0.3.1

* Fri Sep 18 2009 Jens Petersen <petersen@redhat.com> - 1.15-1
- update to 1.15

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Jens Petersen <petersen@redhat.com> - 1.13-1
- update to 1.13
- buildrequires ghc-rpm-macros (cabal2spec-0.16)

* Sat Apr 25 2009 Jens Petersen <petersen@redhat.com> - 1.12-3
- sync with cabal2spec-0.15

* Tue Mar 10 2009 Jens Petersen <petersen@redhat.com> - 1.12-2
- fix url (#488665)
- fix HsColour permissions (#488665)

* Thu Mar  5 2009 Jens Petersen <petersen@redhat.com> - 1.12-1
- initial packaging for Fedora created by cabal2spec
