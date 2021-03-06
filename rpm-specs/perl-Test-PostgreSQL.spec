Name:           perl-Test-PostgreSQL
Version:        1.27
Release:        8%{?dist}
Summary:        PostgreSQL runner for Perl tests
# lib/Test/PostgreSQL.pm:   Artistic 2.0
License:        Artistic 2.0
URL:            https://metacpan.org/release/Test-PostgreSQL
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJC/Test-PostgreSQL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.14
# The DBD::Pg is used via DBI->connect() first argument
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Tie::Hash::Method)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(User::pwent)
BuildRequires:  perl(warnings)
# initdb, pg_ctl, and postgres or postmaster tools are used
BuildRequires:  postgresql-server
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork) >= 0.06
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# The DBD::Pg is used via DBI->connect() first argument
Requires:       perl(DBD::Pg)
# initdb, pg_ctl, and postgres or postmaster tools are used
Requires:       postgresql-server

%description
The Test::PostgreSQL Perl module automatically setups a PostgreSQL instance in
a temporary directory, and destroys it when the Perl script exits.

%prep
%setup -q -n Test-PostgreSQL-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset POSTGRES_HOME TEST_POSTGRESQL_PRESERVE
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-7
- Perl 5.32 rebuild

* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 1.27-6
- Correct a list of the build-time dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-1
- 1.27 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-2
- Perl 5.28 rebuild

* Tue Apr 03 2018 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Mon Mar 26 2018 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Mon Mar 05 2018 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump
- License corrected from "Artistic 2.0 and (GPL+ or Artistic)" to "Artistic 2.0"

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-2
- Perl 5.26 rebuild

* Tue May 02 2017 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Thu Mar 30 2017 Petr Pisar <ppisar@redhat.com> - 1.22-1
- 1.22 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- Perl 5.24 rebuild

* Wed Feb 10 2016 Petr Pisar <ppisar@redhat.com> - 1.20-1
- 1.20 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-2
- Perl 5.22 rebuild

* Thu May 14 2015 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Tue Mar 03 2015 Petr Pisar <ppisar@redhat.com> 1.05-1
- Specfile autogenerated by cpanspec 1.78.
