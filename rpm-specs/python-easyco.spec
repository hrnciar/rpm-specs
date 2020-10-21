%global pypi_name EasyCo
%global pkg_name easyco

Name:           python-%{pkg_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Configuration with YAML files

License:        LGPLv3+
URL:            https://github.com/spacemanspiff2007/EasyCo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The goal of EasyCo is to provide an easy way of configuration using
YAML files for Python programs. It can automatically create a default
configuration from provided default values and will validate the
provided data.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pkg_name}
The goal of EasyCo is to provide an easy way of configuration using
YAML files for Python programs. It can automatically create a default
configuration from provided default values and will validate the
provided data.

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
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-2
- Add license file

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Initial package for Fedora