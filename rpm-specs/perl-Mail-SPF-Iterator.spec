Name:             perl-Mail-SPF-Iterator
Summary:          Iterative SPF lookup
Version:          1.119
Release:          8%{?dist}
License:          GPL+ or Artistic
URL:              https://metacpan.org/release/Mail-SPF-Iterator
Source0:          https://cpan.metacpan.org/authors/id/S/SU/SULLR/Mail-SPF-Iterator-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    make
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:    perl(base)
BuildRequires:    perl(constant)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(Exporter)
BuildRequires:    perl(fields)
BuildRequires:    perl(Net::DNS) >= 0.62
BuildRequires:    perl(Net::DNS::Resolver)
BuildRequires:    perl(Socket)
BuildRequires:    perl(Socket6)
BuildRequires:    perl(strict)
BuildRequires:    perl(URI)
BuildRequires:    perl(URI::Escape)
BuildRequires:    perl(warnings)

Requires:         perl(Net::DNS) >= 0.62
Requires:         perl(URI)
Requires:         perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides an iterative resolving of SPF records. Contrary to
Mail::SPF, which does blocking DNS lookups, this module just returns the
DNS queries and later expects the responses.


%prep
%setup -q -n Mail-SPF-Iterator-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1

make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README samples
%license COPYRIGHT
%{_mandir}/man3/Mail::SPF::Iterator*
%{perl_vendorlib}/Mail


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-7
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-6
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.119-1
- Update to 1.119
- Whitelist known rpmlint errors

* Sun Nov 04 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.118-1
- Update to 1.118

* Sun Sep 30 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.117-1
- Update to 1.117

* Sun Sep 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.116-1
- Update to 1.116

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.114-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.114-2
- Perl 5.28 rebuild

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.114-1
- Update to 1.114

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 21 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.113-1
- Update to 1.113

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.112-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.112-1
- Update to 1.112

* Tue Nov 24 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.111-1
- Update to 1.111

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.11-1
- Initial package for Fedora, with help from cpanspec.
