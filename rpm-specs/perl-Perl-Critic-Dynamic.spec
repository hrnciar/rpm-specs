Name:           perl-Perl-Critic-Dynamic
Version:        0.05
Release:        24%{?dist}
Summary:        Non-static policies for Perl::Critic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-Critic-Dynamic
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Perl-Critic-Dynamic-%{version}.tar.gz
# Adapt to changes in CGI-4.14, bug #1209554, CPAN RT#103382
Patch0:         Perl-Critic-Dynamic-0.05-test_AUTOLOAD_on_private_module.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.36
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Symdump) >= 2.07
BuildRequires:  perl(English)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.108
BuildRequires:  perl(Perl::Critic::Utils) >= 1.108
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Storable) >= 2.16
# Tests only:
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic::Policy)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Devel::Symdump) >= 2.07
Requires:       perl(Perl::Critic::Policy) >= 1.108
Requires:       perl(Perl::Critic::Utils) >= 1.108
Requires:       perl(Storable) >= 2.16

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Symdump\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Perl::Critic::(Policy|Utils)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)$

%description
Perl::Critic is primarily used as a static source code analyzer, which means
that it never compiles or executes any of the code that it examines. But
since Perl is a dynamic language, there are certain types of problems that
cannot be discovered until the code is actually compiled.

This distribution includes Perl::Critic::DynamicPolicy, which can be used as
a base class for Policies that wish to compile the code they analyze. 

%prep
%setup -q -n Perl-Critic-Dynamic-%{version}
%patch0 -p0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-24
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-21
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-18
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-10
- Perl 5.22 rebuild

* Wed Apr 08 2015 Petr Pisar <ppisar@redhat.com> - 0.05-9
- Adapt tests to changes in CGI-4.14 (bug #1209554)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 0.05-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.05-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
