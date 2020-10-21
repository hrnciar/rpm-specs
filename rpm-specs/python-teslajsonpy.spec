%global pypi_name teslajsonpy

Name:           python-%{pypi_name}
Version:        0.10.4
Release:        1%{?dist}
Summary:        Python library to work with Tesla API

License:        ASL 2.0
URL:            https://github.com/zabuldon/teslajsonpy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Async Python module to work with the Tesla API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(backoff)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wrapt)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Async Python module to work with the Tesla API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_values_on_init"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%exclude %{python3_sitelib}/tests/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.4-1
- Initial package for Fedora