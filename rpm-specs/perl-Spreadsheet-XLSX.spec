%global pkgname Spreadsheet-XLSX

Summary:	Perl extension for reading Microsoft Excel 2007 files
Name:		perl-Spreadsheet-XLSX
Version:	0.15
Release:	15%{?dist}
License:	GPL+ or Artistic 
URL:		https://metacpan.org/release/%{pkgname}
Source:		https://cpan.metacpan.org/authors/id/M/MI/MIKEB/%{pkgname}-%{version}.tar.gz
Patch0:		perl-Spreadsheet-XLSX-0.15-archive-zip.patch
Patch1:		perl-Spreadsheet-XLSX-0.15-makemaker.patch
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl-generators
BuildRequires:	perl(Archive::Zip) >= 1.16, perl(Spreadsheet::ParseExcel) >= 0.45
BuildRequires:	perl(ExtUtils::MakeMaker), perl(Data::Dumper), perl(Exporter)
BuildRequires:	perl(Test::More), perl(Test::NoWarnings)
BuildArch:	noarch

%description
The Spreadsheet::XLSX module is a emulation of Spreadsheet::ParseExcel for
Excel 2007 (.xlsx) file format in a quick and dirty way. It supports styles
and many of the Excel's quirks, but not all. It populates the classes from
Spreadsheet::ParseExcel for interoperability; including workbook, worksheet
and cell.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
%patch1 -p1

# Change strange upstream file permissions
chmod 644 Changes README lib/Spreadsheet/{*,*/*}.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Spreadsheet/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Robert Scheck <robert@fedoraproject.org> 0.15-1
- Upgrade to 0.15 (#1285437)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-9
- Perl 5.22 rebuild

* Tue Oct 14 2014 Robert Scheck <robert@fedoraproject.org> 0.13-8
- Modified existing patch to parse value "0" correct (#1152739)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.13-4
- Perl 5.18 rebuild

* Wed May 15 2013 Robert Scheck <robert@fedoraproject.org> 0.13-3
- Modified the existing patch to suppress further warnings

* Thu May 09 2013 Robert Scheck <robert@fedoraproject.org> 0.13-2
- Changes to match with Fedora Packaging Guidelines (#952796)

* Tue Apr 16 2013 Robert Scheck <robert@fedoraproject.org> 0.13-1
- Upgrade to 0.13
- Initial spec file for Fedora and Red Hat Enterprise Linux
