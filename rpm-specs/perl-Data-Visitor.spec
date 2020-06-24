Name:           perl-Data-Visitor
Version:        0.30
Release:        19%{?dist}
Summary:        Visitor style traversal of Perl data structures
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Visitor
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Visitor-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(constant)
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Tie::ToObject) >= 0.01
# Test Suite
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::RefHash)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Sub::Name)
Requires:       perl(Task::Weaken)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n Data-Visitor-%{version}

# Silence rpmlint warnings
sed -i '1s,^#!.*perl,#!%{__perl},' t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README t/
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Visitor.3*
%{_mandir}/man3/Data::Visitor::Callback.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-19
- Perl 5.32 rebuild

* Tue Mar 10 2020 Paul Howarth <paul@city-fan.org> - 0.30-18
- Spec clean-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Drop redundant use of %%{?perl_default_filter}
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Use %%license where possible
  - Make %%files list more explicit

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Iain Arnell <iarnell@gmail.com> 0.30-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.28-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.28-2
- Perl 5.16 rebuild

* Sun Feb 19 2012 Iain Arnell <iarnell@gmail.com> 0.28-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter and DESTDIR
- add LICENSE and README to docs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.27-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.27-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.27-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  1 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.27-1
- update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.26-2
- Mass rebuild with perl-5.12.0

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.26-1
- update to latest upstream version
- BR perl(Moose), not perl(Any::Moose)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.25-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- auto-update to 0.25 (by cpan-spec-update 0.01)
- altered br on perl(Any::Moose) (0 => 0.09)
- altered br on perl(Tie::ToObject) (0 => 0.01)
- altered br on perl(namespace::clean) (0 => 0.08)

* Tue May 05 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.24-1
- update to 0.24

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- update to 0.22

* Wed Nov 12 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21

* Sat Sep 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- update to 0.19

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.09-2
- rebuild for new perl

* Sun Oct 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- update to 0.09
- update license tag: GPL -> GPL+
- add t/ to doc
- back to good old Makefile.PL; Build.PL seems to have gone away

* Thu May 03 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.05-2
- bump

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- Specfile autogenerated by cpanspec 1.70.
