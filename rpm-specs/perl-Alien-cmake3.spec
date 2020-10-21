Name:           perl-Alien-cmake3
Version:        0.05
Release:        4%{?dist}
Summary:        Find or download or build cmake 3 or better
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-cmake3
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-cmake3-%{version}.tar.gz
# This is an Alien::Build plugin, it stores data about architecture specific
# files, therefore this an architecture specific package, yet there is no XS
# code, so debuginfo generation and dependency on perl-devel is disabled.
%global debug_package %{nil}
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(alienfile)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  cmake >= 3.0.0
BuildRequires:  perl(Alien::Base) >= 0.92
BuildRequires:  perl(base)
# Tests:
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien) >= 0.92
Requires:       cmake >= 3.0.0
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Alien::Base) >= 0.92

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This Perl Alien distribution provides an external dependency on the build tool
cmake version 3.0.0 or better.

%prep
%setup -q -n Alien-cmake3-%{version}

%build
unset ALIEN_CMAKE_FROM_SOURCE
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
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Alien*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump

* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 0.03-1
- Specfile autogenerated by cpanspec 1.78.
