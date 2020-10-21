Name:           perl-ColorThemeUtil-ANSI
Version:        0.001
Release:        2%{?dist}
Summary:        Utility routines related to color themes and ANSI code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ColorThemeUtil-ANSI/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/ColorThemeUtil-ANSI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Color::ANSI::Util) >= 0.161
BuildRequires:  perl(Exporter) >= 5.57
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Color::ANSI::Util) >= 0.161
Requires:       perl(Exporter) >= 5.57
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Exporter\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Color::ANSI::Util\\)\\s*$

%description
This module provides utility routines related to color themes and ANSI
code.

%prep
%setup -q -n ColorThemeUtil-ANSI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jitka Plesnikova <jplesnik@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
