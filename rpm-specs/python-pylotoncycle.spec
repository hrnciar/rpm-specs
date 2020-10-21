%global pypi_name pylotoncycle

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Module to access your Peloton workout data

License:        BSD
URL:            https://github.com/justmedude/pylotoncycle
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python Library for getting your Peloton workout data.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python Library for getting your Peloton workout data.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# https://github.com/justmedude/pylotoncycle/pull/2
sed -i -e '/^#!\//, 1d' pylotoncycle/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Initial package for Fedora