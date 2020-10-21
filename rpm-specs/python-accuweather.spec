%global pypi_name accuweather

Name:           python-%{pypi_name}
Version:        0.0.11
Release:        1%{?dist}
Summary:        Python wrapper for getting data from AccuWeather servers

License:        ASL 2.0
URL:            https://github.com/bieniu/accuweather
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python wrapper for getting weather data from AccuWeather
servers for Limited Trial package.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for getting weather data from AccuWeather
servers for Limited Trial package.

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
* Sat oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.11-1
- Update to latest upstream release 0.0.11

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Initial package for Fedora