# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
%bcond_with ucdtest

Name:           perl-Text-Bidi
Version:        2.15
Release:        8%{?dist}
Summary:        Unicode bidirectional algorithm using libfribidi
# LICENSE:          GPL+ or Artistic
## not in the binary package
# t/BidiTest.txt:   Unicode
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-Bidi
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAMENSKY/Text-Bidi-%{version}.tar.gz
# bidi is a plugin, CPAN RT#108737
Patch0:         Text-Bidi-2.12-Remove-script-attributes-from-bidi.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Prefer pkgconfig for locating fribidi
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  swig
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Tie::Array)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(charnames)
%if %{with ucdtext}
BuildRequires:  perl(Data::Dumper)
%endif
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta 2.120900 not useful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This Perl module provides basic support for the Unicode bidirectional (Bidi)
text algorithm, for displaying text consisting of both left-to-right and
right-to-left written languages (such as Hebrew and Arabic.) It does so via
a SWIG interface file to the libfribidi library.

%package urxvt
Summary:        Unicode bidirectional text support for urxvt
License:        GPL+ or Artistic
Requires:       perl(Encode)
Requires:       perl(Text::Bidi)
Requires:       perl(Text::Bidi::Constants)
Requires:       rxvt-unicode

%description urxvt
This extension filters the text displayed by Urxvt, so that Bi-directional 
text (e.g., Hebrew or Arabic mixed with English) is displayed correctly.

%prep
%setup -q -n Text-Bidi-%{version}
%patch0 -p1
# Delete SWIG-generated files
rm private.c lib/Text/Bidi/private.pm
perl -i -ne 'print $_ unless m{^private\.c}' MANIFEST
perl -i -ne 'print $_ unless m{^lib/Text/Bidi/private\.pm}' MANIFEST
# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
%if !%{with ucdtext}
rm t/ucd.t
perl -i -ne 'print $_ unless m{^t/ucd\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
find $RPM_BUILD_ROOT -type f -name '*.3pm' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libdir}/urxvt/perl
install -m 0644 -t ${RPM_BUILD_ROOT}%{_libdir}/urxvt/perl misc/bidi

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files urxvt
%license LICENSE
%{_libdir}/urxvt/perl/bidi

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Petr Pisar <ppisar@redhat.com> - 2.15-5
- Build-require blib for tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Petr Pisar <ppisar@redhat.com> - 2.15-1
- 2.15 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-10
- Perl 5.28 rebuild

* Tue Jun 05 2018 Petr Pisar <ppisar@redhat.com> - 2.12-9
- Remove empty Text::Bidi::private(3pm) manual page

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 2.12-8
- Rebuild with new redhat-rpm-config/perl build flags

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 2.12-7
- Adapt to fribidi-1.0 (CPAN RT#124618)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Petr Pisar <ppisar@redhat.com> - 2.12-1
- 2.12 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> 2.11-1
- Specfile autogenerated by cpanspec 1.78.
