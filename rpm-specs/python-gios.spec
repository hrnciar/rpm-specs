%global pypi_name gios

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        2%{?dist}
Summary:        Python wrapper for GIOS air quality data

License:        ASL 2.0
URL:            https://github.com/bieniu/gios
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python wrapper for getting air quality data from GIOŚ
(Główny Inspektorat Ochrony Środowiska).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for getting air quality data from GIOŚ
(Główny Inspektorat Ochrony Środowiska).

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
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-2
- Use source sanme (rhbz#1877103)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Initial package for Fedora