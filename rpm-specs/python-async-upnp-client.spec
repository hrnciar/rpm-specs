%global pypi_name async-upnp-client

Name:           python-%{pypi_name}
Version:        0.14.14
Release:        1%{?dist}
Summary:        Async Python UPnP Client

License:        ASL 2.0
URL:            https://github.com/StevenLooman/async_upnp_client
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Async UPnP Client Asyncio UPnP Client library for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(async-timeout)
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(python-didl-lite)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(voluptuous)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Async UPnP Client Asyncio UPnP Client library for Python.

%prep
%autosetup -n async_upnp_client-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{_bindir}/upnp-client
%{python3_sitelib}/async_upnp_client/
%{python3_sitelib}/async_upnp_client-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.14-1
- Initial package for Fedora