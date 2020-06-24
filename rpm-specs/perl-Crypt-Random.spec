Summary:	Cryptographically Secure, True Random Number Generator
Name:		perl-Crypt-Random
Version:	1.52
Release:	6%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Crypt-Random
Source0:	https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Random-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Loader)	>= 2.00
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(lib)
BuildRequires:	perl(Math::Pari)	>= 2.001804
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Crypt::Random is an interface module to the /dev/random device found on most
modern unix systems. It also interfaces with egd, a user space entropy
gathering daemon, available for systems where /dev/random (or similar) devices
are not available. When Math::Pari is installed, Crypt::Random can generate
random integers of arbitrary size of a given bitsize or in a specified
interval.

%prep
%setup -q -n Crypt-Random-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{_bindir}/makerandom
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::Random.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Paul Howarth <paul@city-fan.org> - 1.52-1
- Update to 1.52
  - Test no longer looks for non-eq of two generated numbers as these can be
    correctly the same if test is run enough number of times (CPAN RT#99880)
  - Removed outdated dependency info (CPAN RT#94441)
  - Removed /dev/random read from the test, as it can hang when there is
    insufficient entropy (CPAN RT#30423)
  - Removed potentially unsafe include in bin/makerandom (CPAN RT#128062)
  - Add a chi square statistical test, t/chisquare.t
  - Uniform can be passed to the constructor of Crypt::Random::Generator;
    this should be the default, and will likely be in the next release
  - Fixed minor bugs and typos
- Drop legacy Group: tag
- Drop buildroot cleaning in %%install, now redundant
- Simplify find command using -delete

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-31
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Orion Poplawski <orion@cora.nwra.com> - 1.25-28
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-26
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Paul Howarth <paul@city-fan.org> - 1.25-24
- Fix broken previous fix for CPAN RT#99880, RHBZ#1158379

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-22
- Perl 5.22 rebuild

* Wed Oct 29 2014 Paul Howarth <paul@city-fan.org> - 1.25-21
- Prevent test that should fail 0.1%% of the time from causing FTBFS
  (CPAN RT#99880, #1158379)
- Classify buildreqs by usage
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.25-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.25-14
- Perl 5.16 rebuild

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 1.25-13
- Nobody else likes macros for commands
- BR: perl(Carp)

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.25-12
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> 1.25-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> 1.25-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> 1.25-8
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.25-5
- Rebuild for new perl

* Sun Aug 12 2007 Paul Howarth <paul@city-fan.org> 1.25-4
- Clarify license as GPL v1 or later, or Artistic (same as perl)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 1.25-3
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 1.25-2
- FE6 mass rebuild

* Mon Dec  5 2005 Paul Howarth <paul@city-fan.org> 1.25-1
- Initial build
