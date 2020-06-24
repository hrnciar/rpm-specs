Name:           perl-Pod-Weaver
Version:        4.015
Release:        11%{?dist}
Summary:        Weave together a POD document from an outline
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Weaver
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Pod-Weaver-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config::MVP) >= 2
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles)
BuildRequires:  perl(Config::MVP::Reader::Finder)
# An optional INI plugin for Config::MVP::Reader::Finder is required
BuildRequires:  perl(Config::MVP::Reader::INI)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Log::Dispatchouli) >= 1.100710
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Pod::Elemental) >= 0.100220
BuildRequires:  perl(Pod::Elemental::Document)
BuildRequires:  perl(Pod::Elemental::Element::Nested)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Command)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Ordinary)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Region)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Verbatim)
BuildRequires:  perl(Pod::Elemental::Selectors)
BuildRequires:  perl(Pod::Elemental::Transformer::Gatherer)
BuildRequires:  perl(Pod::Elemental::Transformer::Nester)
BuildRequires:  perl(Pod::Elemental::Transformer::Pod5)
BuildRequires:  perl(Pod::Elemental::Types)
BuildRequires:  perl(String::Flogger) >= 1
BuildRequires:  perl(String::Formatter) >= 0.100680
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Text::Wrap)
# Tests:
BuildRequires:  perl(PPI)
BuildRequires:  perl(Software::License::Artistic_1_0)
BuildRequires:  perl(Software::License::Perl_5)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles)
Requires:       perl(Config::MVP::Reader::Finder)
# An optional INI plugin for Config::MVP::Reader::Finder is required
Requires:       perl(Config::MVP::Reader::INI)

%description
Pod::Weaver is a system for building POD documents from templates.
It doesn't perform simple text substitution, but instead builds
a Pod::Elemental::Document. Its plugins sketch out a series of sections
that will be produced based on an existing POD document or other
provided information.

%prep
%setup -q -n Pod-Weaver-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.015-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.015-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.015-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.015-2
- Perl 5.26 rebuild

* Tue Mar 21 2017 Petr Pisar <ppisar@redhat.com> 4.015-1
- Specfile autogenerated by cpanspec 1.78.
