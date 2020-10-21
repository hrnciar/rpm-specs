Name:           perl-Class-DBI-Plugin-Type
Version:        0.02
Release:        43%{?dist}
Summary:        Determine type information for columns
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-DBI-Plugin-Type
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMON/Class-DBI-Plugin-Type-%{version}.tar.gz
# Adapt to changes in DBD-SQLite-1.61_02, bug #1664030, CPAN RT#128135,
# proposed to the upstream
Patch0:         Class-DBI-Plugin-Type-0.02-Fix-compatibility-with-DBD-SQLite-1.61_02.patch
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(Class::DBI::Plugin)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)
Requires:  perl(Class::DBI::Plugin)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.

%prep
%setup -q -n Class-DBI-Plugin-Type-%{version}
%patch0 -p1
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Artistic COPYING Changes
%{perl_vendorlib}/Class/DBI/Plugin/
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-42
- Perl 5.32 rebuild

* Mon Mar 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-41
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-38
- Perl 5.30 rebuild

* Mon Apr 29 2019 Petr Pisar <ppisar@redhat.com> - 0.02-37
- Adapt to changes in DBD-SQLite-1.61_02 (bug #1664030)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-34
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.02-33
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-30
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-28
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-25
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-24
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.02-21
- Perl 5.18 rebuild

* Tue Mar  5 2013 Tom Callaway <spot@fedoraproject.org> - 0.02-20
- add missing BR ExtUtils::MakeMaker

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 0.02-17
- Perl 5.16 rebuild

* Mon Jan 23 2012 Tom Callaway <spot@fedoraproject.org> - 0.02-16
- fix build

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.02-14
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-12
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-11
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.02-10
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-7
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-6
- rebuild for new perl

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-5
- license fix

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-4
- bump for fc6

* Wed Aug 31 2005 Paul Howarth <paul@city-fan.org> 0.02-3
- remove redundant BR: perl
- use %%{?_smp_mflags} with make in %%build
- include license text
- add BR: perl(DBD::SQLite) for %%check

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-1
- Initial package for Fedora Extras
