%global pypi_name voluptuous-serialize

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        1%{?dist}
Summary:        Convert voluptuous schemas to dictionaries

License:        ASL 2.0
URL:            http://github.com/balloob/voluptuous-serialize
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(voluptuous)

%description
Convert Voluptuous schemas to dictionaries so they can be serialized.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(voluptuous)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(voluptuous)
%description -n python3-%{pypi_name}
Convert Voluptuous schemas to dictionaries so they can be serialized.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/voluptuous_serialize/
%{python3_sitelib}/voluptuous_serialize-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Initial package for Fedora
