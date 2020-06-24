Name:           perl-DBIx-ContextualFetch
Version:        1.03
Release:        38%{?dist}
Summary:        Add contextual fetches to DBI
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-ContextualFetch
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/DBIx-ContextualFetch-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(DBI), perl(ExtUtils::MakeMaker)
BuildRequires:  perl(DBD::SQLite), perl(Test::Pod::Coverage), perl(Test::More)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(DBI)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI::(st|db)\\)

%description
%{summary}.

%prep
%setup -q -n DBIx-ContextualFetch-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-38
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-35
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-32
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-29
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-27
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-24
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-23
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.03-20
- Perl 5.18 rebuild

* Tue Mar  5 2013 Tom Callaway <spot@fedoraproject.org> - 1.03-19
- add missing BR: ExtUtils::MakeMaker

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.03-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 1.03-14
- update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-13
- Perl mass rebuild

* Tue Feb 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-12
- new filter with RPM4.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.03-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03-5
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-4
- rebuild for new perl

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-3
- license fix

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-2
- bump for fc6

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-1
- bump to 1.03

* Wed Aug 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-3
- more cleanups

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-1
- Initial package for Fedora Extras
