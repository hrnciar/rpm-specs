Name:           perl-Apache-DBI-Cache
Version:        0.08
Release:        37%{?dist}
Summary:        Perl DBI connection cache
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Apache-DBI-Cache
Source0:        https://cpan.metacpan.org/authors/id/O/OP/OPI/Apache-DBI-Cache-%{version}.tar.gz
Patch0:         0001-DBI-dr-connect-can-clobber-the-arguments.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(DBI) >= 1.37
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(BerkeleyDB)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
Requires:       perl(DBI) >= 1.37
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(DBI::st\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DBI::db\\)$

%description
This module is an alternative to Apache::DBI module. As a drop-in
Apache::DBI replacement it provides persistent DBI connections
while overcoming certain limitations. It is compatible with mod_perl,
though it does not require it.


%prep
%setup -q -n Apache-DBI-Cache-%{version}
%patch0 -p1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-37
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-34
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-31
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-28
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-26
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-23
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 0.08-19
- Perl 5.18 rebuild

* Mon Feb 18 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.08-18
- Invert perl_default_filter and __requires_exclude

* Sun Feb 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.08-17
- Remove no-longer-used macros
- Add ExtUtils::MakeMaker to BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 0.08-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 0.08-12
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.08-11
- Perl mass rebuild

* Fri Feb 25 2011 Marcela Maslanova <mmaslano@redhat.com> - 0.08-10
- filter useless requires

* Fri Feb 25 2011 Marcela Maslanova <mmaslano@redhat.com> - 0.08-9
- filter useless requires

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.08-6
- Fix a bug which made test suite fail with recent DBI

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.08-1
- Specfile autogenerated by cpanspec 1.77.
- Fixup license and dependencies
