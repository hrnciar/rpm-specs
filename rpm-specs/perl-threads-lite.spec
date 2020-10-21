Name:           perl-threads-lite
Version:        0.034
Release:        21%{?dist}
Summary:        Actor model threading for Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/threads-lite
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/threads-lite-%{version}.tar.gz
# Tests halt on these platforms, bug #719874, CPAN RT#69354
ExcludeArch:    aarch64 ppc ppc64 ppc64le
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental) >= 0.003
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(feature)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 2.05
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module implements threads for perl. One crucial difference with
threads.pm threads is that the threads are disconnected, except by message
queues. It thus facilitates a message passing style of multi-threading.

%prep
%setup -q -n threads-lite-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-20
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-17
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-14
- Perl 5.28 rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.034-13
- Modernize spec file
- Do not build for ppc64 because the code is broken there (bug #719874)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Petr Pisar <ppisar@redhat.com> - 0.034-5
- Do not build for aarch64, ppc, and ppc64le because the code is broken there
  (bug #719874)

* Mon Aug 03 2015 Petr Pisar <ppisar@redhat.com> - 0.034-4
- Disable checks on aarch64 (bug #719874)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-2
- Perl 5.22 rebuild

* Mon May 11 2015 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Tue May 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-8
- Fix regex and test for Perl 5.22 (CPAN RT#104229)

* Wed Feb 11 2015 Karsten Hopp <karsten@redhat.com> 0.033-7
- disable checks on ppc64le, (rhbz#719874)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.033-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.033-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.033-2
- Perl 5.18 rebuild

* Wed May 29 2013 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Wed Feb 20 2013 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.031-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.031-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.031-7
- Perl 5.16 rebuild
- Restore compatibility with perl 5.16, RT#77947

* Sat Feb 25 2012 Karsten Hopp <karsten@redhat.com> 0.031-6
- fix arch check

* Sat Feb 25 2012 Karsten Hopp <karsten@redhat.com> 0.031-5
- disable checks on ppc (#719874)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.031-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.031-3
- Perl mass rebuild

* Mon May 30 2011 Petr Pisar <ppisar@redhat.com> - 0.031-2
- Remove explicit defattr

* Mon May 30 2011 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Tue May 10 2011 Petr Pisar <ppisar@redhat.com> 0.030-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
