# Perform author and release tests
%bcond_with perl_POE_Component_SSLify_enables_extra_test

Name:           perl-POE-Component-SSLify
Version:        1.012
Release:        21%{?dist}
Summary:        Makes using SSL in the world of POE easy!
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/POE-Component-SSLify
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz
# Do not use SSLv3 in tests. It's not supported by Net-SSLeay-1.68 with
# OpenSSL-1.0.2a, bug #1222521, CPAN RT#104493
Patch0:         POE-Component-SSLify-1.012-Use-default-SSL-version-in-tests.patch
# Work around a SIGPIPE bug in TLSv1.3 server, bug #1622999, CPAN RT#126976
Patch1:         POE-Component-SSLify-1.012-Disable-sessions-tickets-with-OpenSSL-1.1.1.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Handle) >= 1.28
BuildRequires:  perl(Net::SSLeay) >= 1.36
BuildRequires:  perl(parent)
BuildRequires:  perl(POE) >= 1.267
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Task::Weaken) >= 1.03
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE::Component::Client::TCP)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 1.001002
%if %{with perl_POE_Component_SSLify_enables_extra_test}
# Extra tests
BuildRequires:  perl(POE::Filter::Stream)
# Optional tests:
# CPAN::Meta not usefull
BuildRequires:  perl(IO::Prompt::Tiny)
BuildRequires:  perl(Test::Apocalypse) >= 1.000
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(POE) >= 1.267
Requires:       perl(warnings)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$

%description
This component represents the standard way to do SSL in POE.

%prep
%setup -q -n POE-Component-SSLify-%{version}
%patch0 -p1
%patch1 -p1
%if !%{with perl_POE_Component_SSLify_enables_extra_test}
rm t/99_mire_test.t t/apocalypse.t t/simple_parallel_superbig.t t/simple_superbig.t
perl -i -ne 'print $_ unless m{^\Qt/99_mire_test.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/apocalypse.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_parallel_superbig.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_superbig.t\E}' MANIFEST
%endif

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
# Clean debuginfo generator pollution breaking MANIFEST test
rm -f *.list
# AUTOMATED_TESTING triggers author tests (t/simple_parallel_superbig.t) which
# fails. Upstream says: "thus is marked as TODO." CPAN RT#100549.
%if %{with perl_POE_Component_SSLify_enables_extra_test}
export AUTOMATED_TESTING=1
%else
export AUTOMATED_TESTING=0
%endif
./Build test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-20
- Perl 5.32 rebuild

* Thu Apr 09 2020 Petr Pisar <ppisar@redhat.com> - 1.012-19
- Build-require blib for the tests
- Remove dependencies for author tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Petr Pisar <ppisar@redhat.com> - 1.012-14
- Work around a SIGPIPE bug in TLSv1.3 server (bug #1622999)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-4
- Perl 5.22 rebuild

* Tue Jun 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-3
- Disable using of Test::Apocalypse

* Mon May 18 2015 Petr Pisar <ppisar@redhat.com> - 1.012-2
- Do not use SSLv3 in tests

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 1.012-1
- 1.012 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.008-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.008-4
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 1.008-3
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Iain Arnell <iarnell@gmail.com> 1.008-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.15-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.15-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- auto-update to 0.15 (by cpan-spec-update 0.01)
- altered br on perl(Net::SSLeay) (1.17 => 1.30)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.14-1
- update to 0.14

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.08-2
- rebuild for new perl

* Fri Jun 01 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- update to 0.08

* Sun May 06 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- update to 0.07
- add t/ to %%doc
- some spec rework due to perl splittage

* Mon Sep 18 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- update to 0.06

* Sun Sep 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- update to 0.05
- add Changes
- minor spec cleanups...

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.04-3
- bump for mass rebuild

* Fri Aug 11 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.04-2
- bump for build

* Tue Jul 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
