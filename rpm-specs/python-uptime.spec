%global pypi_name uptime

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Cross-platform uptime library

License:        BSD
URL:            https://github.com/Cairnarvon/uptime
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
This module provides a cross-platform way to retrieve system uptime and boot
time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module provides a cross-platform way to retrieve system uptime and boot
time.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' src/__*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license COPYING.txt
%doc README.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.1-1
- Initial package for Fedora