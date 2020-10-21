# Created by pyp2rpm-3.3.4
%global pypi_name connect_box
%global pkg_name connect-box

Name:           python-%{pkg_name}
Version:        0.2.8
Release:        1%{?dist}
Summary:        Python client for interacting with Compal CH7465LG devices

License:        MIT
URL:            https://github.com/home-assistant-ecosystem/python-connect-box
Source0:        %{pypi_source}
BuildArch:      noarch

%description
connect-box is a Python Client for interacting with the cable modem/router
Compal CH7465LG which is provided under different names by various ISP in
Europe.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
connect-box is a Python Client for interacting with the cable modem/router
Compal CH7465LG which is provided under different names by various ISP in
Europe.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.8-1
- Update to latest upstream release 0.2.8 (rhbz#1874641)

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Initial package for Fedora
