%global pypi_name kismet_rest
%global pkg_name kismet-rest
%global rel_version 2019.05.02

Name:           python-%{pkg_name}
Version:        2019.5.2
Release:        1%{?dist}
Summary:        Python API for the Kismet REST interface

License:        GPLv2
URL:            https://www.kismetwireless.net
Source0:        https://github.com/kismetwireless/python-kismet-rest/archive/%{rel_version}/%{pypi_name}-%{rel_version}.tar.gz
BuildArch:      noarch

%description
Python API wrapper for Kismet RESTful API interface.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python API wrapper for Kismet RESTful API interface.

%prep
%autosetup -n python-kismet-rest-%{rel_version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2019.05.02-1
- Update to latest upstream release 2020.5.2

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2019.05.01-1
- Initial package for Fedora