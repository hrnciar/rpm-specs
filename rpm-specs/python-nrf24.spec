%global pypi_name nrf24

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Library for NRF24L01 communication

License:        MIT
URL:            https://github.com/bjarne-hansen/py-nrf24
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package implement 2.4 Ghz communication using NRF24L01
modules on a Raspberry Pi using Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package implement 2.4 Ghz communication using NRF24L01
modules on a Raspberry Pi using Python.

%prep
%autosetup -n py-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package for Fedora