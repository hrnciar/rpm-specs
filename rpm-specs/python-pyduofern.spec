%global pypi_name pyduofern

Name:           python-%{pypi_name}
Version:        0.34.1
Release:        1%{?dist}
Summary:        Library for controlling Rademacher DuoFern actors

License:        GPLv2+
URL:            https://github.com/gluap/pyduofern
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyduofern is a Python library for controlling Rademacher DuoFern
actors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pyserial-asyncio)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyduofern is a Python library for controlling Rademacher DuoFern
actors.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# https://github.com/gluap/pyduofern/issues/23
#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name}
%license license.txt
%doc README.rst examples/
%{_bindir}/duofern_cli.py
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.34.1-1
- Enable tests (reverted)
- Update to latest upstream release 0.34.1 (#1880663)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.34.0-1
- Initial package for Fedora