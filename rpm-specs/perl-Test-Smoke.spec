Name:           perl-Test-Smoke
Version:        1.78
Release:        2%{?dist}
Summary:        Perl core test smoke suite
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Smoke
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABELTJE/Test-Smoke-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Getopt::Long)
# HTTP::Tiny is not needed for tests
# LWP::Simple is not needed for tests
BuildRequires:  perl(LWP::UserAgent)
# Mail::Sendmail - optional tests - bundled
# BuildRequires:  perl(MIME::Lite)
# Net::FTP is not needed for tests
BuildRequires:  perl(overload)
# Pod::Usage is not needed for tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(System::Info)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Mail::Sendmail)
Requires:       perl(File::Spec) >= 0.82

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Mail::Sendmail\\)

%description
The perl core test smoke suite is a set of scripts and modules that try to run
the perl core tests on as many configurations as possible and combine the
results into an easy to read report.

%prep
%setup -q -n Test-Smoke-%{version}

# Ignore output files from find-debuginfo.sh to fix the test 00-manifest.t
echo '.+\.list' >> MANIFEST.SKIP

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}/%{_bindir}/W32Configure.pl
rm -rf %{buildroot}/%{_mandir}/man1/W32Configure*
rm -rf %{buildroot}/%{perl_vendorlib}/inc/JSON.pm
rm -rf %{buildroot}/%{perl_vendorlib}/inc/Mail/Sendmail.pm

%check
make test

%files
%doc Changes README ReleaseNotes
%{_bindir}/archiverpt.pl
%{_bindir}/chkbcfg.pl
%{_bindir}/configsmoke.pl
%{_bindir}/mailrpt.pl
%{_bindir}/patchtree.pl
%{_bindir}/runsmoke.pl
%{_bindir}/sendrpt.pl
%{_bindir}/smokeperl.pl
%{_bindir}/smokestatus.pl
%{_bindir}/synctree.pl
%{_bindir}/sysinfo.pl
%{_bindir}/tsarchive.pl
%{_bindir}/tsreport.pl
%{_bindir}/tsrunsmoke.pl
%{_bindir}/tssendrpt.pl
%{_bindir}/tssmokeperl.pl
%{_bindir}/tssynctree.pl
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-2
- Perl 5.32 rebuild

* Thu May 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-1
- 1.78 bump

* Thu May 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-1
- 1.77 bump

* Wed May 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-1
- 1.76 bump

* Mon Feb 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-1
- 1.74 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-1
- 1.73 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-2
- Perl 5.28 rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-1
- 1.72 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-1
- 1.71 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-4
- Fix parsing of cpuinfo on aarch64 (CPAN RT#119691)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-3
- Perl 5.24 rebuild

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-2
- Filtered JSON from provides

* Mon May 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-1
- 1.70 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-2
- Perl 5.22 rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- 1.60 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.59-2
- Perl 5.18 rebuild
- find-debuginfo.sh pollutes build directory with more files now

* Mon May 06 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-1
- 1.59 bump, bug-fix release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.53-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Šabata <contyk@redhat.com> - 1.53-1
- 1.53 bump
- Drop command macros

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.47-2
- Perl 5.16 rebuild

* Mon Mar 19 2012 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Iain Arnell <iarnell@gmail.com> 1.44-4
- update filtering for rpm 4.9

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.44-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Petr Sabata <psabata@redhat.com> 1.44-1
- New upstream release, v1.44

* Tue Sep  7 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.43-2
- 630802 filter Mail::Sendmail from provides, require it from RPM

* Fri Mar 26 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.43-1
- Specfile autogenerated by cpanspec 1.78.
