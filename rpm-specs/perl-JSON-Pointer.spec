Name:           perl-JSON-Pointer
Version:        0.07
Release:        14%{?dist}
Summary:        Perl implementation of JSON Pointer
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/JSON-Pointer
Source0:        https://cpan.metacpan.org/authors/id/Z/ZI/ZIGOROU/JSON-Pointer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp) >= 1.20
BuildRequires:  perl(Class::Accessor::Lite) >= 0.05
BuildRequires:  perl(Clone) >= 0.36
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON) >= 2.53
BuildRequires:  perl(overload)
BuildRequires:  perl(URI::Escape) >= 3.31
# Tests:
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.20
Requires:       perl(Class::Accessor::Lite) >= 0.05
Requires:       perl(Clone) >= 0.36
Requires:       perl(JSON) >= 2.53
Requires:       perl(URI::Escape) >= 3.31

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Carp|Class::Accessor::Lite|Clone|JSON|URI::Escape)\\)$

%description
This library is implemented JSON Pointer draft version 9
<http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-09> and some
useful operators from JSON Patch draft version 10
<http://tools.ietf.org/html/draft-ietf-appsawg-json-patch-10>. JSON Pointer is
available to identify a specified value, and it is similar to XPath. Please
see the both of specifications for details.

%prep
%setup -q -n JSON-Pointer-%{version}
# Remove bundled modules
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- 0.07 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.22 rebuild

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-2
- Perl 5.20 rebuild

* Thu Sep 04 2014 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.20 rebuild

* Tue Sep 02 2014 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 0.03-1
- 0.03 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.01-3
- Perl 5.18 rebuild
- return preference and tests fixed (CPAN RT#87314)

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.01-2
- Perl 5.18 rebuild

* Fri Apr 12 2013 Petr Pisar <ppisar@redhat.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
