Name:           perl-JSON-Path
Version:        0.420
Release:        8%{?dist}
Summary:        Search nested hashref/arrayref structures using JSONPath

License:        MIT
URL:            https://metacpan.org/release/JSON-Path
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POPEFELIX/JSON-Path-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-interpreter >= 1:5.16.0
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Easy)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::Parse)
BuildRequires:  perl(LV)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LV)

# Those are only needed when building for RHEL, on Fedora they come in as
# dependencies of the above
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  perl(CPAN)
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements JSONPath, an XPath-like language for searching JSON-
like structures.


%prep
%setup -q -n JSON-Path-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-2
- Perl 5.28 rebuild

* Sun May 06 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.420-1
- Update to 0.420

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.411-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.411-1
- Update to 0.411

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205-4
- Pass NO_PACKLIST to Makefile.PL
- Remove %%defattr macro
- Tighten file listing

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.205-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-2
- Perl 5.22 rebuild

* Sun Sep 07 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205-1
- Update to 0.205

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.101-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.101-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.101-1
- Specfile autogenerated by cpanspec 1.78. (with a couple of tweaks)
