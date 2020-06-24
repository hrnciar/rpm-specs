Name:           perl-Catalyst-Plugin-Session-State-Cookie
Summary:        Maintain session IDs using cookies
Version:        0.17
Release:        30%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Catalyst-Plugin-Session-State-Cookie-%{version}.tar.gz 
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-State-Cookie
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# perl-podlators for pod2text is not used
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
# This is a Catalyst plugin
BuildRequires:  perl(Catalyst) >= 5.80005
# This is a Catalyst::Plugin::Session extension
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::autoclean)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst) >= 0.40
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# This is a Catalyst plugin
Requires:       perl(Catalyst) >= 5.80005
# This is a Catalyst::Plugin::Session extension
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Plugin::Session::State)


%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
In order for Catalyst::Plugin::Session to work the session ID needs to
be stored on the client, and the session data needs to be stored on
the server.  This plugin provides a way to store the session ID on the
client, through a cookie.

%prep
%setup -q -n Catalyst-Plugin-Session-State-Cookie-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\\/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-28
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-25
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-22
- Perl 5.26 rebuild

* Thu May 25 2017 Petr Pisar <ppisar@redhat.com> - 0.17-21
- Fix building on Perl without "." in @INC (CPAN RT#121882)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-19
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-16
- Perl 5.22 rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.17-13
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 0.17-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.17-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.17-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.17-4
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.17-3
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- dropped old BR on perl(Test::Pod::Coverage)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.17-2
- rebuild against perl 5.10.1

* Sun Dec 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- auto-update to 0.17 (by cpan-spec-update 0.01)
- altered br on perl(Catalyst::Plugin::Session) (0.19 => 0.27)
- altered req on perl(Catalyst::Plugin::Session) (0.19 => 0.27)

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.14-1
- switch req/prov filtering systems...
- auto-update to 0.14 (by cpan-spec-update 0.01)
- added a new br on perl(Moose) (version 0)
- added a new br on perl(namespace::autoclean) (version 0)
- added a new req on perl(Moose) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)

* Sat Aug 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.12-1
- auto-update to 0.12 (by cpan-spec-update 0.01)
- altered br on perl(Catalyst) (5.7010 => 5.80005)
- added a new req on perl(Catalyst) (version 5.80005)
- added a new req on perl(MRO::Compat) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.11-2
- add br on CPAN

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- auto-update to 0.11 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Catalyst) (version 5.7010)
- altered br on perl(Test::MockObject) (0 => 1.01)

* Mon Mar 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10-1
- update to 0.10

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.09-2
- bump

* Thu May 29 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- Specfile autogenerated by cpanspec 1.74.
