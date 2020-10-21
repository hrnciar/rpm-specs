Name:           perl-Number-Tolerant
Version:        1.708
Release:        15%{?dist}
Summary:        Tolerance ranges for inexact numbers
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Number-Tolerant
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Number-Tolerant-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter) >= 0.950
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(overload)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Sub::Exporter\\)$

%description
These Perl modules create a number-like object whose value refers
to a range of possible values, each equally acceptable. It overloads
comparison operations to reflect this.

%package -n perl-Test-Tolerant
Summary:        Test routines for testing numbers against tolerances
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Sub::Exporter) >= 0.950

%description -n perl-Test-Tolerant
"is_tol" is the only routine provided by Test::Tolerant Perl module. It
behaves like "is" from Test::More, asserting that two values must be equal,
but it will always use numeric equality, and the second argument is not always
used as the right hand side of comparison directly, but it used to produce
a Number::Tolerant to compare to.


%prep
%setup -q -n Number-Tolerant-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Number/
%{_mandir}/man3/Number::*

%files -n perl-Test-Tolerant
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.708-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.708-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.708-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.708-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.708-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Petr Pisar <ppisar@redhat.com> - 1.708-1
- 1.708 bump

* Mon Jul 20 2015 Petr Pisar <ppisar@redhat.com> - 1.707-1
- 1.707 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.706-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.706-2
- Perl 5.22 rebuild

* Thu Jun 04 2015 Petr Pisar <ppisar@redhat.com> - 1.706-1
- 1.706 bump

* Fri Nov 21 2014 Petr Pisar <ppisar@redhat.com> - 1.705-1
- 1.705 bump

* Mon Nov 03 2014 Petr Pisar <ppisar@redhat.com> - 1.704-1
- 1.704 bump

* Fri Oct 10 2014 Petr Pisar <ppisar@redhat.com> 1.703-1
- Specfile autogenerated by cpanspec 1.78.
