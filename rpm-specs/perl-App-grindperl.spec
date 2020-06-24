Name:           perl-App-grindperl
Version:        0.004
Release:        14%{?dist}
Summary:        Command-line tool to help build and test blead perl
License:        ASL 2.0
URL:            https://metacpan.org/release/App-grindperl
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/App-grindperl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# The only test does not exercise the code
# autodie not used at tests
# Carp not used at tests
# File::Copy not used at tests
# File::HomeDir 0.98 not used at tests
# File::Spec not used at tests
# Getopt::Lucid not used at tests
# namespace::autoclean not used at tests
# Path::Class not used at tests
# Tests:
# CPAN::Meta not usefull
# CPAN::Meta::Prereqs not usefull
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       git
Requires:       make

%description
Hacking on the Perl source tree requires one to regularly build and test. The
grindperl tool helps automate some common configuration, build and test tasks.

%prep
%setup -q -n App-grindperl-%{version}

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
%license LICENSE
# CONTRIBUTING.mkdn is a generic file not specific to this package
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-2
- Perl 5.22 rebuild

* Mon Feb 23 2015 Petr Pisar <ppisar@redhat.com> - 0.003-1
- 0.003 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.002-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.002-2
- Perl 5.18 rebuild

* Tue Jun 18 2013 Petr Pisar <ppisar@redhat.com> - 0.002-1
- 0.002 bump

* Thu May 23 2013 Petr Pisar <ppisar@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
