Name:           perl-Mail-JMAPTalk
Version:        0.15
Release:        2%{?dist}
Summary:        Perl client for JMAP protocol
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Mail-JMAPTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Mail-JMAPTalk-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::Base64)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(JSON)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This is a really basic wrapper around the JMAP protocol <http://jmap.io/>. It
has a rudimentary "Login" command as well, but it doesn't support the entire
protocol yet.

%prep
%setup -q -n Mail-JMAPTalk-%{version}

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
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.32 rebuild

* Tue May 26 2020 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Mon May 25 2020 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-2
- Perl 5.30 rebuild

* Thu Apr 18 2019 Petr Pisar <ppisar@redhat.com> - 0.13-1
- 0.13 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.28 rebuild

* Tue Apr 24 2018 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Fri Aug 11 2017 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.26 rebuild

* Thu Mar 09 2017 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump

* Thu Dec 01 2016 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump

* Fri Nov 11 2016 Petr Pisar <ppisar@redhat.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
