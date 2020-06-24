Name:           perl-Search-Xapian
Version:        1.2.25.2
Release:        6%{?dist}
Summary:        Xapian perl bindings
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Search-Xapian
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLLY/Search-Xapian-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  xapian-core-devel
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests:
BuildRequires:  perl(threads)
BuildRequires:  perl(Test::Pod) >= 1.14
# Test::Pod::Coverage 1.04 not used
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module wraps most methods of most Xapian classes. The missing classes
and methods should be added in the future. It also provides a simplified,
more 'perlish' interface to some common operations, as demonstrated above.


%prep
%setup -q -n Search-Xapian-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# the pod coverage tests fail
TEST_POD=1 make test


%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.25.2-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.25.2-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.25.2-1
- Update to 1.2.25.2

* Sun Jul 15 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.25.1-1
- Update to 1.2.25.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.25.0-4
- Perl 5.28 rebuild

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.25.0-3
- Add gcc-c++ as a missing build-requirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.25.0-1
- Update to 1.2.25.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.24.0-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.24.0-2
- Rebuild against Xapian 1.4

* Sun Oct 02 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.24.0-1
- Update to 1.2.24.0

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.23.0-2
- Perl 5.24 rebuild

* Tue Apr 05 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.23.0-1
- Update to 1.2.23.0
- Pass NO_PACKLIST to Makefile.PL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.22.0-1
- Update to 1.2.22.0

* Wed Oct 14 2015 Petr Pisar <ppisar@redhat.com> - 1.2.21.0-3
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.21.0-1
- Update to 1.2.21.0 (#1230797)

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.19.0-3
- Perl 5.22 rebuild

* Wed Apr 15 2015 Petr Pisar <ppisar@redhat.com> - 1.2.19.0-2
- Rebuild owing to C++ ABI change in GCC-5 (bug #1195353)

* Fri Oct 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.19.0-1
- Update to 1.2.19.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.18.0-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.18.0-1
- Update to 1.2.18.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 16 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.17.0-1
- Update to 1.2.17.0

* Sun Dec 15 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.16.0-1
- Update to 1.2.16.0
- Fix incorrect dates in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Petr Pisar <ppisar@redhat.com> - 1.2.15.0-2
- Perl 5.18 rebuild

* Sun Apr 21 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.15.0-1
- Update to 1.2.15.0

* Sun Mar 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.14.0-1
- Update to 1.2.14.0

* Tue Jan 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.2.10.0-1
- Update to 1.2.10.0
- Add perl default filter
- Clean up URL and Source0
- Remove no-longer-used macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.0.20.0-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0.20.0-6
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0.20.0-5
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0.20.0-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0.20.0-2
- Mass rebuild with perl-5.12.0

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.0.20-1
- Updated to latest 1.0.20

* Wed Jan 13 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.0.17-1
- Updated to latest 1.0.17

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.0.15.0-2
- rebuild against perl 5.10.1

* Sun Sep 13 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.15.0-1
- Updated to 1.0.15 to match xapian-core new updates

* Sun Aug 23 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.11.0-5
- Cleaned %%files section and fixed version in changelog

* Wed Aug 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.11.0-4
- Fixed license issue

* Wed Aug 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.11.0-3
- Fixed version tag

* Tue Aug 11 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.11.0-2
- Updated the license

* Tue Aug 11 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.11.0-1
- Initial version
