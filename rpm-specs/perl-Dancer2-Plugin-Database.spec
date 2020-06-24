Name:           perl-Dancer2-Plugin-Database
Version:        2.17
Release:        6%{?dist}
Summary:        Easy database connections for Dancer2 applications
License:        GPL+ or Artistic

URL:            http://metacpan.org/release/Dancer2-Plugin-Database/
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Dancer2-Plugin-Database-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Dancer2) >= 0.166001
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer::Plugin::Database::Core)
BuildRequires:  perl(Dancer::Plugin::Database::Core::Handle)
# test requirements
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Dancer2::Plugin::Database provides an easy way to obtain a connected
DBI database handle by simply calling the database keyword within
your Dancer2 application

%prep
%setup -q -n Dancer2-Plugin-Database-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Dancer2*
%{_mandir}/man3/Dancer2*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.17-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.17-2
- Add NO_PACKLIST=1 to the options passed to Makefile.PL (#1625411)

* Sat Sep 01 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.17-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
