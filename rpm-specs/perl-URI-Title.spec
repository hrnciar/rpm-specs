Name:           perl-URI-Title
Version:        1.902
Release:        4%{?dist}
Summary:        Get the titles of things on the web in a sensible way
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/URI-Title
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/URI-Title-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type) >= 0.22
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Pluggable) >= 1.2
BuildRequires:  perl(MP3::Info)
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
# Needed for Twitter in live tests
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Encode)
Requires:       perl(File::Type) >= 0.22
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Module::Pluggable) >= 1.2

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Type\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Pluggable\\)$

%description
I keep having to find the title of things on the web.  This seems like a really
simple request, just get() the object, parse for a title tag, you're done.
Ha, I wish.  There are several problems with this approach:

What if the resource is on a very slow server?  Do we wait forever or what?
What if the resource is a 900 gig file?  You don't want to download that.
What if the page title isn't in a title tag, but is buried in the HTML
somewhere?
What if the resource is an MP3 file, or a word document or something?
...

So, let's solve these issues once.

%prep
%setup -q -n URI-Title-%{version}

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
%doc Changes README eg/title.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.902-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.902-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.902-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.902-1
- 1.902 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.901-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.901-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.901-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.901-1
- 1.901 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.900-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.900-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.900-2
- Perl 5.22 rebuild

* Fri Jan 02 2015 Petr Šabata <contyk@redhat.com> - 1.900-1
- 1.900 bump

* Thu Sep 18 2014 Petr Šabata <contyk@redhat.com> - 1.89-1
- 1.89 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.88-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Petr Šabata <contyk@redhat.com> - 1.88-1
- 1.88 bugfix bump

* Tue Jan 28 2014 Petr Šabata <contyk@redhat.com> - 1.86-7
- Fix the live test failures (#1058734, rt#92091)
- Minor spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.86-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.86-2
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Šabata <contyk@redhat.com> - 1.86-1
- 1.86 bump
- Drop command macros

* Fri Jan 20 2012 Petr Šabata <contyk@redhat.com> - 1.85-1
- Specfile autogenerated by cpanspec 1.78.
