Name:           perl-MooseX-Types-DateTime-ButMaintained
Version:        0.16
Release:        25%{?dist}
Summary:        DateTime related constraints and coercions for Moose
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooseX-Types-DateTime-ButMaintained
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/MooseX-Types-DateTime-ButMaintained-%{version}.tar.gz
# Accept DateTime::TimeZone::Tzfile object in place of DateTime::TimeZone,
# bug #1138185
Patch0:         MooseX-Types-DateTime-ButMaintained-0.16-Accept-DateTime-TimeZone-Tzfile-object-in-place-of-D.patch
# Accept DateTime::Locale::FromData object in place of DateTime::Locale,
# bug #1283970
Patch1:         MooseX-Types-DateTime-ButMaintained-0.16-Accept-DateTime-Locale-FromData-object.patch
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
# DateTime >= 0.4302 rounded to two places
BuildRequires:  perl(DateTime) >= 0.44
# DateTime::Locale >= 0.4001 rounded to two places
BuildRequires:  perl(DateTime::Locale) >= 0.41
BuildRequires:  perl(DateTime::TimeZone) >= 0.96
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.30
BuildRequires:  perl(MooseX::Types::Moose) >= 0.30
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Olson::Abbreviations) >= 0.03
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok) >= 0.02
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# DateTime >= 0.4302 rounded to two places
Requires:       perl(DateTime) >= 0.44
# DateTime::Locale >= 0.4001 rounded to two places
Requires:       perl(DateTime::Locale) >= 0.41
Requires:       perl(DateTime::TimeZone) >= 0.96

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime(|::Locale|::TimeZone)\\)\\s*$

%description
This module packages several Moose::Util::TypeConstraints with coercions,
designed to work with the DateTime suite of objects.

%prep
%setup -q -n MooseX-Types-DateTime-ButMaintained-%{version}
%patch0 -p1
%patch1 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
# switch off cpan installation
PERL5_CPANPLUS_IS_RUNNING=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-24
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-21
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-18
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-11
- Accept DateTime::Locale::FromData object in place of DateTime::Locale
  (bug #1283970)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-9
- Perl 5.22 rebuild

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-8
- Perl 5.20 rebuild

* Thu Sep 04 2014 Petr Pisar <ppisar@redhat.com> - 0.16-7
- Accept DateTime::TimeZone::Tzfile object in place of DateTime::TimeZone (bug
  #1138185)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.16-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.15-2
- Perl 5.16 rebuild

* Wed Jun 13 2012 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump
- Drop command macros

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Tue Dec 13 2011 Petr Šabata <contyk@redhat.com> - 0.13-1
- 0.13 bump
- Remove now obsolete Buildroot and defattr
- Removing runtime deps since they get autodetected (including versions) now

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.11-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- Mass rebuild with perl-5.12.0

* Mon Feb 22 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.11-2
- add BR, switch off CPAN, remove unecessary requirements

* Fri Feb 19 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
