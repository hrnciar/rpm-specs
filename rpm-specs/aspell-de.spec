%define lang de
%define langrelease 1
%define aspellversion 6
Summary: German dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 20030222
Release: 23%{?dist}
License: GPLv2
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 12:0.60
Requires: aspell >= 12:0.60

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: German, Swiss German

%prep
%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING
%defattr(-,root,root,-)

%{_libdir}/aspell-0.60/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 50:20030222-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:20030222-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 50:20030222-4
- Autorebuild for GCC 4.3

* Thu Mar 29 2007 Ivana Varekova <varekova@redhat.com> - 50:20030222-3
- add documentation

* Thu Mar 29 2007 Ivana Varekova <varekova@redhat.com> - 50:20030222-1
- update to 20030222
- use configure script to create Makefile
- update default build root
- some minor spec changes

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Jul 18 2005 Ivana Varekova <varekova@redhat.com> 50:0.50-11
- build with aspell-0.60.3

* Mon Apr 11 2005 Ivana Varekova <varekova@redhat.com> 50:0.50-10
- rebuilt

* Wed Sep 29 2004 Adrian Havill <havill@redhat.com> 50:0.50-9
- remove debuginfo

* Wed Aug 11 2004 Adrian Havill <havill@redhat.com> 50:0.50-8
- sync epoch with other aspell dicts

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 23 2003 Adrian Havill <havill@redhat.com> 0.50-5
- data files are arch dependent

* Fri Jun 20 2003 Adrian Havill <havill@redhat.com> 0.50-4
- first build for new aspell (0.50)
