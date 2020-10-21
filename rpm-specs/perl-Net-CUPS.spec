Name:           perl-Net-CUPS
Version:        0.64
Release:        14%{?dist}
Summary:        Perl bindings to the CUPS C API Interface
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-CUPS
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/Net-CUPS-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildRequires:  coreutils
BuildRequires:  cups-devel
BuildRequires:  cups-filters-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Net::CUPS is an interface to the Common Unix Printing System API.  If you feel
an urge to control CUPS servers via Perl, this is a good way to do it :)

%prep
%setup -q -n Net-CUPS-%{version}
find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-7
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-6
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.64-4
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-1
- 0.64 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-1
- 0.63 bump

* Fri Jul 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-1
- 0.62 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-23
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-20
- Perl 5.22 rebuild

* Fri Oct 17 2014 Paul Howarth <paul@city-fan.org> - 0.61-19
- Fix FTBFS due to bad version check in Makefile.PL (#1154078)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-18
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.61-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 09 2012 Petr Šabata <contyk@redhat.com> - 0.61-12
- Build with CUPS 1.6+, thanks to Jiří Popelka <jpopelka@redhat.com>,
  rhbz#841925, rt#78583
- Drop command macros and modernize spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.61-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.61-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.61-6
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.61-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.61-4
- rebuild against perl 5.10.1

* Fri Aug 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.61-3
- bump

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.61-2
- add filtering to remove private so metadata

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.61-1
- auto-update to 0.61 (by cpan-spec-update 0.01)
- added a new req on perl(Test::More) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.59-2
- ...and finish cleaning up

* Sat Jan 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.59-1
- update to 0.59
- drop some fixes that have been applied upstream (RHBZ#455190, RHBZ#455192,
  RT#35966)

* Sun Jul 13 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.56-2
- and remove i18n.h from CUPS.xs.  See bz#455190
- add zlib-devel as a BR.  See bz#455192
- patch t/03_destination.t to not test add/remove functionality -- this is an
  admin action under Fedora, if memory serves

* Sun Jul 13 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.56-1
- update to 0.56

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.55-4
- Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.55-3
- Autorebuild for GCC 4.3

* Wed Jan 02 2008 Ralf Corsépius <rc040203@freenet.de> 0.55-2
- Adjust Licence-tag.
- Spec file cosmetics.
- BR: perl(Test::More) (BZ 419631).

* Tue Dec 04 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.55-1
- update to 0.55

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.51-3
- bump

* Wed Mar 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.51-2
- bump

* Fri Mar 16 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.51-1
- Specfile autogenerated by cpanspec 1.70.
