Name:           perl-Chart
Version:        2.4.10
Release:        17%{?dist}
Summary:        Series of charting modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Chart
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHARTGRP/Chart-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(GD)
BuildRequires:  perl(GD::Image)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This module is an attempt to build a general purpose graphing module that
is easily modified and expanded.  Chart uses Lincoln Stein's GD module for
all of its graphics primitives calls.

%prep
%setup -q -n Chart-%{version}
chmod -c 644 TODO

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc README TODO Documentation.pdf
%{perl_vendorlib}/Chart*
%{_mandir}/man3/Chart.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-6
- Perl 5.24 rebuild

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 2.4.10-5
- Modernize spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-2
- Perl 5.22 rebuild

* Thu Mar 19 2015 Petr Šabata <contyk@redhat.com> - 2.4.10-1
- 2.4.10 bump, no changes

* Mon Feb 09 2015 Petr Šabata <contyk@redhat.com> - 2.4.9-1
- 2.4.9 bump, no changes

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 2.4.8-1
- 2.4.8 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.6-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  1 2013 Paul Howarth <paul@city-fan.org> - 2.4.6-1
- Update to 2.4.6
  - Corrections to imagemap production in Composite.pm and Lines.pm
  - The brush styles to points and linespoints are extended: not only circles
    represent the points but a number of different brush styles, linke donut,
    Star and so on
  - Typo in _draw_x_ticks corrected
  - Methods scalar_png(), scalar_jpeg() corrected for result
  - Test routine t/scalarImage.t added
  - Chart.pod corrected
  - Documentation.pdf explains the use of colors (appendix added)
  - Corrections in base.pm, routines _draw_bottom_legends, _draw_x_number_ticks
  - Corrections in LinesPoints.pm, routine _draw_data
- Add patch for warnings in Perl 5.16+ (CPAN RT#79658)
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.4.2-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.4.2-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.2-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.2-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun Dec 12 2010 Steven Pritchard <steve@kspei.com> 2.4.2-1
- Update to 2.4.2.
- Improve Summary and description.
- Use PERL_INSTALL_ROOT instead of DESTDIR while installing.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.1-10
- Mass rebuild with perl-5.12.0
- remove two tests failing

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.4.1-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.1-6
- Rebuild for new perl

* Mon Apr 09 2007 Steven Pritchard <steve@kspei.com> 2.4.1-5
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.
- Minor spec cleanup to more closely resemble cpanspec output.

* Mon Aug 28 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.1-4
- Rebuild for FC6

* Mon May 29 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.1-3
- rebuilt and reimported in to devel

* Wed Jan 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.4.1-1
- 2.4.1.
- Don't ship rgb.txt in docs.
- Specfile cleanups.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.3-3
- Rebuilt

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.3-2
- Bring up to date with current fedora.us Perl Spec template.

* Thu Jan 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.3-0.fdr.1
- Update to 2.3.
- Fix file permissions.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2-0.fdr.1
- First build.
