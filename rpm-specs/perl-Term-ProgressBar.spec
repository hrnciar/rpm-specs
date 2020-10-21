Name:           perl-Term-ProgressBar
Version:        2.22
Release:        10%{?dist}
Summary:        Provide a progress meter on a standard terminal
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-ProgressBar
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Term-ProgressBar-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MethodMaker) >= 1.02
BuildRequires:  perl(constant)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadKey) >= 2.14
# Tests only
BuildRequires:  perl(Capture::Tiny) >= 0.13
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.80
BuildRequires:  perl(Test::Warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Term::ReadKey) >= 2.14

%{?perl_default_filter}

%description
Term::ProgressBar provides a simple progress bar on the terminal, to let
the user know that something is happening, roughly how much stuff has been
done, and maybe an estimate at how long remains.

%prep
%setup -q -n Term-ProgressBar-%{version}
for file in examples/*.pl; do
    sed -i 's/\r//' ${file}
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-3
- Perl 5.28 rebuild

* Mon May 14 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-1
- 2.22 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Petr Pisar <ppisar@redhat.com> - 2.21-1
- 2.21 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-1
- 2.20 bump

* Tue Jul 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.19-1
- 2.19 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-1
- 2.18 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.17-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.17-2
- Perl 5.22 rebuild

* Mon Feb 02 2015 Petr Šabata <contyk@redhat.com> - 2.17-1
- 2.17 bump
- Support unknown maximum

* Wed Sep 10 2014 Petr Šabata <contyk@redhat.com> - 2.16-1
- 2.16 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Petr Šabata <contyk@redhat.com> - 2.15-1
- 2.15 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Šabata <contyk@redhat.com> - 2.14-1
- 2.14 bump
- Documentation fixes

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 2.13-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 2.13-2
- Perl 5.16 rebuild

* Fri May 18 2012 Petr Šabata <contyk@redhat.com> - 2.13-1
- 2.13 bump

* Fri Feb 17 2012 Petr Šabata <contyk@redhat.com> - 2.11-1
- 2.11 bump, disables the signature check

* Fri Jan 13 2012 Petr Šabata <contyk@redhat.com> - 2.10-1
- 2.10 bump, switch to EE::MM
- Spec cleanup

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.09-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.09-9
- 648598 add requirement on Term::ReadKey, it add width feature

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.09-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.09-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-4
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-3
- rebuild for new perl

* Tue Sep 19 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.09-2
- bump

* Sat Sep 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 2.09-1
- Specfile autogenerated by cpanspec 1.69.1.
