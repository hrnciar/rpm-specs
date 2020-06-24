Name:           perl-Shell-Config-Generate
Version:        0.34
Release:        2%{?dist}
Summary:        Portably generate configuration for any shell
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Shell-Config-Generate
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Shell-Config-Generate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Shell::Guess) >= 0.02
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
# IPC::Open3 not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Mock) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Shell::Guess) >= 0.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Shell::Guess\\)$

%description
This Perl module provides an interface for specifying shell configurations for
different shell environments without having to worry about the arcane
differences between shells such as csh, sh, cmd.exe and command.com.

%prep
%setup -q -n Shell-Config-Generate-%{version}

%build
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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.32 rebuild

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-1
- 0.31 bump

* Mon Sep 04 2017 Petr Pisar <ppisar@redhat.com> - 0.29-1
- 0.29 bump

* Thu Aug 24 2017 Petr Pisar <ppisar@redhat.com> - 0.28-1
- 0.28 bump

* Fri Jul 21 2017 Petr Pisar <ppisar@redhat.com> 0.26-1
- Specfile autogenerated by cpanspec 1.78.