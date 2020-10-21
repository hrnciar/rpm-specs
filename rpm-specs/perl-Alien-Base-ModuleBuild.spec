# Run optional tests
%bcond_without perl_Alien_Base_ModuleBuild_enables_optional_test
# Enable SSL support
%bcond_without perl_Alien_Base_ModuleBuild_enables_ssl

Name:           perl-Alien-Base-ModuleBuild
Version:        1.15
Release:        1%{?dist}
Summary:        Perl framework for building Alien:: modules and their libraries
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-Base-ModuleBuild
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Base-ModuleBuild-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>
# Run-time:
# Alien::Base in lib/Alien/Base/ModuleBuild.pm is optional
BuildRequires:  perl(Alien::Base::PkgConfig) >= 1.20
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir) >= 0.1005
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Tiny) >= 0.044
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny) >= 0.077
# PkgConfig not used if pkg-config tool is available
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Shell::Config::Generate)
BuildRequires:  perl(Shell::Guess)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::ParseWords) >= 3.26
BuildRequires:  perl(URI)
# Optional run-time:
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTML::LinkExtor)
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
# IO::Socket::SSL 1.56 not used at tests
# Net::SSLeay 1.49 not used at tests
%endif
# Tests:
# bash for /bin/sh
BuildRequires:  bash
BuildRequires:  perl(base)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(URI::file)
%if %{with perl_Alien_Base_ModuleBuild_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: Acme::Alien::DontPanic → Alien::Base::ModuleBuild
BuildRequires:  perl(Acme::Alien::DontPanic) >= 0.010
BuildRequires:  perl(Acme::Alien::DontPanic2)
%endif
BuildRequires:  perl(LWP::UserAgent)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Alien::Base::PkgConfig) >= 1.20
Recommends:     perl(Digest::SHA)
Requires:       perl(File::chdir) >= 0.1005
Requires:       perl(File::Find)
Requires:       perl(File::ShareDir) >= 1.00
Recommends:     perl(HTML::LinkExtor)
Requires:       perl(HTTP::Tiny) >= 0.044
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Module::Build) >= 0.4004
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Text::ParseWords) >= 3.26
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
Requires:       perl(IO::Socket::SSL) >= 1.56
Requires:       perl(Net::SSLeay) >= 1.49
%endif
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base::PkgConfig|File::chdir|HTTP::Tiny|List::Util|Module::Build|Path::Tiny|Text::ParseWords)\\)

%description
This is a Perl base class and framework for creating Alien distributions. The
goal of the project is to make things as simple and easy as possible for both
developers and users of Alien modules.

Alien is a Perl name space for defining dependencies in CPAN for libraries and
tools which are not "native" to CPAN. Alien modules will typically use the
system libraries if they are available, or download the latest version from
the internet and build them from source code. These libraries can then be
used by other Perl modules, usually modules that are implemented with XS or FFI.

%prep
%setup -q -n Alien-Base-ModuleBuild-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset ALIEN_FORCE ALIEN_INSTALL_TYPE
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Sep 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-1
- 1.15 bump

* Thu Aug 27 2020 Petr Pisar <ppisar@redhat.com> - 1.14-6
- Fix an external declaration in the tests

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-2
- Perl 5.32 rebuild

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump

* Fri Jan 31 2020 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Mon Nov 25 2019 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Tue Sep 04 2018 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.04-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.04-2
- Perl 5.28 rebuild

* Tue Jun 12 2018 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Mon May 14 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Fri May 04 2018 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Petr Pisar <ppisar@redhat.com> - 1.00-1
- 1.00 bump

* Tue Sep 19 2017 Petr Pisar <ppisar@redhat.com> - 0.046-1
- 0.046 bump

* Fri Sep 08 2017 Petr Pisar <ppisar@redhat.com> - 0.045-1
- 0.045 bump

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 0.044-2
- Enable SSL support by default

* Mon Aug 28 2017 Petr Pisar <ppisar@redhat.com> - 0.044-1
- 0.044 bump

* Fri Aug  4 2017 Petr Pisar <ppisar@redhat.com> 0.042-1
- Specfile autogenerated by cpanspec 1.78.
