# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname DBD-Firebird

Summary:        A Firebird interface for perl
Name:           perl-DBD-Firebird
Version:        1.32
Release:        2%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/M/MA/MARIUZ/%{pkgname}-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  firebird >= 2.5.1
# Build using firebird 2.5.x and 3.0.x without conditionals by requiring libfbclient.so
BuildRequires:  %{_libdir}/libfbclient.so
BuildRequires:  libicu-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  perl-interpreter
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  perl(:VERSION) >= 5.10.1
%endif
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.43
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigFloat) >= 1.55
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  perl(Test::CheckDeps) >= 0.007
%endif
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  perl(Test::More) >= 0.94
%endif
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
DBD::Firebird is a Perl module that works with the DBI module to provide
access to Firebird databases.

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# RHEL/CentOS 6 ships Test::More 0.92 rather 0.94 (thus skip this test)
%if 0%{?rhel} == 6
rm -f t/{,embed-}000-check-dependencies.t
%endif

# Test for ib_set_tx_param() seems to be buggy (thus disable for now)
rm -f t/embed-62-timeout.t

# Disable thread-based test of ib_wait_event, as this test cannot be
# guaranteed to succeed with overloaded host, see:
# - https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=719582
# - https://bugzilla.redhat.com/show_bug.cgi?id=1228642
# - https://bugzilla.redhat.com/show_bug.cgi?id=1161469
export AUTOMATED_TESTING=1

# Full test coverage requires a live Firebird database (see the README file)
make test

%files
%doc Changes README
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{_mandir}/man3/*.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-2
- Perl 5.32 rebuild

* Sun Apr 26 2020 Robert Scheck <robert@fedoraproject.org> 1.32-1
- Upgrade to 1.32 (#1812799)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Robert Scheck <robert@fedoraproject.org> 1.31-1
- Upgrade to 1.31 (#1522691)

* Mon Dec 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- 1.29 bump

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-1
- 1.25 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-1
- 1.24 bump

* Fri Oct 14 2016 Robert Scheck <robert@fedoraproject.org> 1.22-3
- Buildrequire libfbclient.so rather firebird-devel to cover
  building with firebird 2.5.x and 3.0.x without conditionals

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21 (#1267292)

* Mon Jun 22 2015 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Mon Jun 22 2015 Robert Scheck <robert@fedoraproject.org> 1.19-4
- Disable failed test with overloaded host (#1161469, #1228642)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-2
- Perl 5.22 rebuild

* Fri Apr 03 2015 Robert Scheck <robert@fedoraproject.org> 1.19-1
- Upgrade to 1.19 (#1207216)

* Sun Oct 12 2014 Robert Scheck <robert@fedoraproject.org> 1.18-1
- Upgrade to 1.18

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.11-3
- Perl 5.18 rebuild

* Fri Apr 19 2013 Robert Scheck <robert@fedoraproject.org> 1.11-2
- Changes to match with Fedora Packaging Guidelines (#951874)

* Sun Apr 14 2013 Robert Scheck <robert@fedoraproject.org> 1.11-1
- Upgrade to 1.11
- Initial spec file for Fedora and Red Hat Enterprise Linux
