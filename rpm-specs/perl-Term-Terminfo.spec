# Perform optional tests
%bcond_without perl_Term_Terminfo_enables_optional_test
# Parse terminfo database with unibilium instead of ncurses
%bcond_without perl_Term_Terminfo_enables_unibilium

Name:           perl-Term-Terminfo
Version:        0.09
Release:        1%{?dist}
Summary:        Access the terminfo database
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-Terminfo
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Term-Terminfo-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build::Using::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{with perl_Term_Terminfo_enables_unibilium}
BuildRequires:  pkgconfig(unibilium) >= 0.1.0
%else
BuildRequires:  ncurses-devel
BuildRequires:  perl(ExtUtils::CChecker) >= 0.02
%endif
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Term_Terminfo_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Objects in Term::Terminfo Perl class provide access to the terminfo database
entries.

%prep
%setup -q -n Term-Terminfo-%{version}
%if !%{with perl_Term_Terminfo_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{^t/99pod\.t}' MANIFEST
%endif

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Term*
%{_mandir}/man3/*

%changelog
* Wed Sep 30 2020 Petr Pisar <ppisar@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.