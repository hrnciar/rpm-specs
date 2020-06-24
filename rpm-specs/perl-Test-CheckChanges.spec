Name:		perl-Test-CheckChanges
Summary:	Check that the Changes file matches the distribution
Version:	0.14
Release:	28%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-CheckChanges
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-CheckChanges-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build::Version)
BuildRequires:	perl(Test::Builder)
# Test Suite
BuildRequires:	perl(English)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(Perl::Critic::Policy::NamingConventions::Capitalization)
BuildRequires:	perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMagicNumbers)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Module::Build::Version)

%description
This module checks that your Changes file has an entry for the current version
of the Module being tested. The version information for the distribution being
tested is taken out of the Build data, or if that is not found, out of the
Makefile. It then attempts to open, in order, a file with the name Changes or
CHANGES. The Changes file is then parsed for version numbers. If one and only
one of the version numbers matches, the test passes; otherwise the test fails.
A message with the current version is printed if the test passes; otherwise
diagnostic messages are printed to help explain the failure.

%prep
%setup -q -n Test-CheckChanges-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
TEST_AUTHOR=1 ./Build test

%files
%doc Changes examples/ README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CheckChanges.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-28
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Paul Howarth <paul@city-fan.org> - 0.14-26
- Spec clean-up
  - Use author-independent source URL
  - Drop support for building with Test::More < 0.88
  - Drop support for building on RHEL-5
  - Drop redundant buildroot cleaning in %%install section

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-24
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-21
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-13
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-12
- Perl 5.20 rebuild

* Thu Aug 28 2014 Paul Howarth <paul@city-fan.org> - 0.14-11
- Specify all dependencies (#1134856)
- Drop %%defattr, redundant since rpm 4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.14-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.14-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-3
- Perl mass rebuild

* Fri May  6 2011 Paul Howarth <paul@city-fan.org> - 0.14-2
- Sanitize for Fedora submission

* Fri May  6 2011 Paul Howarth <paul@city-fan.org> - 0.14-1
- Initial RPM version
