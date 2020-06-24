# Run optional test
%bcond_without perl_Inline_Filters_enables_optional_test

Name:           perl-Inline-Filters
Version:        0.20
Release:        13%{?dist}
Summary:        Common source code filters for Inline modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Inline-Filters
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Inline-Filters-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
# Required indirectly, optional Inline dependency
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
%if %{with perl_Inline_Filters_enables_optional_test}
# Optional tests only
# Class::XSAccessor not used
# List::MoreUtil not used
# Test::Kwalitee not used
BuildRequires:  perl(Test::Pod) >= 1.00
# Text::CSV_XS not used
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Parse::RecDescent)

%description
Inline::Filters provide common source code filters to Inline language
modules.

%prep
%setup -q -n Inline-Filters-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-7
- Perl 5.28 rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.20-6
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump

* Wed Jan 25 2017 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 0.19 bump

* Wed Sep 07 2016 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump
- Modernize SPEC

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.20 rebuild

* Thu Aug 14 2014 Petr Šabata <contyk@redhat.com> - 0.16-1
- 1.16 bump

* Wed Jul 16 2014 Petr Šabata <contyk@redhat.com> 0.14-1
- Initial packaging
