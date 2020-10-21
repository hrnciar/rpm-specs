Name:           perl-Data-Dump-Streamer
Version:        2.40
Release:        16%{?dist}
Summary:        Accurately serialize a data structure as Perl code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Dump-Streamer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Dump-Streamer-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(B::Utils) >= 0.05
BuildRequires:  perl(bytes)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(PadWalker) >= 0.99
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Test Suite
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(bytes)
Requires:       perl(Compress::Zlib)
Requires:       perl(Hash::Util)
Requires:       perl(MIME::Base64)
Requires:       perl(PadWalker) >= 0.99
Requires:       perl(re)

%global __provides_exclude ::_::|Streamer\\.so
%global __requires_exclude ::_::

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one. Self-referential structures, closures, and objects are
output correctly.

%prep
%setup -q -n Data-Dump-Streamer-%{version}

%build
perl Build.PL DDS --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/Data/
%{perl_vendorarch}/DDS.pm
%{_mandir}/man3/Data::Dump::Streamer.3*
%{_mandir}/man3/DDS.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Petr Pisar <ppisar@redhat.com> - 2.40-13
- Require Hash::Util

* Fri Oct 18 2019 Paul Howarth <paul@city-fan.org> - 2.40-12
- Spec tidy-up
  - Use author-independent source URL
  - Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 30 2016 Paul Howarth <paul@city-fan.org> - 2.40-1
- Update to 2.40
  - Fix up issues with JSON and with non-Padwalker builds
  - Various other tweaks and cleanups to build on newer Perls
  - Updated meta files, etc.

* Thu Jul 28 2016 Paul Howarth <paul@city-fan.org> - 2.39-2
- Incorporate package re-review comments (#1359495)
  - BR:/R: perl(re)
  - Specify version requirement for perl(B::Utils) [≥0.05]
  - R: perl(bytes)

* Sat Jul 23 2016 Paul Howarth <paul@city-fan.org> - 2.39-1
- Update to 2.39
- Add fix for JSON::XS ≥ 3.02 (CPAN RT#112960)
- Classify buildreqs by usage
- General tidy-up and modernization

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.38-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.38-1
- 2.38 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.36-1
- Update to latest upstream version
- Fix build with JSON::XS ≥ 3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.34-5
- Perl 5.18 rebuild
- Perl 5.18 compatibility (CPAN RT#82958)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 2.34-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> - 2.34-1
- Update to latest upstream version

* Tue Apr 03 2012 Iain Arnell <iarnell@gmail.com> - 2.33-1
- Update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> - 2.32-4
- Perl mass rebuild

* Wed Jul 20 2011 Iain Arnell <iarnell@gmail.com> - 2.32-3
- Update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.32-2
- Perl mass rebuild

* Sun Feb 20 2011 Iain Arnell <iarnell@gmail.com> - 2.32-1
- Update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> - 2.31-1
- Update to latest upstream version

* Sun Jan 30 2011 Iain Arnell <iarnell@gmail.com> - 2.25-1
- Update to latest upstream version

* Fri Jan 21 2011 Iain Arnell <iarnell@gmail.com> - 2.23-1
- Update to latest upstream version

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun Jul 18 2010 Iain Arnell <iarnell@gmail.com> - 2.22-1
- Update to 2.22
- Enable DDS shortcut
- Update spec for modern rpmbuild

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> - 2.21-1
- Update to latest upstream

* Mon Jun 14 2010 Iain Arnell <iarnell@gmail.com> - 2.18-1
- Update to latest upstream
- Convert to Module::Build
- Use filtering macros

* Tue Apr 06 2010 Iain Arnell <iarnell@gmail.com> - 2.13-1
- Update to latest upstream
- Drop madness.t patch

* Mon Apr 05 2010 Iain Arnell <iarnell@gmail.com> - 2.11-1
- Update to 2.11 (perl 5.12 compatibility tweaks)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.09-4
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Iain Arnell <iarnell@gmail.com> - 2.09-2
- Fix FTBFS by patching t/madness.t (due to CPAN RT#44610)

* Sat Apr 04 2009 Iain Arnell <iarnell@gmail.com> - 2.09-1
- Update to latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Iain Arnell <iarnell@gmail.com> - 2.08-1
- Specfile autogenerated by cpanspec 1.77
- Strip private provides/requires
