# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName String-Interpolate-Named

Name: perl-%{FullName}
Summary: Interpolated named arguments in string
License: GPL+ or Artistic
Version: 1.00
Release: 3%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1
Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
String::Interpolate::Named provides a single function, interpolate,
that takes a string and substitutes named variables by target texts.

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.32 rebuild

* Fri Feb 28 2020 Johan Vromans <jvromans@squirrel.nl> - 1.00-1
- Initial Fedora package.
