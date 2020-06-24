Name:           perl-Acme-Alien-DontPanic
%global cpan_version 2.1100
Version:        2.110.0
Release:        2%{?dist}
Summary:        Test module for Alien::Base
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Acme-Alien-DontPanic
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic-%{cpan_version}.tar.gz
# Remove useless dependencies,
# <https://github.com/Perl5-Alien/Acme-Alien-DontPanic/issues/3>
Patch0:         Acme-Alien-DontPanic-2.0400-Remove-a-dependency-on-lib.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Base::ModuleBuild) >= 1.14
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Use system dontpanic library instead of downloading it from the Internet at
# build time (it's forbidden in the build system).
BuildRequires:  pkgconfig(dontpanic)
# Dependecies for generated Build script
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
# Run-time:
BuildRequires:  perl(Alien::Base) >= 2.04
BuildRequires:  perl(base)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(Test::Alien) >= 0.05
BuildRequires:  perl(Test::Alien::Diag)
# Optional tests:
# Test::More not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Alien::Base) >= 2.04
# Generated code:
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Build)
# The maning of the package is to dontpanic library is installed and
# application can build against it. Because we use system dontpanic library
# instead of bundling that one that had been dowloaded and compiled at build
# time, we nee to explicitly run-require developmental files of the library.
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This Perl module is a toy module to test the efficacy of the Alien::Base system.

%prep
%setup -q -n Acme-Alien-DontPanic-%{cpan_version}
%patch0 -p1

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.110.0-2
- Perl 5.32 rebuild

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 2.110.0-1
- 2.1100 bump

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 2.40.0-1
- 2.0400 bump

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 2-1
- 2.0000 bump

* Fri Jan 31 2020 Petr Pisar <ppisar@redhat.com> - 1.98.00-1
- 1.9800 bump

* Wed Jan 29 2020 Petr Pisar <ppisar@redhat.com> - 1.96-1
- 1.96 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue May 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.044-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Petr Pisar <ppisar@redhat.com> 0.044-1
- Specfile autogenerated by cpanspec 1.78.
