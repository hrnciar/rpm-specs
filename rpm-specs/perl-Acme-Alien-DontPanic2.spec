Name:           perl-Acme-Alien-DontPanic2
%global cpan_version 2.2901
Version:        2.290.1
Release:        1%{?dist}
Summary:        Test module for Alien::Base + Alien::Build
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Acme-Alien-DontPanic2
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic2-%{cpan_version}.tar.gz
# Full-arch for files storing architecture-specific paths
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Build::MB) >= 0.07
BuildRequires:  perl(alienfile)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(dontpanic)
# Run-time
BuildRequires:  perl(Alien::Base) >= 0.038
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
# Tests
BuildRequires:  perl(Alien::Build) >= 2.29
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline) >= 0.56
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::CPP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien) >= 0.05
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Alien::Base) >= 0.038
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This module is a toy module to test the efficacy of the Alien::Base system.

%prep
%setup -q -n Acme-Alien-DontPanic2-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Acme
%{_mandir}/man3/*

%changelog
* Mon Aug 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.290.1-1
- Specfile autogenerated by cpanspec 1.78.
