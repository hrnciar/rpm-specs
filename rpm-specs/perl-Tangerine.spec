Name:           perl-Tangerine
Version:        0.23
Release:        12%{?dist}
Summary:        Analyse perl files and report module-related information
License:        MIT
URL:            https://metacpan.org/release/Tangerine
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CONTYK/Tangerine-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Exporter)
%if ! ( 0%{?rhel} )
BuildRequires:  perl(List::Util) >= 1.33
%else
BuildRequires:  perl(List::MoreUtils)
%endif
BuildRequires:  perl(parent)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.77
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
%if ! ( 0%{?rhel} )
Requires:       perl(List::Util) >= 1.33
%else
Requires:       perl(List::MoreUtils)
%endif

%description
Tangerine statically analyses perl files and reports various information
about provided, used (compile-time dependencies) and required (runtime
dependencies) modules.

%prep
%setup -q -n Tangerine-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README.md TODO
%{perl_vendorlib}/*
%{_mandir}/man*/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Perl 5.24 rebuild

* Thu Feb 25 2016 Petr Šabata <contyk@redhat.com> - 0.22-1
- 0.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Petr Šabata <contyk@redhat.com> - 0.21-1
- 0.21 bump

* Mon Aug 24 2015 Petr Šabata <contyk@redhat.com> - 0.19-1
- 0.19 bump

* Thu Jun 25 2015 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-2
- Perl 5.22 rebuild

* Mon May 18 2015 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump, metadata improvements

* Thu May 14 2015 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Mon Apr 27 2015 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump
- The utility is now provided by a separate distribution/package

* Tue Mar 31 2015 Petr Šabata <contyk@redhat.com> - 0.14-1
- 0.14 bump

* Wed Feb 25 2015 Petr Šabata <contyk@redhat.com> - 0.13-1
- 0.13 bump

* Mon Jan 12 2015 Petr Šabata <contyk@redhat.com> - 0.12-1
- 0.12 bump

* Wed Nov 26 2014 Petr Šabata <contyk@redhat.com> - 0.11-1
- 0.11 bugfix bump

* Thu Oct 16 2014 Petr Šabata <contyk@redhat.com> - 0.10-1
- 0.10 bump

* Wed Oct 08 2014 Petr Šabata <contyk@redhat.com> - 0.06-1
- 0.06 bump, test suite enhancements

* Tue Sep 30 2014 Petr Šabata <contyk@redhat.com> - 0.05-1
- 0.05 bump

* Mon Sep 08 2014 Petr Šabata <contyk@redhat.com> - 0.03-1
- 0.03 bump
- Install the tangerine script

* Sun Sep 07 2014 Petr Šabata <contyk@redhat.com> 0.02-1
- Initial package
