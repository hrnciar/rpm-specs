Name:           perl-MooX-Cmd
Version:        0.017
Release:        13%{?dist}
Summary:        Giving an easy Moo style way to make command organized CLI apps
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooX-Cmd
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils) >= 0.406
BuildRequires:  perl(Module::Pluggable::Object) >= 4.8
BuildRequires:  perl(Module::Runtime)
# 0.009013 from Moo in META which is not used
BuildRequires:  perl(Moo::Role) >= 0.009013
BuildRequires:  perl(Package::Stash) >= 0.33
BuildRequires:  perl(Params::Util) >= 0.37
BuildRequires:  perl(parent)
BuildRequires:  perl(Regexp::Common) >= 2011121001
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Text::ParseWords)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moo) >= 0.009013
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-MooX-ConfigFromFile → perl-MooX-Cmd
# → perl-MooX-ConfigFromFile
BuildRequires:  perl(MooX::ConfigFromFile) >= 0.008
# Break build-cycle: perl-MooX-Options → perl-MooX-Cmd → perl-MooX-Options
BuildRequires:  perl(MooX::Options) >= 4.103
%endif
BuildRequires:  perl(Text::Abbrev)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(List::MoreUtils) >= 0.406
Requires:       perl(Module::Pluggable::Object) >= 4.8
# 0.009013 from Moo in META which is not used
Requires:       perl(Moo::Role) >= 0.009013
Requires:       perl(Package::Stash) >= 0.33
Requires:       perl(Params::Util) >= 0.37
Requires:       perl(Regexp::Common) >= 2011121001
Requires:       perl(Test::More) >= 0.98

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Pluggable::Object\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Package::Stash\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Regexp::Common\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
Works together with MooX::Options for every command on its own, so options
are parsed for the specific context and used for the instantiation:

%prep
%setup -q -n MooX-Cmd-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-12
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-8
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-1
- 0.017 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Petr Pisar <ppisar@redhat.com> - 0.015-2
- Break build-cycle: perl-MooX-Options → perl-MooX-Cmd → perl-MooX-Options
- Break build-cycle: perl-MooX-ConfigFromFile → perl-MooX-Cmd →
  perl-MooX-ConfigFromFile

* Mon Jul 20 2015 Petr Pisar <ppisar@redhat.com> - 0.015-1
- Update to 0.015 (thanks to Emmanuel Seyman)
- Clean up spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-2
- Perl 5.22 rebuild

* Sat Jan 24 2015 David Dick <ddick@cpan.org> - 0.011-1
- Upgrade to 0.11

* Wed Aug 27 2014 David Dick <ddick@cpan.org> - 0.009-1
- Initial release
