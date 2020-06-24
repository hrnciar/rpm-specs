Name:           perl-Perl-Critic-Deprecated
Version:        1.119
Release:        18%{?dist}
Summary:        Perl::Critic policies which have been superseded by others
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-Critic-Deprecated
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Perl-Critic-Deprecated-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(English)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
# Carp not used by tests
# Exporter not used by tests
# List::MoreUtils not used by tests
BuildRequires:  perl(Perl::Critic::Policy) >= 1.094
BuildRequires:  perl(Perl::Critic::Utils) >= 1.094
# PPI::Node not used by tests
BuildRequires:  perl(Readonly)
# Optional run-time:
# Regexp::Parser not used by tests
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.094
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Perl::Critic::Policy) >= 1.094
Requires:       perl(Perl::Critic::Utils) >= 1.094
# Perl::Critic::Policy::Miscellanea::RequireRcsKeywords moved from
# perl-Perl-Critic-More here. Bugs #839815, 1023708.
Conflicts:      perl-Perl-Critic-More <= 1.000-11

# Filter underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Perl::Critic::Policy|Perl::Critic::Utils)\\)$

%description
The included policies are:
  - Write "$my_variable = 42" instead of "$MyVariable = 42".
  - Write "sub my_function{}" instead of "sub MyFunction{}".
  - Put source-control keywords in every file.

%prep
%setup -q -n Perl-Critic-Deprecated-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-12
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.119-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 Petr Pisar <ppisar@redhat.com> - 1.119-1
- 1.119 bump

* Tue Oct 29 2013 Petr Pisar <ppisar@redhat.com> - 1.118-1
- 1.118 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 1.108-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.108-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 1.108-3
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.108-2
- Perl mass rebuild

* Wed Mar 02 2011 Petr Pisar <ppisar@redhat.com> 1.108-1
- Specfile autogenerated by cpanspec 1.78.
- Summary shortened
- Remove BuildRoot stuff
