Name:           perl-SQL-Interp
Version:        1.26
Release:        2%{?dist}
Summary:        Interpolate Perl variables into SQL statements
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/SQL-Interp
Source0:        https://cpan.metacpan.org/authors/id/Y/YO/YORHEL/SQL-Interp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1
BuildRequires:  perl(Exporter)
# perl(Filter::Simple)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# perl(Text::Balanced) >= 1.87
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DBI) >= 1

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(DBI::db)\s*$

%description
SQL::Interp converts a list of intermixed SQL fragments and variable
references into a conventional SQL string and list of bind values suitable
for passing onto DBI. This simple technique creates database calls that are
simpler to create and easier to read, while still giving you full access to
custom SQL.

%prep
%setup -q -n SQL-Interp-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes ex README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-2
- Perl 5.32 rebuild

* Mon Apr 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-1
- 1.26 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-1
- 1.25 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-2
- Perl 5.24 rebuild

* Fri Feb 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-1
- 1.24 bump

* Wed Feb 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- Initial release
