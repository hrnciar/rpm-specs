Name:           perl-Nagios-Plugin
Version:        0.37
Release:        17%{?dist}
Summary:        Family of perl modules to streamline writing Nagios plugins
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Nagios-Plugin
Source0:        https://cpan.metacpan.org/modules/by-module/Nagios/Nagios-Plugin-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Monitoring::Plugin)
BuildRequires:  perl(Monitoring::Plugin::Config)
BuildRequires:  perl(Monitoring::Plugin::ExitResult)
BuildRequires:  perl(Monitoring::Plugin::Functions)
BuildRequires:  perl(Monitoring::Plugin::Getopt)
BuildRequires:  perl(Monitoring::Plugin::Performance)
BuildRequires:  perl(Monitoring::Plugin::Range)
BuildRequires:  perl(Monitoring::Plugin::Threshold)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This module is deprecated in favor of Monitoring::Plugin.

Nagios::Plugin and its associated Nagios::Plugin::* modules are a family of
perl modules to streamline writing Nagios plugins. The main end user
modules are Nagios::Plugin, providing an object-oriented interface to the
entire Nagios::Plugin::* collection, and Nagios::Plugin::Functions,
providing a simpler functional interface to a useful subset of the
available functionality.

%prep
%setup -q -n Nagios-Plugin-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Nagios
%{_mandir}/man3/Nagios::Plugin*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-17
- Perl 5.32 rebuild

* Mon Jun 15 2020 Petr Pisar <ppisar@redhat.com> - 0.37-16
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-2
- Perl 5.22 rebuild

* Mon Dec 08 2014 Petr Šabata <contyk@redhat.com> - 0.37-1
- 0.37 bump; this module is now deprecated in favor of Monitoring::Plugin

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 0.36-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.36-2
- Perl 5.16 rebuild

* Mon Apr 02 2012 Petr Šabata <contyk@redhat.com> - 0.36-1
- Modernize the spec and bump to 0.36
- Correct dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.35-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.35-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.35-1
- Upstream released new version

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.34-1
- Upstream released new version

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.33-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.33-3
- rebuild against perl 5.10.1

* Thu Aug 27 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.33-2
- Review fixes (#517497)

* Thu Aug 13 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.33-1
- Initial import
