Name:           perl-Bot-BasicBot
Version:        0.93
Release:        9%{?dist}
Summary:        Simple IRC bot base class
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Bot-BasicBot
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Bot-BasicBot-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IRC::Utils)
BuildRequires:  perl(POE::Component::IRC::Plugin::Connector)
# POE::Component::IRC::State version from POE::Component::IRC in META.json
BuildRequires:  perl(POE::Component::IRC::State) >= 6.90
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Text::Wrap)
# Tests:
# IO::Socket not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
# POE::Component::IRC::State version from POE::Component::IRC in META.json
Requires:       perl(POE::Component::IRC::State) >= 6.90

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(POE::Component::IRC::State\\)$

%description
Basic bot system designed to make it easy to do simple bots, optionally
forking longer processes (like searches) concurrently in the background.

%prep
%setup -q -n Bot-BasicBot-%{version}
find examples -type f -exec chmod 644 {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Petr Pisar <ppisar@redhat.com> - 0.93-1
- 0.93 bump

* Fri Feb 02 2018 Petr Pisar <ppisar@redhat.com> - 0.92-1
- 0.92 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-2
- Perl 5.26 rebuild

* Fri Apr 07 2017 Petr Pisar <ppisar@redhat.com> - 0.91-1
- 0.91 bump

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 0.90-1
- 0.90 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.89-6
- Perl 5.24 rebuild

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 0.89-5
- Modernize spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.89-2
- Perl 5.22 rebuild

* Fri Sep 19 2014 Petr Šabata <contyk@redhat.com> - 0.89-1
- 0.89 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Pisar <ppisar@redhat.com> - 0.87-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.87-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> 0.87-1
- Initial package.
