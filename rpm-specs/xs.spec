%global commit0 9592d9b192a79653e86ae934170b6743ceac2164
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# workaround upstream expectations in test-suite
%global _vpath_builddir build


Name:		xs
Version:	1.2
Release:	2.git%{shortcommit0}%{?dist}
Summary:	Shell supporting functional programming

License:	Public Domain
URL:		https://github.com/TieDyedDevil/XS
Source0:	https://github.com/TieDyedDevil/XS/archive/%{commit0}.tar.gz#/XS-%{commit0}.tar.gz

BuildRequires:	meson
BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	gc-devel
BuildRequires:	libffi-devel
BuildRequires:	gcc-c++
BuildRequires:	readline-devel
BuildRequires:	git

%description
Xs is a cleanly-designed shell with functional programming.  It is based off
the source-code for the es project, which was in the public domain.
Currently, the changes in xs can also be considered to be in the public domain.

Most of the xs source code remains untouched from es.
The primary authors of that shell can be found in that source code,
currently located at: ftp://ftp.sys.utoronto.ca/pub/es/. Modifications
since es-0.9-beta1 are all parts of xs and have been written by
Frederic Koehler.


%prep
%setup -q -n XS-%{commit0}

# workaround upstream buildsystem, it requires to have an actual git checkout ...
git init
git config user.email "xs-owner@fedoraproject.org"
git config user.name "Fedora XS owner"
git add .
git commit -a -q -m "upstream commit %{shortcommit0}"
git remote add origin "%URL"


%build
%meson
%meson_build


%install
%meson_install


%check
# upstream uses "check" instead of "test"
%meson_build check


%files
%{_bindir}/xs
%{_mandir}/man1/xs.1*
%{_pkgdocdir}/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2.git9592d9b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May  2 2020 Jens Petersen <petersen@redhat.com> - 1.2-1.git9592d9b1
- update to git 9592d9b1: fixes FTBFS (#1800280)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-7.git22afec1
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2.git22afec1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Dan Horák <dan[at]danny.cz> - 1.1-1.git22afec1
- rebased to current HEAD

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25.gitc9a0b29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1-24.gitc9a0b29
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1-23.gitc9a0b29
- Rebuild for readline 7.x

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-22.gitc9a0b29
- Rebuilt attempt to fix FTBFS rhbz #1308259

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.gitc9a0b29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1-20.gitc9a0b29
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1-19.gitc9a0b29
- Rebuilt for Boost 1.59

* Tue Jul 28 2015 Jens Petersen <petersen@redhat.com> - 0.1-18.gitc9a0b29
- drop xs-dump-cxx.patch too (Jonathan Wakely)

* Tue Jul 28 2015 Jens Petersen <petersen@redhat.com> - 0.1-17.gitc9a0b29
- update to latest github snapshot
- fix url
- xs-automake-1.12-bison-hxx.patch is upstream

* Thu Jul 23 2015 Jonathan Wakely <jwakely@redhat.com> 0.1-16.git9c19777
- Patch dump.cxx to make foreach loop use references not copies.

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1-15.git9c19777
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.1-13.git9c19777
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Jens Petersen <petersen@redhat.com> - 0.1-11.git9c19777%{?dist}
- pass -i to autoreconf

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.1-9.git9c19777
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.1-7.git9c19777
- Rebuild for boost 1.54.0

* Fri Feb  1 2013 Jens Petersen <petersen@redhat.com> - 0.1-6.git9c19777%{?dist}
- patch for automake-1.12 using .hxx for bison output
- explicitly BR gcc-c++

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.git9c19777
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3.git9c19777
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep  7 2011 Jens Petersen <petersen@redhat.com> - 0.1-2.git9c19777
- fix description, use install -p, and include COPYING (Parag Nemade, #735705)
- add a check section

* Fri Sep  2 2011 Jens Petersen <petersen@redhat.com> - 0.1-1.git9c19777
- initial packaging
