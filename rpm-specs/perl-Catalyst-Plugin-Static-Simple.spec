Name:           perl-Catalyst-Plugin-Static-Simple
Version:        0.36
Release:        9%{?dist}
Summary:        Make serving static pages painless
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Catalyst-Plugin-Static-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Catalyst-Plugin-Static-Simple-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst) >= 5.30
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Log)
BuildRequires:  perl(Catalyst::Plugin::SubRequest)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80008
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Types) >= 1.25
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)

Requires:       perl(Catalyst) >= 5.30
Requires:       perl(Catalyst::Runtime) >= 5.80008
Requires:       perl(MIME::Types) >= 1.25
Requires:       perl(MRO::Compat)
Requires:       perl(Moose)
Requires:       perl(MooseX::Types)
Requires:       perl(namespace::autoclean)

%{?perl_default_filter}

%description
The Static::Simple plugin is designed to make serving static content in
your application during development quick and easy, without requiring a
single line of code from you.

%prep
%setup -q -n Catalyst-Plugin-Static-Simple-%{version}
chmod -x Changes lib/Catalyst/Plugin/Static/Simple.pm
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

# silence rpmlint warnings
find t -type f -print0 | xargs -0 sed -i '1s,#!.*perl,#!%{__perl},;s/\r//;'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +

%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.28 rebuild

* Sun Mar 18 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.36-1
- Update to 0.36
- Drop upstreamed patch

* Sun Feb 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.34-3
- Rename err.omg to err.abcdefgh ('omg' is now a valid mimetype) #1540586

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.34-1
- Update to 0.34
- Drop Group tag
- Drop obsolete/provide for tests subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-8
- Perl 5.26 rebuild

* Wed May 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-7
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-2
- Perl 5.22 rebuild

* Sat Nov 22 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.33-1
- Update to 0.33
- Fix rights on certain files

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.30-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.30-2
- Perl 5.16 rebuild

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 0.30-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.29-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29-2
- Mass rebuild with perl-5.12.0

* Sun Feb 07 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.29-1
- add perl_default_filter
- add perl_default_subpackage_tests, drop t/ from doc
- PERL_INSTALL_ROOT => DESTDIR
- auto-update to 0.29 (by cpan-spec-update 0.01)
- added a new br on perl(Moose) (version 0)
- added a new br on perl(MooseX::Types) (version 0)
- added a new br on perl(namespace::autoclean) (version 0)
- added a new req on perl(Moose) (version 0)
- added a new req on perl(MooseX::Types) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- switch to new filtering system
- auto-update to 0.22 (by cpan-spec-update 0.01)
- altered br on perl(Catalyst::Runtime) (5.30 => 5.80008)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on CPAN (inc::Module::Install::AutoInstall found)
- added a new req on perl(Catalyst::Runtime) (version 5.80008)
- added a new req on perl(MIME::Types) (version 1.25)
- added a new req on perl(MRO::Compat) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- auto-update to 0.21 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.50)
- added a new br on perl(MRO::Compat) (version 0)
- added a new br on perl(Catalyst::Runtime) (version 5.30)
- altered br on perl(MIME::Types) (1.15 => 1.25)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.20-2
- rebuild for new perl

* Sat Mar 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- update to 0.20

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- update to 0.19

* Fri Jun 08 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- update to 0.17
- switch build/install incantations; module switched to Module::Install

* Tue Jun 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.15-3
- bump

* Tue Jun 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.15-2
- add perl(HTTP::Request::AsCGI) as br
- include all of t/, not just t/lib/TestApp/

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- Specfile autogenerated by cpanspec 1.71.
