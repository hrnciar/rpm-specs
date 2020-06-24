Name:           perl-POE-Filter-Transparent-SMTP
Version:        0.2
Release:        35%{?dist}
Summary:        A POE filter for SMTP

# note license definition in Makefile.PL
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/POE-Filter-Transparent-SMTP
Source0:        https://cpan.metacpan.org/authors/id/U/UL/ULTRADM/POE-Filter-Transparent-SMTP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(POE)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
POE data filter which aims to make SMTP data transparent 
just before going onto the wire as per RFC 821 Section 4.5.2.

%prep
%setup -q -n POE-Filter-Transparent-SMTP-%{version}
chmod -x LICENSE

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-35
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-32
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-29
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-26
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-24
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Yanko Kaneti <yaneti@declera.com>
- Remove defattr. Use license.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-21
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.2-17
- Perl 5.18 rebuild

* Sun Feb 17 2013 Yanko Kaneti <yaneti@declera.com> - 0.2-16
- BR: perl(ExtUtils::MakeMaker). Fix bogus changelog date.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.2-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.2-11
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.2-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2-8
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Yanko Kaneti <yaneti@declera.com> - 0.2-4
- Must own everything under %%{perl_vendorlib}

* Wed Jun  3 2009 Yanko Kaneti <yaneti@declera.com> - 0.2-3
- Don't own %%{perl_vendorlib}/POE + Filter
- Initial import

* Thu Apr 16 2009 Yanko Kaneti <yaneti@declera.com> - 0.2-2
- fix LICENSE permissions

* Wed Apr 15 2009 Yanko Kaneti <yaneti@declera.com> - 0.2-1
- First attempt on packaging. Based on perl-POE-Filter-Zlib
