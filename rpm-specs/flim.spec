%define	lispdir		%{_datadir}/emacs/site-lisp
%define	pkgdir		%{_datadir}/xemacs/xemacs-packages

Summary: Basic library for handling email messages for Emacs
Name: flim
Version: 1.14.9
Release: 18%{?dist}
License: GPLv2+
URL: http://www.kanji.zinbun.kyoto-u.ac.jp/~tomo/elisp/FLIM/
BuildRequires: apel, emacs
BuildArch: noarch
Source: http://www.kanji.zinbun.kyoto-u.ac.jp/~tomo/comp/emacsen/lisp/flim/flim-1.14/%{name}-%{version}.tar.gz
Requires: apel

%description
FLIM is a library to provide basic features about message
representation and encoding for Emacs.


%package xemacs
Summary: Basic library for handling email messages for XEmacs
Requires: apel-xemacs
BuildRequires: apel-xemacs, xemacs

%description xemacs
FLIM is a library to provide basic features about message
representation and encoding for Emacs.


%prep
%setup -q


%build
rm -f mailcap*
make LISPDIR=$RPM_BUILD_ROOT%{lispdir}


%install
# build for emacs
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix} LISPDIR=$RPM_BUILD_ROOT%{lispdir}

# remove files which shadow elisp files from emacs itself (#722186)
for i in md4 hex-util sasl-cram sasl-digest ntlm sasl sasl-ntlm hmac-def hmac-md5; do
  rm $RPM_BUILD_ROOT%{lispdir}/flim/$i.el*
done

make clean

# build for xemacs
## hack for batch-update-autoloads
touch auto-autoloads.el custom-load.el
make EMACS=xemacs PACKAGEDIR=$RPM_BUILD_ROOT%{pkgdir} install-package


%files
%doc FLIM-API.en README.en README.ja
%{lispdir}


%files xemacs
%doc README.en README.ja
%{pkgdir}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb  3 2012 Jens Petersen <petersen@redhat.com> - 1.14.9-4
- remove elisp files that shadow libraries from emacs (Andreas Schwab, #722186)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 1.14.9-1
- update to 1.14.9
- flim-xemacs-batch-autoloads.patch no longer needed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 1.14.8-3
- update license to GPLv2+

* Mon Sep 25 2006 Jens Petersen <petersen@redhat.com> - 1.14.8-2
- update url and source location

* Fri Aug  4 2006 Jens Petersen <petersen@redhat.com> - 1.14.8-1
- update to 1.14.8
- add flim-xemacs-batch-autoloads.patch to fix generation of autoloads
  for xemacs-21.5

* Mon May 30 2005 Jens Petersen <petersen@redhat.com> - 1.14.7-3
- Initial import into Extras
- restore xemacs subpackage

* Wed Feb 23 2005 Elliot Lee <sopwith@redhat.com> 1.14.7-2
- Remove xemacs subpackage

* Sat Oct  9 2004 Jens Petersen <petersen@redhat.com> - 1.14.7-1
- update to 1.14.7 release
- flim-1.14.6-mel-u-tempfile.patch no longer needed

* Wed Oct  6 2004 Jens Petersen <petersen@redhat.com> - 1.14.6-3
- drop requirements on emacs/xemacs for -nox users
  (Lars Hupfeldt Nielsen, 134479)

* Tue Sep 28 2004 Warren Togami <wtogami@redhat.com> - 1.14.6-2
- remove redundant docs, large changelog, tests

* Thu May 20 2004 Jens Petersen <petersen@redhat.com> - 1.14.6-1
- update to 1.14.6
- add flim-1.14.6-mel-u-tempfile.patch to fix CAN-2004-0422
- move redundant %%emacsver and %%xemacsver into requirements
- better url and summary

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> - 1.14.5-2
- rebuilt

* Sat Aug  2 2003 Jens Petersen <petersen@redhat.com> - 1.14.5-1
- update to 1.14.5

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 24 2002 Jens Petersen <petersen@redhat.com> 1.14.4-1
- update to 1.14.4
- install xemacs package under datadir
- own emacs site-lisp and down
- own xemacs-packages and down

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 1.14.3-7
- add the owned directory.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb 22 2002 Tim Powers <timp@redhat.com>
- rebuilt in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov 30 2001 Jens Petersen <petersen@redhat.com> 1.14.3-2
- noarch, since xemacs available on ia64 
- require apel

* Fri Oct 26 2001 Akira TAGOH <tagoh@redhat.com> 1.14.3-1
- Initial release.
  Separated from semi package.
