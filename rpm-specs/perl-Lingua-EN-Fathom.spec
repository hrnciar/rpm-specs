Name:           perl-Lingua-EN-Fathom
Version:        1.22
Release:        7%{?dist}
Summary:        Measure readability of English text
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Lingua-EN-Fathom
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/Lingua-EN-Fathom-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Lingua::EN::Sentence) >= 0.28
BuildRequires:  perl(Lingua::EN::Syllable) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Lingua::EN::Sentence) >= 0.28
Requires:       perl(Lingua::EN::Syllable) >= 0.28

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Lingua::EN::Syllable\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Lingua::EN::Sentence\\)$

%description
This module analyses English text in either a string or file. Totals are
then calculated for the number of characters, words, sentences, blank and
non blank (text) lines and paragraphs.

%prep
%setup -q -n Lingua-EN-Fathom-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Jeff fearn <jfearn@redhat.com> 1.19-1
- New upstream

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 8 2014 Jeff fearn <jfearn@redhat.com> 1.15-2
- Remove unnecessary requires and dircetory clean up command. BZ #1033987

* Mon Nov 04 2013 Jeff fearn <jfearn@redhat.com> 1.15-1
- Specfile autogenerated by cpanspec 1.79.
