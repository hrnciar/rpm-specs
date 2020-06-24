Name:           perl-Apache-Reload
Version:        0.13
Release:        14%{?dist}
Summary:        Reload changed Perl modules
License:        ASL 2.0
URL:            https://metacpan.org/release/Apache-Reload
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/Apache-Reload-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Apache::Reload from ./lib is loaded
BuildRequires:  perl(Config)
# ExtUtils::MakeMaker not used because we build for mod_perl-2 only
# File::Spec not used because we build for mod_perl-2 only
BuildRequires:  perl(lib)
# mod_perl not used
BuildRequires:  perl(mod_perl2) >= 1.99022
BuildRequires:  perl(ModPerl::MM)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Apache2::Connection)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(ModPerl::Util)
BuildRequires:  perl(warnings)
# Tests:
# All tests will be skipped if Apache::Test 1.34, etc. or Test::More is not
# availabe.
# Apache::Constants not used
BuildRequires:  perl(Apache::Test) >= 1.34
BuildRequires:  perl(Apache::TestMM)
BuildRequires:  perl(Apache::TestRunPerl)
BuildRequires:  perl(Apache::TestRequest)
BuildRequires:  perl(Apache::TestUtil)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# The mod_perl2 1.99022 is not used, pick for example ModPerl::Util to
# constrain the version.
Requires:       perl(ModPerl::Util) >= 1.99022
Conflicts:      mod_perl < 2.0.10-4

# Fiter-underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ModPerl::Util\\)$

%description
This mod_perl extension allows to reload Perl modules that changed on the disk.

%prep
%setup -q -n Apache-Reload-%{version}

%build
# MOD_PERL_2_BUILD=1 requires MP_APXS variable set to the apxs executable.
# Use MOD_PERL=2 argument instead.
unset MOD_PERL_2_BUILD
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 MOD_PERL=2
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# RELEASE is not for users
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Petr Pisar <ppisar@redhat.com> 0.13-5
- This package replaces code bundled to mod_perl
