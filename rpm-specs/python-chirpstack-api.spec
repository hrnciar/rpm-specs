# Created by pyp2rpm-3.3.4
%global pypi_name chirpstack-api

Name:           python-%{pypi_name}
Version:        3.7.7
Release:        1%{?dist}
Summary:        Chirpstack Python API

License:        MIT
URL:            https://github.com/brocaar/chirpstack-api
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
ChirpStack gRPC API message and service wrappers for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ChirpStack gRPC API message and service wrappers for Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/chirpstack_api
%{python3_sitelib}/chirpstack_api-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7-1
- Initial package for Fedora
