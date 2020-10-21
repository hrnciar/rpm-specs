Name:           perl-Inline-Struct
Version:        0.27
Release:        7%{?dist}
Summary:        Manipulate C structures directly from Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Inline-Struct
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-Struct-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Inline) >= 0.66
BuildRequires:  perl(Inline::C) >= 0.62
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Inline) >= 0.66
Requires:       perl(Inline::C) >= 0.62
Requires:       perl(Parse::RecDescent)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Inline\\)$

%description
Inline::Struct is not a new language. It's a language extension designed to
be used by Inline::C. It parses struct definitions and creates typemaps and
XS code which bind each struct into a Perl class. This code is passed to
Inline::C, which compiles it in the normal way.

%prep
%setup -q -n Inline-Struct-%{version}
chmod -c a-x benchmark

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO benchmark
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump

* Wed Jan 23 2019 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Mon Jan 21 2019 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-8
- Perl 5.28 rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.23-7
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Perl 5.24 rebuild

* Thu May 05 2016 Petr Pisar <ppisar@redhat.com> - 0.23-1
- 0.23 bump

* Tue May 03 2016 Petr Pisar <ppisar@redhat.com> - 0.21-1
- 0.21 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-2
- Perl 5.22 rebuild

* Thu Jan 08 2015 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Wed Nov 26 2014 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Mon Oct 20 2014 Petr Šabata <contyk@redhat.com> - 0.12-1
- 0.12 bump

* Mon Sep 29 2014 Petr Šabata <contyk@redhat.com> - 0.11-1
- 0.11 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.20 rebuild

* Thu Aug 14 2014 Petr Šabata <contyk@redhat.com> - 0.10-1
- 0.10 bump

* Wed Jul 16 2014 Petr Šabata <contyk@redhat.com> 0.06-1
- Initial packaging
