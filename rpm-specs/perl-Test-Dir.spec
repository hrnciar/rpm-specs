# Perform optional tests
%bcond_without perl_Test_Dir_enables_optional_test

Name:           perl-Test-Dir
Version:        1.16
Release:        13%{?dist}
Summary:        Some simple tests on directories and folders
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Dir
Source0:        https://cpan.metacpan.org/authors/id/M/MT/MTHURN/Test-Dir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
%if %{with perl_Test_Dir_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This modules provides a collection of test utilities for directory and folder
attributes. Use it in combination with Test::More in your test programs.

%prep
%setup -q -n Test-Dir-%{version}
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_Test_Dir_enables_optional_test}
rm -r t/pod*.t
perl -i -ne 'print $_ unless m{^t/pod.\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-12
- Perl 5.32 rebuild

* Fri Mar 13 2020 Petr Pisar <ppisar@redhat.com> - 1.16-11
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-2
- Perl 5.26 rebuild

* Mon Apr 24 2017 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump

* Fri Apr 07 2017 Petr Pisar <ppisar@redhat.com> - 1.15-2
- Fix Test::Dir::VERSION declaration (CPAN RT#121007)

* Mon Apr 03 2017 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-10
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.014-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.014-3
- Perl 5.16 rebuild

* Fri May 04 2012 Petr Pisar <ppisar@redhat.com> - 1.014-2
- Use Test::Pod for optional test

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 1.014-1
- Specfile autogenerated by cpanspec 1.78.
