%global pypi_name bravado-core

Name:           python-%{pypi_name}
Version:        5.17.0
Release:        1%{?dist}
Summary:        Library for adding Swagger support to clients and servers

License:        BSD
URL:            https://github.com/Yelp/bravado-core
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
bravado-core is a Python library that adds client-side and
server-side support for the OpenAPI Specification v2.0.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
bravado-core is a Python library that adds client-side and
server-side support for the OpenAPI Specification v2.0.


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/bravado_core
%{python3_sitelib}/bravado_core-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 5.17.0-1
- Initial package.
