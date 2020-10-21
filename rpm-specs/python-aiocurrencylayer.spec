%global pypi_name aiocurrencylayer

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        Python wrapper for interacting with the currencylayer API

License:        MIT
URL:            https://github.com/home-assistant-ecosystem/aiocurrencylayer
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python wrapper for interacting with the currencylayer API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for interacting with the currencylayer API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 0.1.3

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora
