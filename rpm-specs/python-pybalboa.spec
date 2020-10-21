# Created by pyp2rpm-3.3.4
%global pypi_name pybalboa

Name:           python-%{pypi_name}
Version:        0.10
Release:        1%{?dist}
Summary:        Module to communicate with a Balboa spa Wifi adapter

License:        ASL 2.0
URL:            https://github.com/garbled1/pybalboa
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Module to communicate with a Balboa spa Eifi adapter.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Module to communicate with a Balboa spa Wifi adapter.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10-1
- Initial package for Fedora