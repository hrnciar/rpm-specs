Name:           perl-Config-General
Version:        2.63
Release:        12%{?dist}
Summary:        Generic configuration module for Perl

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Config-General
Source0:        https://cpan.metacpan.org/authors/id/T/TL/TLINDEN/Config-General-%{version}.tar.gz
Patch0:         %{name}-2.50-system-ixhash.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(constant)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module opens a config file and parses its contents for
you. After parsing the module returns a hash structure which contains
the representation of the config file.
The format of config files supported by Config::General is inspired by
the well known Apache config format, in fact, this module is 100%
read-compatible with Apache config files, but you can also just use simple
name/value pairs in your config files.
In addition to the capabilities of an Apache config file it supports
some enhancements such as here-documents, C-style comments or
multiline options. It is also possible to save the config back to
disk, which makes the module a perfect backend for configuration
interfaces.
It is possible to use variables in config files and there exists also
support for object oriented access to the configuration.


%prep
%setup -q -n Config-General-%{version}
%patch0 -p1
rm -r t/Tie # see patch0
f=Changelog ; iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f ; mv $f.utf8 $f


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test



%files
%doc Changelog README example.cfg
%{perl_vendorlib}/Config/
%{_mandir}/man3/Config::*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.63-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.63-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.63-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.63-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.63-1
- 2.63 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.61-2
- Perl 5.24 rebuild

* Tue Apr 19 2016 Nathanael Noblet <nathanael@noblet.ca> - 2.61-1
- New upstream release 2.61
- Rebased the system qt patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Nathanael Noblet <nathanael@noblet.ca> - 2.60-1
- New upstream release 2.60

* Fri Aug 28 2015 Petr Pisar <ppisar@redhat.com> - 2.58-1
- 2.58 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.56-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.56-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Nathanael Noblet <nathanael@noblet.ca> - 2.56-1
- Upstream new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.52-1
- 2.52 bump

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.51-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.51-1
- Update to 2.51.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.50-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.50-7
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Petr Pisar <ppisar@redhat.com> - 2.50-5
- Build-require Carp because Carp dual-lives now (bug #736768)

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.50-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.50-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec  2 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.50-1
- Update to 2.50, fixes #658945, #659046.

* Tue Jun 29 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.49-2
- Rebuild.

* Tue Jun  8 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.49-1
- Update to 2.49 (#601611).

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.48-2
- Mass rebuild with perl-5.12.0

* Fri Apr 23 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.48-1
- Update to 2.48.
- Sync with current rpmdevtools Perl spec template.

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.44-2
- rebuild against perl 5.10.1

* Tue Sep  8 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.44-1
- Update to 2.44 (#521756).
- Prune pre-2005 %%changelog entries.

* Sun Jul 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.43-1
- Update to 2.43 (#513796).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan  4 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.42-1
- 2.42.
- Patch test suite to use system installed Tie::IxHash.
- Fix some spelling errors in %%description.
- Use Source0: instead of Source:.

* Sat Jun 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.40-1
- 2.40.

* Tue Jun 17 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.39-1
- 2.39.

* Tue Mar  4 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.38-1
- 2.38.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.37-2
- rebuild for new perl

* Tue Nov 27 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.37-1
- 2.37 (#398801).
- Convert docs to UTF-8.

* Tue Aug  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.33-2
- License: GPL+ or Artistic

* Wed Apr 18 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.33-1
- 2.33.
- BuildRequire perl(ExtUtils::MakeMaker) and perl(Test::More).

* Sat Feb 24 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.32-1
- 2.32.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.31-2
- Fix order of arguments to find(1).
- Drop version from perl build dependency.

* Thu Jan 12 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.31-1
- 2.31.

* Fri Sep 16 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.30-1
- 2.30.

* Wed May 18 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.28-2
- 2.28.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.27-2
- rebuilt
