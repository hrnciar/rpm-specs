# Provides/Requires filtering is different from rpm 4.9 onwards
%global rpm49 %(rpm --version | perl -p -e 's/^.* (\\d+)\\.(\\d+).*/sprintf("%d.%03d",$1,$2) ge 4.009 ? 1 : 0/e' 2>/dev/null || echo 0)

Name:		perl-Declare-Constraints-Simple
Version:	0.03
Release:	41%{?dist}
Summary:	Declarative Validation of Data Structures
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Declare-Constraints-Simple
Source0:	https://cpan.metacpan.org/authors/id/P/PH/PHAYLON/Declare-Constraints-Simple-%{version}.tar.gz
Patch0:		Declare-Constraints-Simple-0.03-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
# Dependencies of bundled Module::Install
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(ExtUtils::MM_Unix)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(YAML)
# Module Runtime
BuildRequires:	perl(aliased)
BuildRequires:	perl(base)
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util) >= 1.14
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Filter unwanted Requires (rpm 4.9 onwards)
%global __requires_exclude ^perl\\(Declare::Constraints::Simple-Library\\)

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep
%setup -q -n Declare-Constraints-Simple-%{version}
%patch0 -p1

# Filter unwanted Requires (prior to rpm 4.9)
%if ! %{rpm49}
%global reqfilt /bin/sh -c "%{__perl_requires} | grep -Fvx 'perl(Declare::Constraints::Simple-Library)'"
%global __perl_requires %{reqfilt}
%endif

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
%doc Changes README t/
%{perl_vendorlib}/Declare/
%{_mandir}/man3/Declare::Constraints::Simple.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Array.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Base.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Exportable.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::General.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Hash.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Numerical.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::OO.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Operators.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Referencial.3*
%{_mandir}/man3/Declare::Constraints::Simple::Library::Scalar.3*
%{_mandir}/man3/Declare::Constraints::Simple::Result.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-41
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-38
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Paul Howarth <paul@city-fan.org> - 0.03-36
- Spec tidy-up
  - Simplify find command using -delete
  - Drop redundant buildroot cleaning in %%install section
  - Drop redundant explicit %%clean section

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-34
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-31
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-30
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 0.03-28
- Adjust RPM version detection to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-27
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Paul Howarth <paul@city-fan.org> - 0.03-25
- Spec clean-up
  - Prefer %%global over %%define
  - Drop %%defattr, redundant since rpm 4.4
  - Don't need to remove empty directories from the buildroot

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-23
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.03-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.03-16
- Perl 5.16 rebuild

* Mon Jan 23 2012 Paul Howarth <paul@city-fan.org> - 0.03-15
- Spec clean-up
  - Make %%files list more explicit
  - Classify buildreqs by build/module/test
  - Use search.cpan.org source URL
  - Don't use macros for commands
  - Use tabs

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.03-14
- Spec clean-up
  - Simplify pre-rpm-4.9 provides filter
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Make %%files list more specific

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-13
- Perl mass rebuild

* Sun Feb 13 2011 Paul Howarth <paul@city-fan.org> - 0.03-12
- Fix dependency filter for rpm 4.9 onwards

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-9
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-8
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-6
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.03-3
- Rebuild for new perl

* Fri May 04 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.03-2
- Bump

* Tue May 01 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.03-1
- Specfile autogenerated by cpanspec 1.71
