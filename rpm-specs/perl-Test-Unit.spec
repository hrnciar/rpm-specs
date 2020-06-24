Name:           perl-Test-Unit
Version:        0.25
Release:        37%{?dist}
Summary:        The PerlUnit testing framework

License:        GPL+ or Artistic
URL:            http://perlunit.sourceforge.net/
Source0:        https://cpan.metacpan.org/authors/id/M/MC/MCAST/Test-Unit-%{version}.tar.gz
# https://rt.cpan.org/Public/Bug/Display.html?id=69025
Patch0:         tests5.14.patch
# https://rt.cpan.org/Public/Bug/Display.html?id=77779
Patch1:         perl5.16.patch
# Fix random test failures with perl 5.18, bug #1104134, CPAN RT#87017
Patch2:         Test-Unit-0.25-Accept-all-family-differences-in-the-AssertTest-test.patch
# Adapt tests to Perl 5.30, bugs #1716422, #1749253, CPAN RT#129738
Patch3:         Test-Unit-0.25-Adapt-tests-to-Perl-5.30.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inner)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::DialogBox)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This framework is intended to support unit testing in an object-oriented
development paradigm (with support for inheritance of tests etc.) and is
derived from the JUnit testing framework for Java by Kent Beck and Erich
Gamma.

%perl_default_filter
%global __provides_exclude %{?__provides_exclude}|perl\\(Experimental::Sample\\)|perl\\(fail_example\\)|perl\\(fail_example_testsuite_setup\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(Exporter\\)

%prep
%setup -q -n Test-Unit-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's/\r//' examples/Experimental/Sample.pm
chmod a+x TkTestRunner.pl TestRunner.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc AUTHORS ChangeLog Changes COPYING.Artistic COPYING.GPL-2 doc examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-37
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Petr Pisar <ppisar@redhat.com> - 0.25-35
- Adapt tests to changed Perl 5.30 (bug #1749253)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Petr Pisar <ppisar@redhat.com> - 0.25-33
- Adapt tests to Perl 5.30 (bug #1716422)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-32
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-29
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-26
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-24
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-21
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-20
- Perl 5.20 rebuild

* Fri Jun 20 2014 Petr Pisar <ppisar@redhat.com> - 0.25-19
- Fix random test failures with perl 5.18 (bug #1104134)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.25-16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.25-13
- Perl 5.16 rebuild
- Specify all dependencies
- apply patch to for Test::Unit::TestBase RT#77779

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.25-11
- Perl mass rebuild & clean spec & new filters
- apply upstream patch for tests RT#69025

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.25-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.25-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.25-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.25-4
Rebuild for new perl

* Fri Dec 21 2007 Xavier Bachelot <xavier@bachelot.org> - 0.25-3
- Mangle Summary.
- Fix License.
- Filter unwanted provides.

* Thu Dec 20 2007 Xavier Bachelot <xavier@bachelot.org> - 0.25-2
- Filter unwanted require.

* Tue Dec 11 2007 Xavier Bachelot <xavier@bachelot.org> - 0.25-1
- Initial build.
