%global pypi_name pyedimax
%global pkg_name edimax

Name:           python-%{pkg_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Interface with Edimax Smart Plugs

License:        MIT
URL:            https://github.com/andreipop2005/pyedimax
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Pyedimax is a python library for interfacing with the Edimax Smart
Plug switches.

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Pyedimax is a python library for interfacing with the Edimax Smart
Plug switches.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i 's/\r$//' README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora
