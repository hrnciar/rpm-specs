Name:           perl-Template-Toolkit-Simple
Version:        0.31
Release:        22%{?dist}
Summary:        Simple interface to Template Toolkit
# inc/Text/Diff.pm (not in binary package):     GPLv2+ or Artistic
# rest:     GPL+ or Artistic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Template-Toolkit-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Template-Toolkit-Simple-%{version}.tar.gz
# Old TestML API moved to TestML1 name space, bug #1650156
Patch0:         Template-Toolkit-Simple-0.31-Old-TestML-API-moved-to-TestML1-name-space.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Template) >= 2.22
BuildRequires:  perl(Template::Constants)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS) >= 0.37
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
# Break dependency cycle: perl-Template-Toolkit-Simple → perl-TestML1
# → perl-Template-Toolkit-Simple
BuildRequires:  perl(lib)
BuildRequires:  perl(TestML1)
BuildRequires:  perl(TestML1::Bridge)
BuildRequires:  perl(TestML1::Util)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(JSON::XS)
Requires:       perl(Template) >= 2.22
Requires:       perl(warnings)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS) >= 0.37

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Template|YAML::XS)\\)$

%description
This Perl module is a simple wrapper around Template Toolkit. It exports
a function called `tt' which returns a new Template::Toolkit::Simple object.
The object supports method calls for setting all the Template Toolkit options.

This module also installs a program called `tt-render' which you can use from
the command line to render templates with all the power of the Perl object.
All of the object methods become command line arguments in the command line
version.


%prep
%setup -q -n Template-Toolkit-Simple-%{version}
%patch0 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST
# Fix shellbang
sed -i -e '1 s,^#!/usr/bin/env perl,#!perl,' bin/tt-render

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
%if %{defined perl_bootstrap}
# Break dependency cycle: perl-Template-Toolkit-Simple → perl-TestML1
# → perl-Template-Toolkit-Simple
make test TEST_FILES="$(find t -name '*.t' \
    \! -exec grep -q -e 'use TestML1' {} \; -print | tr \"\\n\" ' ')"
%else
make test
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/tt-render

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-19
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-18
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Petr Pisar <ppisar@redhat.com> - 0.31-16
- Old TestML API moved to TestML1 name space (bug #1650156)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-14
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-10
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.22 rebuild

* Wed Dec 10 2014 Petr Pisar <ppisar@redhat.com> - 0.31-1
- 0.31 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.20 rebuild

* Mon Aug 18 2014 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Tue Aug 12 2014 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Finish perl-TestML bootstrap

* Wed Aug 06 2014 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Wed Jul 30 2014 Petr Pisar <ppisar@redhat.com> 0.19-1
- Specfile autogenerated by cpanspec 1.78.
