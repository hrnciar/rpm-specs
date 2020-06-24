Summary:	Provable prime number generator for cryptographic applications
Name:		perl-Crypt-Primes
Version:	0.50
Release:	40%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Crypt-Primes
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Crypt-Primes-%{version}.tar.gz
Patch0:		Crypt-Primes-0.50-more-stack.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Crypt::Random)	>= 0.33
BuildRequires:	perl(Exporter)
BuildRequires:	perl(integer)
BuildRequires:	perl(Math::Pari)	>= 2.001804
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements Ueli Maurer's algorithm for generating large provable
primes and secure parameters for public-key cryptosystems. The generated primes
are almost uniformly distributed over the set of primes of the specified
bitsize and expected time for generation is less than the time required for
generating a pseudo-prime of the same size with Miller-Rabin tests. Detailed
description and running time analysis of the algorithm can be found in Maurer's
paper, "Fast Generation of Prime Numbers and Secure Public-Key Cryptographic
Parameters" (1994).

%prep
%setup -q -n Crypt-Primes-%{version}

# Allocate more stack for tests to avoid intermittent build failures
%patch0

# Remove redundant shellbang to placate rpmlint
sed -i -e '/^#! *\/usr\/bin\/perl /d' lib/Crypt/Primes.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%files
%doc Changes README docs/*
%{_bindir}/largeprimes
%{perl_vendorlib}/Crypt/
%{_mandir}/man1/largeprimes.1*
%{_mandir}/man3/Crypt::Primes.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-40
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-37
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-34
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Paul Howarth <paul@city-fan.org> - 0.50-31
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  8 2016 Paul Howarth <paul@city-fan.org> - 0.50-29
- Bump stack size for t/genprime_elgamal.t too

* Wed Aug  3 2016 Paul Howarth <paul@city-fan.org> - 0.50-28
- Allocate more stack for t/genprime.t to avoid intermittent build failures
- Simplify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-27
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Paul Howarth <paul@city-fan.org> - 0.50-25
- Classify buildreqs by usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-23
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.50-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.50-16
- Perl 5.16 rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.50-15
- Perl 5.16 rebuild

* Mon Apr  9 2012 Paul Howarth <paul@city-fan.org> 0.50-14
- Own directory %%{perl_vendorlib}/Crypt/
- BR: perl(Exporter)
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 0.50-13
- Nobody else likes macros for commands

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.50-12
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.50-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.50-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.50-8
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.50-5
- Rebuild for new perl

* Sun Aug 12 2007 Paul Howarth <paul@city-fan.org> 0.50-4
- Clarify license as GPL v1 or later, or Artistic (same as perl)

* Thu Mar  8 2007 Paul Howarth <paul@city-fan.org> 0.50-3
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.50-2
- FE6 mass rebuild

* Tue Dec  6 2005 Paul Howarth <paul@city-fan.org> 0.50-1
- Initial build
