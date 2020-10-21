Name:           perl-DBIx-Class-Schema-Config
Version:        0.001013
Release:        6%{?dist}
Summary:        Credential Management for DBIx::Class
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-Class-Schema-Config
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYMKAT/DBIx-Class-Schema-Config-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Config::Any) >= 0.23
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.08100
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Config::Any) >= 0.23
Requires:       perl(DBIx::Class) >= 0.08100
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Any\\)\s*$ 

%description
DBIx::Class::Schema::Config is a subclass of DBIx::Class::Schema that
allows the loading of credentials & configuration from a file. The actual
code itself would only need to know about the name used in the
configuration file. This aims to make it simpler for operations teams to
manage database credentials.

%prep
%setup -q -n DBIx-Class-Schema-Config-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001013-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001013-2
- Perl 5.30 rebuild

* Mon Feb 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001013-1
- 0.001013 bump

* Wed Feb 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001012-1
- 0.001012 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001011-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001011-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001011-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.001011-2
- Perl 5.22 rebuild

* Wed Feb 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.001011-1
- Specfile autogenerated by cpanspec 1.78.
