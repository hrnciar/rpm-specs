Name:           perl-DBIx-DBSchema
Version:        0.45
Release:        18%{?dist}
Summary:        Database-independent schema objects

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-DBSchema
Source0:	https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz

BuildArch:      noarch
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:	perl(DBI)
BuildRequires:  perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FreezeThaw)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)


# Required by the tests
BuildRequires:  perl(Test::More)
BuildRequires:	perl(DBD::Pg) >= 1.41

%description
DBIx::DBSchema objects are collections of DBIx::DBSchema::Table objects and 
represent a database schema.

This module implements an OO-interface to database schemas. Using this module, 
you can create a database schema with an OO Perl interface. You can read the
schema from an existing database. You can save the schema to disk and restore
it a different process. Most importantly, DBIx::DBSchema can write SQL CREATE
statements statements for different databases from a single source.

Currently supported databases are MySQL and PostgreSQL. 

%prep
%setup -q -n DBIx-DBSchema-%{version}
chmod -x README Changes
find -name '*.pm' -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-6
- Perl 5.24 rebuild

* Sun Feb 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.45-5
- Modernize spec.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-2
- Perl 5.22 rebuild

* Thu May 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.45-1
- Upstream update.
- Update BRs.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 26 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.44-1
- Upstream update.
- Spec cleanup.
- Fix bogus changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.40-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 0.40-2
- Perl 5.16 rebuild

* Thu Jan 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.40-1
- Upstream update.
- Modernize specfile.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.39-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.39-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.39-1
- Upstream update.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.38-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.36-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.36-2
- rebuild for new perl

* Sat Dec 22 2007 Ralf Corsépius <rc040203@freenet.de> - 0.36-1
- Upstream update.
- Remove DBIx-DBSchema-0.28-version.diff.

* Wed Oct 31 2007 Ralf Corsépius <rc040203@freenet.de> - 0.35-1
- Upstream update.

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 0.34-1
- Upstream update.
- Update license tag.

* Mon Jul 02 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-1
- Upstream update.

* Thu Apr 19 2007 Ralf Corsépius <rc040203@freenet.de> - 0.32-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.31-2
- Mass rebuild.

* Sat Apr 22 2006  Ralf Corsépius <rc040203@freenet.de> - 0.31-1
- Upstream update.

* Sun Feb 19 2006  Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Upstream update.

* Wed Dec 21 2005  Ralf Corsépius <rc040203@freenet.de> - 0.28-2
- Apply work around to CPAN incompatibility (PR #175468, J.V. Dias).

* Mon Dec 05 2005  Ralf Corsépius <rc040203@freenet.de> - 0.28-1
- Upstream update.

* Sun Nov 06 2005  Ralf Corsépius <rc040203@freenet.de> - 0.27-2
- Change URL (PR #170384, Paul Howard).

* Mon Oct 10 2005  Ralf Corsépius <rc040203@freenet.de> - 0.27-1
- Initial package.
- FE submission.
 
