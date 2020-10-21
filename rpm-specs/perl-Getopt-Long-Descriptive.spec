Name:           perl-Getopt-Long-Descriptive
Summary:        Getopt::Long with usage text
Version:        0.105
Release:        3%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Getopt-Long-Descriptive
Source0:        https://cpan.metacpan.org/modules/by-module/Getopt/Getopt-Long-Descriptive-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long) >= 2.33
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Validate) >= 0.97
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter) >= 0.972
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Moose::Conflicts)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Convenient wrapper for Getopt::Long and program usage output.

%prep
%setup -q -n Getopt-Long-Descriptive-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Getopt/
%{_mandir}/man3/Getopt::Long::Descriptive.3*
%{_mandir}/man3/Getopt::Long::Descriptive::Opts.3*
%{_mandir}/man3/Getopt::Long::Descriptive::Usage.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.105-2
- Perl 5.32 rebuild

* Wed Feb 26 2020 Paul Howarth <paul@city-fan.org> - 0.105-1
- Update to 0.105
  - one_of sub-options now get accessors

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.104-2
- Perl 5.30 rebuild

* Sun Apr 28 2019 Paul Howarth <paul@city-fan.org> - 0.104-1
- Update to 0.104
  - Allow for verbatim text in description options

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.103-1
- Update to 0.103
  - Show --[no-]option for boolean toggle options

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.102-2
- Perl 5.28 rebuild

* Wed Feb 21 2018 Paul Howarth <paul@city-fan.org> - 0.102-1
- Update to 0.102
  - Long spacer lines are now line broken
  - "Empty" spacer lines no longer have leading whitespace
  - Option specifications ":+" and ":5" (etc.) now get better presentation in
    the usage description

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Paul Howarth <paul@city-fan.org> - 0.101-1
- Update to 0.101
  - Escape some unescaped braces in regex
- Drop legacy Group: tag

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Paul Howarth <paul@city-fan.org> - 0.100-1
- Update to 0.100
  - Show off "shortcircuit" in synopsis
  - Fix rendering of complex types ('i@' → 'INT...', etc.)
- Simplify find command using -delete
- Make %%files list more explicit
- Drop redundant %%{?perl_default_filter}

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.099-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.099-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.099-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.099-2
- Perl 5.22 rebuild

* Tue Feb 03 2015 Petr Pisar <ppisar@redhat.com> - 0.099-1
- 0.099 bump

* Thu Dec 04 2014 Petr Pisar <ppisar@redhat.com> - 0.098-1
- 0.098 bump
- Stop providing dummy tests sub-package symbol

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.093-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 0.093-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 0.093-1
- update to latest upstream version

* Fri Aug 03 2012 Iain Arnell <iarnell@gmail.com> 0.092-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.091-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.091-2
- Perl 5.16 rebuild

* Thu Feb 23 2012 Iain Arnell <iarnell@gmail.com> 0.091-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.090-4
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.090-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.090-2
- Perl mass rebuild

* Sat Jul 02 2011 Iain Arnell <iarnell@gmail.com> 0.090-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.087-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 Iain Arnell <iarnell@gmail.com> 0.087-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.084-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.084-2
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.084-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- added a new br on perl(Getopt::Long) (version 2.33)
- dropped old BR on perl(IO::Scalar)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Getopt::Long) (version 2.33)
- dropped old requires on perl(IO::Scalar)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.077-2
- rebuild against perl 5.10.1

* Sun Aug 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.077-1
- auto-update to 0.077 (by cpan-spec-update 0.01)
- added a new br on perl(List::Util) (version 0)
- added a new br on perl(Sub::Exporter) (version 0)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(Params::Validate) (version 0.74)
- added a new req on perl(Sub::Exporter) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.074-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.074-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.074-2
- bump

* Tue Jul 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.074-1
- Specfile autogenerated by cpanspec 1.74.
