%global pypi_name afsapi

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Python wrapper for the Frontier Silicon API

License:        ASL 2.0
URL:            https://github.com/zhelev/python-afsapi
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous python implementation of the Frontier Silicon API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous python implementation of the Frontier Silicon API.

%prep
%autosetup -n %{name}-%{version}
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
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Initial package for Fedora
