%global rpm_name pg_activity

Name:           %{rpm_name}
Version:        1.6.0
Release:        2%{?dist}
Summary:        Command line tool for PostgreSQL server activity monitoring

License:        PostgreSQL
URL:            https://github.com/dalibo/pg_activity/
Source0:        https://github.com/dalibo/pg_activity/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(psutil) >= 0.4.1
Requires:       python3dist(psycopg2)

%{?python_provide:%python_provide python3-%{rpm_name}}

%description
Top like application for PostgreSQL server activity monitoring

%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/pg_activity
%{python3_sitelib}/pgactivity
%{python3_sitelib}/pg_activity-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.0-1
- Initial package.
- fix autosetup usage and license