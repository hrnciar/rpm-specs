Name:           perl-Test2-Plugin-MemUsage
%global cpan_version 0.002003
Version:        0.2.3
Release:        3%{?dist}
Summary:        Test2 plugin that collects and displays memory usage information
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Plugin-MemUsage
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-MemUsage-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Test2::API) >= 1.302165
# Tests:
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Defer)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test2::API) >= 1.302165
# Removed from perl-Test2-Harness-0.001083
Conflicts:      perl-Test2-Harness < 0.001083

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test2::API\\)$

%description
This Test2 plugin will collect memory usage information from /proc/PID/status
and display it for you when the test is done running.

%prep
%setup -q -n Test2-Plugin-MemUsage-%{cpan_version}

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.3-2
- Perl 5.32 rebuild

* Thu Feb 27 2020 Petr Pisar <ppisar@redhat.com> - 0.2.3-1
- 0.002003 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Petr Pisar <ppisar@redhat.com> - 0.2.2-1
- 0.002002 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> 0.2.1-1
- Specfile autogenerated by cpanspec 1.78.
