Name:           perl-Catalyst-Plugin-Authentication
Summary:        Infrastructure plugin for the Catalyst authentication framework
Version:        0.10023
Release:        18%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Authentication-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-Authentication
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Authority)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Catalyst::Plugin::Session) >= 0.10
Requires:       perl(Catalyst::Runtime)
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.10018-3
Provides:       %{name}-tests = %{version}-%{release}

%{?perl_default_filter}

%description
The authentication plugin provides generic user support for Catalyst apps.
It is the basis for both authentication (checking the user is who they
claim to be), and authorization (allowing the user to do what the system
authorizes them to do).

%prep
%setup -q -n Catalyst-Plugin-Authentication-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-8
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-7
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10023-2
- Perl 5.22 rebuild

* Sat Nov 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.10023-1
- Update to 0.10023

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10022-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 0.10022-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.10022-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.10021-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 0.10020-2
- Perl 5.16 rebuild

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 0.10020-1
- update to latest upstream version

* Sun Apr 29 2012 Iain Arnell <iarnell@gmail.com> 0.10019-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.10018-3
- drop tests subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 01 2011 Iain Arnell <iarnell@gmail.com> 0.10018-1
- update to latest upstream version

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.10017-2
- Perl mass rebuild

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 0.10017-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10016-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10016-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10016-2
- Mass rebuild with perl-5.12.0

* Tue Feb 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.10016-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- altered br on perl(Test::More) (0 => 0.88)

* Thu Sep 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10015-1
- switch filtering systems...
- auto-update to 0.10015 (by cpan-spec-update 0.01)
- added a new br on perl(Class::MOP) (version 0)
- added a new br on perl(Moose) (version 0)

* Sat Aug 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10013-2
- auto-update to 0.10013 (by cpan-spec-update 0.01)
- added a new br on CPAN (inc::Module::AutoInstall found)

* Sat Aug 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10013-1
- auto-update to 0.10013 (by cpan-spec-update 0.01)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10012-1
- switch fitering system to a cleaner one
- auto-update to 0.10012 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new req on perl(Class::Inspector) (version 0)
- added a new req on perl(MRO::Compat) (version 0)

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10011-1
- update to 0.10011

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.10010-1
- update to 0.10010

* Sun Jan 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.100092-1
- update to 0.100092

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10008-1
- update to 0.10008

* Thu Sep 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10007-1
- update to 0.10007

* Tue Jun 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10006-4
- bump

* Mon Jun 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10006-3
- add br on Test::Exception

* Mon Jun 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10006-2
- drop buildroot references from prep

* Sat May 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.10006-1
- Specfile autogenerated by cpanspec 1.75.
