%global pypi_name subarulink

Name:           python-%{pypi_name}
Version:        0.3.6
Release:        1%{?dist}
Summary:        Python package to interact with Subaru Starlink Remote Services API

License:        ASL 2.0
URL:            https://github.com/G-Two/subarulink
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python package for interacting with the Subaru Starlink remote
vehicle services API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python package for interacting with the Subaru Starlink remote
vehicle services API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# https://github.com/G-Two/subarulink/issues/18
rm -rf subarulink/{__pycache__,app/__pycache__,.DS_Store}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/subarulink
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to latest upstream release 0.3.6

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Initial package for Fedora