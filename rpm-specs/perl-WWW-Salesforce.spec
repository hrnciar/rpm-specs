Name:           perl-WWW-Salesforce
Version:        0.303
Release:        9%{?dist}
Summary:        Simple abstraction layer between SOAP::Lite and Salesforce.com
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WWW-Salesforce
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/WWW-Salesforce-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Socket::SSL) >= 1.94
BuildRequires:  perl(LWP::Protocol::https) >= 6.00
BuildRequires:  perl(POSIX)
BuildRequires:  perl(SOAP::Lite) >= 1.0
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(IO::Socket::SSL) >= 1.94
Requires:       perl(LWP::Protocol::https) >= 6.00
Requires:       perl(SOAP::Lite) >= 1.0

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SOAP::Lite\\)$

%description
This class provides a simple abstraction layer between SOAP::Lite and
Salesforce.com. Because SOAP::Lite does not support complexTypes, and
document/literal encoding is limited, this module works around those
limitations and provides a more intuitive interface a developer can
interact with.


%prep
%setup -q -n WWW-Salesforce-%{version}


%build
# Don't answer interactive build questions
exec </dev/null

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.303-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.303-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.303-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.303-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.303-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.303-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.303-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.303-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.303-1
- 0.303 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.24 rebuild

* Tue Mar 01 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.25-1
- Update to 0.25 (#1281982)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.24-1
- Update to 0.24

* Mon Jun 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump
- Update build-requires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Filip Andres <filip@andresovi.net> - 0.21-1
- Update to later version

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.20-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Mon Oct 14 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.20-1
- Update to later version

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.13-8
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 0.13-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.13-2
- Perl mass rebuild

* Tue Nov 02 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.13-1
- Bump to later release

* Fri Aug 28 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
- Disable tests, they use network connection
- Remove Crypt::SSLeay dependency
