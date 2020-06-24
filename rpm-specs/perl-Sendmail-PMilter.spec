Summary:	Perl binding of Sendmail Milter protocol
Name:		perl-Sendmail-PMilter
Version:	1.00
Release:	28%{?dist}
License:	BSD
URL:		https://metacpan.org/release/Sendmail-PMilter
Source0:	https://cpan.metacpan.org/authors/id/A/AV/AVAR/Sendmail-PMilter-%{version}.tar.gz
Patch0:		Sendmail-PMilter-Context.pm_pod.patch
Patch1:		Sendmail-PMilter-0.97-setdbg-settimeout.patch
Patch2:		Sendmail-PMilter-0.97-data-command.patch
Patch3:		Sendmail-PMilter-1.00-macro-head.patch
Patch4:		Sendmail-PMilter-1.00-sigchld.patch
Patch5:		Sendmail-PMilter-1.00-protocol.patch
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
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(IO::Socket::UNIX)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
BuildRequires:	perl(Socket6)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Thread::Semaphore)
BuildRequires:	perl(threads)
BuildRequires:	perl(threads::shared)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(UNIVERSAL)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(IO::Socket::INET)
Requires:	perl(IO::Socket::INET6)
Requires:	perl(IO::Socket::UNIX)
Requires:	perl(Socket6)
Requires:	perl(Thread::Semaphore)
Requires:	perl(threads)
Requires:	perl(threads::shared)
Obsoletes:	perl-Sendmail-Milter <= 0.18

%description
Sendmail::PMilter is a mail filtering API implementing the Sendmail milter
protocol in pure Perl. This allows Sendmail servers (and perhaps other MTAs
implementing milter) to filter and modify mail in transit during the SMTP
connection, all in Perl.

It should be noted that PMilter 0.90 and later is NOT compatible with
scripts written for PMilter 0.5 and earlier.  The API has been reworked
significantly, and the enhanced APIs and rule logic provided by PMilter
0.5 and earlier has been factored out for inclusion in a separate package
called Mail::Milter.

%prep
%setup -q -n Sendmail-PMilter-%{version}

# Fix up POD errors in Sendmail::PMilter::Context
%patch0 -p1

# Pretend to have succeeeded in Sendmail::Milter::{setdb,settimeout}
# (these are no-op functions in the Sendmail::Milter implementation)
# CPAN RT#50144
%patch1 -p1

# Handle SMFIC_DATA (CPAN RT#51058)
%patch2 -p1

# Fix addheader, getsymval bugs (CPAN RT#84941, #957886)
%patch3 -p1

# Reset SIGCHLD handler in milters (CPAN RT#85826, #970138)
%patch4

# Block instead of erroring on max children (CPAN RT#85833, #970197)
%patch5

# Fix interpreters in examples and turn off exec bits to avoid extra deps
sed -i -e 's@/usr/local/bin/perl@/usr/bin/perl@' examples/*.pl
chmod -x examples/*.pl

%build
# Using "echo" to bypass the interactive 'yes/no' question in Makefile.PL
echo yes | perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README doc/milter-protocol.txt examples/
%{perl_vendorlib}/Sendmail/
%{_mandir}/man3/Sendmail::Milter.3*
%{_mandir}/man3/Sendmail::PMilter.3*
%{_mandir}/man3/Sendmail::PMilter::Context.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-28
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-25
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-22
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 1.00-17
- Classify buildreqs by usage
- Simplify find command using -delete
- Drop %%defattr, redundant since rpm 4.4

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-13
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.00-9
- Perl 5.18 rebuild

* Thu Jun 13 2013 Paul Howarth <paul@city-fan.org> - 1.00-8
- Reset SIGCHLD handler in milters (CPAN RT#85826, #970138)
- Block instead of erroring on max children (CPAN RT#85833, #970197)
- BR: perl(Thread::Semaphore) and perl(Time::HiRes)
- BR:/R: all optional modules for different socket/dispatcher styles

* Tue Apr 30 2013 Paul Howarth <paul@city-fan.org> - 1.00-7
- Fix addheader, getsymval bugs (CPAN RT#84941, #957886)
- Don't need to remove empty directories from the buildroot
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.00-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.00-2
- Perl mass rebuild

* Mon Apr 18 2011 Paul Howarth <paul@city-fan.org> 1.00-1
- Update to 1.00
  - Avoid infinite loop: signal handler modifies errno
  - Added support for SMFIC_UNKNOWN
- Nobody else likes macros for commands

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Paul Howarth <paul@city-fan.org> 0.99-1
- Update to 0.99
  - Handle IPv6 addresses in SMFIC_CONNECT in Sendmail::PMilter::Context
    (CPAN RT#65499)

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.98-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.98-2
- Mass rebuild with perl-5.12.0

* Sat Mar 13 2010 Paul Howarth <paul@city-fan.org> 0.98-1
- Update to 0.98 (fixes for CPAN RT#51713 and CPAN RT#51759)
- Drop upstreamed POD patch (CPAN RT#51713)

* Mon Feb  8 2010 Paul Howarth <paul@city-fan.org> 0.97-4
- Cosmetic spec changes for new maintainer
- Obsolete perl-Sendmail-Milter <= 0.18 since we provide a compatibility
  wrapper for it; we don't add a provide for this since we would be
  self-obsoleting if we did so
- Add patch to make the no-op functions Sendmail::Milter::{setdb,settimeout}
  return "success" values to avoid messages like "Failed to set timeout value!"
  (CPAN RT#50144)
- Add patch to handle SMFIC_DATA (CPAN RT#51058)
- Add patch for more POD fixes (CPAN RT#51713)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 0.97-3
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 John Guthrie <guthrie@counterexample.org> 0.97-1
- Re-released with version 0.97
- Added BuildRequirement for perl(Test::More)

* Sun Feb 15 2009 John Guthrie <guthrie@counterexample.org> 0.96-5
- Added small patch to fix an error in the POD documentation for Context.pm

* Fri Feb 06 2009 John Guthrie <guthrie@counterexample.org> 0.96-4
- Fixed rpmlint warnings caused by including the examples directory in the %%doc
  section

* Fri Feb 06 2009 John Guthrie <guthrie@counterexample.org> 0.96-3
- Added files to %%doc list
- Corrected license

* Thu Feb 05 2009 John Guthrie <guthrie@counterexample.org> 0.96-2
- Expanded %%description section
- Ran "perl Makefile.PL" as the receiving end of a pipe since there is an
  interactive part to that script

* Thu Feb 05 2009 John Guthrie <guthrie@counterexample.org> 0.96-1
- Specfile autogenerated by cpanspec 1.77
