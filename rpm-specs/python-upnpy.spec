%global pypi_name upnpy

Name:           python-%{pypi_name}
Version:        1.1.8
Release:        1%{?dist}
Summary:        Lightweight UPnP client library

License:        MIT
URL:            https://github.com/5kyc0d3r/upnpy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Lightweight UPnP client library for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Lightweight UPnP client library for Python.

%package -n python-%{pypi_name}-doc
Summary:        %{pypi_name} documentation

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/UPnPy-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.8-1
- Initial package for Fedora