Name:           perl-Data-Validate-Domain
Version:        0.14
Release:        14%{?dist}
Summary:        Domain validation methods Perl module

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Validate-Domain
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-Domain-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Net::Domain::TLD) >= 1.74
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))


%description
This module collects domain validation routines to make input validation, and
untainting easier and more readable.

All functions return an untainted value if the test passes, and undef if it
fails. This means that you should always check for a defined status explicitly.
Don't assume the return will be true. (e.g. is_username('0'))

The value to test is always the first (and often only) argument.


%prep
%setup -q -n Data-Validate-Domain-%{version}
find lib -name "*.pm" -exec chmod -c a-x {} +


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
%{make_build} test


%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-13
- Perl 5.32 rebuild

* Sun Apr 05 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.14-12
- Replace calls to perl with /usr/bin/perl
- Replace calls to make pure_install with %%{make_install}
- Replace calls to make with %%{make_build}
- Pass NO_PACKLIST=1 NO_PERLLOCAL=1 to Makefile.PL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-1
- 0.14 bump

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- 0.12 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-1
- 0.11 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.10-2
- Perl 5.18 rebuild

* Tue Jan 22 2013 Normunds Neimanis <fedorapkg at rule.lv> 0.10-1
- Initial package for Fedora
