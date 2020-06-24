Name:           perl-Test-Deep-Fuzzy
Version:        0.01
Release:        5%{?dist}
Summary:        Fuzzy number comparison with Test::Deep
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Deep-Fuzzy
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARUPA/Test-Deep-Fuzzy-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(B)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Math::Round)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Cmp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::Deep::Fuzzy provides fuzzy number comparison with Test::Deep.

%prep
%setup -q -n Test-Deep-Fuzzy-%{version}

%build
perl ./Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Yanko Kaneti <yaneti@declera.com> - 0.01-3
- Incorporate some more review feedback

* Fri Sep 27 2019 Yanko Kaneti <yaneti@declera.com> - 0.01-2
- Incorporate review feedback

* Thu Sep 26 2019 Yanko Kaneti <yaneti@declera.com> - 0.01-1
- Specfile autogenerated by cpanspec 1.78.
