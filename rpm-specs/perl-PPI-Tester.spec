Name:           perl-PPI-Tester
Version:        0.15
Release:        20%{?dist}
Summary:        A wxPerl-based interactive PPI debugger/tester

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PPI-Tester
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/PPI-Tester-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install::DSL) >= 0.86
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::Dumpvar) >= 0.04
BuildRequires:  perl(PPI) >= 1.201
BuildRequires:  perl(PPI::Dumper) >= 1.000
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(Wx) >= 0.85
BuildRequires:  perl(Wx::Event)
# Wx::Frame not used at tests time
# Tests:
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Script) >= 1.02
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Wx::Frame)

%description
This package implements a wxWindows desktop application which provides
the ability to interactively test the PPI perl parser.


%prep
%setup -q -n PPI-Tester-%{version}
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST


%build
# Hack, we work around weirdness in Wx probing.
%{__perl} Makefile.PL INSTALLDIRS=vendor || :
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
xvfb-run -a make test



%files
%doc Changes LICENSE README
%{_bindir}/*
%{perl_vendorlib}/PPI/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-10
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.15-2
- Perl 5.18 rebuild

* Wed Feb 27 2013 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.06-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.06-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-10
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-5
- hack: work around Wx probing issues

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-4
- add BR: Test::More

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-3
- rebuild for new perl

* Wed Oct  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-2
- Added missing BR perl(ExtUtils::AutoInstall).
- Changed the build process: Build.PL -> Makefile.PL
  (Build.PL just requires Makefile.PL).

* Sun Sep 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-1
- First build.
