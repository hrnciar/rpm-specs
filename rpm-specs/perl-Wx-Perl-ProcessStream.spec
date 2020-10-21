# Tests need X display
%global enable_test 1

Name:           perl-Wx-Perl-ProcessStream
Version:        0.32
Release:        23%{?dist}
Summary:        Access IO of external processes via events
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Wx-Perl-ProcessStream
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDOOTSON/Wx-Perl-ProcessStream-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes) >= 1.2
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Wx) >= 0.5
BuildRequires:  perl(Wx::App)
BuildRequires:  perl(Wx::Event)
BuildRequires:  perl(Wx::EvtHandler)
BuildRequires:  perl(Wx::Frame)
BuildRequires:  perl(Wx::Perl::Carp)
BuildRequires:  perl(Wx::PlCommandEvent)
BuildRequires:  perl(Wx::Process)
%if %enable_test
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
%endif
Requires:       perl(Time::HiRes) >= 1.2
Requires:       perl(Wx) >= 0.5
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module provides the STDOUT, STDERR and exit codes of asynchronously
running processes via events. It may be used for long running or blocking
processes that provide periodic updates on state via STDOUT. Simple IPC is
possible via STDIN.

%prep
%setup -q -n Wx-Perl-ProcessStream-%{version}
chmod -x example/*

%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %enable_test
    xinit /bin/sh -c '%{_bindir}/make test && touch tests.ok' \
        -- %{_bindir}/Xvfb :666
    [ -f tests.ok ] || exit 1
%endif

%files
%doc Changes example README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-16
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-13
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-11
- Perl 5.24 rebuild

* Tue Feb 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-10
- Package cleanup

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-8
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.32-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.32-2
- Perl 5.16 rebuild

* Fri Apr  6 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.32-1
- 0.32 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.30-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump
- Remove BuildRoot stuff

* Fri Dec 03 2010 Petr Pisar <ppisar@redhat.com> - 0.29-1
- 0.29 bump
- Enable tests by running own X server

* Wed Sep 22 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.28-1
- update, works with Wx > 0.97

* Tue Jun  1 2010 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump (0.26 breaks API, do not backport to stable distributions)
- Sort dependencies and parametrize make test
- Remove executable bit from examples in documentation

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.24-2
- Mass rebuild with perl-5.12.0

* Mon Feb  8 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.24-1
- update

* Wed Dec 23 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.22-1
- update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  4 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.11-1
- add BR, remove checking gtk
- Specfile autogenerated by cpanspec 1.77.
