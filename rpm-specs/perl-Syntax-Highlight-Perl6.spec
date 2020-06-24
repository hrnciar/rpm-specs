Name:           perl-Syntax-Highlight-Perl6
Version:        0.88
Release:        27%{?dist}
Summary:        Perl 6 Syntax Highlighter
License:        (GPL+ or Artistic) and Artistic 2.0 and (MIT or GPLv2) 
URL:            https://metacpan.org/release/Syntax-Highlight-Perl6
Source0:        https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Syntax-Highlight-Perl6-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires:  perl(File::ShareDir::Install) >= 0.03
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(open)
BuildRequires:  perl(STD) >= 32116
BuildRequires:  perl(Term::ANSIColor) >= 2.00
BuildRequires:  perl(utf8)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(Encode)
Requires:       perl(File::ShareDir)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(STD) >= 32116
Requires:       perl(Term::ANSIColor)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(STD\\)\s*$

%description
Syntax::Highlight::Perl6 parses Perl 6 source code using an embedded
STD.pm. It matches parse tree nodes to colors then returns them in
different output formats. It can be used to create web pages with colorful
source code samples in its simple and snippet HTML modes, or it can be used
as a learning tool in examining STD.pm's output using the JavaScript node
viewer in its full HTML mode. Or you can use its parse tree Perl 5 records
to build your next great idea.

%prep
%setup -q -n Syntax-Highlight-Perl6-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_privlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-27
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-24
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-21
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-14
- Specified all build-requires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-12
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.88-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.88-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.88-4
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.88-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Petr Pisar <ppisar@redhat.com> - 0.88-1
- 0.88 bump
- Move to ExtUtils::MakeMaker build system

* Mon Sep 27 2010 Petr Pisar <ppisar@redhat.com> - 0.87-1
- 0.87 bump (RT#61522)

* Tue Sep 21 2010 Petr Pisar <ppisar@redhat.com> - 0.86-1
- 0.86 bump
- Move from ExtUtils::Maker to Module::Build
- Remove useless wrong_interpreter patch
- Move from vendor to core perl paths
- Remove BuildRoot related code
- Package not installed hilitep6 (upstream mistake? RT#61522)
- Correct Summary spelling

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.78-3
- Mass rebuild with perl-5.12.0

* Mon Feb  8 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.78-2
- fix rpmlint complaints

* Thu Feb 04 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.78-1
- Specfile autogenerated by cpanspec 1.78.
