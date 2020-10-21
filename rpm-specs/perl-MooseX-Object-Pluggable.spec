Name:           perl-MooseX-Object-Pluggable
Version:        0.0014
Release:        17%{?dist}
Summary:        Make your Moose classes pluggable
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/MooseX-Object-Pluggable
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Object-Pluggable-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 0.35
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# keep rpmlint happy
Requires:       perl(strict), perl(warnings), perl(Moose)

%{?perl_default_filter}

%description
This module aids in the development and deployment of plugin-enabled
Moose-based classes. It extends the Moose framework via roles to enable
this behavior.

%prep
%setup -q -n MooseX-Object-Pluggable-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|; s|^#!/usr/local|#!/usr|' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
AUTHOR_TESTING=1 make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0014-2
- Perl 5.22 rebuild

* Tue Jan 20 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.0014-1
- Update to 0.0014

* Tue Nov 11 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.0013-1
- Update to 0.0013
- Clean up spec file
- Add perl default filter
- Drop tests from the documentation
- Switch AutoProv on
- Fix description

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0011-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.0011-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.0011-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.0011-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0011-5
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0011-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.0011-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.0011-1
- auto-update to 0.0011 (by cpan-spec-update 0.01)
- altered br on perl(Moose) (0.17 => 0.35)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.0009-2
- rebuild against new Moose level

* Tue Dec 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.0009-1
- update to 0.0009

* Tue Jul 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.0007-2
- ...and fix build failure

* Tue Jul 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.0007-1
- update to 0.0007

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.0005-2
- rebuild for new perl

* Thu Apr 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.0005-1
- update to 0.0005
- update BR's
- add bits from t/lib/ to %%doc -- examples are always useful

* Wed Jan 24 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.0004-2
- bump

* Wed Jan 24 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.0004-1
- update to 0.0004

* Wed Jan 17 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.0002-1
- Specfile autogenerated by cpanspec 1.70.
