%global pypi_name epson-projector

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Python support for Epson projectors

License:        MIT
URL:            https://github.com/pszafer/epson_projector
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous Python library to control Epson projectors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous Python library to control Epson projectors.

%prep
%autosetup -n epson_projector-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Not all tests are not ported to Python 3.8 yet
#%%check
#%%pytest -v test_*.py

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/epson_projector/
%{python3_sitelib}/epson_projector-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-1
- Initial package for Fedora