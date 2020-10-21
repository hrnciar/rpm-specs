# Declare the CPAN name of the module
%define mod_basename Class-Accessor-Classy

Name:           perl-%{mod_basename}
Version:        0.9.1
Release:        23%{?dist}
Summary:        Accessors with minimal inheritance
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{mod_basename}
Source:         https://cpan.metacpan.org/modules/by-module/Class/%{mod_basename}-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build) >= 0.28
# These are needed for "Build test"
BuildRequires:  perl(attributes)
BuildRequires:  perl(version)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
The Class::Accessor::Classy Perl module provides an extremely small
footprint accessor/mutator declaration scheme for fast and convenient
object attribute setup.  It is intended as a simple and speedy mechanism
for preventing hash-key typos rather than a full-blown object system
with type checking and so on.

The accessor methods appear as a hidden parent class of your package
and generally try to stay out of the way.  The accessors and mutators
generated are of the form C<foo()> and C<set_foo()>, respectively.

%prep
%setup -q -n %{mod_basename}-v%{version}

%build
# Using Module::Build since a Build.PL is present
perl Build.PL installdirs=vendor
./Build

%install
%if 0%{?rhel} && 0%{?rhel} < 6
rm -rf %{buildroot}
%endif
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-22
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-8
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.1-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 John C. Peterson <jcp@eskimo.com> 0.9.1-5
- Fixed some errors in conditional tests for when to remove buildroot (RHEL < 6)
- Removed the redundant defattr macro from the files section
- Replaced all occurances of the __perl macro with just perl

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9.1-3
- Perl 5.18 rebuild

* Tue Jul  2 2013 John C. Peterson <jcp@eskimo.com> 0.9.1-2
- Added missing build requirements identified by the reviewer.

* Wed Jun 26 2013 John C. Peterson <jcp@eskimo.com> 0.9.1-1
- Some minor cosmetic fixes to improve readability and to pacify rpmlint.

* Tue Jun 18 2013 John C. Peterson <jcp@eskimo.com> 0.9.1-1
- Baseline specfile autogenerated by cpanspec 1.78.

