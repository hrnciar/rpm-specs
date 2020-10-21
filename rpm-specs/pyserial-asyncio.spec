%global pypi_name pyserial-asyncio

Name:           %{pypi_name}
Version:        0.4
Release:        1%{?dist}
Summary:        Asynchronous Python Serial Port Extension

License:        BSD
URL:            https://github.com/pyserial/pyserial-asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Async I/O extension package for the Python Serial Port Extension.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Async I/O extension package for the Python Serial Port Extension.

%package -n python-%{pypi_name}-doc
Summary:        pyserial-asyncio documentation

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for pyserial-asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' serial_asyncio/__init__.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 documentation html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/serial_asyncio/
%{python3_sitelib}/pyserial_asyncio-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora