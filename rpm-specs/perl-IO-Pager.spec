# Use File::Which for locating the pager executables
%bcond_without perl_IO_Pager_enables_File_Which
# Use Text::Wrap for wrapping the long lines
%bcond_without perl_IO_Pager_enables_wrap

Name:           perl-IO-Pager
Version:        1.03
Release:        3%{?dist}
Summary:        Select a pager and pipe text to it if destination is a TTY
# The license is something home-made or "the same terms as Perl itself".
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Pager
Source0:        https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/IO-Pager-%{version}.tgz
# Do not use /usr/local/bin for executing perl
Patch0:         IO-Pager-1.02-perl-is-in-usr-bin.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
# B not used at tests
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
# Data::Dumper not used at tests
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Spec)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Term::Cap not used at tests
# Term::ReadKey not used at tests
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(warnings)
# Optional run-time:
%if %{with perl_IO_Pager_enables_File_Which}
BuildRequires:  perl(File::Which)
%endif
# POSIX not used at tests
# Text::Wrap not used at tests
# Tests:
BuildRequires:  perl(bignum)
BuildRequires:  perl(blib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Optional tests:
# PerlIO::Util not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
%if %{with perl_IO_Pager_enables_File_Which}
Recommends:     perl(File::Which)
%endif
Requires:       perl(IO::Handle)
Recommends:     perl(POSIX)
%if %{with perl_IO_Pager_enables_wrap}
Recommends:     perl(Text::Wrap)
%endif

%description
IO::Pager is used to locate an available pager and programmatically decide
whether or not to pipe a file handle's output to the pager.

%prep
%setup -q -n IO-Pager-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.32 rebuild

* Mon Jun 15 2020 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Mon Jun 08 2020 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Tue Oct 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Updated dependencies

* Tue Oct 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- 1.00 bump

* Mon Sep 30 2019 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Mon Sep 30 2019 Petr Pisar <ppisar@redhat.com> - 0.43-1
- 0.43 bump

* Fri Sep 06 2019 Petr Pisar <ppisar@redhat.com> - 0.42-1
- 0.42 bump
- IO::Pager::Perl was removed due to a dependency on Term::Pager that has
  a non-free license (CPAN RT#130460)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 0.39-1
- 0.39 bump

* Fri May 12 2017 Petr Pisar <ppisar@redhat.com> - 0.38-1
- 0.38 bump

* Wed Apr 26 2017 Petr Pisar <ppisar@redhat.com> - 0.37-1
- 0.37 bump

* Tue Mar 14 2017 Petr Pisar <ppisar@redhat.com> 0.36-1
- Specfile autogenerated by cpanspec 1.78.
