# generated by cabal-rpm-2.0.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hslogger
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.2.12
Release:        4%{?dist}
Summary:        Versatile logging framework

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-prof
# End cabal-rpm deps

%description
Hslogger is a logging framework for Haskell, roughly similar to Python's
logging module.

hslogger lets each log message have a priority and source be associated with
it. The programmer can then define global handlers that route or filter
messages based on the priority and source. hslogger also has a syslog handler
built in.


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


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 1.2.12-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.2.12-1
- update to 1.2.12

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.2.10-11
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.2.10-9
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 1.2.10-6
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 1.2.10-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 1.2.10-1
- update to 1.2.10

* Mon Jun 20 2016 Jens Petersen <petersen@redhat.com> - 1.2.9-1
- update to 1.2.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 1.2.6-1
- update to 1.2.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 1.2.1-4
- update to cblrpm-0.8.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 1.2.1-1
- update to 1.2.1
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.1.5-7
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 1.1.5-5
- change prof BRs to devel

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 1.1.5-4
- rebuild

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 1.1.5-3
- add license to ghc_files

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 1.1.5-2
- update to cabal2spec-0.25.2

* Sun Jan 01 2012 Bruno Wolff III <bruno@wolff.to> - 1.1.5-1.4
- Rebuild for libHSnetwork update so that test hegdewars can be built

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.5-1.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.5-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.1.5-1.1
- rebuild with new gmp

* Sat Aug 27 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 1.1.5-1
- package update to 1.1.5
- upgrade to cabal2spec 0.24
- license change from LGPLv2 to BSD

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 1.1.4-2
- BR ghc-Cabal-devel instead of ghc-prof (cabal2spec-0.23.2)

* Fri Mar 11 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 1.1.4-1
- upgrade to hslogger-1.1.4

* Fri Mar 11 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 1.1.3-5
- Rebuild for ghc-7.0.2

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.3-4
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 1.1.3-3
- rebuild for haskell-platform-2011.1 updates
- bump network dependency for haskell-platform-2011.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 1 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 1.1.3-1
- upstream package update to 1.1.3

* Thu Jan 6 2011 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.1.0-6
- rebuild for new ghc changes
- updating to cabal2spec-0.22.4

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 1.1.0-5
- rebuild

* Sun Nov 28 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.1.0-4
- Rebuilding for ghc7

* Fri Sep 3 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.1.0-3
- Modified the way COPYING is put into the package, using mkdir and install commands
- Added explicit permissions in install command as the COPYING file in package had execute permissions

* Wed Sep 1 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.1.0-2
- Added COPYING to the list of files to be included in the doc folder.
- The presence of doc directive wipes out COPYRIGHT from BUILD directory. COPYRIGHT would have been copied during cabal install. Hence it has to be included explicitly in .files. If this problem was not there, only COPYING need to put.

* Thu Aug 26 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.1.0-1
- source package updated from 1.0.10 to 1.1.0

* Tue Aug 24 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.0.10-3
- updated using cabal2spec-0.22.2 and ghc-rpm-macros-0.8.1
- corrected LICENSE string to LGPLv2+

* Sat Jul  3 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.0.10-2
- updated using cabal2spec-0.22.1
- Updated to use ghc_lib_package, ghc_lib_build, ghc_lib_install macros instead of cabal macros

* Tue May 25 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 1.0.10-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.3
