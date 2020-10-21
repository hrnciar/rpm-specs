Name:           perl-Gtk2-Ex-Simple-List
Version:        0.50
Release:        37%{?dist}
Summary:        Simple interface to Gtk2's complex MVC list widget
License:        LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Ex-Simple-List
Source0:        https://cpan.metacpan.org/authors/id/R/RM/RMCFARLA/Gtk2-Perl-Ex/Gtk2-Ex-Simple-List-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Gtk2 has a powerful, but complex MVC (Model, View, Controller) system used
to implement list and tree widgets. Gtk2::Ex::Simple::List automates the
complex setup work and allows you to treat the list model as a more natural
list of lists structure.

%prep
%setup -q -n Gtk2-Ex-Simple-List-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc examples/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-36
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-33
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-30
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-27
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-25
- Perl 5.24 rebuild

* Thu Feb 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-24
- Package cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-21
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.50-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.50-14
- Perl 5.16 rebuild

* Tue Jan 17 2012 Ralf Corsépius <corsepiu@fedoaproject.org> - 0.50-13
- Add BR: perl(Test::More) (Fix mass rebuild FTBFS).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.50-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.50-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.50-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.50-7
- rebuild against perl 5.10.1

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.50-6
- Fix mass rebuild breakdown: Add BR: perl(Glib::MakeHelper).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.50-3
Rebuild for new perl

* Sat Dec 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.50-2
- bump

* Thu Nov 30 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.50-1
- Specfile autogenerated by cpanspec 1.69.1.
