%global pkg haskell-mode
%global pkgname Haskell-mode
%global commit b441b9353cf5693392bf16f2d6d5cd41164493be
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# until defined for all current releases
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:       emacs-%{pkg}
Version:    16.2
Release:    0.4%{?dist}
Summary:    Haskell editing mode for Emacs

License:    GPLv3+
URL:        https://github.com/haskell/haskell-mode

# git clone https://github.com/haskell/haskell-mode.git
# cd haskell-mode
# git archive --format tar.gz  -o ../emacs-haskell-mode-b441b93.tar.gz --prefix haskell-mode-16.2/ master
Source0:    Source0:  https://github.com/haskell/haskell-mode/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:    haskell-mode-init.el

BuildArch:  noarch
BuildRequires:  emacs
BuildRequires:  texinfo
Requires:   emacs(bin) >= %{_emacs_version}
Requires(post): info
Requires(preun): info
Obsoletes:      %{name}-el < %{version}-%{release}
Provides:       %{name}-el = %{version}-%{release}

%description
This package adds a Haskell major mode to Emacs.  The Haskell mode
supports font locking,declaration scanning, documentation,
indentation, and interaction with Hugs and GHCi.


%prep
%setup -q -n %{pkg}-%{version}

%build
make EMACS=%{_bindir}/emacs


%install
%{__rm} -rf %{buildroot}
%{__install} -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
%{__install} -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
%{__install} -pm 755 -d %{buildroot}%{_pkgdocdir}/examples
%{__install} -pm 755 -d %{buildroot}%{_infodir}
%{__install} -pm 644 build-%{_emacs_version}/*.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
%{__install} -pm 644 *.el %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
%{__install} -pm 644 haskell-mode.info %{buildroot}%{_infodir}/
%{__install} -pm 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}

%files
%license COPYING
%doc README.md NEWS
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/%{pkg}-init.el
%{_infodir}/%{pkg}.info*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Arun S A G <sagarun@fedoraproject.org> - 16.2-0.1
- Build the latest master of emacs-haskell-mode

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Jens Petersen <petersen@redhat.com> - 16.1-1
- update to 16.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar  8 2016 Jens Petersen <petersen@fedoraproject.org> - 13.18-1
- update to 13.18 (#1209674)
- update to modern packaging and drop subpackage (#1234529)
- build with Makefile
- update haskell-mode-init.el to autoloads
- build and install info file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Jens Petersen <petersen@redhat.com> - 2.9.1-3
- fix build with unversioned docdir using _pkgdocdir (#992201)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 Arun S A G <sagarun [AT] gmail dot com> - 2.9.1-1
- update to new upstream release
- Project moved to github. New source url
- Asked upstream to correct fsf address https://github.com/haskell/haskell-mode/issues/129

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 21 2012 Arun SAG <sagarun@gmail.com> - 2.8.0-1
- Updated to 2.8.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 12 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.7.0-3
- Fixed installation in centos

* Mon Dec 7 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.7.0-2
- Fixed installation failure in EL-5

* Sat Dec 5 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.7.0-1
- Updated to version 2.7.0-1

* Sun Nov 15 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.5.1-2
- Patch1 is moved to Source1

* Thu Oct 29 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.5.1-1
- Updated to version 2.5.1

* Mon Aug 17 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.4-5.20090815cvs
- Patch0 updated to include haskell-indentation-mode .
- Source0 changed,comment added for generating the source.
- Cleaned up CVS snapshot for control characters.
- Defined snapshot macro. 

* Sun Aug 16 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.4-4.20090815cvs
- Fixed the snapshot date.

* Sat Aug 15 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.4-3.20090815cvs
- Updated to Bugfix CVS snapshot 2.4-3.20091015cvs.
- Changelog fixed.

* Thu Aug 13 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.4-2
- Fixed the Makefile.
- Cleaned the upstream source.
- Spec file updated.

* Tue Aug 11 2009 Arun SAG <sagarun [AT] gmail dot com> - 2.4-1
- Updated to haskell-mode 2.4
- Spec file is adjusted according to Fedora packaging guidelines.
- Added patch to generate haskell-mode-init.el.
- Added patch to modify the makefile. 

* Wed Feb 14 2007 Tom Moertel <tom [AT] moertel dot com> - 2.3-1.tgm
- Updated to haskell-mode 2.3

* Mon Feb 12 2007 Tom Moertel <tom [AT] moertel dot com> - 2.2-2.tgm
- Removed version suffix from package's site-lisp subdirectory
- Switched to using the default site file from the haskell-mode tarball

* Mon Feb 12 2007 Tom Moertel <tom [AT] moertel dot com> - 2.2-1.tgm
- Updated to haskell-mode 2.2
- Added NEWS, ChangeLog, and README to package docs

* Wed Nov  9 2005 Tom Moertel <tom [AT] moertel dot com> - 2.1-1.tgm
- Updated for haskell-mode 2.1

* Mon Apr 25 2005 Tom Moertel <tom [AT] moertel dot com> - 2.0-1.tgm
- Updated for haskell-mode 2.0

* Sat Nov 13 2004 Tom Moertel <tom [AT] moertel dot com> 1.45-2.tgm
- Merged changes from Carwyn Edwards <tom [AT] moertel dot com>:
- Fixed permissions on installed files
- Install non bytecode compiled versions too
- Rewrote emacs byte compilation method

* Mon May  3 2004 Tom Moertel <tom [AT] moertel dot com> 1.45-1.tgm
- Updated to 1.45 of haskell-mode
- Made GHCi the default for interactive mode (instead of Hugs)

* Wed Nov  6 2002 Tom Moertel <tom [AT] moertel dot com>
- Removed prompt and alignment patches because they are now merged into
  the main distribution

* Mon Sep  2 2002 Tom Moertel <tom [AT] moertel dot com>
- Revised patch to handle ModuleA ModuleB ... > prompts

* Sat Aug 31 2002 Tom Moertel <tom [AT] moertel dot com>
- Added patch to handle new *ModuleName> prompts

* Tue Jul 23 2002 Tom Moertel <tom [AT] moertel dot com>
- Added support for aligning rhsides on a given column

* Fri Mar 22 2002 Tom Moertel <tom [AT] moertel dot com>
- Created spec file
- Added README.RPM 
- Added site-lisp/site-start.d init file for emacs-haskell-mode
