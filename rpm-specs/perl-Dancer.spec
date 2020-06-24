Name:           perl-Dancer
Version:        1.3513
Release:        2%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dancer
Source0:        http://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Dancer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(HTTP::Body) >= 1.07
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Server::Simple::PSGI) >= 0.11
BuildRequires:  perl(HTTP::Tiny) >= 0.014
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP)
BuildRequires:  perl(MIME::Types) >= 2.17
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time for tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::CookieJar) >= 0.008
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(mro)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(URI::Escape)
# Optional tests:
BuildRequires:  perl(HTTP::Parser::XS)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Dancer::Session::Cookie) >= 0.14
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(HTTP::Body) >= 1.07
Requires:       perl(HTTP::Server::Simple::PSGI) >= 0.11
Requires:       perl(HTTP::Tiny) >= 0.014
Requires:       perl(MIME::Types) >= 2.17
Requires:       perl(Try::Tiny) >= 0.09
Requires:       perl(URI) >= 1.59
Requires:       perl(YAML)

%{?perl_default_filter}

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::Body\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Server::Simple::PSGI\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(MIME::Types\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Try::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(URI\\)\\s*$

%description
Dancer is a web application framework designed to be as effortless as
possible for the developer, taking care of the boring bits as easily as
possible, yet staying out of your way and letting you get on with writing
your code.

%prep
%setup -q -n Dancer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc AUTHORS Changes examples
%{_bindir}/dancer
%{perl_vendorlib}/*
%{_mandir}/man1/dancer.1*
%{_mandir}/man3/*

%changelog
* Thu Mar 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-2
- Add BR: perl(blib)

* Wed Feb 05 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-1
- 1.3513 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3512-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3512-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-2
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-1
- 1.3512 bump

* Wed Mar 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3510-1
- 1.3510 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3500-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3500-1
- 1.3500 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3400-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-1
- 1.3400 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-7
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-1
- 1.3202 bump

* Tue Sep 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3142-1
- 1.3142 bump

* Tue Jul 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3140-1
- 1.3140 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3138-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3138-1
- 1.3138 bump

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-2
- Perl 5.22 rebuild

* Mon May 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-1
- 1.3136 bump

* Thu Apr 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3135-1
- 1.3135 bump

* Mon Feb 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3134-1
- 1.3134 bump

* Tue Oct 21 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3132-1
- 1.3132 bump

* Thu Sep 18 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3130-1
- 1.3130 bump

* Thu Sep 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3129-1
- 1.3129 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-2
- Perl 5.20 rebuild

* Thu Jul 17 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-1
- 1.3126 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3124-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3124-1
- 1.3124 bump

* Mon Apr 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3123-1
- 1.3123 bump

* Thu Feb 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3121-1
- 1.3121 bump

* Thu Jan 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3120-1
- 1.3120 bump

* Tue Oct 29 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3119-1
- 1.3119 bump

* Mon Sep 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3118-1
- 1.3118 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3117-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Thu Aug 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3117-1
- 1.3117 bump

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.3116-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3116-1
- 1.3116 bump

* Mon Jun 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3115-1
- 1.3115 bump

* Tue Jun 04 2013 Petr Pisar <ppisar@redhat.com> - 1.3114-1
- 1.3114 bump

* Mon Jun 03 2013 Petr Pisar <ppisar@redhat.com> - 1.3113-2
- Fix CVE-2012-5572 (cookie name CR-LF injection) (bug #880330)

* Mon May 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3113-1
- 1.3113 bump

* Tue May 07 2013 Petr Pisar <ppisar@redhat.com> - 1.3112-2
- Return proper exit code on dancer tool failure (bug #960184)

* Thu Apr 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3112-1
- 1.3112 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 1.3111-1
- 1.3111 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Petr Šabata <contyk@redhat.com> - 1.3110-1
- 1.3110 bump

* Mon Aug 27 2012 Petr Šabata <contyk@redhat.com> - 1.3100-1
- 1.3100 bump

* Thu Aug 23 2012 Petr Šabata <contyk@redhat.com> - 1.3099-1
- 1.3099 bump

* Mon Jul 30 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.3098-1
- 1.3098 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3097-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.3097-1
- 1.3097 bump

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.3095-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 1.3095-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.3095-1
- 1.3095 bump
- 810865 bootstrap macro for test only BR

* Thu Mar 01 2012 Petr Šabata <contyk@redhat.com> - 1.3093-1
- 1.3093 bump

* Mon Jan 30 2012 Petr Šabata <contyk@redhat.com> - 1.3092-1
- 1.3092 bump
- Package examples

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3091-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 03 2012 Petr Pisar <ppisar@redhat.com> - 1.3091-2
- Enable optional tests requiring perl(Dancer::Session::Cookie).

* Mon Dec 19 2011 Petr Pisar <ppisar@redhat.com> - 1.3091-1
- 1.3091 bump

* Wed Dec 14 2011 Petr Šabata <contyk@redhat.com> - 1.3090-1
- 1.3090 bump

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3080-1
- 1.3080 bump

* Wed Aug 24 2011 Petr Sabata <contyk@redhat.com> - 1.3072-1
- 1.3072 bump

* Wed Aug 10 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3071-1
- update
- add filter for RPM 4.8

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.3040-3
- Perl mass rebuild

* Mon May 16 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3040-2
- add tests BR: CGI, YAML, Template, Clone

* Fri May 13 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3040-1
- Specfile autogenerated by cpanspec 1.79.
