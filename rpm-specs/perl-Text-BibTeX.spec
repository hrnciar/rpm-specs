Name:           perl-Text-BibTeX
Version:        0.88
Release:        6%{?dist}
Summary:        Interface to read and parse BibTeX files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-BibTeX
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Text-BibTeX-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf) >= 0.16
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
# These don't work?  perl(Scalar::List::Utils), perl(Scalar::Util)
BuildRequires:  perl-Scalar-List-Utils >= 1.42
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl-Scalar-List-Utils >= 1.42

%description
The Text::BibTeX module processes BibTeX data.  It includes object-oriented
interfaces to both BibTeX database files and individual bibliographic
entries, as well as other miscellaneous functions.

%prep
%setup -q -n Text-BibTeX-%{version}
chmod a-x scripts/* examples/*

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

%check
./Build test

%files
%doc Changes examples README README.OLD scripts THANKS btool_faq.pod
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so
# no devel package needed?
# https://fedoraproject.org/wiki/Packaging:Perl#.h_files_in_module_packages
# Note also that Debian has split off "libbtparse" (and -dev)
%{_includedir}/btparse.h

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-2
- Perl 5.30 rebuild

* Mon Apr 29 2019 Colin B. Macdonald <cbm@m.fsf.org> - 0.88-1
- Version bump (#1704393)

* Sat Apr 06 2019 Colin B. Macdonald <cbm@m.fsf.org> - 0.87-1
- Version bump (#1696957)

* Mon Apr 01 2019 Colin B. Macdonald <cbm@m.fsf.org> - 0.86-1
- Version bump (#1694434)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.85-1
- Version bump (#1485751)

* Tue Aug 29 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.83-1
- Version bump (#1485751)

* Tue Aug 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-1
- 0.81 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-2
- Perl 5.26 rebuild

* Fri Apr 07 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.80-1
- Version bump (#1439774)

* Tue Mar 14 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.79-1
- Version bump (#1431901)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.78-1
- Version bump (#1412105)

* Wed Jan 04 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.77-2
- Patch from upstream for s390 arch (#1400921)

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-1
- 0.77 bump

* Fri Aug 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-1
- 0.76 bump

* Wed Jun 15 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.74-1
- Version bump (#1346644)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.72-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.72-1
- Version bump (#1149256)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.71-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Colin B. Macdonald <cbm@m.fsf.org> 0.71-1
- Version bump, drop old patches

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-6
- Perl 5.22 rebuild

* Thu Apr 30 2015 Jitka Plesnikova <jplesnik@redhat.com> 0.70-5
- Stop using import from UNIVERSAL (RT#104119)

* Sat Dec 13 2014 Dan Horák <dan[at]danny.cz> 0.70-4
- fix build on non-x86 64-bit arches

* Sat Nov 22 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.70-3
- install faq file.
- no need to split out btparse (used to be a standalone library but is
  now a part of this package).

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.70-2
- revision from other feedback on other packages, clean up.

* Fri Oct 03 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.70-1
- Version bump.

* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.69-1
- Changes file changed case.
- Add a TODO for the various files doc files.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.64-1
- Specfile autogenerated by cpanspec 1.78.
