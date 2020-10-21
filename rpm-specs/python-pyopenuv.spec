%global pypi_name pyopenuv

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Python API data from openuv.io

License:        MIT
URL:            https://github.com/bachya/pyopenuv
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
A simple Python API for data from openuv.io.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A simple Python API for data from openuv.io.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -i -e '/asynctest/d' pyproject.toml      

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.md README.md

%changelog
* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0
- Add AUTHORS.md (rhbz#1877784)

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora