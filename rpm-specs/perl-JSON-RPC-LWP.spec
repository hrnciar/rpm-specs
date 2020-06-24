Name:           perl-JSON-RPC-LWP
Version:        0.007
Release:        2%{?dist}
Summary:        JSON RPC over any libwww supported protocol
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/JSON-RPC-LWP
Source0:        https://cpan.metacpan.org/authors/id/B/BG/BGILLS/JSON-RPC-LWP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.008
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::RPC::Common)
BuildRequires:  perl(JSON::RPC::Common::Marshal::HTTP)
BuildRequires:  perl(JSON::RPC::Common::TypeConstraints)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Deprecated)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI) >= 1.58
BuildRequires:  perl(Util)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Use any version of JSON RPC over any libwww supported transport protocols.

%prep
%setup -q -n JSON-RPC-LWP-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Yanko Kaneti <yaneti@declera.com> - 0.007-1
- Specfile autogenerated by cpanspec 1.78 and tweaked
