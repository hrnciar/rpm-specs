Name:           perl-XML-Atom
Version:        0.42
Release:        13%{?dist}
Summary:        Atom feed and API implementation
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/XML-Atom
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-%{version}.tar.gz
# enable unicode tests (we have LibXML)
Patch0:         enable-unicode-tests.patch
Patch1:         XML-Atom-0.42-Fix-building-on-Perl-without-dot-in-INC.patch
# Tests failed with XML-LibXML-2.0202 due to disable loading external DTDs
# or external entities by default
Patch2:         XML-Atom-0.42-Fix-test-with-XML-LibXML-2.0202.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
# Run-time:
# Apache::Constants not used at tests
BuildRequires:  perl(base)
# CGI not used at tests
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# HTML::Parser not used at tests
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.69
# XML::XPath not needed if XML::LibXML is available
# Optional run-time:
# DateTime::Format::Atom not used
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser)
# Optional tests:
# DateTime::Format::Atom not yet packaged
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not automatically detected
Requires:       perl(HTML::Parser)
Requires:       perl(XML::LibXML) >= 1.69

%{?perl_default_filter}

%description
Atom is a syndication, API, and archiving format for web blogs and other
data. XML::Atom implements the feed format as well as a client for the API.

%package Server
Summary:        Server for the Atom API
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Apache::Constants)
Requires:       perl(CGI)

%description Server
XML::Atom::Server Perl module provides a base class for Atom API servers. It
handles all core server processing, both the SOAP and REST formats of the
protocol, and WSSE authentication. It can also run as either a mod_perl
handler or as part of a CGI program.


%prep
%setup -q -n XML-Atom-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%exclude %{perl_vendorlib}/XML/Atom/Server.pm
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/XML::Atom::Server.3*

%files Server
%doc Changes README
%{perl_vendorlib}/XML/Atom/Server.pm
%{_mandir}/man3/XML::Atom::Server.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-11
- Fixed tests for XML-LibXML-2.0202

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-3
- Perl 5.26 rebuild

* Tue May 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-2
- Fix building on Perl without '.' in @INC

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-1
- Update to 0.42
- Switch to Module::Build::Tiny workflow
- Drop backported patch from upstream

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-17
- Remove deprecated pragma encoding

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-15
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.41-13
- Remove Group declaration (no longer used)
- Pass NO_PACKLIST=1 when creating the Makefile

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-11
- Perl 5.22 rebuild

* Tue Dec 02 2014 Petr Pisar <ppisar@redhat.com> - 0.41-10
- Specify all dependencies (bug #1169791)
- Sub-package XML::Atom::Server because it requires Apache

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.41-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.41-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Iain Arnell <iarnell@gmail.com> 0.41-1
- update to latest upstream version

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.39-3
- Perl mass rebuild

* Sat Jun 25 2011 Iain Arnell <iarnell@gmail.com> 0.39-2
- restore doc files

* Sat Jun 25 2011 Iain Arnell <iarnell@gmail.com> 0.39-1
- update to latest upstream version
- use perl_default_filter

* Wed May 25 2011 Iain Arnell <iarnell@gmail.com> 0.38-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-2
- Mass rebuild with perl-5.12.0

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.37-1
- update to latest upstream version
- BR/R perl(XML::XPath)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.35-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Iain Arnell 0.35-1
- Specfile autogenerated by cpanspec 1.77.
