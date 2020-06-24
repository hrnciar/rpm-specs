Name:           perl-HTML-Tidy
Version:        1.60
Release:        9%{?dist}
Summary:        (X)HTML cleanup in a Perl object
License:        Artistic 2.0 and (GPL+ or Artistic)
URL:            https://metacpan.org/release/HTML-Tidy
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Tidy-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtidyp-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Script Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(LWP::Simple)
# Test Suite
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# needed by webtidy to fetch URLs
Requires:       perl(LWP::Simple)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user
looking to migrate, see the section "Converting from HTML::Lint".

%prep
%setup -q -n HTML-Tidy-%{version}

find .  -type f -exec chmod -c -x                              {} +
find .  -type f -exec perl -pi -e 's/\r//'                     {} +
find t/ -type f -exec perl -pi -e 's|^#!perl|#!/usr/bin/perl|' {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs'  -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README.markdown t/
%{perl_vendorarch}/auto/HTML/
%{perl_vendorarch}/HTML/
%{_bindir}/webtidy
%{_mandir}/man3/HTML::Tidy.3*
%{_mandir}/man3/HTML::Tidy::Message.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Paul Howarth <paul@city-fan.org> - 1.60-1
- Update to 1.60
  - Fixed t/clean.t to be insensitive to tidyp library version (GH#26)
- Classify buildreqs by usage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-2
- Perl 5.26 rebuild

* Sun May 28 2017 Paul Howarth <paul@city-fan.org> - 1.58-1
- Update to 1.58 (test fixes and more tests)
- Work around overly restrictive platform+tidpy version requirement in t/clean.t
  (https://github.com/petdance/html-tidy/issues/26)
- Drop redundant Group: tag
- Simplify find commands using -empty and -delete

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.56-1
- Update to 1.56

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.54-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Petr Šabata <contyk@redhat.com> - 1.54-8
- Correct the license tag (HTML::Tidy::Message uses the "Perl" license)

* Mon Nov 12 2012 Petr Šabata <contyk@redhat.com> - 1.54-7
- Fix dependencies
- Modernize the spec a bit

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.54-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.54-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Paul Howarth <paul@city-fan.org> - 1.54-1
- Update to 1.54
- Build against libtidyp rather than libtidy
- License changed from "same as Perl" to Artistic 2.0
- Drop old patch, no longer needed
- README changed to README.markdown
- Add dependencies on perl(Exporter) and perl(LWP::Simple)
- Use %%{?perl_default_filter}

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.08-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 13 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-3
- bump

* Thu Oct 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.08-2
- apply patch from rt tracker
- misc spec cleanups

* Fri May 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.08-1
- Specfile autogenerated by cpanspec 1.71.
