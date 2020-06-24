# Perform tests that need the Internet
%bcond_with perl_LWP_Online_enables_network_test

Name:           perl-LWP-Online
Version:        1.08
Release:        28%{?dist}
Summary:        Check whether your process has an access to the web
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/LWP-Online
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/LWP-Online-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install::DSL) >= 1.01
BuildRequires:  perl(Module::Install::Metadata)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(LWP::Simple) >= 5.805
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter)
Requires:       perl(Test::More) >= 0.42

%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is: Am I on the internet?

%prep
%setup -q -n LWP-Online-%{version}
# Remove bundled libraries
rm -r inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if %{with perl_LWP_Online_enables_network_test}
rm t/02_main.t
perl -i -ne 'print $_ unless m{^t/02_main.t$}' MANIFEST
%endif

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTOMATED_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-28
- Perl 5.32 rebuild

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 1.08-27
- Modernize the spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-24
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-21
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-18
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-17
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-15
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-12
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.08-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Petr Šabata <contyk@redhat.com> - 1.08-6
- Update the vague description (#847151)
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.08-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.08-2
- Perl mass rebuild

* Mon Jul 11 2011 Petr Sabata <contyk@redhat.com> - 1.08-1
- 1.08 bump
- Fix (Build)Requires
- Remove now obsolete Buildroot and defattr

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-4
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.07-2
- rebuild against perl 5.10.1

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.07-1
- Specfile autogenerated by cpanspec 1.78.
