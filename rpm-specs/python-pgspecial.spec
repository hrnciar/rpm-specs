%global pypi_name pgspecial

Name:           python-%{pypi_name}
Version:        1.11.10
Release:        2%{?dist}
Summary:        Meta-commands handler for Postgres Database

License:        BSD
URL:            https://www.dbcli.com
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click) >= 4.1
BuildRequires:  python3dist(psycopg2) >= 2.7.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlparse) >= 0.1.19

%description
This package provides an API to execute meta-commands
AKA "special", or "backslash commands") on PostgreSQL.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(click) >= 4.1
Requires:       python3dist(psycopg2) >= 2.7.4
Requires:       python3dist(sqlparse) >= 0.1.19
%description -n python3-%{pypi_name}
This package provides an API to execute meta-commands
AKA "special", or "backslash commands") on PostgreSQL.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license License.txt
%doc scripts/README.rst README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.10-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.11.10-1
- Initial package.
