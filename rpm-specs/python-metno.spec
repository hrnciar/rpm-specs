%global pypi_name PyMetno
%global pkg_name metno

Name:           python-%{pkg_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Library to communicate with the met.no API

License:        MIT
URL:            https://github.com/Danielhiversen/pyMetno/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Library to communicate with the met.no API.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Library to communicate with the met.no API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.md
# https://github.com/Danielhiversen/pyMetno/pull/26
#%%license LICENSE
%{python3_sitelib}/%{pkg_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Initial package for Fedora
