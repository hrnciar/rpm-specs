Summary:	Hashes (and objects based on hashes) with encrypting fields
Name:		perl-Tie-EncryptedHash
Version:	1.24
Release:	32%{?dist}
License:	GPL+ or Artistic
Url:		https://metacpan.org/release/Tie-EncryptedHash
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Tie-EncryptedHash-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:	perl(Carp)
BuildRequires:	perl(Crypt::CBC)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Digest::MD5)
# Tests
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(lib)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Tie::EncryptedHash augments Perl hash semantics to build secure, encrypting
containers of data. Tie::EncryptedHash introduces special hash fields that are
coupled with encrypt/decrypt routines to encrypt assignments at STORE() and
decrypt retrievals at FETCH(). By design, encrypting fields are associated with
keys that begin in single underscore. The remaining keyspace is used for
accessing normal hash fields, which are retained without modification.

While the password is set, a Tie::EncryptedHash behaves exactly like a standard
Perl hash. This is its transparent mode of access. Encrypting and normal fields
are identical in this mode. When password is deleted, encrypting fields are
accessible only as ciphertext. This is Tie::EncryptedHash's opaque mode of
access, optimized for serialization.

Encryption is done with Crypt::CBC(3), which encrypts in the cipher block
chaining mode with Blowfish, DES or IDEA. Tie::EncryptedHash uses Blowfish by
default, but can be instructed to employ any cipher supported by Crypt::CBC(3).

%prep
%setup -q -n Tie-EncryptedHash-%{version}
sed -i -e '/^#! *\/usr\/bin\/perl /d' lib/Tie/EncryptedHash.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%files
%doc Changes LICENSE README.html TODO
%{perl_vendorlib}/Tie/
%{_mandir}/man3/Tie::EncryptedHash.3pm*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-31
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-28
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-25
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-22
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.24-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Paul Howarth <paul@city-fan.org> - 1.24-10
- Don't use macros for system commands
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Drop %%defattr, redundant since rpm 4.4

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.24-9
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.24-7
- Perl mass rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-6
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.24-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Paul Howarth <paul@city-fan.org> 1.24-1
- Update to 1.24 (upstream has clarified the license - see
  http://rt.cpan.org/Ticket/Display.html?id=28813)
- Include LICENSE file as %%doc

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.23-1
- update to 1.23
- license changed to GPL+ or Artistic

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.21-4
- rebuild for new perl

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 1.21-3
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 1.21-2
- FE6 mass rebuild

* Tue Dec  6 2005 Paul Howarth <paul@city-fan.org> 1.21-1
- Initial build
