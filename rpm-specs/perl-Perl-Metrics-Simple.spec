Name:           perl-Perl-Metrics-Simple
Version:        0.18
Release:        17%{?dist}
Summary:        Count packages, subs, lines, etc. of many files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-Metrics-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATISSE/Perl-Metrics-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find) >= 1.01
BuildRequires:  perl(IO::File) >= 1.14
# Pod::Usage not used at tests
BuildRequires:  perl(PPI) >= 1.113
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Readonly) >= 1.03
BuildRequires:  perl(Statistics::Basic::Mean)
BuildRequires:  perl(Statistics::Basic::Median)
BuildRequires:  perl(Statistics::Basic::StdDev)
# Recommended:
BuildRequires:  perl(Readonly::XS) >= 1.02
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Moose not used, t/test_files/Perl/Code/Analyze/Test/Moose.pm is not compiled
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Perl::Critic not used
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Find) >= 1.01
Requires:       perl(IO::File) >= 1.14
Requires:       perl(PPI) >= 1.113
Requires:       perl(Readonly) >= 1.03
# Recommended:
Requires:       perl(Readonly::XS) >= 1.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(File::Find\\)$
%global __requires_exclude %__requires_exclude|perl\\(IO::File\\)$
%global __requires_exclude %__requires_exclude|perl\\(PPI\\)$
%global __requires_exclude %__requires_exclude|perl\\(Readonly\\)$

%description
Perl::Metrics::Simple provides just enough methods to run static analysis
of one or many Perl files and obtain a few metrics: packages, subroutines,
lines of code, and an approximation of cyclomatic (McCabe) complexity for
the subroutines and the "main" portion of the code.

%prep
%setup -q -n Perl-Metrics-Simple-%{version}
sed -i '1 s|^#!.*|#!%{__perl}|' bin/countperl

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes EXAMPLES LICENSE README Todo
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-3
- Perl 5.22 rebuild

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Build-require Test::Pod module for tests again

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.17-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump

* Mon Oct 29 2012 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.15-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-4
- add RPM4.9 macro filter

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Tune dependencies
