Name:       perl-Config-ApacheFormat
Version:    1.2
Release:    22%{?dist}
Summary:    Use Apache format config files
License:    GPL+ or Artistic
URL:        https://metacpan.org/release/Config-ApacheFormat
Source0:    https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/Config-ApacheFormat-%{version}.tar.gz
# Fix a Use of uninitialized value in lc warning, CPAN RT#132271
Patch0:     Config-ApacheFormat-1.2-Fix-a-Use-of-uninitialized-value-in-lc-warning.patch
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MethodMaker) >= 1.08
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Balanced) >= 1.89
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
Requires:   perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# (Data::Dumper is used only in runtime, not in tests)
Requires:   perl(Class::MethodMaker) >= 1.08
Requires:   perl(Data::Dumper)
Requires:   perl(File::Spec) >= 0.82
Requires:   perl(Text::Balanced) >= 1.89

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Class::MethodMaker|File::Spec|Text::Balanced)\\)$

%description
This Perl module is designed to parse a configuration file in the same syntax
used by the Apache web server (see <http://httpd.apache.org/> for details).
This enables you to build applications which can be easily managed by
experienced Apache administrators.  Also, by using this module, you'll benefit
from the support for nested blocks with built-in parameter inheritance. This
can greatly reduce the amount or repeated information in your configuration
files.

%prep
%setup -q -n Config-ApacheFormat-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-22
- Perl 5.32 rebuild

* Tue Mar 31 2020 Petr Pisar <ppisar@redhat.com> - 1.2-21
- Modernize a spec file
- Fix a Use of uninitialized value in lc warning (CPAN RT#132271)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.2-3
- Perl 5.18 rebuild

* Mon Jun 17 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.2-2
- Added missing Require Class::MethodMaker

* Wed Jan 23 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.2-1
- Package for current Fedora
