# Execute extra test
%bcond_with perl_DateTime_Format_Flexible_enables_extra_test

Name:       perl-DateTime-Format-Flexible
Version:    0.32
Release:    4%{?dist}
License:    GPL+ or Artistic
Summary:    Flexibly parse strings and turn them into DateTime objects
Source:     https://cpan.metacpan.org/authors/id/T/TH/THINC/DateTime-Format-Flexible-%{version}.tar.gz
Url:        https://metacpan.org/release/DateTime-Format-Flexible
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.74
BuildRequires:  perl(DateTime::Infinite)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
# Extra tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
If you have ever had to use a program that made you type in the date a certain
way and thought "Why can't the computer just figure out what date I wanted?",
this module is for you.

DateTime::Format::Flexible attempts to take any string you give it and parse
it into a DateTime object.

%prep
%setup -q -n DateTime-Format-Flexible-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
export TEST_POD=1
%else
export TEST_POD=0
%endif
make test

%files
%license LICENSE
%doc Changes example/ README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Petr Pisar <ppisar@redhat.com> - 0.32-1
- 0.32 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Petr Pisar <ppisar@redhat.com> - 0.31-1
- 0.31 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.28 rebuild

* Mon Mar 12 2018 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump
- Disable extra tests by default

* Fri Feb 23 2018 Petr Pisar <ppisar@redhat.com> - 0.29-1
- 0.29 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.26 rebuild

* Fri Mar 24 2017 Petr Pisar <ppisar@redhat.com> - 0.28-1
- 0.28 bump

* Mon Mar 06 2017 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.25-2
- Perl 5.18 rebuild

* Tue Mar 05 2013 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.23-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.23-1
- 0.23 bump

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Wed Jan 25 2012 Petr Pisar <ppisar@redhat.com> - 0.21-1
- 0.21 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.15-5
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.15-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-1
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- auto-update to 0.09 (by cpan-spec-update 0.01)

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- auto-update to 0.08 (by cpan-spec-update 0.01)
- added a new br on perl(DateTime::TimeZone) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- brush up for submission

* Sun Dec 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.05-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.6)
