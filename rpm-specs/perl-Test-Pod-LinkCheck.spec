Name:           perl-Test-Pod-LinkCheck
Version:        0.008
Release:        23%{?dist}
Summary:        Tests POD for invalid links
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Pod-LinkCheck
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Pod-LinkCheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# ExtUtils::MakeMaker not used
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(App::PodLinkCheck::ParseLinks) >= 4
BuildRequires:  perl(App::PodLinkCheck::ParseSections)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose) >= 1.01
BuildRequires:  perl(Moose::Util::TypeConstraints) >= 1.01
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::Pod) >= 1.44
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
# Optional tests:
# Test::Apocalypse skips all tests as release tests, do not use it. It is also
# in build cycle with this package.
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(App::PodLinkCheck::ParseSections)
Requires:       perl(Capture::Tiny)
Requires:       perl(Config)
Requires:       perl(File::Spec)
Requires:       perl(Pod::Find)

%description
This module looks for any links in your POD and verifies that they point to
a valid resource. It uses the Pod::Simple parser to analyze the pod files
and look at their links. In a nutshell, it looks for L<Foo> links and makes
sure that Foo exists. It also recognizes section links, L</SYNOPSIS> for
example. Also, manual pages are resolved and checked.

%prep
%setup -q -n Test-Pod-LinkCheck-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install "--destdir=$RPM_BUILD_ROOT" --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
./Build test

%files
%license LICENSE
%doc AUTHOR_PLEDGE Changes CommitLog examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-23
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-22
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Petr Pisar <ppisar@redhat.com> - 0.008-20
- Do not build-require optional Test::Apocalypse

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-18
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-17
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-14
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-10
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.22 re-rebuild of bootstrapped packages
- Disable using of Test::Apocalypse with Perl 5.22

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-2
- Perl 5.22 rebuild

* Tue Nov 04 2014 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-11
- Perl 5.20 re-rebuild of bootstrapped packages

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-8
- Perl 5.18 re-rebuild of bootstrapped packages
- Specify all dependencies
- Remove perl_bootstrap definition

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.007-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.007-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.007-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Petr Pisar <ppisar@redhat.com> 0.007-1
- Specfile autogenerated by cpanspec 1.78.
