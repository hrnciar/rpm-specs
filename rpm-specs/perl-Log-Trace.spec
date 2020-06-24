Name:           perl-Log-Trace
Version:        1.070
Release:        32%{?dist}
License:        GPLv2+
Summary:        A unified approach to tracing
Source:         https://cpan.metacpan.org/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
Url:            https://metacpan.org/release/Log-Trace
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Serializer)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Recommends:     perl(Data::Dumper)
Recommends:     perl(Data::Serializer)
Recommends:     perl(Sys::Syslog)
Recommends:     perl(Time::HiRes)

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)$

%description
This module provides a unified approach to tracing. A script can 'use
Log::Trace qw( < mode > )' to set the behaviour of the TRACE function.By
default, the trace functions are exported to the calling package only.
You can export the trace functions to other packages with the 'Deep'
option. See the "OPTIONS" manpage for more information.

%prep
%setup -q -n Log-Trace-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-32
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-29
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-26
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-23
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-21
- Perl 5.24 rebuild

* Mon Feb 29 2016 Petr Šabata <contyk@redhat.com> - 1.070-20
- Package cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.070-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.070-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.070-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.070-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.070-8
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.070-7
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.070-5
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.070-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.070-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.070-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.070-1
- submission

* Wed Apr 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.070-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
