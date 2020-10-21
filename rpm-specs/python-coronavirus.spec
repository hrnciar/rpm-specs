%global pypi_name coronavirus

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Python client for getting Corona virus info

License:        MIT
URL:            https://github.com/nabucasa/coronavirus
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python API fetching latest Corona Virus information.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python API fetching latest Corona Virus information.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/NabuCasa/coronavirus/pull/10
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package for Fedora
