Name:           perl-Net-Stomp
Version:        0.60
Release:        3%{?dist}
Summary:        Stomp client module for Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-Stomp
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Net-Stomp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(IO::Select)
# Prefer IO::Socket::IP over IO::Socket::INET
# IO::Socket::IP 0.20 not used at tests
BuildRequires:  perl(Log::Any)
# Socket not used at tests
# Optional run-time:
# IO::Socket::SSL 1.75 not used at tests
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::TAP)
BuildRequires:  perl(Log::Any::Adapter::Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NiceDump)
# Optional tests:
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Prefer IO::Socket::IP over IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.20
Requires:       perl(Socket)
# Keep IO::Socket::SSL optional

%description
This module allows you to write a Stomp client. Stomp, the Streaming Text
Orientated Messaging Protocol, is a simple and easy to implement protocol
for working with Message Orientated Middleware.

Net::Stomp can be used to communicate with Apache ActiveMQ, an
enterprise-level Java Message Service 1.1 (JMS) message broker.

%prep
%setup -q -n Net-Stomp-%{version}

# Perl interpreter path
sed -i -e 's~^#!perl~%(perl -MConfig -e 'print $Config{startperl}')~' examples/*.pl

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-1
- 0.60 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-1
- 0.57 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Thu Jun 25 2015 Petr Pisar <ppisar@redhat.com> - 0.55-1
- 0.55 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.45-1
- Update to a later upstream release

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.42-8
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.42-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.42-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.42-1
- apply Jose Pedro Oliviera's patch:
-  Updated to 0.42
-  Examples included as documentation files
-  Source URL updated (different maintainer)

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.36-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.36-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jun 27 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.36-1
- Update to later release

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.34-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.34-2
- Fix description wording (thanks to Manuel Wolfshant)

* Fri Jan 30 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.34-1
- Specfile autogenerated by cpanspec 1.77.
- Fixed BuildRequires
