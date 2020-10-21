Name:       perl-Eval-Context 
Version:    0.09.11 
Release:    24%{?dist}
# see lib/Eval/Context.pm
License:    GPL+ or Artistic
Summary:    Evalute perl code in context wraper 
Source:     https://cpan.metacpan.org/authors/id/N/NK/NKH/Eval-Context-%{version}.tar.gz 
# Perl 5.18 comptability, CPAN RT#86017
Patch0:     Eval-Context-0.09.11-hash-randomization.patch
Url:        https://metacpan.org/release/Eval-Context
Requires:   perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildArch:  noarch

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Carp)
BuildRequires: perl(constant)
BuildRequires: perl(Data::Compare)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Directory::Scratch::Structured)
BuildRequires: perl(English)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Package::Generator)
BuildRequires: perl(Readonly)
BuildRequires: perl(Safe) >= 2.16
BuildRequires: perl(strict)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(vars)
BuildRequires: perl(version) >= 0.5
BuildRequires: perl(warnings)


%description
This module defines a subroutine that let you evaluate Perl code in a
specific context. The code can be passed directly as a string or as a file
name to read from.  It also provides some subroutines to let you define and
optionally share variables and subroutines between your code and the code
you wish to evaluate. Finally there is some support for running your code
in a safe compartment.

%prep
%setup -q -n Eval-Context-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes Todo.txt 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-23
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-20
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-17
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.09.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-9
- Perl 5.22 rebuild
- Update the list of BRs

* Thu Sep 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09.11-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.09.11-6
- Perl 5.18 rebuild
- Perl 5.18 comptability (CPAN RT#86017)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Petr Pisar <ppisar@redhat.com> - 0.09.11-2
- Perl 5.16 rebuild

* Fri Jan 27 2012 Marcela Maslanova <mmaslano@redhat.com> - 0.09.11-1
- update and clean spec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.07-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-8
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.07-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.07-2
- drop Test::Perl::Critic -- it's failing, and an author test to boot

* Sat Nov 29 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- update for submission

* Sat Nov 29 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.07-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)

