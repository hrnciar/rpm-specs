Name:           perl-HTML-FormFu-MultiForm
Version:        1.03
Release:        11%{?dist}
Summary:        Handle multi-page/stage forms
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-FormFu-MultiForm
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-FormFu-MultiForm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Crypt::CBC)
# Crypt::DES is a default cipher used by the Crypt::CBC, bug #1087536
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(HTML::FormFu)
BuildRequires:  perl(HTML::FormFu::Attribute)
BuildRequires:  perl(HTML::FormFu::ObjectUtil)
BuildRequires:  perl(HTML::FormFu::QueryType::CGI)
BuildRequires:  perl(HTML::FormFu::Role::FormAndElementMethods)
BuildRequires:  perl(HTML::FormFu::Role::FormBlockAndFieldMethods)
BuildRequires:  perl(HTML::FormFu::Role::NestedHashUtils)
BuildRequires:  perl(HTML::FormFu::Role::Populate)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Test:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(YAML::XS)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Crypt::DES is a default cipher used by the Crypt::CBC, bug #1087536
Requires:       perl(Crypt::DES)
Requires:       perl(HTML::FormFu::Role::FormAndElementMethods)
Requires:       perl(HTML::FormFu::Role::FormBlockAndFieldMethods)
Requires:       perl(HTML::FormFu::Role::NestedHashUtils)
Requires:       perl(HTML::FormFu::Role::Populate)

%description
Multi-page support for HTML::FormFu, a Perl HTML form framework.

%prep
%setup -q -n HTML-FormFu-MultiForm-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Mon Jul 24 2017 Petr Pisar <ppisar@redhat.com> - 1.00-11
- Remove CGI tests that fail randomly (bug #1460679)

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Petr Pisar <ppisar@redhat.com> - 1.00-6
- Do not use Test::Aggregate::Nested for tests because it's not available
  anymore (bug #1231204)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> 1.00-1
- Specfile autogenerated by cpanspec 1.78.
