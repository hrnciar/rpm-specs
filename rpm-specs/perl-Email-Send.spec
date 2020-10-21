Name:           perl-Email-Send
Version:        2.201
Release:        18%{?dist}
Summary:        Module for sending email
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-Send
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Send-%{version}.tar.gz
BuildRequires:  coreutils, findutils, make
BuildRequires:  perl-generators, perl-interpreter
BuildRequires:  perl(blib), perl(Capture::Tiny), perl(Cwd), perl(Email::Abstract)
BuildRequires:  perl(Email::Address), perl(Email::Simple), perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path), perl(File::Spec), perl(File::Temp), perl(IO::All),
BuildRequires:  perl(IO::Handle), perl(IPC::Open3), perl(lib),
BuildRequires:  perl(Mail::Internet), perl(MIME::Entity), perl(Module::Pluggable)
BuildRequires:  perl(Return::Value), perl(Scalar::Util), perl(strict), perl(Symbol),
BuildRequires:  perl(Test::More), perl(Test::Pod), perl(Test::Pod::Coverage)
BuildRequires:  perl(vars), perl(version), perl(warnings),
BuildRequires:  sed
BuildRequires:  /usr/sbin/sendmail
BuildArch:      noarch
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Not automatically detected, but needed.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1000737
#     https://bugzilla.redhat.com/show_bug.cgi?id=1031298
Requires:	perl(Module::Pluggable)
Requires:	perl(Return::Value)

%description
This module provides a very simple, very clean, very specific interface
to multiple Email mailers. The goal of this software is to be small and
simple, easy to use, and easy to extend.

%prep
%setup -q -n Email-Send-%{version}

%build
sed -i '/LICENSE/ d' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT _docs
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README LICENSE
%{perl_vendorlib}/Email/
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-17
- Perl 5.32 rebuild

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-16
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-2
- Perl 5.22 rebuild

* Fri Mar 20 2015 Tom Callaway <spot@fedoraproject.org> - 2.201-1
- update to 2.201

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.199-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.199-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Tom Callaway <spot@fedoraproject.org> - 2.199-2
- add another explicit Requires: perl(Return::Value)

* Wed Sep  4 2013 Tom Callaway <spot@fedoraproject.org> - 2.199-1
- update to 2.199
- add explicit Requires: perl(Module::Pluggable)
- add missing BuildRequires

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 2.198-10
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.198-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.198-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.198-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 2.198-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.198-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.198-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.198-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.198-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.198-1
- update to 2.198

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.194-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.194-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.194-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.194-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.194-1
- update to 2.194

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.192-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.192-2
Rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.192-1
- bump to 2.192

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.185-3
- license tag fix

* Tue Apr 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.185-2
- get rid of WARNING: LICENSE... 
- add missing BR

* Sun Apr  1 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.185-1
- Initial package for Fedora
