Name:           perl-JSON-Color
Version:        0.130
Release:        3%{?dist}
Summary:        Encode to colored JSON
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/JSON-Color/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/JSON-Color-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Color::ANSI::Util)
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Graphics::ColorNamesLite::WWW)
BuildRequires:  perl(Module::Load::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Role::Tiny)
# Not used for tests - Scalar::Util::LooksLikeNumber
BuildRequires:  perl(Term::ANSIColor) >= 3.00
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(ColorThemeRole::ANSI)
Requires:       perl(Module::Load::Util)
Requires:       perl(Role::Tiny)
Requires:       perl(Term::ANSIColor) >= 3.00
Recommends:     perl(Scalar::Util::LooksLikeNumber)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Term::ANSIColor)\\)\s*$

%description
This module generates JSON, colorized with ANSI escape sequences.

%prep
%setup -q -n JSON-Color-%{version}

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.130-2
- Specify all dependencies

* Fri Jul 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.130-1
- 0.130 bump

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-7
- Perl 5.32 rebuild

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 0.12-6
- Build-require blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- Specfile autogenerated by cpanspec 1.78.
