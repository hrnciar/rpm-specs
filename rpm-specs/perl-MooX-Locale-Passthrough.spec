Name:           perl-MooX-Locale-Passthrough
Version:        0.001
Release:        11%{?dist}
Summary:        Provide API used in translator modules without translating
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooX-Locale-Passthrough
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Locale-Passthrough-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moo::Role)
# Tests
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Test::More) >= 0.90
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# 1.003 from Moo in META.json which is not used
Requires:       perl(Moo::Role) >= 1.003

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)$

%description
MooX::Locale::Passthrough is made to allow CPAN modules use translator API
without adding heavy dependencies (external software) or requirements
(operating resulting solution).

%prep
%setup -q -n MooX-Locale-Passthrough-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-1
- Initial release
