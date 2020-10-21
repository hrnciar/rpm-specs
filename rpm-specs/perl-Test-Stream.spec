Name:           perl-Test-Stream
Version:        1.302027
Release:        19%{?dist}
Summary:        Successor to Test::More and Test::Builder
# The license URL in COPYRIGHT POD sections is wrong,
# <https://github.com/Test-More/Test-Stream/issues/66>
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Stream
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Stream-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Sub::Name) >= 0.11
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Term::ReadKey) >= 2.03
BuildRequires:  perl(Unicode::GCString) >= 2013.10
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
# Optional test:
# Break build-cycle: perl-Test-Stream → perl-Trace-Mask → perl-Test-Stream
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Trace::Mask) >= 0.000005
BuildRequires:  perl(Trace::Mask::Reference)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(utf8)
# Optional run-time:
Suggests:       perl(Sub::Name) >= 0.11
Suggests:       perl(Sub::Util) >= 1.40
Suggests:       perl(Term::ReadKey) >= 2.03
Suggests:       perl(Unicode::GCString) >= 2013.10

%description
This is a framework for writing and running tests in Perl. Test::Stream is
inspired by Test::Builder, but it provides a much more sane approach. Bundles
and Tools are kept separate, this way you can always use tools without being
forced to adopt the authors ideal bundle.

This distribution is deprecated in favor of Test2.

%prep
%setup -q -n Test-Stream-%{version}

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
# README.md duplicates README's content
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-18
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-14
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-10
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-6
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.302027-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.302027-2
- Perl 5.24 rebuild

* Mon Feb 08 2016 Petr Šabata <contyk@redhat.com> - 1.302027-1
- 1.302027 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.302026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Petr Pisar <ppisar@redhat.com> - 1.302026-2
- Remove local bootstrap because perl-Trace-Mask has been packaged

* Mon Nov 23 2015 Petr Pisar <ppisar@redhat.com> 1.302026-1
- Specfile autogenerated by cpanspec 1.78.
