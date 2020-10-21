%global pypi_name devolo-home-control-api

Name:           python-%{pypi_name}
Version:        0.15.0
Release:        1%{?dist}
Summary:        Devolo Home Control API in Python

License:        GPLv3
URL:            https://github.com/2Fake/devolo_home_control_api
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module implements parts of the devolo Home Control API
in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(websocket-client)
BuildRequires:  python3dist(zeroconf)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module implements parts of the devolo Home Control API
in Python.

%prep
%autosetup -n devolo_home_control_api-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc docs/CHANGELOG.md README.md
%{python3_sitelib}/devolo_home_control_api
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/devolo_home_control_api-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.0-1
- Initial package for Fedora