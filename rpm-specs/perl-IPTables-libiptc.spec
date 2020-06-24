Name:           perl-IPTables-libiptc
Version:        0.52
Release:        34%{?dist}
Summary:        Perl extension for iptables libiptc
License:        GPLv2+
URL:            https://metacpan.org/release/IPTables-libiptc
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAWK/IPTables-libiptc-%{version}.tar.gz
# RT#70639
Patch0:         %{name}-0.51-Support-iptables-1.4.12.patch
# RT#70639
Patch1:         IPTables-libiptc-0.52-Support-for-1.4.16.2.patch
# RT#70639, bug #992659
Patch2:         IPTables-libiptc-0.52-Support-for-1.4.18.patch
# RT#70639, bug #1327038
Patch3:         IPTables-libiptc-0.52-Support-for-1.6.0.patch
# RT#70639, bug #1420338
Patch4:         IPTables-libiptc-0.52-Support-for-1.6.1.patch
# croak() expects formatting string, bug #1106081
Patch5:         IPTables-libiptc-0.52-Fix-GCC-format-security-warning.patch
# Do not link to nsl library, CPAN RT#124095
Patch6:         IPTables-libiptc-0.52-Stop-linking-against-nsl-library.patch
# Disable locking in iptables library, bug #1670047
Patch7:         IPTables-libiptc-0.52-Disable-locking.patch
# Fix make install invocation
Patch8:         IPTables-libiptc-0.52-Fix-make-install.patch
# kernel-headers >= 4.5.0-0.rc0.git6.1.fc24 and < 4.6.0-0.rc7.git3.1.fc25
# were broken, bug #1300223
BuildConflicts: kernel-headers < 4.6.0-0.rc7.git3.1.fc25
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  iptables-devel >= 1.6.0
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# ExtUtils::Constant not needed
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Part of iptables is bundled because iptables do not provide a stable
# library API.
Provides:       bundled(iptables) = 1.6.1

%{?perl_default_filter}

# Filter bogus libiptc.so() Provides, this is intentional rpm-build feature,
# bug #1309664
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libiptc\\.so()

%description
This package provides a perl interface to the netfilter/iptables C-code and
library libiptc.

%prep
%setup -q -n IPTables-libiptc-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor NO_PACKLIST=1 \
    NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IPTables*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-34
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 0.52-31
- Rebuilt (iptables)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-30
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Pisar <ppisar@redhat.com> - 0.52-28
- Disable locking in iptables library (bug #1670047)
- Fix make install invocation

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-26
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Petr Pisar <ppisar@redhat.com> - 0.52-24
- Do not link to nsl library (CPAN RT#124095)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-21
- Perl 5.26 rebuild

* Wed Feb 08 2017 Petr Pisar <ppisar@redhat.com> - 0.52-20
- Support for iptables-1.6.1 (bug #1420338)

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-19
- Perl 5.24 rebuild

* Mon May 16 2016 Petr Pisar <ppisar@redhat.com> - 0.52-18
- Remove workaround for kernel headers bug (bug #1300223)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-17
- Perl 5.24 rebuild

* Thu Apr 14 2016 Petr Pisar <ppisar@redhat.com> - 0.52-16
- Support for iptables-1.6.0 (bug #1327038)

* Thu Feb 18 2016 Petr Pisar <ppisar@redhat.com> - 0.52-15
- Work around bug in kernel headers (bug #1300223)
- Specify all dependencies
- Filter bogus libiptc.so() Provides caused by rpmdeps (bug #1309664)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-12
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-11
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Petr Pisar <ppisar@redhat.com> - 0.52-9
- Fix GCC format-security warning (bug #1106081)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Support for iptables-1.4.18 (bug #992659)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.52-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
- Support for iptables-1.4.16.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.52-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 Petr Pisar <ppisar@redhat.com> - 0.52-1
- 0.52 bump

* Wed Aug 31 2011 Petr Pisar <ppisar@redhat.com> 0.51-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr from spec code
- Add support for iptables-1.4.12 (RT#70639)
