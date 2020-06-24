Name:           perl-TAP-Formatter-JUnit
Version:        0.11
Release:        16%{?dist}
Summary:        Harness output delegate for JUnit output
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/TAP-Formatter-JUnit
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-JUnit-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(TAP::Formatter::Console)
BuildRequires:  perl(TAP::Formatter::Console::Session)
BuildRequires:  perl(Storable)
BuildRequires:  perl(XML::Generator)
# Script Runtime
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(TAP::Parser::Aggregator)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(TAP::Harness) >= 3.12
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::XML)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(TAP::Formatter::Console)
Requires:       perl(TAP::Formatter::Console::Session)

%description
This module provides JUnit output formatting for TAP::Harness (a replacement
for Test::Harness.

%prep
%setup -q -n TAP-Formatter-JUnit-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes README
%{_bindir}/tap2junit
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.22 rebuild

* Wed Oct  8 2014 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - Use "IPC::Run" instead of "IPC::Open2" in tests, to fix problems with tests
    freezing on Windows

* Wed Oct  1 2014 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10
  - Switch from "Test::Differences" to "Test::XML", to eliminate failures due
    to differences in ordering of XML attributes (CPAN RT#81552)
  - Use "File::Spec->null()" to get proper path to NULL (CPAN RT#81200,
    CPAN RT#82227)
  - Moved POD tests to "xt/" directory
  - Move timing sensitive tests to "xt/" directory (CPAN RT#69777)
- Classify buildreqs by usage

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Paul Howarth <paul@city-fan.org> - 0.09-7
- Address test failures due to hash order randomization (CPAN RT#81552)
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.09-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Perl 5.16 rebuild

* Fri Jan 27 2012 Daniel P. Berrange <berrange@redhat.com> - 0.09-1
- Update to 0.09 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Daniel P. Berrange <berrange@redhat.com> - 0.08-2
- Updated with suggestions from review (rhbz #752838)

* Mon Nov 07 2011 Daniel P. Berrange <berrange@redhat.com> - 0.08-1
- Specfile autogenerated by cpanspec 1.78.
