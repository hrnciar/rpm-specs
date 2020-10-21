# Recommend RDF::Trine::Node::Literal::XML for RDFied XML literals
%bcond_without perl_XML_Atom_OWL_enables_literal

Name:           perl-XML-Atom-OWL
Version:        0.104
Release:        6%{?dist}
Summary:        Parse an Atom file into RDF
# CONTRIBUTING: CC-BY-SA
# COPYRIGHT:    Public Domain
# LICENSE:      GPL+ or Artistic
License:        (GPL+ or Artistic) and CC-BY-SA and Public Domain
URL:            https://metacpan.org/release/XML-Atom-OWL
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-Atom-OWL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Carp) >= 1.00
BuildRequires:  perl(common::sense)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Link::Parser) >= 0.100
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI) >= 1.30
BuildRequires:  perl(XML::LibXML) >= 1.70
# Optional run-time:
# RDF::Trine::Node::Literal::XML not used at tests
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if %{with perl_XML_Atom_OWL_enables_literal}
Recommends:     perl(RDF::Trine::Node::Literal::XML)
%endif

%description
This Perl module parses an Atom file into an RDF tree.

%prep
%setup -q -n XML-Atom-OWL-%{version}

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS examples README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.104-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.104-2
- Perl 5.30 rebuild

* Thu May 02 2019 Petr Pisar <ppisar@redhat.com> 0.104-1
- Specfile autogenerated by cpanspec 1.78.
