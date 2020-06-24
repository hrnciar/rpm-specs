Name:           perl-iCal-Parser
Version:        1.21
Release:        12%{?dist}
Summary:        Parse iCalendar files into a data structure
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/iCal-Parser
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIXED/iCal-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(DateTime::Format::ICal) >= 0.08
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File) >= 1.1
BuildRequires:  perl(IO::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::vFile::asData) >= 0.02
# Tests:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(FreezeThaw) >= 0.43
BuildRequires:  perl(Test::More) >= 0.54
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DateTime::Format::ICal) >= 0.08
Requires:       perl(Text::vFile::asData) >= 0.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DateTime::Format::ICal|Text::vFile::asData)\\)$

%description
This Perl module processes iCalendar (vCalendar 2.0) files as specified in
RFC 2445 into a data structure. It handles recurrences (RRULEs), exclusions
(EXDATEs), event updates (events with a RECURRENCE-ID), and nested data
structures (ATTENDEES and VALARMs). It currently ignores the VTIMEZONE,
VJOURNAL and VFREEBUSY entry types.

%prep
%setup -q -n iCal-Parser-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- Perl 5.24 rebuild

* Mon Mar 14 2016 Petr Pisar <ppisar@redhat.com> 1.20-1
- Specfile autogenerated by cpanspec 1.78.
