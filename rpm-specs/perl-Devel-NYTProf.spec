Name:           perl-Devel-NYTProf
Version:        6.06
Release:        9%{?dist}
Summary:        Powerful feature-rich perl source code profiler
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-NYTProf
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMB/Devel-NYTProf-%{version}.tar.gz
Patch1:         Devel-NYTProf-6.06-Unbundled-flamegraph.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flamegraph
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  zlib-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# Unused BuildRequires:  perl(ActiveState::Browser)
# Unused BuildRequires:  perl(Apache)
BuildRequires:  perl(base)
# Unused BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
# Unused BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(AutoSplit)
# Unused BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Sub::Name) >= 0.11
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
# Unneded Requires:       perl(Apache)
# Optional features
Suggests:       perl(Browser::Open)
Suggests:       perl(JSON::MaybeXS)
Requires:       flamegraph

%{?perl_default_filter}

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

%prep
%setup -q -n Devel-NYTProf-%{version}
%patch1 -p1

# Remove bundled flamegraph.pl
rm -r bin/flamegraph.pl
sed -i -e '/flamegraph.pl\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# remove duplicate installed lib in wrong location
rm -rf %{buildroot}/%{perl_vendorarch}/Devel/auto/
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes HACKING demo README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-7
- Unbundle flamegraph (bug #1781251)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-1
- 6.06 bump

* Tue Mar 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.05-1
- 6.05 bump

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-7
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-1
- 6.04 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-2
- Perl 5.24 rebuild

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-1
- 6.03 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Petr Šabata <contyk@redhat.com> - 6.02-1
- 6.02 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.01-2
- Perl 5.22 rebuild

* Wed Apr 08 2015 Petr Šabata <contyk@redhat.com> - 6.01-1
- 6.01 bump

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 5.07-1
- 5.07 bump
- Modernize the spec and fix the dependency list

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.06-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.06-1
- 5.06 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Iain Arnell <iarnell@gmail.com> 5.05-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 5.00-2
- Perl 5.18 rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 5.00-1
- update to latest upstream version

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 4.25-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 4.23-1
- update to latest upstream version

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 4.09-1
- update to latest upstream version

* Sun Aug 19 2012 Iain Arnell <iarnell@gmail.com> 4.08-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 4.06-7
- Perl 5.16 rebuild

* Tue Jun 12 2012 Iain Arnell <iarnell@gmail.com> 4.06-6
- specify additional build dependencies

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 4.06-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.06-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 03 2010 Iain Arnell <iarnell@gmail.com> 4.06-1
- update to latest upstream version

* Wed Sep 29 2010 jkeating - 4.05-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Iain Arnell <iarnell@gmail.com> 4.05-1
- update to latest upstream
- clean up spec for modern rpmbuild
- reenable t/70-subname.t

* Sun Jul 11 2010 Iain Arnell <iarnell@gmail.com> 4.04-1
- update to latest upstream

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 4.03-1
- update to latest upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 4.02-2
- perftest.pl has been removed from upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 4.02-1
- update to latest upstream

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 4.01-1
- update to latest upstream

* Tue Jun 15 2010 Iain Arnell <iarnell@gmail.com> 4.00-1
- update to latest upstream
- enable zlib support

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.11-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.11-2
- Mass rebuild with perl-5.12.0

* Wed Mar 17 2010 Iain Arnell <iarnell@gmail.com> 3.11-1
- update to latest upstream version
- BR perl(Sub::Name)

* Sun Mar 07 2010 Iain Arnell <iarnell@gmail.com> 3.02-1
- update to latest upstream version
- requires perl(JSON::Any)

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 3.01-1
- update to latest upstream version
- use perl_default_filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.10-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Iain Arnell <iarnell@gmail.com> 2.10-1
- update to latest upstream version

* Fri Apr 10 2009 Iain Arnell <iarnell@gmail.com> 2.09-1
- update to latest upstream

* Tue Mar 17 2009 Iain Arnell 2.08-1
- Specfile autogenerated by cpanspec 1.77.
- strip private perl libs from provides
- add scripts and man pages to files
