Name:           perl-CPAN-Uploader
Version:        0.103015
Release:        1%{?dist}
Summary:        Upload things to the CPAN
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CPAN-Uploader
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Uploader-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
# Unused BuildRequires:  perl(Config::Identity)
# Unused BuildRequires:  perl(Data::Dumper)
# Unused BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
# Unused BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
# Unused BuildRequires:  perl(LWP::Protocol::https) >= 1
BuildRequires:  perl(LWP::UserAgent)
# Unused BuildRequires:  perl(Term::ReadKey)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5)
Requires:       perl(LWP::Protocol::https) >= 1
Requires:       perl(Term::ReadKey)

# cpan-upload replaced by perl-CPAN-Uploader, bugs #1043581, #1095426
Provides:       cpan-upload = 2.2-17
Obsoletes:      cpan-upload < 2.2-18

%{?perl_default_filter}

%description
CPAN::Uploader is a module which automates the process of uploading a file to
CPAN using PAUSE, the Perl Authors Upload Server.

%prep
%setup -q -n CPAN-Uploader-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Aug 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.103015-1
- 0.103015 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.103014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.103014-2
- Perl 5.32 rebuild

* Mon Jun 08 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.103014-1
- 0.103014 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.103013-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.103013-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.103013-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.103013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.103013-1
- 0.103013 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.103012-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.103012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Petr Šabata <contyk@redhat.com> - 0.103012-1
- 0.103012 bump

* Tue Oct 06 2015 Petr Šabata <contyk@redhat.com> - 0.103011-1
- 0.103011 bump, docs updated

* Wed Aug 12 2015 Petr Šabata <contyk@redhat.com> - 0.103010-1
- 0.103010 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.103009-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Šabata <contyk@redhat.com> - 0.103009-1
- 0.103009 bump

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.103008-2
- Perl 5.22 rebuild

* Mon Feb 09 2015 Petr Šabata <contyk@redhat.com> - 0.103008-1
- 0.103008 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.103007-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Petr Pisar <ppisar@redhat.com> - 0.103007-2
- Obsolete cpan-upload properly (bug #1095426)
- Restore the utility name back to cpan-upload

* Mon May 05 2014 Petr Pisar <ppisar@redhat.com> - 0.103007-1
- 0.103007 bump

* Tue Dec 17 2013 Marcela Mašláňová <mmaslano@redhat.com> - 0.103002-5
- add Obsoletes/Provides to cpan-upload 1043581

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 0.103002-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.103002-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.103001-2
- Perl 5.16 rebuild

* Fri Mar 30 2012 Iain Arnell <iarnell@gmail.com> 0.103001-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.103000-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.103000-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.103000-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102150-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.102150-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Aug 05 2010 Iain Arnell <iarnell@gmail.com> 0.102150-1
- update to latest upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.101670-1
- update to latest upstream

* Sat Jun 05 2010 Iain Arnell <iarnell@gmail.com> 0.101550-1
- update to latest upstream

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 0.101260-2
- bump release for rebuild with perl-5.12.0

* Sun May 09 2010 Iain Arnell <iarnell@gmail.com> 0.101260-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100760-2
- Mass rebuild with perl-5.12.0

* Thu Apr 08 2010 Iain Arnell <iarnell@gmail.com> 0.100760-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
- tweak requires
