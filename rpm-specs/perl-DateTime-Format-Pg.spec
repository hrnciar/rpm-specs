Name:           perl-DateTime-Format-Pg
Version:        0.16013
Release:        11%{?dist}
Summary:        Parse and format PostgreSQL dates and times
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Format-Pg
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 0.13
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.72
BuildRequires:  perl(DateTime::TimeZone) >= 0.12
BuildRequires:  perl(DateTime::TimeZone::Floating)
BuildRequires:  perl(DateTime::TimeZone::UTC)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional tests only
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create DateTime or DateTime::Duration objects, and it can take
a DateTime or DateTime::Duration object and produce a string representing
it in a format accepted by PostgreSQL.

%prep
%setup -q -n DateTime-Format-Pg-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16013-11
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16013-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.16013-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16013-2
- Perl 5.26 rebuild

* Fri May 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16013-1
- 0.16013 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Petr Pisar <ppisar@redhat.com> - 0.16012-2
- Support durations with fractional seconds again (bug #1377428)

* Wed Jul 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16012-1
- 0.16012 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16011-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Petr Šabata <contyk@redhat.com> - 0.16011-1
- 0.16011 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16010-7
- Perl 5.22 rebuild

* Fri Nov 14 2014 Petr Šabata <contyk@redhat.com> - 0.16010-6
- 0.16010 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16008-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.16008-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.16008-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.16007-3
- Perl 5.16 rebuild
- Specify all dependencies

* Tue Jan 17 2012 Iain Arnell <iarnell@gmail.com> - 0.16007-2
- rebuilt again for F17 mass rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.16007-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.16005-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.16005-2
- Perl mass rebuild

* Sun Mar 27 2011 Iain Arnell <iarnell@gmail.com> 0.16005-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16004-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16004-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16004-2
- rebuild against perl 5.10.1

* Tue Aug 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.16004-1
- auto-update to 0.16004 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new req on perl(DateTime) (version 0.10)
- added a new req on perl(DateTime::Format::Builder) (version 0.72)
- added a new req on perl(DateTime::TimeZone) (version 0.05)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.16003-1
- update to 0.16003

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 03 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.16002-2
- bump

* Sun Aug 24 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.16002-1
- Specfile autogenerated by cpanspec 1.77.
