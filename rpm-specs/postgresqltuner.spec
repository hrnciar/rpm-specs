Name:    postgresqltuner
Version: 1.0.1
Release: 4%{?dist}
Summary: Simple script to analyze PostgreSQL database configuration and tuning

License: GPLv3
URL:     https://github.com/jfcoz/postgresqltuner/
Source0: https://github.com/jfcoz/postgresqltuner/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch


Requires: perl(DBI)
Requires: perl(DBD::Pg)
Requires: perl(Getopt::Long)
Requires: perl(Term::ANSIColor)

%description
postgresqltuner is a simple script to analyze your PostgreSQL database. It is 
inspired by mysqltuner.pl

%prep
%autosetup

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a postgresqltuner.pl %{buildroot}%{_bindir}/postgresqltuner

%files
%{_bindir}/postgresqltuner

%doc README.md README.fr.md
%license LICENSE.txt

%changelog
* Fri Mar 29 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0.1-4
- Change Source to use macros
- Add missing dep
- Use perl macro for all deps

* Mon Mar 25 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0.1-3
- Fix requirements
- Extend changelog

* Fri Mar 22 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0.1-1
- Initial version of the package
