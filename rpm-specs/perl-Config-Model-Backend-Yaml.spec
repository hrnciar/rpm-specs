Name:           perl-Config-Model-Backend-Yaml
Version:        2.133
Release:        5%{?dist}
Summary:        Read and write configuration as a YAML data structure
License:        LGPLv2
URL:            https://metacpan.org/release/Config-Model-Backend-Yaml/
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Backend-Yaml-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 2.131
BuildRequires:  perl(Config::Model::Backend::Any)
BuildRequires:  perl(Config::Model::Exception)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(YAML::XS) >= 0.69
# Tests
BuildRequires:  perl(Config::Model::BackendMgr)
BuildRequires:  perl(Config::Model::Tester) >= 3.006
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module is used directly by Config::Model to read or write the content
of a configuration tree written with YAML syntax in Config::Model
configuration tree.

%prep
%setup -q -n Config-Model-Backend-Yaml-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.133-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.133-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.133-1
- 2.133 bump

* Tue Dec 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.132-1
- Specfile autogenerated by cpanspec 1.78.
