%global pypi_name pydanfossair
%global pkg_name danfossair

Name:           python-%{pkg_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Python interface for Danfoss Air HRV systems

License:        ASL 2.0
URL:            https://github.com/JonasPed/pydanfoss-air
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python module and client for Danfoss Air HRV systems.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python module and client for Danfoss Air HRV systems.

%prep
%autosetup -n pydanfoss-air-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
