Name:           perl-RDF-Query
Version:        2.918
Release:        14%{?dist}
Summary:        SPARQL 1.1 Query and Update implementation for RDF::Trine
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/RDF-Query
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/RDF-Query-%{version}.tar.gz
# Do not run author tests
Patch0:         RDF-Query-2.917-Disable-author-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# None of the ./bin scripts is executed at tests
BuildRequires:  perl(base)
# Benchmark not used at tests
BuildRequires:  perl(Carp)
# CGI not used at tests
BuildRequires:  perl(constant)
# Cwd not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl)
# LWP::MediaTypes not used at tests
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(POSIX)
# RDF::Endpoint::Server does not exist
# <https://github.com/kasei/perlrdf/issues/139>
BuildRequires:  perl(RDF::Trine) >= 1.004
BuildRequires:  perl(RDF::Trine::Iterator)
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(RDF::Trine::Node::Variable)
BuildRequires:  perl(RDF::Trine::Statement)
BuildRequires:  perl(RDF::Trine::Statement::Quad)
BuildRequires:  perl(RDF::Trine::VariableBindings)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(sort)
BuildRequires:  perl(Storable)
# Term::ReadKey not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
# Optional run-time:
BuildRequires:  perl(Geo::Distance) >= 0.09
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(Test::JSON)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(CGI)
Requires:       perl(Exporter)
Recommends:     perl(Geo::Distance) >= 0.09
Requires:       perl(JSON) >= 2
Requires:       perl(URI) >= 1.52

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((JSON|URI)\\)$

%description
RDF::Query allows SPARQL and RDQL queries to be run against an RDF model,
returning rows of matching results.

%prep
%setup -q -n RDF-Query-%{version}
%patch0 -p1
# Remove bundled modules, but keep the directory to prevent from runing author
# tests.
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST
# Remove executable bits from documentation
find examples -type f -exec chmod -x {} +
# Fix shellbangs
for F in bin/rqsh examples/*.pl; do
    sed -i -e '1 s|^#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc examples Changes.ttl README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Petr Pisar <ppisar@redhat.com> - 2.918-11
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Petr Pisar <ppisar@redhat.com> - 2.918-1
- 2.918 bump

* Thu Oct 27 2016 Petr Pisar <ppisar@redhat.com> 2.917-1
- Specfile autogenerated by cpanspec 1.78.
