Name:           perl-WWW-Shorten
Version:        3.093
Release:        15%{?dist}
Summary:        Interface to URL shortening sites
License:        Artistic 2.0
URL:            https://metacpan.org/release/WWW-Shorten
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/WWW-Shorten-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Auto)
BuildRequires:  perl(LWP) >= 5.75
BuildRequires:  perl(LWP::UserAgent) >= 2.023
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Try::Tiny) >= 0.24
BuildRequires:  perl(URI) >= 1.27
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A unified interface to various URL shortening services on the web, such as
TinyURL or makeashorterlink.com.

%prep
%setup -q -n WWW-Shorten-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes MANIFEST README.md
%{perl_vendorlib}/*
%{_bindir}/shorten
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.093-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.093-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.093-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Petr Pisar <ppisar@redhat.com> - 3.093-6
- Package LICENSE file correctly (bug #1481228)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.093-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.093-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.093-2
- Perl 5.24 rebuild

* Sat May 07 2016 Julian C. Dunn <jdunn@aquezada.com> - 3.093-1
- Upgrade to 3.093 (bz#1318639)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 9 2016 Julian C. Dunn <jdunn@aquezada.com> - 3.08-1
- Upgrade to 3.08 (bz#1296197)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.06-2
- Perl 5.22 rebuild

* Fri Jan 23 2015 Julian C. Dunn <jdunn@aquezada.com> - 3.06-1
- Upgrade to 3.06 (bz#1142983)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-2
- Perl 5.20 rebuild

* Sat Jun 07 2014 Julian C. Dunn <jdunn@aquezada.com> - 3.05-1
- Upgrade to 3.05 (bz#1095263)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Julian C. Dunn <jdunn@aquezada.com> - 3.04-1
- Upgrade to 3.04 (bz#1000526)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 3.03-5
- Perl 5.18 rebuild
- Skip t/98pod-coverage.t test (CPAN RT#85418)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 3.03-2
- Perl 5.16 rebuild

* Sun Apr 08 2012 Julian C. Dunn <jdunn@aquezada.com> 3.03-1
- Update to 3.03
- Run only tests that do not require network access

* Thu Apr 05 2012 Julian C. Dunn <jdunn@aquezada.com> 3.02-2
- Changes per review in bz#810028

* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 3.02-1
- Initial packaging based on cpanspec 1.78 output
