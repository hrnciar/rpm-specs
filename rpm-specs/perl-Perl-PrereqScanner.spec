Name:           perl-Perl-PrereqScanner
Version:        1.023
Release:        16%{?dist}
Summary:        Tool to scan your Perl code for its prerequisites
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-PrereqScanner
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Perl-PrereqScanner-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.124
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
# Getopt::Long::Descriptive not used at tests
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Path)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(PPI) >= 1.215
# Scalar::Util not used at tests
BuildRequires:  perl(String::RewritePrefix) >= 0.005
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
# Optional tests only
# CPAN::Meta not useful
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Module::Path)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Requirements\\)$ 

%description
The scanner will extract loosely your distribution prerequisites from
your files.

%prep
%setup -q -n Perl-PrereqScanner-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-15
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Petr Šabata <contyk@redhat.com> - 1.023-1
- 1.023 bump

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-2
- Perl 5.22 rebuild

* Tue Jan 06 2015 Petr Šabata <contyk@redhat.com> - 1.022-1
- 1.022 bugfix bump

* Wed Nov 26 2014 Petr Pisar <ppisar@redhat.com> - 1.021-1
- 1.021 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Petr Pisar <ppisar@redhat.com> - 1.019-1
- 1.019 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.015-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Iain Arnell <iarnell@gmail.com> 1.015-1
- update to latest upstream version

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 1.014-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.011-2
- Perl 5.16 rebuild

* Sun Mar 25 2012 Iain Arnell <iarnell@gmail.com> 1.011-1
- update to latest upstream version

* Thu Feb 23 2012 Iain Arnell <iarnell@gmail.com> 1.010-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.009-1
- update to the latest release

* Sun Nov 06 2011 Iain Arnell <iarnell@gmail.com> 1.008-1
- update to latest upstream version

* Thu Sep 22 2011 Iain Arnell <iarnell@gmail.com> 1.007-1
- update to latest upstream version

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 1.006-1
- update to latest upstream version

* Thu Aug 18 2011 Iain Arnell <iarnell@gmail.com> 1.005-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.004-2
- Perl mass rebuild

* Sun Jun 05 2011 Iain Arnell <iarnell@gmail.com> 1.004-1
- update to latest upstream version

* Wed May 18 2011 Iain Arnell <iarnell@gmail.com> 1.003-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 1.002-1
- update to latest upstream version

* Thu Jan 06 2011 Iain Arnell <iarnell@gmail.com> 1.001-1
- update to latest upstream version
- fixes scan_prereqs script

* Thu Dec 16 2010 Iain Arnell <iarnell@gmail.com> 1.000-1
- update to latest upstream version

* Mon Dec 06 2010 Iain Arnell <iarnell@gmail.com> 0.101892-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Nov 19 2010 Iain Arnell <iarnell@gmail.com> 0.101891-1
- update to latest upstream version

* Sun May 30 2010 Iain Arnell <iarnell@gmail.com> 0.101480-1
- update to latest upstream version

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 0.101250-2
- bump release for rebuild with perl-5.12.0

* Sun May 09 2010 Iain Arnell <iarnell@gmail.com> 0.101250-1
- update to latest upstream
- BR perl(Moose)
- BR perl(Moose::Role)
- BR perl(Params::Util)
- BR perl(String::RewritePrefix)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100960-2
- Mass rebuild with perl-5.12.0

* Sun Apr 11 2010 Iain Arnell <iarnell@gmail.com> 0.100960-1
- update to latest upstream version

* Thu Apr 08 2010 Iain Arnell <iarnell@gmail.com> 0.100830-2
- drop perl BR

* Sun Apr 04 2010 Iain Arnell <iarnell@gmail.com> 0.100830-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
