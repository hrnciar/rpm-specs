# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Net_CardDAVTalk_enables_optional_test
%else
%bcond_with perl_Net_CardDAVTalk_enables_optional_test
%endif

Name:           perl-Net-CardDAVTalk
Version:        0.09
Release:        8%{?dist}
Summary:        CardDAV client
License:        Artistic 2.0
URL:            https://metacpan.org/release/Net-CardDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CardDAVTalk-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format) >= 2.24
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::MMagic) >= 1.30
BuildRequires:  perl(List::MoreUtils) >= 0.01
BuildRequires:  perl(List::Pairwise) >= 1.00
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DAVTalk) >= 0.08
BuildRequires:  perl(Text::VCardFast) >= 0.07
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice) >= 0.04
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Net_CardDAVTalk_enables_optional_test}
# Optional tests:
# Pod::Coverage 0.18 not used
# Test::CheckManifest 0.9 not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Date::Format) >= 2.24
Requires:       perl(File::MMagic) >= 1.30
Requires:       perl(List::MoreUtils) >= 0.01
Requires:       perl(List::Pairwise) >= 1.00
Requires:       perl(Net::DAVTalk) >= 0.08
Requires:       perl(Text::VCardFast) >= 0.07
Requires:       perl(XML::Spice) >= 0.04

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:{%__requires_exclude}|}^perl\\((Date::Format|File::MMagic|List::MoreUtils|List::Pairwise|Net::DAVTalk|Text::VCardFast|XML::Spice)\\)$

%description
This is an CardDAV client with FastMail Perl API.

%prep
%setup -q -n Net-CardDAVTalk-%{version}

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
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.26 rebuild

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Petr Pisar <ppisar@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
