# Created by pyp2rpm-3.3.4
%global pypi_name regenmaschine

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python API for RainMachine sprinkler controllers

License:        MIT
URL:            https://github.com/bachya/regenmaschine
Source0:        %{pypi_source}
BuildArch:      noarch

%description
regenmaschine (German for "rain machine") is a simple Python library for
interacting with RainMachine smart sprinkler controllers. It gives developers
an easy API to manage their controllers over their local LAN or remotely via
the RainMachine cloud.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
regenmaschine (German for "rain machine") is a simple Python library for
interacting with RainMachine smart sprinkler controllers. It gives developers
an easy API to manage their controllers over their local LAN or remotely via
the RainMachine cloud.

%prep
%autosetup -n %{pypi_name}-%{version}

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
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Initial package for Fedora
