Name:           perl-Test-POE-Server-TCP
Version:        1.20
Release:        14%{?dist}
Summary:        POE Component providing TCP server services for test cases
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-POE-Server-TCP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Test-POE-Server-TCP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.004
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(blib)
# Missed by the automatic perl dependancy generator.
Requires:       perl(POE) >= 1.004
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Test::POE::Server::TCP is a POE component that provides a TCP server
framework for inclusion in client component test cases, instead of having
to roll your own.

%prep
%setup -q -n Test-POE-Server-TCP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-14
- Perl 5.32 rebuild

* Wed Mar 11 2020 Yanko Kaneti <yaneti@declera.com> - 1.20-13
- BR: perl(blib) - split recently

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-10
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- Perl 5.24 rebuild

* Sat Apr 23 2016 Jehane <jehane@fedoraproject.org> - 1.20-1
- Update to 1.20

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-12
- Perl 5.22 rebuild

* Mon Dec 15 2014 Yanko Kaneti <yaneti@declera.com> 1.18-1
- Update to 1.18

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.16-8
- Perl 5.18 rebuild

* Sun Feb 17 2013 Yanko Kaneti <yaneti@declera.com> 1.16-7
- BR: perl(ExtUtils::MakeMaker)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.16-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.16-2
- Perl mass rebuild

* Wed Jun 29 2011 Yanko Kaneti <yaneti@declera.com> 1.16-1
- Latest upstream release - 1.16

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Yanko Kaneti <yaneti@declera.com> 1.14-1
- Latest upstream release - 1.14

* Fri Jun 18 2010 Petr Pisar <ppisar@redhat.com> 1.10-2
- Rebuild against perl-5.12

* Thu May 06 2010 Yanko Kaneti <yaneti@declera.com> 1.10-1
- Specfile autogenerated by cpanspec 1.78.
- Initial revision with feedback from package review bug 589471
