%global pypi_name rak811

Name:           python-%{pypi_name}
Version:        0.7.3
Release:        1%{?dist}
Summary:        Interface for RAK811 LoRa module

License:        ASL 2.0
URL:            https://github.com/AmedeeBulle/pyrak811
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python 3 library and command-line interface for use with the Raspberry
Pi LoRa pHAT.The library exposes the AT commands as described in the
RAK811 Lora AT Command User Guide V1.4.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python 3 library and command-line interface for use with the Raspberry
Pi LoRa pHAT.The library exposes the AT commands as described in the
RAK811 Lora AT Command User Guide V1.4.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/rak811
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.3-1
- Initial package for Fedora