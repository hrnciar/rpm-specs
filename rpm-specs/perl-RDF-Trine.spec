# Add support for a MySQL database
%bcond_without perl_RDF_Trine_enables_mysql
# Add support for a PostgreSQL database
%bcond_without perl_RDF_Trine_enables_postgresql
# Add support for a Redis database
%bcond_without perl_RDF_Trine_enables_redis
# Add support for a Redland database
%bcond_without perl_RDF_Trine_enables_redland
# Add support for a SQLite database
%bcond_without perl_RDF_Trine_enables_sqlite

Name:           perl-RDF-Trine
Version:        1.019
Release:        9%{?dist}
Summary:        RDF Framework for Perl
# README:           GPLv+ or Artistic
# lib/RDF/Trine.pm: GPLv+ or Artistic
## Not in binary package
# t/data/turtle-2013/LICENSE:               BSD or W3C Test Suite License
# t/data/rdfxml-w3c/xmlsch-02/test003.rdf:  W3C
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/RDF-Trine
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/RDF-Trine-%{version}.tar.gz
# Remove unwanted build script features
Patch0:         RDF-Trine-1.016-Disable-release-code.patch
# Load only installed database backends. Otherwise we would have to require
# all of them.
Patch1:         RDF-Trine-1.014-Make-database-backends-optional.patch
BuildArch:      noarch
BuildRequires:  coreutils
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
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(base)
# Cache::LRU not used at tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
# DBD::mysql not used at tests
# DBD::Pg not used at tests
BuildRequires:  perl(DBD::SQLite) >= 1.14
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
# GraphViz not used at tests
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IRI)
BuildRequires:  perl(JSON) >= 2.0
# List::MoreUtils not used at tests
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Load::Conditional) >= 0.38
BuildRequires:  perl(Moose) >= 2
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(overload)
# RDF::Redland 1.00 not used at tests
# Redis not used at tests because it requires configured and running server
BuildRequires:  perl(Scalar::Util) >= 1.24
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::CommonNS) >= 0.04
# XML::LibXML not used directly, but XML::Namespace is unversioned
BuildRequires:  perl(XML::LibXML) >= 1.7
BuildRequires:  perl(XML::Namespace)
BuildRequires:  perl(XML::SAX) >= 0.96
BuildRequires:  perl(XML::SAX::Base)
# Optional run-time:
# Data::UUID and UUID::Tiny
# Term::ANSIColor
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(URI::file)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(Data::UUID)
Requires:       perl(GraphViz)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Load::Conditional) >= 0.38
Requires:       perl(Moose) >= 2
Requires:       perl(Scalar::Util) >= 1.24
Recommends:     perl(Term::ANSIColor)
Recommends:     perl(UUID::Tiny)
Requires:       perl(XML::LibXML) >= 1.7
Requires:       perl(XML::SAX) >= 0.96

# Remove dependencies from documentation
%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((JSON|List::Util|Module::Load::Conditional|Moose|Scalar::Util|Test::More|URI|XML::SAX)\\)$ 

%description
RDF::Trine provides an Resource Descriptive Framework (RDF) with an
emphasis on extensibility, API stability, and the presence of a test suite.

Support for MySQL, PosgreSQL, Redland, Redis, and SQLite is delivered by
separate packages (e.g. %{name}-mysql).

%if %{with perl_RDF_Trine_enables_redland}
%package redland
Summary:        Redland support for RDF::Trine
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Scalar::Util) >= 1.24

%description redland
This provides Redland parser and storage for RDF::Trine Perl framework.
%endif

%if %{with perl_RDF_Trine_enables_postgresql}
%package postgresql
Summary:        RDF::Trine store in PostgreSQL
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DBD::Pg)
Requires:       perl(Scalar::Util) >= 1.24

%description postgresql
This provides an RDF::Trine::Store API to interact with PostgreSQL server. 
%endif

%if %{with perl_RDF_Trine_enables_mysql}
%package mysql
Summary:        RDF::Trine store in MySQL
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DBD::mysql)
Requires:       perl(Scalar::Util) >= 1.24

%description mysql
This provides an RDF::Trine::Store API to interact with MySQL server. 
%endif

%if %{with perl_RDF_Trine_enables_sqlite}
%package sqlite
Summary:        RDF::Trine store in SQLite
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DBD::SQLite) >= 1.14
Requires:       perl(Scalar::Util) >= 1.24

%description sqlite
This provides an RDF::Trine::Store API to interact with MySQL server. 
%endif

%if %{with perl_RDF_Trine_enables_redis}
%package redis
Summary:        RDF::Trine store in Redis
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(JSON) >= 2.0
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Scalar::Util) >= 1.24

%description redis
This provides an RDF::Trine::Store API to interact with a Redis server.
%endif

%package -n perl-Test-RDF-Trine-Store
Summary:        Collection of functions to test RDF::Trine stores
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test::More) >= 0.88

%description -n perl-Test-RDF-Trine-Store
This Perl module packages a few functions that you can call to test a
RDF::Trine::Store.

%prep
%setup -q -n RDF-Trine-%{version}
%patch0 -p1
%patch1 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc/d' MANIFEST
# Fix shellbangs
for F in bin/srx2csv bin/srx2table examples/foaf_labels.pl; do
    sed -i -e '1 s,#!/usr/bin/env perl,%(perl -MConfig -e 'print $Config{startperl}'),' "$F"
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
%doc Changes.ttl examples README
%{_bindir}/srx2csv
%{_bindir}/srx2table
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/RDF/Trine/Parser/Redland.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/Pg.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/mysql.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/SQLite.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/Redland.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/Redis.pm
%exclude %{perl_vendorlib}/Test
%{_mandir}/man3/*
%exclude %{_mandir}/man3/RDF::Trine::Parser::Redland.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::Pg.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::mysql.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::SQLite.*
%exclude %{_mandir}/man3/RDF::Trine::Store::Redland.*
%exclude %{_mandir}/man3/RDF::Trine::Store::Redis.*
%exclude %{_mandir}/man3/Test::RDF::Trine::Store.*

%if %{with perl_RDF_Trine_enables_redland}
%files redland
%{perl_vendorlib}/RDF/Trine/Parser/Redland.pm
%{perl_vendorlib}/RDF/Trine/Store/Redland.pm
%{_mandir}/man3/RDF::Trine::Parser::Redland.*
%{_mandir}/man3/RDF::Trine::Store::Redland.*
%endif

%if %{with perl_RDF_Trine_enables_postgresql}
%files postgresql
%{perl_vendorlib}/RDF/Trine/Store/DBI/Pg.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::Pg.*
%endif

%if %{with perl_RDF_Trine_enables_mysql}
%files mysql
%{perl_vendorlib}/RDF/Trine/Store/DBI/mysql.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::mysql.*
%endif

%if %{with perl_RDF_Trine_enables_sqlite}
%files sqlite
%{perl_vendorlib}/RDF/Trine/Store/DBI/SQLite.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::SQLite.*
%endif

%if %{with perl_RDF_Trine_enables_redis}
%files redis
%{perl_vendorlib}/RDF/Trine/Store/Redis.pm
%{_mandir}/man3/RDF::Trine::Store::Redis.*
%endif

%files -n perl-Test-RDF-Trine-Store
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::RDF::Trine::Store.*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Petr Pisar <ppisar@redhat.com> - 1.019-8
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Petr Pisar <ppisar@redhat.com> - 1.019-1
- 1.019 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-1
- 1.018 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-2
- Perl 5.26 rebuild

* Fri Jun 02 2017 Petr Pisar <ppisar@redhat.com> - 1.017-1
- 1.017 bump

* Tue Apr 25 2017 Petr Pisar <ppisar@redhat.com> - 1.016-1
- 1.016 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Petr Pisar <ppisar@redhat.com> - 1.015-1
- 1.015 bump

* Fri May 27 2016 Petr Pisar <ppisar@redhat.com> - 1.014-3
- Fix loading optional database backends

* Wed May 25 2016 Petr Pisar <ppisar@redhat.com> - 1.014-2
- Avoid TryCatch that does not work with perl-5.24 (bug #1339244)
- Perl 5.24 rebuild

* Wed Mar 16 2016 Petr Pisar <ppisar@redhat.com> 1.014-1
- Specfile autogenerated by cpanspec 1.78.
