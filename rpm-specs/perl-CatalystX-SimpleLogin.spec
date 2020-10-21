Name:           perl-CatalystX-SimpleLogin
Version:        0.20
Release:        11%{?dist}
Summary:        Provide a simple Login controller which can be reused
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/CatalystX-SimpleLogin
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/CatalystX-SimpleLogin-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Action::REST) >= 0.74
BuildRequires:  perl(Catalyst::ActionRole::ACL)
# not available in fedora and upstream is currently broken
# see https://rt.cpan.org/Public/Bug/Display.html?id=70417
# BuildRequires:  perl(Catalyst::Authentication::Credential::OpenID)
BuildRequires:  perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80013
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CatalystX::Component::Traits) >= 0.13
BuildRequires:  perl(CatalystX::InjectComponent)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::FormHandler) >= 0.28001
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::Any) >= 1.22
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::MethodAttributes) >= 0.18
BuildRequires:  perl(MooseX::RelatedClassRoles) >= 0.004
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::JSON) >= 0.02
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
Requires:       perl(Catalyst::Action::REST) >= 0.74
Requires:       perl(Catalyst::Plugin::Authentication)
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Runtime) >= 5.80013
Requires:       perl(Catalyst::View::TT)
Requires:       perl(CatalystX::Component::Traits) >= 0.13
Requires:       perl(HTML::FormHandler) >= 0.28001
Requires:       perl(MooseX::MethodAttributes) >= 0.18
Requires:       perl(MooseX::RelatedClassRoles) >= 0.004
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Common)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
CatalystX::SimpleLogin is an application class which provides a simple login
and logout page with the addition of only one line of code and one template to
your application.

%prep
%setup -q -n CatalystX-SimpleLogin-%{version}
# Remove bundled libs
rm -rf inc/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Update to 0.20
- Get rid of Group tag (no longer used)

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.24 rebuild

* Fri Feb 26 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19
- Remove bundled libs and use the system-provided ones
- Pass NO_PACKLIST to Makefile.PL
- Use RPM_BUILD_ROOT instead of buildroot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-7
- Perl 5.22 rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Iain Arnell <iarnell@gmail.com> 0.18-3
- pass skipdeps to Makefile.PL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 0.15-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Iain Arnell <iarnell@gmail.com> 0.15-2
- fix spelling in description

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
