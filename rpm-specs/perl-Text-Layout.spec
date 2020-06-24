# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName Text-Layout

Name: perl-%{FullName}
Summary: Pango style text formatting
License: (GPL+ or Artistic) and Artistic 2.0
Version: 0.018.1
Release: 4%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# note intended for general use.
%global __requires_exclude Text::Layout::Font(Config|Descriptor)
%global __provides_exclude_from /(Cairo|Markdown|Pango|PDFAPI2)\\.pm$

Requires: perl(:VERSION) >= 5.10.1
Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

Recommends: perl(PDF::API2) >= 2.036
Recommends: perl(HarfBuzz::Shaper) >= 0.018

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Basename)
BuildRequires: perl(HarfBuzz::Shaper) >= 0.018
BuildRequires: perl(PDF::API2) >= 2.036
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
Text::Layout provides methods for Pango style text formatting. Where
possible the methods have identical names and (near) identical
behavior as their Pango counterparts.

See https://developer.gnome.org/pango/stable/pango-Layout-Objects.html.

Text::Layout uses backend modules to render the marked up text.
Backends are included for PDF::API2 and PDF::Builder.

The package uses Text::Layout::FontConfig (included) to organize fonts
by description.

If module HarfBuzz::Shaper is installed, Text::Layout can use it for
text shaping.

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.018.1-4
- Perl 5.32 rebuild

* Thu Feb 27 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.1-3
- Incorporate reviewer feedback.
- Upgrade to upstream 0.018.1.
* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018-2
- Incorporate reviewer feedback.
* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018-1
- Incorporate reviewer feedback.
- Upgrade to upstream 0.018.
* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.016-1
- Initial Fedora package.
