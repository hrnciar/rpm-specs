Name:           perl-Plack
Version:        1.0047
Release:        10%{?dist}
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Plack
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz
BuildArch:      noarch

# Build with apache2 tests enabled
# - works in local mocks, but fails in Fedora's koji.
# - requires customized apache setup with apache >= 2.4.
# Default to not testing apache2.
%bcond_with apache

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(Apache::LogFormat::Compiler) >= 0.33
BuildRequires:  perl(Cookie::Baker) >= 0.07
BuildRequires:  perl(Devel::StackTrace) >= 1.23
BuildRequires:  perl(Devel::StackTrace::AsHTML) >= 0.11
BuildRequires:  perl(Devel::StackTrace::WithLexicals) >= 0.8
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(Hash::MultiValue) >= 0.05
BuildRequires:  perl(HTTP::Entity::Parser) >= 0.17
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.18
BuildRequires:  perl(HTTP::Message) >= 5.814
BuildRequires:  perl(HTTP::Tiny) >= 0.03
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.36
BuildRequires:  perl(Stream::Buffered) >= 0.02
BuildRequires:  perl(Test::TCP) >= 2.15
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23

# tests
BuildRequires:  perl(Authen::Simple::Adapter)
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Compile) >= 0.03
BuildRequires:  perl(CGI::Emulate::PSGI) >= 0.10
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Server::Simple::PSGI)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(Log::Dispatch::Array) >= 1.001
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP::UserAgent) >= 5.814
BuildRequires:  perl(LWP::Protocol::http10)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)

# For mod_perl.so
BuildRequires:  mod_perl >= 2

# For httpd tests
BuildRequires:  /usr/sbin/httpd

# For t/Plack-Middleware/cgibin_exec.t
BuildRequires:  /usr/bin/python

# For lighttpd tests
BuildRequires:  /usr/sbin/lighttpd
BuildRequires:  lighttpd-fastcgi

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

%package Test
Summary: Test-modules for perl-Plack
Requires: perl-Plack = %{version}-%{release}

%description Test
%{summary}.

%prep
%setup -q -n Plack-%{version}

# Fedora's mod_perl.so is under modules/
sed -i -e 's,libexec/apache2/mod_perl.so,modules/mod_perl.so,' \
t/Plack-Handler/apache2.t t/Plack-Handler/apache2-registry.t

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
# missing modules
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test %{?_with_apache:TEST_APACHE2=1 TEST_FCGI_CLIENT=1}

%files
%doc Changes README
%{_bindir}/plackup
%{_mandir}/man1/plackup.*
%{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack.pm
%{perl_vendorlib}/HTTP
# Abandoned/Unsupported in Fedora: Apache1
%exclude %{perl_vendorlib}/Plack/Handler/Apache1.pm
%exclude %{_mandir}/man3/Plack::Handler::Apache1.3pm*
# Packaged separately in perl-Plack-Test
%exclude %{perl_vendorlib}/Plack/Test
%exclude %{perl_vendorlib}/Plack/Test.pm
%exclude %{perl_vendorlib}/auto/*
%exclude %{_mandir}/man3/Plack::Test*

%{_mandir}/man3/*

%files Test
%{_mandir}/man3/Plack::Test*
%dir %{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack/Test
%{perl_vendorlib}/Plack/Test.pm
# Used by Plack/Test/Suite.pm
%{perl_vendorlib}/auto/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-9
- Perl 5.32 rebuild

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-8
- Add perl(DirHandle) needed for build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-2
- Perl 5.28 rebuild

* Sun Feb 18 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0047-1
- Update to 1.0047.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0045-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0045-1
- Update to 1.0045.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0044-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0044-2
- Perl 5.26 rebuild

* Fri Apr 28 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0044-1
- Update to 1.0044.

* Thu Feb 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0043-1
- Update to 1.0043.
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0042-1
- Update to 1.0042 (RHBZ#1382923).
- Spec cleanup.

* Sat Oct 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0039-2
- Preps for Plack-1.0042.

* Sat Jun 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0039-1
- Update to 1.0039.
- Cleanup BRs.

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0034-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0034-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-5
- Merge preps for pending upstream updates:
  - Preps for 1.0039:
    - BR: perl(HTTP::Headers::Fast) >= 0.18.
  - Preps for 1.0038:
    - BR: perl(HTTP::Headers::Fast) >= 0.20.
  - Preps for 1.0037:
    - BR: perl(HTTP::Headers::Fast) >= 0.18.
  - Preps for 1.0036:
    - BR: perl(Cookie::Baker), perl(HTTP::Headers::Fast).

* Fri Jan 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-4
- Modernize spec.
- Remove ref to %%{perl_vendorlib}/Plack/Server/Apache1.pm.
- Exclude stray %%{_mandir}/man3/Plack::Handler::Apache1.3pm* manpage.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0034-2
- Perl 5.22 rebuild

* Wed Feb 04 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-1
- Upstream update.

* Mon Oct 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0033-1
- Upstream update.

* Mon Oct 13 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0032-1
- Upstream update.

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0031-2
- Perl 5.20 rebuild

* Fri Aug 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0031-1
- Upstream update.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-3
- Move misplaced %%exclude-line from base-package to *-Test.

* Wed Jan 15 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-2
- Split out perl-Plack-Test to avoid dependency on Test::More (RHBZ #1052859).

* Mon Dec 30 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-1
- Upstream update.

* Wed Sep 18 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0029-1
- Upstream update.
- Update BRs.
- Modernize spec.

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.0022-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0022-1
- Upstream update.
- Add BR: perl(File::ShareDir::Install).
- Add BR: perl(Stream::Buffered).
- Remove perl-Plack-1.0004.patch (Not required anymore).
- Preps for Plack > 1.0022.

* Mon Feb 18 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0004-3
- Fix changelog dates (Fedora_19_Mass_Rebuild FTBFS).
- Add perl-Plack-1.0004.patch.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0004-1
- Upstream update.

* Sun Sep 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0003-1
- Upstream update.

* Thu Aug 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0002-1
- Upstream update.

* Mon Jul 30 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0001-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9989-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 0.9989-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9989-1
- Upstream update.

* Mon May 21 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9988-1
- Upstream update.

* Mon Mar 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9986-1
- Upstream update.

* Wed Jan 18 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9985-3
- Activate optional BR: perl(Devel::StackTrace::WithLexicals).
- Activate optional BR: perl(LWP::Protocol::http10).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9985-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9985-1
- Upstream update.

* Fri Oct 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9984-2
- Add %%bcond_with apache to work around building failures in koji.

* Thu Oct 13 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9984-1
- Upstream update.

* Fri Aug 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9982-1
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.9980-2
- Perl mass rebuild

* Wed Jun 08 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9980-1
- Upstream update.

* Thu May 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9979-1
- Upstream update.
- Activate lighttpd and lighttpd-fcgi tests.

* Wed May 11 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9978-1
- Upstream update.

* Mon May 02 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9977-1
- Upstream update.

* Sun Apr 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9976-1
- Upstream update.

* Mon Mar 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9974-2
- Reflect HTTP-Server-Simple-PSGI having entered Fedora
  (Add BR: perl(HTTP::Server::Simple::PSGI)).

* Mon Mar 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9974-1
- Upstream update.

* Thu Mar 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9973-1
- Upstream update.
- Reflect upstream not shipping Plack/Handler/Net/FastCGI.pm anymore.
- Spec file cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9967-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9967-1
- Upstream update.

* Tue Jan 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9964-1
- Upstream update.

* Tue Jan 18 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9963-1
- Upstream update.
- Hack around incorrect hard-coded path to mod_perl.so.
- Activate Apache2 test.

* Mon Jan 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9960-1
- Upstream update.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9959-2
- Re-add %%{perl_vendorlib}/auto/*jpg (Used by Plack/Test).
- Add BR: perl(Authen::Simple::Passwd).
- Add BR: perl(CGI::Emulate::PSGI).

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9959-1
- Update to 0.9959.

* Tue Dec 21 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9958-1
- Initial Fedora package.
