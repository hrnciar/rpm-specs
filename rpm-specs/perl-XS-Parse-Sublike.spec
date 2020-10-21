# Perform optional tests
%bcond_without perl_XS_Parse_Sublike_enables_optional_tests

Name:           perl-XS-Parse-Sublike
Version:        0.10
Release:        1%{?dist}
Summary:        XS functions to assist in parsing sub-like syntax
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XS-Parse-Sublike
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Sublike-%{version}.tar.gz
# Fix an integer overflow in croak(), CPAN RT#133035
Patch0:         XS-Parse-Sublike-0.10-Fix-type-mismatch-in-croak-format-string-width-argum.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(feature)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_XS_Parse_Sublike_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module provides some XS functions to assist in writing parsers for
sub-like syntax, primarily for authors of keyword plugins using the
PL_keyword_plugin hook mechanism.

%prep
%setup -q -n XS-Parse-Sublike-%{version}
%patch0 -p1
%if !%{with perl_XS_Parse_Sublike_enables_optional_tests}
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
%{perl_vendorarch}/XS*
%{_mandir}/man3/*

%changelog
* Wed Jul 22 2020 Petr Pisar <ppisar@redhat.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.