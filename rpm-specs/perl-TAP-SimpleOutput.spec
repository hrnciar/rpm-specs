Name:           perl-TAP-SimpleOutput
Version:        0.009
Release:        12%{?dist}
Summary:        Simple closure-driven TAP generator
License:        LGPLv2
URL:            https://metacpan.org/release/TAP-SimpleOutput
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/TAP-SimpleOutput-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
# Perl::Version checked by t/00-check-deps.t
BuildRequires:  perl(Perl::Version)
BuildRequires:  perl(Sub::Exporter::Progressive)
# Test::More 0.98 not used at tests
# Tests:
BuildRequires:  perl(blib) >= 1.01
# CPAN::Meta not useful
# CPAN::Meta::Prereq not useful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Perl::Version)
Requires:       perl(Test::More) >= 0.98

%description
We provide one function, counters(), that returns a number of simple closures
designed to help output TAP easily and correctly, with a minimum of fuss.

%prep
%setup -q -n TAP-SimpleOutput-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-2
- Perl 5.26 rebuild

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Wed Nov 09 2016 Petr Pisar <ppisar@redhat.com> - 0.007-1
- 0.007 bump

* Wed Nov 02 2016 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 0.003-1
- 0.003 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Petr Pisar <ppisar@redhat.com> - 0.002-1
- 0.002 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.001-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Petr Pisar <ppisar@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
