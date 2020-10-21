Name:           perl-Log-ger
Version:        0.037
Release:        3%{?dist}
Summary:        Lightweight, flexible logging framework
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Log-ger
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-ger-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Data::Dmp) >= 0.21
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dmp) >= 0.21

%description
The Log::ger Perl module provides another lightweight, flexible logging
framework.

%prep
%setup -q -n Log-ger-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-2
- Perl 5.32 rebuild

* Wed Mar 11 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-1
- 0.037 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-1
- 0.036 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-1
- 0.034 bump

* Mon Mar 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-1
- 0.033 bump

* Wed Mar 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.031-1
- 0.031 bump

* Tue Feb 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- 0.029 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-2
- Perl 5.30 rebuild

* Tue May 07 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-1
- 0.028 bump

* Mon Apr 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.027-1
- 0.027 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.025-1
- 0.025 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-1
- 0.023 bump

* Wed Aug 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- 0.021 bump

* Wed Jul 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-1
- Initial release
