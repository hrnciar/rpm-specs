Name:           perl-Sys-Statistics-Linux
Version:        0.66
Release:        22%{?dist}
Summary:        Front-end module to collect system statistics
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sys-Statistics-Linux
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLOONIX/Sys-Statistics-Linux-%{version}.tar.gz
# https://rt.cpan.org/Public/Bug/Display.html?id=128904
Patch0:         linux-4.18-diskstats.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Sys::Statistics::Linux is a front-end module and gather different linux
system information like processor workload, memory usage, network and disk
statistics and a lot more. Refer the documentation of the distribution
modules to get more information about all possible statistics.

%prep
%setup -q -n Sys-Statistics-Linux-%{version}
%patch0 -p1

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ChangeLog README
%license LICENCE
%{perl_vendorlib}/Sys*
%{_mandir}/man3/Sys*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-22
- Perl 5.32 rebuild

* Wed Apr 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.66-21
- Use /usr/bin/perl instead of %%{__perl}
- Use license tag
- Patch DiskStats.pm to take into account new fields (#1819677)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-18
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-15
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.66-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.66-1
- Update to 0.66
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.59-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.59-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.59-3
- Drag Time::HiRes in BR

* Tue Dec 14 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.59-2
- Spelling fix

* Sun Dec 12 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.59-1
- Run tests
- Later release

* Fri Nov 26 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.42-2
- BR Test::More

* Mon Oct 06 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.42-1
- Specfile autogenerated by cpanspec 1.77.
- Fixed build-time requires
