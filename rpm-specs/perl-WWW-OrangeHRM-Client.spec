%global tarname WWW-OrangeHRM-Client
Name:           perl-%{tarname}
Version:        0.12.0
Release:        4%{?dist}
Summary:        Client for OrangeHRM
License:        GPL+
URL:            http://ppisar.fedorapeople.org/%{tarname}/
Source0:        %{url}%{tarname}-v%{version}.tar.gz
Source1:        %{url}%{tarname}-v%{version}.tar.gz.asc
# Exported from owner's keyring
Source2:        gpgkey-4B528393E6A3B0DFB2EF3A6412C9C5C767C6FAA2.gpg
BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# Run-time:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::TreeBuilder::LibXML)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WWW::Mechanize)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(LWP::Authen::Negotiate)
Requires:       perl(LWP::Protocol::https)

%description
This module implements client for OrangeHRM information system. It has been
developed against Red Hat instance, so I cannot guarantee it works with
other instances.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{tarname}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12.0-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Petr Pisar <ppisar@redhat.com> - 0.12.0-1
- 0.12.0 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11.0-2
- Perl 5.30 rebuild

* Wed Mar 06 2019 Petr Pisar <ppisar@redhat.com> - 0.11.0-1
- 0.11.0 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.3-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.3-2
- Perl 5.26 rebuild

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 0.10.3-1
- 0.10.3 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Petr Pisar <ppisar@redhat.com> - 0.10.2-1
- 0.10.2 bump

* Wed Dec 21 2016 Petr Pisar <ppisar@redhat.com> - 0.10.1-1
- 0.10.1 bump
- Make dependency on LWP::Authen::Negotiate optional

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Petr Pisar <ppisar@redhat.com> - 0.10.0-1
- 0.10.0 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-2
- Perl 5.22 rebuild

* Thu Jan 08 2015 Petr Pisar <ppisar@redhat.com> - 0.9.1-1
- 0.9.1 bump

* Wed Oct 08 2014 Petr Pisar <ppisar@redhat.com> - 0.9.0-1
- 0.9.0 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.8.0-2
- Perl 5.20 rebuild

* Tue Aug 26 2014 Petr Pisar <ppisar@redhat.com> - 0.8.0-1
- 0.8.0 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Petr Pisar <ppisar@redhat.com> - 0.7.2-1
- 0.7.2 bump

* Tue Dec 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.1-1
- 0.7.1 bump

* Thu Nov 28 2013 Petr Pisar <ppisar@redhat.com> - 0.7.0-1
- 0.7.0 bump

* Thu Aug 29 2013 Petr Pisar <ppisar@redhat.com> - 0.6.0-1
- 0.6.0 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5.0-2
- Perl 5.18 rebuild

* Thu Apr 11 2013 Petr Pisar <ppisar@redhat.com> - 0.5.0-1
- 0.5.0 bump

* Tue Mar 05 2013 Petr Pisar <ppisar@redhat.com> - 0.4.0-1
- 0.4.0 bump

* Fri Jan 25 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Tue Jan 08 2013 Petr Pisar <ppisar@redhat.com> - 0.2.0-1
- 0.2.0 bump

* Fri Dec 14 2012 Petr Pisar <ppisar@redhat.com> 0.1.1-1
- Specfile autogenerated by cpanspec 1.78.
