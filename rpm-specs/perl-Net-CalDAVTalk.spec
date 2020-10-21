# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Net_CalDAVTalk_enables_optional_test
%else
%bcond_with perl_Net_CalDAVTalk_enables_optional_test
%endif

Name:           perl-Net-CalDAVTalk
Version:        0.12
Release:        10%{?dist}
Summary:        CalDAV client with JSON data interface
License:        Artistic 2.0
URL:            https://metacpan.org/release/Net-CalDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CalDAVTalk-%{version}.tar.gz
# Fix using Data::Dumper, CPAN RT#123646
Patch0:         Net-CalDAVTalk-0.12-Load-Data-Dumper.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Display)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Email)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(Data::ICal::Entry::TimeZone)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Daylight)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Standard)
BuildRequires:  perl(Data::ICal::TimeZone) >= 1.23
BuildRequires:  perl(DateTime::Format::ICal) >= 0.09
BuildRequires:  perl(DateTime::Format::ISO8601) >= 0.08
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Net::DAVTalk) >= 0.02
BuildRequires:  perl(Text::LevenshteinXS) >= 0.03
BuildRequires:  perl(Text::VCardFast) >= 0.06
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice)
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Net_CalDAVTalk_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
# Test::CheckManifest 0.9 not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(Data::ICal::TimeZone) >= 1.23
Requires:       perl(DateTime::Format::ICal) >= 0.09
Requires:       perl(DateTime::Format::ISO8601) >= 0.08
Requires:       perl(Net::DAVTalk) >= 0.02
Requires:       perl(Text::LevenshteinXS) >= 0.03
Requires:       perl(Text::VCardFast) >= 0.06

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::ICal::TimeZone|DateTime::Format::ICal|DateTime::Format::ISO8601|Net::DAVTalk|Text::LevenshteinXS|Text::VCardFast)\\)$

%description
This a Perl library for accessing CalDAV servers providing JSON interface to
the data.

%prep
%setup -q -n Net-CalDAVTalk-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.26 rebuild

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Petr Pisar <ppisar@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
