Name:           perl-Inline-C
Version:        0.81
Release:        6%{?dist}
Summary:        Write Perl subroutines in C
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Inline-C
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/Inline-C-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(Inline) >= 0.83
# Inline::Filters and Inline::Struct are optional and introduce circular deps
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
# t/27inline_maker.t uses example/modules/Boo-2.01 that uses Inline::MakeMaker
# that generated Makefile.PL with "perl -Mblib".
BuildRequires:  perl(blib)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Inline::MakeMaker)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(YAML::XS)
# It executes C compiler to build generated XS code
Requires:       gcc
# It executes make
Requires:       make
# It executes "perl Makefile.PL"
Requires:       perl-interpreter
# It requires Perl header files in the generated and compiled XS code
Requires:       perl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Fcntl)
Requires:       perl(FindBin)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Inline) >= 0.83
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Time::HiRes)
# Split from Inline in 0.58
Conflicts:      perl-Inline < 0.58

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
Inline::C is a module that allows you to write Perl subroutines in C. Since
version 0.30 the Inline module supports multiple programming languages and
each language has its own support module.

%prep
%setup -q -n Inline-C-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset ACTIVEPERL_CONFIG_SILENT AUTHOR_TESTING CPATH DEBUG INCLUDE MAKEFLAGS \
    PERL_INLINE_BUILD_NOISY PERL_INLINE_DEVELOPER_TEST PERL_INSTALL_ROOT \
    PERL_PEGEX_AUTO_COMPILE NO_INSANE_DIRNAMES
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/auto/*
%{perl_vendorlib}/Inline/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-6
- Perl 5.32 rebuild

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 0.81-5
- Build-require Inline::MakeMaker and blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-2
- Perl 5.30 rebuild

* Mon May 13 2019 Petr Pisar <ppisar@redhat.com> - 0.81-1
- 0.81 bump

* Tue Apr 30 2019 Petr Pisar <ppisar@redhat.com> - 0.80-2
- Adjust a test to changes in Inline-C-0.82_001

* Thu Apr 18 2019 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-7
- Perl 5.28 rebuild

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 0.78-6
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.78-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-2
- Perl 5.26 rebuild

* Wed May 31 2017 Petr Pisar <ppisar@redhat.com> - 0.78-1
- 0.78 bump

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 0.77-1
- 0.77 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-4
- Perl 5.24 rebuild

* Wed Apr 20 2016 Petr Pisar <ppisar@redhat.com> - 0.76-3
- Require packages needed for building XS code

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr Šabata <contyk@redhat.com> - 0.76-1
- 0.76 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-2
- Perl 5.22 rebuild

* Wed Mar 18 2015 Petr Šabata <contyk@redhat.com> - 0.75-1
- 0.75 bump, documentation fixes

* Wed Feb 18 2015 Petr Šabata <contyk@redhat.com> - 0.74-1
- 0.74 bump, Win32 fixes only

* Thu Jan 08 2015 Petr Šabata <contyk@redhat.com> - 0.73-1
- 0.73 bump

* Wed Nov 26 2014 Petr Šabata <contyk@redhat.com> - 0.67-1
- 0.67 bump

* Wed Nov 05 2014 Petr Šabata <contyk@redhat.com> - 0.64-2
- Backport "PERL IN SPACE" changes from ETJ's 0.65,
  fixing FTBFS with EE::UU 7.00 (#1158390)

* Mon Sep 29 2014 Petr Šabata <contyk@redhat.com> - 0.64-1
- 0.64 bump, include Cookbook.pod again

* Fri Sep 19 2014 Petr Šabata <contyk@redhat.com> - 0.62-1
- 0.62 bump, test suite and documentation changes

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-2
- Perl 5.20 rebuild

* Wed Jul 16 2014 Petr Šabata <contyk@redhat.com> 0.60-1
- Initial packaging
