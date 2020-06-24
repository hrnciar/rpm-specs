Name:           perl-App-DuckDuckGo
Version:        0.008
Release:        17%{?dist}
Summary:        Application class used to query duckduckgo.com from the command line
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-DuckDuckGo
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/App-DuckDuckGo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Moose) >= 1.24
BuildRequires:  perl(MooseX::Getopt) >= 0.35
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(WWW::DuckDuckGo) >= 0.004
BuildRequires:  perl(warnings)
Requires:       perl(Moose) >= 1.24
Requires:       perl(MooseX::Getopt) >= 0.35
Requires:       perl(WWW::DuckDuckGo) >= 0.004
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Moose\\)$
%global __requires_exclude %__requires_exclude|^perl\\(WWW::DuckDuckGo\\)$
%description
This is the class which is used by the duckduckgo command to do the work. Please
refer to the duckduckgo package to get the documentation for the command line
tool.

%prep
%setup -q -n App-DuckDuckGo-%{version}
sed -i 's|#!/usr/bin/env perl|#!%{__perl}|' bin/duckduckgo

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n duckduckgo
Summary: Command line tool to use the DuckDuckGo API

%description -n duckduckgo
This application queries the DuckDuckGo API and displays the result in
a nice human-readable way or in a batch mode which could be used by a 
shell script to automatically work with the DuckDuckGo API results.

%files -n duckduckgo
%doc LICENSE README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-2
- Perl 5.20 rebuild

* Fri Jun 27 2014 David Dick <ddick@cpan.org> - 0.008-1
- Initial release
