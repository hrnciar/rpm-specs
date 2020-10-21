Name:           perl-CGI-Application-Plugin-Authentication
Version:        0.23
Release:        9%{?dist}
Summary:        Authentication framework for CGI::Application
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/CGI-Application-Plugin-Authentication
Source0:        https://cpan.metacpan.org/authors/id/W/WE/WESM/CGI-Application-Plugin-Authentication-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Apache::Htpasswd)
BuildRequires:  perl(Attribute::Handlers)
# BuildRequires:  perl(Authen::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::ActionDispatch)
BuildRequires:  perl(CGI::Application::Plugin::AutoRunmode)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Color::Calc)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(English)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(overload)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::ConsistentVersion)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Regression)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(overload)

%{?perl_default_filter}

%description
CGI::Application::Plugin::Authentication adds the ability to
authenticate users in your CGI::Application modules. It imports one
method called 'authen' into your CGI::Application module. Through the
'authen' method you can call all the methods of the
CGI::Application::Plugin::Authentication plugin.

%prep
%setup -q -n CGI-Application-Plugin-Authentication-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README example
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Perl 5.28 rebuild

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23
- Drop upstreamed patch

* Sun Feb 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-2
- Apply Debian patch to adjust tests to SQLite 3.22.0 (#1543899)

* Thu Feb 08 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Update to 0.22

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.26 rebuild

* Sun Mar 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.21-2
- Really drop all patchs

* Sun Mar 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.21-1
- Update to 0.21
- Drop all patchs (upstreamed)
- Move to Makefile.PL build-system

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-15
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-13
- Perl 5.22 rebuild

* Tue May 12 2015 Petr Pisar <ppisar@redhat.com> - 0.20-12
- Fix warnings (bug #1195338)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 0.20-8
- Perl 5.18 rebuild
- Disable tests failing due to hash randomization (CPAN RT#85969)

* Sun Feb 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-7
- Replace perl(Digest::SHA1) with perl(Digest::SHA) in BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.20-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.20-2
- Perl mass rebuild

* Fri Jul 08 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.20-1
- Update to 0.20
- Add new BuildRequires
- Clean up spec file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.19-1
- Update to 0.19

* Mon Jul 19 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.18-1
- Update to 0.18
- Add new BuidlRequires
- Remove BR on Authen::Simple

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.17-3
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.17-2
- Add example directory to doc stanza

* Mon Oct 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.17-1
- Specfile autogenerated by cpanspec 1.78.
