%global pypi_name asyncio-dgram
%global mod_name asyncio_dgram

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Higher level Datagram support for Asyncio

License:        MIT
URL:            https://github.com/jsbronder/asyncio-dgram
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The goal of this package is to make implementing common patterns that
use datagrams simple and straight-forward while still supporting more
esoteric options. This is done by taking an opinionated stance on the
API that differs from parts of asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The goal of this package is to make implementing common patterns that
use datagrams simple and straight-forward while still supporting more
esoteric options. This is done by taking an opinionated stance on the
API that differs from parts of asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v test -k "not test_protocol_pause_resume"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{mod_name}/
%{python3_sitelib}/%{mod_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
