%global pypi_name thingserver

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        HTTP Web Thing implementation

License:        MPLv2.0
URL:            https://github.com/labthings/python-thingserver
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Implementation of an HTTP Web Thing.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Implementation of an HTTP Web Thing.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora