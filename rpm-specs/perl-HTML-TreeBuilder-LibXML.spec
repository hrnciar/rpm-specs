Name:           perl-HTML-TreeBuilder-LibXML
Version:        0.26
Release:        17%{?dist}
Summary:        HTML::TreeBuilder and XPath compatible interface with libxml
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-TreeBuilder-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-TreeBuilder-LibXML-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(HTML::TreeBuilder::XPath) >= 0.14
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(XML::LibXML) >= 1.7

# perl-Web-Scraper requires HTML::TreeBuilder::LibXML so don't pull
# in this optional test requirement when bootstrapping (#982293)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Web::Scraper)
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not picked up by rpm deptracker
Requires:       perl(HTML::TreeBuilder::XPath) >= 0.14
Requires:       perl(XML::LibXML) >= 1.7

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::LibXML\\)

%description
HTML::TreeBuilder::XPath is a libxml based compatible interface to
HTML::TreeBuilder, which could be slow for a large document.
HTML::TreeBuilder::LibXML is drop-in-replacement for HTML::TreeBuilder::XPath.

%prep
%setup -q -n HTML-TreeBuilder-LibXML-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-16
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-15
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-12
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-8
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.26-1
- Update to 0.26

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25
- Tighten file listing

* Sat Sep 27 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.24-1
- Update to 0.24

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-8
- Perl 5.20 re-rebuild of bootstrapped packages

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.23-3
- Perl 5.18 rebuild

* Tue Jul  9 2013 Paul Howarth <paul@city-fan.org> - 0.23-2
- perl-Web-Scraper requires HTML::TreeBuilder::LibXML so don't pull
  in this optional test requirement when bootstrapping (#982293)

* Sun May 19 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23

* Sun May 12 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Update to 0.20
- Switch to Build.PL buildsystem

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Perl 5.16 rebuild

* Mon Jun 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.17-1
- Update to 0.17

* Wed Apr 04 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.16-2
- Take into account the review (#809633)

* Tue Apr 03 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.16-1
- Update to 0.16
