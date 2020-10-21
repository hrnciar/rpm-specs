%global pypi_name pyhomeworks
%global pkg_name homeworks

Name:           python-%{pkg_name}
Version:        0.0.6
Release:        1%{?dist}
Summary:        Lutron Homeworks Series 4 and 8 interface

License:        MIT
URL:            https://github.com/dubnom/pyhomeworks
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python package to connect to Lutron Homeworks Series-4 and Series-8
systems over Ethernet.

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python package to connect to Lutron Homeworks Series-4 and Series-8
systems over Ethernet.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
chmod -x README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.md
# https://github.com/dubnom/pyhomeworks/pull/2
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-1
- Initial package for Fedora