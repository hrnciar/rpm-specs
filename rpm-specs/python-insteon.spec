%global pypi_name pyinsteon
%global pkg_name insteon


Name:           python-%{pkg_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Python API for controlling Insteon devices

License:        MIT
URL:            https://github.com/pyinsteon/pyinsteon
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a Python package to interface with an Insteon Modem. It has been tested
to work with most USB or RS-232 serial based devices such as the 2413U, 2412S,
2448A7 and Hub models 2242 and 2245.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiofiles)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(async-generator)
BuildRequires:  python3dist(pypubsub)
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pyserial-asyncio)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
This is a Python package to interface with an Insteon Modem. It has been tested
to work with most USB or RS-232 serial based devices such as the 2413U, 2412S,
2448A7 and Hub models 2242 and 2245.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%license LICENSE.rst
%doc README.rst
%{_bindir}/insteon_tools
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.8-1
- Update to latest upstream release 1.0.8 (#1879765)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.7-1
- Initial package for Fedora