# Perform optional tests
%bcond_without perl_DBD_Mock_enabled_optional_test

Name:           perl-DBD-Mock
Version:        1.55
Release:        3%{?dist}
Summary:        Mock database driver for testing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBD-Mock
Source0:        https://cpan.metacpan.org/modules/by-module/DBD/DBD-Mock-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(DBI) >= 1.3
BuildRequires:  perl(List::Util) >= 1.27
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.47
%if %{with perl_DBD_Mock_enabled_optional_test}
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DBI) >= 1.3
Requires:       perl(List::Util) >= 1.27

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DBI|List::Util)\\)$

%description
Testing with databases can be tricky. If you are developing a system married
to a single database then you can make some assumptions about your environment
and ask the user to provide relevant connection information.  But if you need
to test a framework that uses DBI, particularly a framework that uses
different types of persistence schemes, then it may be more useful to simply
verify what the framework is trying to do -- ensure the right SQL is generated
and that the correct parameters are bound. DBD::Mock makes it easy to just
modify your configuration (presumably held outside your code) and just use it
instead of DBD::Foo (like DBD::Pg or DBD::mysql) in your framework.

%prep
%setup -q -n DBD-Mock-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
find blib/libdoc -type f -empty -delete
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset REPORT_TEST_ENVIRONMENT
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.55-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Petr Pisar <ppisar@redhat.com> - 1.55-1
- 1.55 bump

* Tue Dec 03 2019 Petr Pisar <ppisar@redhat.com> - 1.53-1
- 1.53 bump

* Thu Oct 31 2019 Petr Pisar <ppisar@redhat.com> - 1.52-1
- 1.52 bump

* Wed Oct 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-1
- 1.51 bump

* Wed Oct 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-1
- 1.50 bump

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 1.49-1
- 1.49 bump

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 1.48-1
- 1.48 bump

* Fri Sep 06 2019 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Do not package empty manual pages

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Petr Pisar <ppisar@redhat.com> - 1.45-9
- Correct dependency filter
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.45-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.43-2
- Perl 5.16 rebuild

* Wed Jan 25 2012 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.39-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.39-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.39-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.39-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.39-1
- update to 1.39

* Sat Oct 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.37-1
- update to 1.37

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.36-2
- rebuild for new perl

* Tue Oct 23 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.36-1
- update to 1.36
- license tag: GPL -> GPL+

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.35-1
- update to 1.35
- add t/ to doc
- refactor perl br's
- update source url to pull by module, rather than by author

* Mon Mar 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.34-2
- bump

* Sat Mar 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.34-1
- Specfile autogenerated by cpanspec 1.70.
