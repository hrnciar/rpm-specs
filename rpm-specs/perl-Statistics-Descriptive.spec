Name:           perl-Statistics-Descriptive
Version:        3.0800
Release:        1%{?dist}
Summary:        Perl module of basic descriptive statistical functions
# lib/Statistics/Descriptive.pm:            GPL+ or Artistic
# lib/Statistics/Descriptive/Full.pm:       GPL+ or Artistic
# lib/Statistics/Descriptive/Sparse.pm:     GPL+ or Artistic
# lib/Statistics/Descriptive/Smoother*:     MIT
# t/lib/Utils.pm:                           MIT
# examples/statistical-analysis.pl:         MIT
License:        (GPL+ or Artistic) and MIT
URL:            https://metacpan.org/release/Statistics-Descriptive
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%{?perl_default_filter}

%description
This module provides basic functions used in descriptive statistics. It has
an object oriented design and supports two different types of data storage
and calculation objects: sparse and full. With the sparse method, none of
the data is stored and only a few statistical measures are available. Using
the full method, the entire data set is retained and additional functions
are available.

%prep
%setup -q -n Statistics-Descriptive-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README UserSurvey.txt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0800-1
- 3.0800 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0702-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0702-7
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0702-6
- Add missing BR

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0702-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0702-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0702-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0702-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0702-1
- 3.0702 bump

* Mon Jul 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0701-1
- 3.0701 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0613-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0613-2
- Perl 5.28 rebuild

* Thu May 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0613-1
- 3.0613 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0612-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0612-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.0612-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0612-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.0612-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Petr Šabata <contyk@redhat.com> - 3.0612-1
- 3.0612 bump, just a metadata update

* Fri Jan 08 2016 Petr Šabata <contyk@redhat.com> - 3.0611-1
- 3.0611 bump

* Thu Sep 24 2015 Petr Šabata <contyk@redhat.com> - 3.0609-1
- 3.0609 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.0608-2
- Perl 5.22 rebuild

* Tue Feb 03 2015 Petr Pisar <ppisar@redhat.com> - 3.0608-1
- 3.0608 bump

* Mon Nov 24 2014 Petr Pisar <ppisar@redhat.com> - 3.0607-1
- 3.0607 bump
- License changed to ((GPL+ or Artistic) and MIT)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.0604-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0604-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0604-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 3.0604-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0604-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 3.0604-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0603-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 3.0603-2
- Perl 5.16 rebuild

* Fri May 18 2012 Iain Arnell <iarnell@gmail.com> 3.0603-1
- update to latest upstream version

* Fri Mar 02 2012 Iain Arnell <iarnell@gmail.com> 3.0400-1
- update to latest upstream version

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 3.0300-1
- update to latest upstream version

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 3.0203-1
- update to latest upstream version

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 3.0202-1
- update to latest upstream

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.0201-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 03 2010 Iain Arnell <iarnell@gmail.com> 3.0201-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 3.0200-1
- update to latest upstream

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 3.0101-1
- update to latest upstream

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.0100-2
- Mass rebuild with perl-5.12.0

* Sat May 01 2010 Iain Arnell <iarnell@gmail.com> 3.0100-1
- update to latest upstream

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.6-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 29 2006 Patrice Dumas <pertusus at free.fr> - 2.6-2
- Rebuild for FC6

* Fri Jul 14 2006 Patrice Dumas <pertusus at free.fr> - 2.6-1
- Submit to Fedora Extras.

* Mon Mar 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.6-0.2
- Rebuild.

* Fri Jun  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.6-0.1
- Rebuild for FC4.

* Sat Jun 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6-0.fdr.2
- Bring up to date with current fedora.us Perl spec template.

* Mon Oct 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6-0.fdr.1
- First build.
