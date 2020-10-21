Name:           perl-Test-Module-Used
Version:        0.2.6
Release:        17%{?dist}
Summary:        Test required module is really used and vice versa between lib/t and META.yml
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Module-Used
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSUCCHI/Test-Module-Used-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-Time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Used)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version) >= 0.77
# Tests:
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(version) >= 0.77

# Remove under-specified depepndencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$

%description
This module reads META.yml and gets build_requires and requires. It compares
required module is really used and used module is really required.

%prep
%setup -q -n Test-Module-Used-%{version}
find -type f -exec chmod -x {} +

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.6-2
- Perl 5.22 rebuild

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 0.2.6-1
- 0.2.6 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.4-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.2.4-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Petr Pisar <ppisar@redhat.com> - 0.2.4-1
- 0.2.4 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.2.3-2
- Perl 5.16 rebuild

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 0.2.3-1
- Specfile autogenerated by cpanspec 1.78.
