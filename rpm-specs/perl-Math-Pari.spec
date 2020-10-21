%global extraversion	%{nil}
%global extrasuffix	%{nil}

Summary:	Perl interface to PARI
Name:		perl-Math-Pari
Version:	2.030518
Release:	6%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Math-Pari
Source0:	https://cpan.metacpan.org/modules/by-module/Math/Math-Pari-%{version}%{extraversion}%{?extrasuffix}.zip
Patch0:		Math-Pari-2.030518-system-pari.patch
Patch1:		Math-Pari-2.030506-docs-and-testsuite.patch
Patch3:		Math-Pari-2.030512-utf8.patch
Patch4:		Math-Pari-2.030506-escape-left-braces-in-regex.patch
Patch5:		Math-Pari-2.030518-MP_NOGNUPLOT.patch
Patch6:		Math-Pari-2.030509-optflags.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	libpari23-devel
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::Constant)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(strict)
BuildRequires:	pkgconfig
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(subs)
# Test Suite
# (no additional dependencies)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Enforce dependency against same version of pari that we're built for
Requires:	libpari23%{?_isa} = %(pkg-config --modversion libpari23 2>/dev/null || echo 0)

# Don't "provide" private Perl libs or the redundant unversioned perl(Math::Pari)
%global __provides_exclude ^(perl\\(Math::Pari\\)$|Pari\\.so)

%description
This package is a Perl interface to the famous library PARI for numerical/
scientific/ number-theoretic calculations. It allows use of most PARI functions
as Perl functions, and (almost) seamless merging of PARI and Perl data.

%prep
%setup -q -n Math-Pari-%{version}%{extraversion}

# Create a directory structure for libpari23 like Math::Pari expects it to be
mkdir libpari23
ln -s $(pkg-config --cflags-only-I libpari23 | sed -e 's/-I//') libpari23/include
ln -s $(pkg-config --variable=paridir libpari23)/src libpari23/src

# Fix for using system pari library (with source available)
%patch0

# We want to build the docs and test suite too
%patch1

# Recode Changes file as UTF-8
%patch3

# Escape left braces in regexes (#1452519)
%patch4

# Fix operation of MP_NOGNUPLOT
%patch5

# Don't try to fiddle with compiler flags, we'll set them ourselves anyway
%patch6

%build
paridir=$(pkg-config --variable=paridir libpari23)
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="$(pkg-config --cflags-only-I libpari23) %{optflags}" \
	paridir="${paridir}" \
	pariincludes=$(pwd)/libpari23 \
	parilibs="$(pkg-config --libs libpari23)"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test MP_NOGNUPLOT=1

%files
%doc Changes README
%dir %{perl_vendorarch}/Math/
%exclude %doc %{perl_vendorarch}/Math/libPARI.dumb.pod
%doc %{perl_vendorarch}/Math/libPARI.pod
%{perl_vendorarch}/Math/*.pm
%{perl_vendorarch}/auto/Math/
%{_mandir}/man3/Math::Pari.3*
%{_mandir}/man3/Math::PariInit.3*
%{_mandir}/man3/Math::libPARI.3*
%exclude %{_mandir}/man3/Math::libPARI.dumb.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.030518-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.030518-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.030518-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.030518-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.030518-2
- Perl 5.30 rebuild

* Mon Apr 22 2019 Paul Howarth <paul@city-fan.org> - 2.030518-1
- Update to 2.030518 (see Changes for details)
- Modernize spec using %%{make_build} and %%{make_install}

* Sat Apr  6 2019 Paul Howarth <paul@city-fan.org> - 2.030517-1
- Update to 2.030517 (see Changes for details)

* Thu Apr  4 2019 Paul Howarth <paul@city-fan.org> - 2.030516-1
- Update to 2.030516 (see Changes for details)

* Thu Mar 28 2019 Paul Howarth <paul@city-fan.org> - 2.030515-1
- Update to 2.030515 (see Changes for details)

* Tue Mar 26 2019 Paul Howarth <paul@city-fan.org> - 2.030514-1
- Update to 2.030514 (see Changes for details)

* Mon Mar 25 2019 Paul Howarth <paul@city-fan.org> - 2.030513-1
- Update to 2.030513 (see Changes for details)

* Sun Mar 24 2019 Paul Howarth <paul@city-fan.org> - 2.030512-1
- Update to 2.030512 (see Changes for details)

* Tue Mar 19 2019 Paul Howarth <paul@city-fan.org> - 2.030510-1
- Update to 2.030510 (see Changes for details)

* Sat Mar  2 2019 Paul Howarth <paul@city-fan.org> - 2.030509-1
- Update to 2.030509 (see Changes for details)

* Mon Feb 25 2019 Paul Howarth <paul@city-fan.org> - 2.030508-1
- Update to 2.030508 (see Changes for details)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.030507-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Paul Howarth <paul@city-fan.org> - 2.030507-1
- Update to 2.030507 (see Changes for details)

* Wed Aug 15 2018 Paul Howarth <paul@city-fan.org> - 2.030506-1
- Update to 2.030506 (see Changes for details)
- Rework patches and build process to get it to build again

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.010809-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.010809-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.010809-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.010809-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.010809-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.010809-5
- Perl 5.26 rebuild

* Fri May 19 2017 Paul Howarth <paul@city-fan.org> - 2.010809-4
- Escape left braces in regexes (#1452519)
- Fix operation of MP_NOGNUPLOT and use it
- Drop redundant Group: tag

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.010809-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.010809-2
- Perl 5.24 rebuild

* Sat May  7 2016 Paul Howarth <paul@city-fan.org> - 2.010809-1
- Update to 2.010809b
  - MakeMaker of 5.22 (and, maybe, 5.20) started to call test_dynamic target
    in the daughter Makefile
  - Correct "{" in RExes of libPARI/gphelp
  - Attempt to workaround a broken config of gcc on vendor's Perl on Solaris
- This release is a tarball rather than a zipfile
- Update no-fake-version patch

* Tue Apr 19 2016 Paul Howarth <paul@city-fan.org> - 2.010808-7
- Classify buildreqs by usage
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.010808-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010808-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.010808-4
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.010808-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Paul Howarth <paul@city-fan.org> - 2.010808-1
- Update to 2.010808
  - Fixed problems of parse_of_gp with the operator \ and empty lines (test
    suite updated)
  - Various build system fixes
- Upstream did this release as a zip file
- Update no-fake-version patch
- Add patch to recode Changes file as UTF-8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010807-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Paul Howarth <paul@city-fan.org> - 2.010807-1
- Update to 2.010807
  - Too long version name was a misprint
  - Pay attention to PERL_EXTUTILS_AUTOINSTALL when interpreting empty answers
    to prompt (probably an overkill)
  - Report bytes in the answer for prompt
  - Split into separate subroutines inspecting versions available for download
    from the actual download
  - Change the logic of fallback Net::FTP -> LWP
  - __wrap_PARI_macro: new function (not exported)
  - parse_as_gp: new function (exported by default)
  - More verbose error message for "Cannot load a Pari macro"
- Specify all dependencies

* Sat Apr 26 2014 Paul Howarth <paul@city-fan.org> - 2.010806-23
- Update to 2.01080607
  - Correct the documention about fraction of witnesses from ≳ 0.25 to ≳ 0.75
  - Define HAS_STAT and HAS_OPENDIR based on $Config{i_sysstat} and
    $Config{i_dirent}
  - Correct spelling errors in POD and comments in Pari.pm
  - On AIX, do merge_822 separately in subdirectories (exceeds command line
    length otherwise)
  - On pari ≳ 2.3.0, reset had-newline-on-output to 1 at startup (saves one
    spurious NL)
  - New patch: diff_2.3.5_stderr_clobber
  - New test: 01_no_extra_newlines.t
  - Allow download not only via FTP, but also through HTTP
  - In presence of PERL5_CPAN_IS_RUNNING, assume that NO ANSWER on prompt is
    agreement (it looks like cygwin and MSWin32 automated-testing environment
    do not have AUTOMATED_TESTING and PERL_MM_USE_DEFAULT set...)
  - Do not auto-download on 64-bit builds of MSWin32

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 2.010806-22
- Update to 2.01080606a (re-release with sane permissions)

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 2.010806-21
- Update to 2.01080606 (fixes for downloading pari and Windows builds)
- Fix dubious permissions from upstream's tarball

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010806-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.010806-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010806-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010806-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 2.010806-16
- Perl 5.16 rebuild

* Tue Jul  3 2012 Paul Howarth <paul@city-fan.org> - 2.010806-15
- BR: perl(Cwd) and perl(ExtUtils::Constant)

* Wed Jun 13 2012 Paul Howarth <paul@city-fan.org> - 2.010806-14
- Migrate to build against libpari23, since the new pari 2.5.x is not yet
  supported upstream (CPAN RT#69295, CPAN RT#70990)
- BR: perl(Carp)
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.010806-13
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 2.010806-12
- Update pari source URL to reflect that we're using an OLD version
- Add buildreqs for perl core modules, which might be dual-lived
- Rewrite provides filter for rpm-4.9 compatibility
- Rename patches to strip 'perl-' prefix

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.010806-11
- Perl mass rebuild

* Sat Apr 30 2011 Paul Howarth <paul@city-fan.org> - 2.010806-10
- Update to 2.01080605 (see Changes for details)
- Remove buildroot definition and cleaning, redundant with modern rpmbuild
- Nobody else likes macros for commands
- PERL_INSTALL_ROOT => DESTDIR
- Use %%{_fixperms} macro instead of our own chmod incantation

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010806-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.010806-8
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Jul  9 2010 Paul Howarth <paul@city-fan.org> - 2.010806-7
- Rebuild with pari 2.3.5
- Tweak application of intnum test patch to apply with different pari versions

* Tue Jun 22 2010 Paul Howarth <paul@city-fan.org> - 2.010806-6
- Make stack size bigger for intnum test to avoid test failures on some
  arches (e.g. s390x, ppc64 - #551988)

* Mon May  3 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.010806-5
- Mass rebuild with perl-5.12.0

* Thu Mar  4 2010 Paul Howarth <paul@city-fan.org> - 2.010806-4
- Update to 2.01080604 (see Changes for details)

* Fri Dec 11 2009 Paul Howarth <paul@city-fan.org> - 2.010806-3
- Update to 2.01080603 (see Changes for details)

* Thu Nov 12 2009 Paul Howarth <paul@city-fan.org> - 2.010806-2
- Update to 2.01080602 (see Changes for details)
- No longer need to fix test suite for 64-bit builds

* Fri Nov  6 2009 Paul Howarth <paul@city-fan.org> - 2.010806-1
- Update to 2.010806

* Wed Nov  4 2009 Paul Howarth <paul@city-fan.org> - 2.010805-1
- Update to 2.010805

* Mon Nov  2 2009 Paul Howarth <paul@city-fan.org> - 2.010804-1
- Update to 2.010804

* Thu Oct 29 2009 Paul Howarth <paul@city-fan.org> - 2.010802-1
- Update to 2.010802
- Use system pari library (version 2.3.4) rather than a local build
  (requires patches to Makefile.PL to get docs and test suite)
- Enforce tight dependency on system pari version to ensure we stay in step
- Fix test suite so that 64-bit builds work with pari-2.3.4
- Use standard filter macros for provides filter

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010801-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Paul Howarth <paul@city-fan.org> - 2.010801-3
- Filter out unwanted provides for perl shared objects

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.010801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Paul Howarth <paul@city-fan.org> - 2.010801-1
- update to 2.010801, but build with pari-2.1.7 since 2.1.8 doesn't exist
  (upstream forgot their own numbering convention - CPAN RT#35493)
- re-enable tests
- drop patch for perl 5.10, no longer needed
- remove spurious exec bits on files in upstream distribution

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.010709-7
- disable tests, they're being weird in the buildservers

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.010709-6
- fix for perl 5.10 (many many thanks to Nicholas Clark)

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.010709-5
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.010709-4
- Autorebuild for GCC 4.3

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 2.010709-3
- clarify license as GPL v1 or later, or Artistic (same as perl)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 2.010709-2
- Buildrequire perl(ExtUtils::MakeMaker)

* Fri Oct 27 2006 Paul Howarth <paul@city-fan.org> 2.010709-1
- Update to 2.010709

* Wed Oct 18 2006 Paul Howarth <paul@city-fan.org> 2.010708-1
- Update to 2.010708
- Fix argument order for find with -depth
- Fix Source1 URL

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 2.010706-2
- FE6 mass rebuild

* Fri Jun  2 2006 Paul Howarth <paul@city-fan.org> 2.010706-1
- Update to 2.010706

* Wed May 31 2006 Paul Howarth <paul@city-fan.org> 2.010705-1
- Update to 2.010705

* Tue Apr 18 2006 Paul Howarth <paul@city-fan.org> 2.010704-2
- Omit dumb docs (#175198)

* Mon Mar 20 2006 Paul Howarth <paul@city-fan.org> 2.010704-1
- Update to 2.010704

* Fri Mar 17 2006 Paul Howarth <paul@city-fan.org> 2.010703-2
- Simplify %%{__perl_requires} filter

* Wed Feb  1 2006 Paul Howarth <paul@city-fan.org> 2.010703-1
- Update to 2.010703
- Make pari version number calculation more robust

* Wed Dec  7 2005 Paul Howarth <paul@city-fan.org> 2.010702-1
- Initial build
