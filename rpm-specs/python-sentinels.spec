%global pypi_name sentinels

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Various objects to denote special meanings in Python

License:        BSD
URL:            https://github.com/vmalloc/sentinels
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The sentinels module is a small utility providing the Sentinel class, along
with useful instances.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The sentinels module is a small utility providing the Sentinel class, along
with useful instances.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora
