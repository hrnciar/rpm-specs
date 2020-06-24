# Perform optional tests
%bcond_without perl_Attean_enables_optional_test

Name:           perl-Attean
Version:        0.026
Release:        1%{?dist}
Summary:        Semantic web framework
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Attean
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/Attean-%{version}.tar.gz
# Do not use /usr/bin/env in shebangs,
# <https://github.com/kasei/attean/pull/117>, refused by the upstream
Patch0:         Attean-0.017-Canonize-shebangs.patch
# Disable changelog generator and other not helpful dependencies
Patch1:         Attean-0.018-Disable-unwanted-build-time-dependecies.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny) >= 1
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(IRI) >= 0.005
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::Cartesian::Product) >= 1.008
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moo) >= 2.000002
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Log::Any)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(open)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Role::Tiny) >= 2.000003
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(sort)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util) >= 1.4
BuildRequires:  perl(Test::Modern) >= 0.012
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::Roo::Role)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Type::Tiny::Role)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Namespace)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(Types::UUID)
BuildRequires:  perl(URI::Escape) >= 1.36
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::Namespace)
BuildRequires:  perl(URI::NamespaceMap) >= 0.12
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::Simple)
# Tests:
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Roo)
%if %{with perl_Attean_enables_optional_test}
# Optional tests:
BuildRequires:  perl(RDF::Trine)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter::Tiny) >= 1
Requires:       perl(IRI) >= 0.005
Requires:       perl(Math::Cartesian::Product) >= 1.008
Requires:       perl(Moo) >= 2.000002
Requires:       perl(MooX::Log::Any)
Requires:       perl(Role::Tiny) >= 2.000003
Requires:       perl(sort)
Requires:       perl(Sub::Util) >= 1.4
Requires:       perl(URI::Escape) >= 1.36
Requires:       perl(URI::NamespaceMap) >= 0.12
# Provide collections of modules defined in one file.
# This is a public API, see Attean::API::Query POD.
# Search for "utility package" in the sources.
Provides:       perl(Attean::Algebra) = %{version}
Provides:       perl(Attean::API::Query) = %{version}
Provides:       perl(Attean::Expression) = %{version}
Provides:       perl(Attean::Plan) = %{version}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|IRI|Math::Cartesian::Product|Moo|Role::Tiny|Sub::Util|Test::Modern|URI::Escape|URI::NamespaceMap)\\)

%description
Attean provides APIs for parsing, storing, querying, and serializing semantic
web (RDF and SPARQL) data.

%package tests
Summary:        Modules for testing Attean semantic web framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test::Modern) >= 0.012

%description tests
These are helper Perl modules for testing Attean, a semantic web framework.

%prep
%setup -q -n Attean-%{version}
%patch0 -p1
%patch1 -p1
# Remove bundled modules
rm -r inc/*
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING README.md
%{_bindir}/*
%{perl_vendorlib}/Attean*
%{perl_vendorlib}/Types
%{_mandir}/man3/Attean*
%{_mandir}/man3/Types::*

%files tests
%{perl_vendorlib}/Test/*

%changelog
* Thu Feb 20 2020 Petr Pisar <ppisar@redhat.com> - 0.026-1
- 0.026 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Petr Pisar <ppisar@redhat.com> - 0.025-1
- 0.025 bump

* Mon Sep 23 2019 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-2
- Perl 5.30 rebuild

* Thu May 02 2019 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Fri Mar 22 2019 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Mon Feb 18 2019 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Jan 11 2018 Petr Pisar <ppisar@redhat.com> - 0.018-2
- Provide Perl module collections as an RPM symbol

* Mon Jan 08 2018 Petr Pisar <ppisar@redhat.com> 0.018-1
- Specfile autogenerated by cpanspec 1.78.
