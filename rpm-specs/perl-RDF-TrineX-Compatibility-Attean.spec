Name:           perl-RDF-TrineX-Compatibility-Attean
Version:        0.100
Release:        2%{?dist}
Summary:        Compatibility layer between Attean and RDF::Trine
# COPYRIGHT:    Public Domain
# LICENSE:      GPL+ or Artistic
License:        (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/RDF-TrineX-Compatibility-Attean
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-TrineX-Compatibility-Attean-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(RDF::Trine::Model)
BuildRequires:  perl(RDF::Trine::Node)
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Do not provide private redefinitions
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(RDF::Trine::(Model|Node|Node::Literal|Node::Resource)\\)

%description
This Perl module adds a support for the methods of certain Attean classes to
an RDF::Trine framework.

%prep
%setup -q -n RDF-TrineX-Compatibility-Attean-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Petr Pisar <ppisar@redhat.com> 0.100-1
- Specfile autogenerated by cpanspec 1.78.
