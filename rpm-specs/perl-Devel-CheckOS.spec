Name:           perl-Devel-CheckOS
Version:        1.83
Release:        2%{?dist}
Summary:        Check what OS we're running on
# Devel/AssertOS/Extending.pod: CC-BY-SA
# Devel/CheckOS/Families.pod:   CC-BY-SA
# Other files:  GPLv2 or Artistic
License:        (GPLv2 or Artistic) and CC-BY-SA
URL:            https://metacpan.org/release/Devel-CheckOS
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Find::Rule) >= 0.28

# Remove unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Find::Rule\\)$

%description
Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS families such as Unix, which includes things like Linux,
*BSD, AIX, HPUX, Solaris etc.

%prep
%setup -q -n Devel-CheckOS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README TODO
%{_bindir}/use-devel-assertos
%{perl_vendorlib}/*
%{_mandir}/man1/use-devel-assertos.1.gz
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.83-2
- Perl 5.32 rebuild

* Mon Feb 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.83-1
- 1.83 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-1
- 1.81 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-2
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-1
- 1.80 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.79-1
- 1.79 bump

* Mon Oct 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-1
- 1.77 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-2
- Perl 5.22 rebuild

* Mon Mar 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-1
- 1.76 bump

* Thu Mar 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-1
- 1.75 bump
- Correct license from (GPLv2 or Artistic) to ((GPLv2 or Artistic) and
  CC-BY-SA)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-2
- Perl 5.20 rebuild

* Tue Aug 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-1
- 1.73 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-1
- 1.72 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.71-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Petr Pisar <ppisar@redhat.com> - 1.71-1
- 1.71 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.64-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 1.64-4
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-2
- Perl mass rebuild

* Wed Apr 27 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.64-1
- update to 1.64

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.63-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump
- Remove `dontask' patch as interactive code is not run anymore
- Add versioned Requires, filter unversioned ones out

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.50-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-2
- remove two tests, because they can't pass in rpmbuild.

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-1
- Specfile autogenerated by cpanspec 1.77.
