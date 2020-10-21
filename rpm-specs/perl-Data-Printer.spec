Name:           perl-Data-Printer
Version:        0.40
Release:        10%{?dist}
Summary:        Pretty printer for Perl data structures
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Printer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Printer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::HomeDir) >= 0.91
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::Util::FieldHash)
# Hash::Util::FieldHash::Compat not used
BuildRequires:  perl(if)
BuildRequires:  perl(mro)
# MRO::Compat not used
BuildRequires:  perl(Package::Stash) >= 0.3
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Term::ANSIColor) >= 3
BuildRequires:  perl(version) >= 0.77
# Win32::Console::ANSI not used
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::HomeDir::Test)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Class::Date)
BuildRequires:  perl(Date::Calc::Object)
BuildRequires:  perl(Date::Handler)
BuildRequires:  perl(Date::Handler::Delta)
BuildRequires:  perl(Date::Pcalc::Object)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::Incomplete)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(IO::Pty::Easy)
BuildRequires:  perl(Time::Piece)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(B)
Requires:       perl(B::Deparse)
Requires:       perl(File::HomeDir) >= 0.91
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(mro)
Requires:       perl(Package::Stash) >= 0.3
Requires:       perl(Term::ANSIColor) >= 3
Requires:       perl(version) >= 0.77

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\((File::HomeDir|Term::ANSIColor)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Package::Stash\\)$

%description
Data::Printer is a Perl module to pretty-print Perl data structures and
objects in full color. It is meant to display variables on screen, properly
formatted to be inspected by a human.

%prep
%setup -q -n Data-Printer-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.26 rebuild

* Wed Apr 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-1
- 0.39 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.24 rebuild

* Mon Mar 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- 0.38 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-3
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-2
- Perl 5.20 rebuild

* Tue Jul 22 2014 David Dick <ddick@cpan.org> - 0.35-1
- Initial release
