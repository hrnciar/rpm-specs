Name:           perl-Text-RecordParser
Version:        1.6.5
Release:        17%{?dist}
Summary:        Read record-oriented files
License:        GPLv2
URL:            https://metacpan.org/release/Text-RecordParser
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCLARK/Text-RecordParser-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::TabularDisplay)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This module is for reading record-oriented data in a delimited text file.
The most common example have records separated by newlines and fields
separated by commas or tabs, but this module aims to provide a consistent
interface for handling sequential records in a file however they may be
delimited. Typically this data lists the fields in the first line of the
file, in which case you should call bind_header to bind the field name (or
not, and it will be called implicitly). If the first line contains data,
you can still bind your own field names via bind_fields. Either way, you
can then use many methods to get at the data as arrays or hashes.

%prep
%setup -q -n Text-RecordParser-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST
# Fix shebangs
perl -pi -e 's|^#!perl|#!%{__perl}|' t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man[13]/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-8
- Perl 5.26 rebuild

* Thu May 18 2017 Petr Pisar <ppisar@redhat.com> - 1.6.5-7
- Fix building on Perl without "." in @INC (CPAN RT#121759)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-2
- Perl 5.22 rebuild

* Thu Apr 23 2015 Petr Šabata <contyk@redhat.com> - 1.6.5-1
- 1.6.5 bump
- Update source URL

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.3-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 10 2013 Petr Šabata <contyk@redhat.com> - 1.6.3-1
- 1.6.3 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 1.5.0-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.5.0-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.5.0-2
- Perl mass rebuild

* Sat May 07 2011 Iain Arnell <iarnell@gmail.com> 1.5.0-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.3.0-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.3.0-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.3.0-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.3.0-1
- auto-update to 1.3.0 (by cpan-spec-update 0.01)
- added a new br on perl(List::Util) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.1-4
- rebuild for new perl

* Wed May 16 2007 Chris Weyl <cweyl@alumni.drew.edu> v1.2.1-3
- bump

* Wed May 16 2007 Chris Weyl <cweyl@alumni.drew.edu> v1.2.1-2
- additional BR for test suite: perl(IO::Scalar)

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> v1.2.1-1
- Specfile autogenerated by cpanspec 1.71.
