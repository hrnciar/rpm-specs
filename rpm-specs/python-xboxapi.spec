%global pypi_name xboxapi

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Python XBOX One API wrapper

License:        MIT
URL:            https://github.com/mKeRix/xboxapi-python
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This is a Python wrapper for the unofficial Xbox API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a Python wrapper for the unofficial Xbox API.

%prep
%autosetup -n %{pypi_name}-python-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Initial package for Fedora
