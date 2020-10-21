%global pypi_name pyarlo

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Python library to interact with Netgear Arlo cameras

License:        LGPLv3+
URL:            https://github.com/tchellomello/python-arlo
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python Arlo is a library written in Python that exposes the Netgear
Arlo cameras as Python objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sseclient-py)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests-mock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python Arlo is a library written in Python that exposes the Netgear
Arlo cameras as Python objects.

%package -n python-%{pypi_name}-doc
Summary:        %{pypi_name} documentation

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n python-arlo-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-2
- Update BR (rhbz#1877811)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Initial package for Fedora