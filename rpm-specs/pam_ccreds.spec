Summary: Pam module to cache login credentials
Name: pam_ccreds
Version: 10
Release: 21%{?dist}
License: GPL+
URL: http://www.padl.com/OSS/pam_ccreds.html
Source0: http://www.padl.com/download/%{name}-%{version}.tar.gz
Patch1: pam_ccreds-3-inst-no-root.patch
Patch2: pam_ccreds-7-no-filename.patch
Patch3: pam_ccreds-7-open.patch

BuildRequires:  gcc
BuildRequires: automake libdb-devel libgcrypt-devel pam-devel

%description
The pam_ccreds module provides a mechanism for caching
credentials when authenticating against a network
authentication service, so that authentication can still
proceed when the service is down. Note at present no
mechanism is provided for caching _authorization_ 
information, i.e. whether you are allowed to login once
authenticated.

%prep
%setup -q
%patch1 -p1 -b .inst-no-root
%patch2 -p1 -b .no-filename
%patch3 -p1 -b .open
touch compile
autoreconf

%build
%configure --libdir=/%{_lib} --enable-gcrypt
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

install -m 755 cc_test $RPM_BUILD_ROOT%{_sbindir}
install -m 755 cc_dump $RPM_BUILD_ROOT%{_sbindir}

%files
%doc AUTHORS README
/%{_lib}/security/pam_ccreds.so
%attr(4755,root,root) %{_sbindir}/ccreds_chkpwd
%{_sbindir}/cc_test
%{_sbindir}/cc_dump

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> - 10-9
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Mat Booth <fedora@matbooth.co.uk> - 10-7
- Fix FTBFS following mass rebuild.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 12 2010 Caolán McNamara <caolanm@redhat.com> - 10-2
- rebuild against db4-4.8

* Mon Sep 28 2009 Avesh Agarwal <avagarwa@redhat.com> - 10-1
- Upgrade to latest upstream
- Updated patches

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7-3
- rebuild against db4-4.7

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7-2
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Tomas Mraz <tmraz@redhat.com> - 7-1
- upgrade to latest upstream
- build against libgcrypt and not openssl

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 4-3
- license tag fix
- build with open defined as macro

* Thu Apr  5 2007 Tomas Mraz <tmraz@redhat.com> - 4-2
- minor updates for merge review (#226224)

* Mon Feb  5 2007 Tomas Mraz <tmraz@redhat.com> - 4-1
- new upstream version

* Tue Aug 22 2006 Tomas Mraz <tmraz@redhat.com> - 3-5
- add cc_test and cc_dump utilities

* Fri Jul 21 2006 Tomas Mraz <tmraz@redhat.com> - 3-4
- fixed mistake in chkpwd patch causing update creds to fail

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3-3.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Tomas Mraz <tmraz@redhat.com> - 3-3
- don't change ownership in make install
- build ccreds_validate as PIE

* Wed Jan  4 2006 Tomas Mraz <tmraz@redhat.com> - 3-2
- the path to ccreds_validate helper was wrong

* Wed Jan  4 2006 Tomas Mraz <tmraz@redhat.com> - 3-1
- new upstream version
- added patch (slightly modified) by W. Michael Petullo to support
  operation from non-root accounts (#151914)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> - 1-8
- rebuilt against new openssl

* Thu Jun  9 2005 John Dennis <jdennis@redhat.com> - 1-7
- fix bug #134674, change BuildPrereq openssl to openssl-devel

* Wed Mar 16 2005 John Dennis <jdennis@redhat.com> 1-6
- bump rev for gcc4 build

* Wed Mar 16 2005 Dan Williams <dcbw@redhat.com> pam_ccreds-1-5
- rebuild to pick up new libcrypto.so.5

* Mon Feb 14 2005 Nalin Dahyabhai <nalin@redhat.com> pam_ccreds-1-4
- change install dir from /lib/security to /%%{_lib}/security

* Tue Oct 12 2004 Miloslav Trmac <mitr@redhat.com> pam_ccreds-1-3
- BuildRequire: automake16, openssl (from Maxim Dzumanenko, #134674)

* Wed Sep  1 2004 John Dennis <jdennis@redhat.com> pam_ccreds-1-2
- change install dir from /%%{_lib}/security to /lib/security

* Sun Jun 13 2004 John Dennis <jdennis@redhat.com> ccreds-1
- Initial build.
