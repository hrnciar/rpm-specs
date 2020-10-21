%global pypi_name py-smart-gardena
%global pkg_name smart-gardena

Name:           python-%{pkg_name}
Version:        0.7.10
Release:        1%{?dist}
Summary:        Python client to communicate with Gardena systems

License:        MIT
URL:            https://github.com/py-smart-gardena/py-smart-gardena
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The py-smart-gardena library aims to provide python way to communicate
with Gardena smart systems and all Gardena smart equipment.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(websocket-client)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pkg_name}
The py-smart-gardena library aims to provide python way to communicate
with Gardena smart systems and all Gardena smart equipment.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Superfluous file
rm -rf src/__init__.py

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/gardena/
%{python3_sitelib}/py_smart_gardena-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.10-1
- Shebang issue was fixed upstream
- Update to latest upstream release 0.7.10

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.9-1
- Initial package for Fedora