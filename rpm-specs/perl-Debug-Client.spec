Name:           perl-Debug-Client
Version:        0.31
Release:        11%{?dist}
Summary:        Client side code for perl debugger
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Debug-Client
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Debug-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install) >= 1.08
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(Carp) >= 1.33
BuildRequires:  perl(constant) >= 1.27
BuildRequires:  perl(English)
BuildRequires:  perl(IO::Socket::IP) >= 0.29
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine) >= 1.14
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl-debugger
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter) >= 5.70
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::HomeDir) >= 1.00
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.38
BuildRequires:  perl(PadWalker) >= 1.98
BuildRequires:  perl(parent) >= 0.228
BuildRequires:  perl(Test::CheckDeps) >= 0.01
BuildRequires:  perl(Test::Class) >= 0.42
BuildRequires:  perl(Test::Deep) >= 0.112
BuildRequires:  perl(Test::More) >= 1.001003
BuildRequires:  perl(Test::Requires) >= 0.07
BuildRequires:  perl(version) >= 0.9908
# Optional tests:
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.20

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp|IO::Socket\\)$

%description
Client side module for debugging. This module is part of padre's debugger.

%prep
%setup -q -n Debug-Client-%{version}
# Removed bundled EE::MM
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-11
- Perl 5.32 rebuild

* Fri Apr 03 2020 Petr Pisar <ppisar@redhat.com> - 0.31-10
- Build-require perl-debugger for the tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-1
- 0.31 bump

* Mon Jun 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-1
- 0.30 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 0.29-5
- Adjust to perl-5.22 (bug #1231216)

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Fri Aug 09 2013 Petr Pisar <ppisar@redhat.com> - 0.26-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump
- Update dependencies

* Thu Apr 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump

* Wed Feb 20 2013 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.20-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.20-1
- 0.20 bump

* Thu Mar 15 2012 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump
- Correct dependencies

* Wed Jan 25 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-1
- update to 0.16
- clean specfile

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- Mass rebuild with perl-5.12.0

* Fri Mar 19 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.11-2
- change to DESTDIR
- fix Description

* Mon Feb 08 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
