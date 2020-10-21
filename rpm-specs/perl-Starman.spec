Name:           perl-Starman
Version:        0.4015
Release:        6%{?dist}
Summary:        High-performance preforking PSGI/Plack web server
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Starman
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Starman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::Server)
BuildRequires:  perl(Net::Server::SS::PreFork)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Server::Starter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Starman is a PSGI perl web server that has unique features such as high
performance, preforking, use of signals and a small memory footprint. It is PSGI
compatible and offers HTTP/1.1 support.

%prep
%setup -q -n Starman-%{version}

%build
%{__perl} Build.PL --installdirs vendor
./Build

%install
./Build install --destdir $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/HTTP
%{perl_vendorlib}/Plack
%{perl_vendorlib}/Starman
%{perl_vendorlib}/Starman.pm
%{_bindir}/starman
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4015-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4015-2
- Perl 5.30 rebuild

* Sun May 26 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4015-1
- Update to 0.4015

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.4014-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.4014-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4014-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.4014-2
- Perl 5.22 rebuild

* Sun Jun 07 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4014-1
- Update to 0.4014

* Sun May 17 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4013-1
- Update to 0.4013

* Sat Nov 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4011-1
- Update to 0.4011
- Use %%license tag

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.4010-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4010-1
- Update to 0.4010

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4009-1
- Update to 0.4009

* Sun Sep 15 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4008-1
- Update to 0.4008

* Sun Aug 18 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4006-1
- Update to 0.4006

* Wed Aug 14 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4004-1
- Update to 0.4004

* Sat Aug 10 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.4003-1
- Update to 0.4003

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.3014-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3014-1
- Update to 0.3014

* Sun Jun 02 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3011-2
- Remove ugly hack for the man page name

* Sun Apr 28 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3011-1
- Update to 0.3011
- Switch to Module::Build::Tiny as building mecanism

* Sun Mar 31 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3007-1
- Update to 0.3007
- Switch to Module::Build as building mecanism

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3006-1
- Update to 0.3006
- Remove the Group macro (no longer used)

* Sun Nov 18 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3005-1
- Update to 0.3005

* Sun Nov 11 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3004-1
- Update to 0.3004

* Sun Sep 30 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.3003-1
- Update to 0.3003

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.3001-2
- Perl 5.16 rebuild

* Tue Jun 26 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.3001-1
- Update to 0.3001

* Tue Feb 21 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.3000-1
- Update to 0.3000
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.2014-1
- Update to 0.2014

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.2013-3
- Perl mass rebuild

* Thu Jul 07 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.2013-2
- Change the files stanza to be more explicit

* Fri Jun 17 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.2013-1
- Specfile autogenerated by cpanspec 1.78.
