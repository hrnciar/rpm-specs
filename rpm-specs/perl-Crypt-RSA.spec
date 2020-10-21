Summary:	RSA public-key cryptosystem
Name:		perl-Crypt-RSA
Version:	1.99
Release:	32%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Crypt-RSA
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Crypt-RSA-%{version}.tar.gz
Patch0:		Crypt-RSA-1.99-utf8.patch
Patch1:		Crypt-RSA-1.99-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(Benchmark)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Loader)		>= 2.00
BuildRequires:	perl(constant)
BuildRequires:	perl(Convert::ASCII::Armour)
BuildRequires:	perl(Crypt::Random)		>= 0.34
BuildRequires:	perl(Crypt::Primes)		>= 0.38
BuildRequires:	perl(Crypt::CBC)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Buffer)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Digest::MD2)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::MM_Unix)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Math::Pari)		>= 2.001804
BuildRequires:	perl(lib)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Sort::Versions)
BuildRequires:	perl(strict)
BuildRequires:	perl(Tie::EncryptedHash)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Class::Loader)		>= 2.00

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the RSA public-key
cryptosystem. It uses Math::Pari(3), a perl interface to the blazingly fast
PARI library, for big integer arithmetic and number theoretic computations.

Crypt::RSA provides arbitrary size key-pair generation, plaintext-aware
encryption (OAEP) and digital signatures with appendix (PSS). For compatibility
with SSLv3, RSAREF2, PGP and other applications that follow the PKCS #1 v1.5
standard, it also provides PKCS #1 v1.5 encryption and signatures.

%prep
%setup -q -n Crypt-RSA-%{version}

# Convert documentation to UTF-8
%patch0 -p1

# Fix building on Perls without '.' in @INC
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

# Additional manpages
pod2man --section=3 extradocs/crypt-rsa-interoperablity.pod \
	%{buildroot}%{_mandir}/man3/crypt-rsa-interoperablity.3
pod2man --section=3 extradocs/crypt-rsa-interoperablity-template.pod \
	%{buildroot}%{_mandir}/man3/crypt-rsa-interoperablity-template.3

%check
make test

%files
%if 0%{?_licensedir:1}
%license ARTISTIC COPYING
%else
%doc ARTISTIC COPYING
%endif
%doc Changes README TODO
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::RSA.3*
%{_mandir}/man3/Crypt::RSA::DataFormat.3*
%{_mandir}/man3/Crypt::RSA::Debug.3*
%{_mandir}/man3/Crypt::RSA::ES::OAEP.3*
%{_mandir}/man3/Crypt::RSA::ES::PKCS1v15.3*
%{_mandir}/man3/Crypt::RSA::Errorhandler.3*
%{_mandir}/man3/Crypt::RSA::Key.3*
%{_mandir}/man3/Crypt::RSA::Key::Private.3*
%{_mandir}/man3/Crypt::RSA::Key::Private::SSH.3*
%{_mandir}/man3/Crypt::RSA::Key::Public.3*
%{_mandir}/man3/Crypt::RSA::Key::Public::SSH.3*
%{_mandir}/man3/Crypt::RSA::Primitives.3*
%{_mandir}/man3/Crypt::RSA::SS::PKCS1v15.3*
%{_mandir}/man3/Crypt::RSA::SS::PSS.3*
%{_mandir}/man3/crypt-rsa-interoperablity.3*
%{_mandir}/man3/crypt-rsa-interoperablity-template.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-31
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-28
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-25
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Paul Howarth <paul@city-fan.org> - 1.99-22
- Use %%license where possible
- Simplify find command using -delete
- No need to remove empty directories from the buildroot
- Drop EOL EPEL distribution support
  - Drop %%defattr, redundant since rpm 4.4
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-21
- Fix building on Perl without '.' in @INC
- Specify all dependencies

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-19
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-16
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.99-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.99-9
- Perl 5.16 rebuild

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 1.99-8
- Nobody else likes macros for commands
- Use a patch rather than scripted iconv to fix character encodings
- Use %%{_fixperms} macro rather than our own chmod incantation
- BR: perl(Carp)

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.99-7
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> 1.99-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> 1.99-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> 1.99-3
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  8 2009 Paul Howarth <paul@city-fan.org> 1.99-1
- Update to 1.99
  - Fix CPAN RT#37489 (precedence error in C::R::Key::{Private,Public}::write)
  - Fix CPAN RT#37862 (Crypt::RSA doesn't work under setuid Perl)
  - Fix CPAN RT#46577 (invalid signature calling verify())

* Wed May 13 2009 Paul Howarth <paul@city-fan.org> 1.98-3
- Recode Crypt::RSA manpage as UTF-8

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul  8 2008 Paul Howarth <paul@city-fan.org> 1.98-1
- Update to 1.98

* Mon Jul  7 2008 Paul Howarth <paul@city-fan.org> 1.97-1
- Update to 1.97

* Mon Jul  7 2008 Paul Howarth <paul@city-fan.org> 1.96-1
- Update to 1.96
- Convert "Changes" to UTF-8
- Shellbangs no longer need removing
- Module is now UTF-8 and doesn't need converting
- Need manual perl(Class::Loader) dep due to move to use of "use base",
  as rpm auto-dep-finder doesn't spot it

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.58-4
- Rebuild for new perl

* Sun Aug 12 2007 Paul Howarth <paul@city-fan.org> 1.58-3
- Clarify license as GPL v1 or later, or Artistic (same as perl)

* Tue Apr 17 2007 Paul Howarth <paul@city-fan.org> 1.58-2
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Fri Dec 22 2006 Paul Howarth <paul@city-fan.org> 1.58-1
- Update to 1.58
- GPL license text now included upstream (CPAN RT#18771)

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 1.57-3
- FE6 mass rebuild

* Tue Apr 18 2006 Paul Howarth <paul@city-fan.org> 1.57-2
- Fix non-UTF8-encoded manpage (#183888)
- Add manpages for crypt-rsa-interoperablity(3) and
  crypt-rsa-interoperablity-template(3) (#183888)

* Mon Nov 28 2005 Paul Howarth <paul@city-fan.org> 1.57-1
- Initial build
