Name:           perl-Canary-Stability
Version:        2013
Release:        6%{?dist}
Summary:        Canary to check perl compatibility for Schmorp's modules
# See COPYING file.
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Canary-Stability
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(ExtUtils::MakeMaker)

%description
This module is used by Schmorp's modules during configuration stage to test
the installed perl for compatibility with his modules.

%prep
%setup -q -n Canary-Stability-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTOMATED_TESTING PERL_CANARY_STABILITY_COLOUR \
    PERL_CANARY_STABILITY_DISABLE PERL_CANARY_STABILITY_NOPROMPT
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2013-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2013-2
- Perl 5.30 rebuild

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 2013-1
- 2013 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2012-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2012-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2012-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 2012-1
- 2012 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2011-2
- Perl 5.24 rebuild

* Mon Mar 14 2016 Petr Pisar <ppisar@redhat.com> - 2011-1
- 2011 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Petr Pisar <ppisar@redhat.com> - 2006-1
- 2006 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2001-2
- Perl 5.22 rebuild

* Mon Jun 08 2015 Petr Pisar <ppisar@redhat.com> 2001-1
- Specfile autogenerated by cpanspec 1.78.
