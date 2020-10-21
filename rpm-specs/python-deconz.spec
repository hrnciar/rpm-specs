%global pypi_name pydeconz
%global pkg_name deconz

Name:           python-%{pkg_name}
Version:        73
Release:        1%{?dist}
Summary:        Python library for communicating with deCONZ REST API

License:        MIT
URL:            https://github.com/Kane610/deconz
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python library for communicating with deCONZ REST API by
dresden elektronik. This implementation should cover most
devices supported by deCONZ.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python library for communicating with deCONZ REST API by
dresden elektronik. This implementation should cover most
devices supported by deCONZ.

%prep
%autosetup -n %{pkg_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Tests requires asynctest
# https://github.com/Kane610/deconz/issues/76
#%%check
#%%pytest -v tests

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 73-1
- Update to latest upstream release 73

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 72-1
- Initial package