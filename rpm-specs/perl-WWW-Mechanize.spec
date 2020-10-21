Name:           perl-WWW-Mechanize
Version:        2.02
Release:        1%{?dist}
Summary:        Automates web page form & link interaction
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WWW-Mechanize
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))
# HTML::Status is not used anymore probably
#Requires:       perl(HTTP::Status)
# LWP is not run-time dependecy probably
#Requires:       perl(LWP) >= 5.829
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Form) >= 1.038
BuildRequires:  perl(HTML::HeadParser)
# HTML::Parser is not used anymore probably
#BuildRequires:  perl(HTML::Parser) >= 3.33
BuildRequires:  perl(HTML::TreeBuilder)
# HTML::Status is not used anymore probably
#BuildRequires:  perl(HTTP::Status)
# HTML::HeadParser optional
BuildRequires:  perl(HTML::TokeParser) >= 2.28
BuildRequires:  perl(HTTP::Daemon) >= 6.05
BuildRequires:  perl(HTTP::Request) >= 1.3
# HTTP::Response::Encoding is not used anymore probably
BuildRequires:  perl(HTTP::Response::Encoding) >= 0.05
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP) >= 6.45
BuildRequires:  perl(LWP::UserAgent) >= 6.45
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(Test::More) >= 0.34
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(warnings)
# For %%check only:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
# HTTP::Server::Simple is not used anymore probably
BuildRequires:  perl(HTTP::Server::Simple) >= 0.35
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI) >= 1.36
BuildRequires:  perl(URI::Escape)
# $mech->content( format => 'text' ) requires HTML::TreeBuilder to be installed
# https://metacpan.org/pod/WWW::Mechanize#$mech-%3Econtent(...)
Requires:       perl(HTML::TreeBuilder)

%description
"WWW::Mechanize", or Mech for short, helps you automate interaction
with a website.  It supports performing a sequence of page fetches
including following links and submitting forms. Each fetched page is
parsed and its links and forms are extracted. A link or a form can be
selected, form fields can be filled and the next page can be fetched.
Mech also stores a history of the URLs you've visited, which can be
queried and revisited.

%prep
%setup -q -n WWW-Mechanize-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test TEST_VERBOSE=1

%files
%doc Changes etc/www-mechanize-logo.png
%{_bindir}/mech-dump
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*

%changelog
* Sun Oct 18 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.02-1
- Update to 2.02

* Sun Sep 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.01-1
- Update to 2.01

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-2
- Perl 5.32 rebuild

* Sun Jun 14 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.00-1
- Update to 2.00

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.97-1
- Update to 1.97

* Fri Mar 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-2
- Specify all dependencies
- Remove switches for live/local tests, they are not used since 1.78

* Sun Feb 23 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.96-1
- Update to 1.96

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.95-1
- Update to 1.95

* Sun Oct 13 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.94-1
- Update to 1.94

* Sun Oct 06 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.93-1
- Upate to 1.93

* Sun Sep 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.92-1
- Update to 1.92
- Replace calls to %%{__perl} with /usr/bin/perl
- Pass NO_PERLLOCAL=1 to Makefile.PL
- Replace calls to "make pure_install" with %%{make_install}
- Replace calls to "make" with %%{make_build}
- Remove patch (no longer needed)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.91-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.91-1
- Update to 1.91

* Sun Nov 18 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.90-1
- Update to 1.90

* Sun Oct 21 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.89-1
- Update to 1.89

* Thu Aug 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.88-4
- Add perl(HTML::TreeBuilder) as a Requires (#1613504)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.88-2
- Perl 5.28 rebuild

* Sun Mar 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.88-1
- Update to 1.88

* Thu Feb 08 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.87-1
- Update to 1.87

* Sun Aug 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.86-1
- Update to 1.86
- Drop upstreamed patch
- Add patch to use localhost instead of 127.0.0.1 in tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-3
- Perl 5.26 rebuild

* Sun May 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.84-2
- Backport ppisar's patch from upstream to fix build failures (#1444442)

* Thu Mar 09 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.84-1
- Update to 1.84

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.83-1
- Update to 1.83

* Sun Oct 09 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.82-1
- Update to 1.82
- Drop the Group tag

* Sun Oct 02 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.80-1
- Update to 1.80

* Sun Sep 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.79-1
- Update to 1.79
- Pass NO_PACKLIST to Makefile.PL
- Remove UTF-8 transformation since Changes is already in UTF-8

* Sun Aug 14 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.78-2
- Add the changelog entry for 1.78-1

* Sun Aug 14 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.78-1
- Update to 1.78

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-2
- Perl 5.22 rebuild

* Sun Jun 07 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.75-1
- Update to 1.75

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-2
- Perl 5.22 rebuild

* Sun Jan 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.74-1
- Update to 1.74

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 25 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.73-1
- Update to 1.73

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.72-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.72-2
- Perl 5.16 rebuild

* Fri Feb 03 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.72-1
- Update to 1.72

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Petr Šabata <contyk@redhat.com> - 1.71-1
- 1.71 bump
- Remove defattr
- Correct Source URL

* Sat Aug 27 2011 Petr Sabata <contyk@redhat.com> - 1.70-1
- 1.70 bump (live tests won't run by default now)

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.68-2
- Perl mass rebuild

* Tue Apr 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.68-1
- update to 1.68
- add BR HTML::TreeBuilder, remove duplicated requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.66-2
- Add BR: perl(CGI) (Fix FTBS: BZ 661086).

* Sun Nov 21 2010 Iain Arnell <iarnell@gmail.com> 1.66-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.62-2
- Mass rebuild with perl-5.12.0

* Wed Apr 21 2010 Petr Pisar <ppisar@redhat.com> 1.62-1
- version bump
- clean dependecies up

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.60-1
- auto-update to 1.60 (by cpan-spec-update 0.01)
- added a new br on perl(Carp) (version 0)
- added a new br on perl(File::Temp) (version 0)
- added a new br on perl(FindBin) (version 0)
- added a new br on perl(Getopt::Long) (version 0)
- added a new br on perl(HTML::Form) (version 1.038)
- added a new br on perl(HTML::HeadParser) (version 0)
- added a new br on perl(HTML::Parser) (version 3.33)
- altered br on perl(HTML::TokeParser) (0 => 2.28)
- added a new br on perl(HTTP::Daemon) (version 0)
- added a new br on perl(HTTP::Request) (version 1.3)
- altered br on perl(HTTP::Server::Simple) (0 => 0.35)
- added a new br on perl(HTTP::Server::Simple::CGI) (version 0)
- added a new br on perl(HTTP::Status) (version 0)
- added a new br on perl(LWP) (version 5.829)
- altered br on perl(LWP::UserAgent) (0 => 5.829)
- added a new br on perl(Pod::Usage) (version 0)
- altered br on perl(Test::More) (0 => 0.34)
- altered br on perl(Test::Warn) (0 => 0.11)
- added a new br on perl(URI::file) (version 0)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(File::Temp) (version 0)
- added a new req on perl(FindBin) (version 0)
- added a new req on perl(Getopt::Long) (version 0)
- added a new req on perl(HTML::Form) (version 1.038)
- added a new req on perl(HTML::HeadParser) (version 0)
- added a new req on perl(HTML::Parser) (version 3.33)
- added a new req on perl(HTML::TokeParser) (version 2.28)
- added a new req on perl(HTTP::Daemon) (version 0)
- added a new req on perl(HTTP::Request) (version 1.3)
- added a new req on perl(HTTP::Server::Simple) (version 0.35)
- added a new req on perl(HTTP::Server::Simple::CGI) (version 0)
- added a new req on perl(HTTP::Status) (version 0)
- added a new req on perl(LWP) (version 5.829)
- added a new req on perl(LWP::UserAgent) (version 5.829)
- added a new req on perl(Pod::Usage) (version 0)
- added a new req on perl(URI) (version 1.36)
- added a new req on perl(URI::URL) (version 0)
- added a new req on perl(URI::file) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.54-1
- Upstream update.
- Add BR: perl(URI), perl(HTTP::Server::Simple),
  perl(HTTP::Response::Encoding).
- Use %%bcond_with and %%with to process build options.

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.34-1
- update to 1.34

* Tue Feb 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.32-2
- rebuild for new perl

* Fri Dec 07 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.32-1
- update to 1.32

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-2
- New rebuild option: "--with livetests".

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-1
- Update to 1.30.
- The Makefile.PL --mech-dump option is now deprecated.

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.24-1
- Update to 1.24.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-2
- New BR: perl(IO::Socket::SSL).

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.22-1
- Update to 1.22.

* Tue Sep  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.20-1
- Update to 1.20.
- Live tests have been dropped.

* Tue Feb 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.18-2
- Re-enable test suite but without local and live tests.
  One local test fails in mock (see #165650 comment 4).
- New rebuild option: "--with localtests".

* Thu Feb  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.18-1
- Update to 1.18.

* Thu Nov 10 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Wed Aug 31 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-2
- Added Test::LongString to the live tests build requirements.

* Wed Aug 31 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Fri Aug 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-4
- Added Test::Pod::Coverage to the BR list in order to improve test coverage.
- Disabled test suite as it fails in mock (see #165650 comment 4).

* Thu Aug 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-3
- Conditional rebuild switch to enable live tests (RFE in #165650).

* Fri Jul  1 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-2
- Dist tag.

* Sat Feb 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.12-0.fdr.1
- Update to 1.12.

* Mon Feb 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.10-0.fdr.1
- Update to 1.10.

* Sat Dec 25 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.08-0.fdr.1
- Update to 1.08.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.02-0.fdr.1
- First build.
