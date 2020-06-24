# We have an older version of CryptX with ECC support stripped out
# so that we can unbundle libtomcrypt; as such, we need to remove the
# parts of Net-SSH-Perl that use this functionality
# https://bugzilla.redhat.com/show_bug.cgi?id=1545816
%global hobbled_cryptx 1

Summary:	SSH (Secure Shell) client
Name:		perl-Net-SSH-Perl
Version:	2.14
Release:	9%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Net-SSH-Perl
Source0:	https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/Net-SSH-Perl-%{version}.tar.gz
Patch0:		Net-SSH-Perl-2.14-hobbled.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
#BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(constant)
BuildRequires:	perl(Crypt::Cipher::AES)
BuildRequires:	perl(Crypt::Cipher::Blowfish)
BuildRequires:	perl(Crypt::Cipher::DES)
%if ! %{hobbled_cryptx}
BuildRequires:	perl(Crypt::Curve25519)		>= 0.05
%endif
BuildRequires:	perl(Crypt::Digest::MD5)
BuildRequires:	perl(Crypt::Digest::SHA1)
BuildRequires:	perl(Crypt::Digest::SHA256)
BuildRequires:	perl(Crypt::Digest::SHA512)
BuildRequires:	perl(Crypt::DSA::Key)
BuildRequires:	perl(Crypt::IDEA)
BuildRequires:	perl(Crypt::Mac::HMAC)
BuildRequires:	perl(Crypt::Misc)
BuildRequires:	perl(Crypt::PK::DH)
BuildRequires:	perl(Crypt::PK::DSA)
%if ! %{hobbled_cryptx}
BuildRequires:	perl(Crypt::PK::ECC)
%endif
BuildRequires:	perl(Crypt::PK::RSA)
BuildRequires:	perl(Crypt::PRNG)
BuildRequires:	perl(CryptX)			>= 0.032
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(if)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::Socket::Socks)
BuildRequires:	perl(Math::GMP)			>= 1.04
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(String::CRC32)		>= 1.2
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Tie::Handle)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Optional Functionality
BuildRequires:	perl(Digest::BubbleBabble)
# Test Suite
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)		>= 0.61
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if 0%{?fedora:1}
Suggests:	perl(Crypt::RSA)
Suggests:	perl(Crypt::RSA::DataFormat)
%endif
Requires:	perl(Digest::BubbleBabble)
Requires:	perl(File::Basename)
Requires:	perl(File::Path)
Requires:	perl(Term::ReadKey)

%description
Net::SSH::Perl is a mostly-Perl module implementing an SSH (Secure Shell)
client. It is compatible with both the SSH-1 and SSH-2 protocols.

%prep
%setup -q -n Net-SSH-Perl-%{version}

# If we have a hobbled CryptX without ECC support, we have to remove some functionality
%if %{hobbled_cryptx}
rm lib/Net/SSH/Perl/Kex/C25519.pm
rm lib/Net/SSH/Perl/Key/ECDSA.pm
rm lib/Net/SSH/Perl/Key/ECDSA256.pm
rm lib/Net/SSH/Perl/Key/ECDSA384.pm
rm lib/Net/SSH/Perl/Key/ECDSA521.pm
%patch0
%endif

%build
# Protocol support (select one)
# 1=SSH1 2=SSH2 3=Both
echo 3 | perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README eg ToDo
%{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/Net/
%{_mandir}/man3/Net::SSH::Perl*.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 2.14-2
- Rebuild with new redhat-rpm-config/perl build flags

* Thu Feb 15 2018 Paul Howarth <paul@city-fan.org> - 2.14-1
- Update to 2.14
  - This is a significant refactoring of the code to use CryptX for most of the
    low-level cryptographic functionality, replacing a raft of old,
    un-maintained dependencies
  - A lot of additional functionality matching OpenSSH has been added, but much
    of the elliptical curve cipher support has been removed in packaging
    because the perl-CryptX package in Fedora does not support it
  - The module is no longer pure-Perl, with XS code added for Chacha20, BSD
    Blowfish, and Ed25519 routines
- Remove parts that require ECC support from perl-CryptX, which is currently
  hobbled in Fedora
- Package is now arch-specific
- Drop author tests, some of which don't work and others require excessive
  spec file work-arounds to run cleanly
- Simplify find command using -delete

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Paul Howarth <paul@city-fan.org> - 1.42-9
- Perl 5.26 rebuild

* Thu Apr  6 2017 Paul Howarth <paul@city-fan.org> - 1.42-8
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section
  - BR: perl(Test::YAML::Meta) unconditionally
- Use gnupg2 rather than gnupg, and explicitly build-require it

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Paul Howarth <paul@city-fan.org> - 1.42-6
- Enable IDEA support unconditionally (patent expired a few years ago)

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 1.42-5
- Adjust RPM version detection to SRPM build root without perl

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Paul Howarth <paul@city-fan.org> - 1.42-2
- Prefer %%global over %%define

* Mon Sep 28 2015 Paul Howarth <paul@city-fan.org> - 1.42-1
- Update to 1.42
  - Fix issue with long selects getting interrupted by signals and dying
  - Fix version CPAN meta info

* Fri Sep 18 2015 Paul Howarth <paul@city-fan.org> - 1.41-1
- Update to 1.41
  - Declare new dependency to File::HomeDir in Makefile.PL
  - Use Errno constants in a more portable way

* Wed Sep 16 2015 Paul Howarth <paul@city-fan.org> - 1.39-1
- Update to 1.39
  - Fix shell terminal width and height (CPAN RT#83978)
  - Fix algorithm negotiation issue in ::Kex.pm (CPAN RT#94574)
  - Fix VERSION methods (CPAN RT#105728)
  - Code modernization (strict+warnings)
  - Pass tests on Win32
  - Use Win32::LoginName on Windows
  - Use File::HomeDir to simplify handling
- This release by SCHWIGON → update source URL
- Classify buildreqs by usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-2
- Perl 5.22 rebuild

* Thu Oct  9 2014 Paul Howarth <paul@city-fan.org> - 1.38-1
- Update to 1.38
  - Install valid SIGNATURE file (CPAN RT#99284)
- Re-enable the signature test
- This release by TURNSTEP → update source URL
- Use %%license where possible

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Paul Howarth <paul@city-fan.org> - 1.37-1
- Update to 1.37
  - Enabled config option "StrictHostKeyChecking"; the corresponding code
    already existed (CPAN RT#91840)
- Don't test signature because upstream forgot to re-generate it

* Sat Aug 10 2013 Paul Howarth <paul@city-fan.org> - 1.36-1
- Update to 1.36
  - CPAN RT#48338 - Fix race condition with SSHv2
  - CPAN RT#55195 - Fix race condition in KEXINIT
  - CPAN RT#67586 - Fix test '03-packet.t' hangs forever
  - CPAN RT#64517 - Enable PTY support in SSH2
  - CPAN RT#23947 - Replacement for KeyboardInt.pm
- Drop %%defattr, redundant since rpm 4.4
- Disable spell check test, which simplifies the spec considerably

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.35-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec  3 2012 Paul Howarth <paul@city-fan.org> 1.35-1
- Update to 1.35
  - Apply patch to t/03-packet.t for 5.15+ (CPAN RT#76482)
- This release by SCHWIGON -> update source URL
- Drop upstreamed patch for CPAN RT#76482

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Paul Howarth <paul@city-fan.org> 1.34-16
- Fix breakage with Perl 5.16 (CPAN RT#76482)
- Drop buildreqs for modules that are not dual-lived
- Don't need to remove empty directories from the buildroot

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 1.34-15
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> 1.34-14
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Add buildreqs not mentioned in module metadata

* Wed Jul 20 2011 Paul Howarth <paul@city-fan.org> 1.34-13
- Perl mass rebuild
- Work around MYMETA.yml causing signature test to fail
- Use LANG rather than LC_ALL to set locale for spell check test

* Thu Jun 23 2011 Paul Howarth <paul@city-fan.org> 1.34-12
- Nobody else likes macros for commands
- Update fix for spell check test again

* Sat Feb 12 2011 Paul Howarth <paul@city-fan.org> 1.34-11
- Fix dependency filtering for Crypt::IDEA in rpm 4.9

* Wed Feb  9 2011 Paul Howarth <paul@city-fan.org> 1.34-10
- Update fix for spell check test as dictionary coverage in Rawhide appears
  to have gone down

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct  4 2010 Paul Howarth <paul@city-fan.org> 1.34-8
- BR: hunspell-en rather than aspell-en now that Text::SpellChecker uses a
  hunspell back-end
- Fix spell check test to add words not in hunspell dictionary

* Thu May 13 2010 Paul Howarth <paul@city-fan.org> 1.34-7
- Don't clobber ~/.gnupg during build

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.34-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.34-5
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Paul Howarth <paul@city-fan.org> 1.34-2
- Add buildreq aspell-en for spell check test

* Mon Feb  2 2009 Paul Howarth <paul@city-fan.org> 1.34-1
- Update to 1.34, fixes various upstream bugs:
  * Rekey properly after 1 GB of data (rt.cpan.org #25044)
  * Don't try to process nonexistent or empty auth file (rt.cpan.org #41877)
  * Fix typo in croak message (rt.cpan.org #42056)
  * Move 'use base' call after Crypt module loading (rt.cpan.org #42051)
  * Only apply stdin if defined in SSH1 (rt.cpan.org #42583)

* Tue Nov  4 2008 Paul Howarth <paul@city-fan.org> 1.33-2
- Run tests in en_US locale, so spell checker doesn't complain about the use of
  American English when the host is in a non-US locale

* Mon Nov  3 2008 Paul Howarth <paul@city-fan.org> 1.33-1
- Update to 1.33 (#469612), fixes various upstream bugs:
  * Fix open() calls (rt.cpan.org #40020)
  * Fix non-shell problem (rt.cpan.org #39980)
  * Allow full agent forwarding (rt.cpan.org #32190)
  * Handle hashed known_hosts files (rt.cpan.org #25175)
  * Add IO::Handle to Perl.pm (rt.cpan.org #40057, #35985)
  * Prevent t/03-packet.t from hanging due to high file descriptor
  | (rt.cpan.org #6101)
  * If ENV{HOME} is not set, use getpwuid. If both fail and the dir 
  | is needed, we croak (rt.cpan.org #25174)
  * Fix incorrect logical/bitwise AND mixup (rt.cpan.org #31490)
  * Allow empty stdin for SSH2 (rt.cpan.org #32730)
  * Adjust terminal dimensions dynamically if Term::ReadKey is available
  | (rt.cpan.org #34874)
- New upstream (co-)maintainer, new source URL
- t/03-packet.t re-enabled as it should no longer hang
- Add buildreqs Module::Signature, Test::Pod, Test::Pod::Coverage,
  Perl::Critic, Test::YAML::Meta, Text::SpellChecker for additional test
  coverage
- Add dependency on Term::ReadKey to provide dynamic terminal resizing
- Include upstream maintainer's GPG key for signature checking

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.30-6
- Rebuild for new perl

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 1.30-5
- Clarify license as GPL v1 or later, or Artistic (same as perl)
- Add buildreq perl(Test::More)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 1.30-4
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 1.30-3
- Skip test 03-packet, which can sometimes hang (cpan rt#6101)
- Add manual Crypt::Blowfish dep to ensure we have blowfish support

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 1.30-2
- FE6 mass rebuild

* Mon Mar 20 2006 Paul Howarth <paul@city-fan.org> 1.30-1
- Update to 1.30
- Patch for cpan rt#11674 no longer needed, fixed upstream

* Thu Mar  2 2006 Paul Howarth <paul@city-fan.org> 1.29-1
- Initial build
