Name:           perl-MaxMind-DB-Reader-XS
Version:        1.000008
Release:        1%{?dist}
Summary:        Fast XS implementation of MaxMind DB reader
# Build.PL:                 Artistic 2.0
# c/perl_math_int128.c:     Public Domain
# c/perl_math_int64.c:      Public Domain
# c/ppport.h:               GPL+ or Artistic
# LICENSE:                  Artistic 2.0 text
# lib/MaxMind/DB/Reader/XS.pm:  Artistic 2.0
# README.md:                Artistic 2.0
## Not in any binary package
# maxmind-db/LICENSE:       CC-BY-SA
# maxmind-db/MaxMind-DB-spec.md:    CC-BY-SA
## Unbundled
# inc/Capture/Tiny.pm:      ASL 2.0
# inc/Config/AutoConf.pm:   GPL+ or Artistic
License:        Artistic 2.0 and (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/MaxMind-DB-Reader-XS
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-XS-%{version}.tar.gz
# Do not hardcore debugging
Patch0:         MaxMind-DB-Reader-XS-1.000008-Do-not-hardcode-debugging.patch
# Math::Int128 is not supported on 32-bit platforms, bugs #1871719, #1871720
ExcludeArch:    %{arm} %{ix86}
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libmaxminddb-devel >= 1.2.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Math::Int64)
BuildRequires:  perl(MaxMind::DB::Metadata) >= 0.040001
BuildRequires:  perl(MaxMind::DB::Reader::Role::HasMetadata)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Moo)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MaxMind::DB::Reader)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Path::Class) >= 0.27
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
# Optional tests:
BuildRequires:  perl(Net::Works::Network) >= 0.21
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(MaxMind::DB::Reader::Role::HasMetadata)

%description
Simply installing this module causes MaxMind::DB::Reader to use the XS
implementation, which is much faster than the Perl implementation.

%prep
%setup -q -n MaxMind-DB-Reader-XS-%{version}
%patch0 -p1
# Remove bundled modules
rm -r ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST
# FIXME: remove compiler flag -g from Build.PL

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
%doc Changes CONTRIBUTING.md README.md valgrind.supp
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/MaxMind*
%{_mandir}/man3/*

%changelog
* Fri Aug 07 2020 Petr Pisar <ppisar@redhat.com> 1.000008-1
- Specfile autogenerated by cpanspec 1.78.