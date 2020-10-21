%global pypi_name pyairvisual

Name:           python-%{pypi_name}
Version:        5.0.2
Release:        1%{?dist}
Summary:        Python API client for AirVisual air quality data

License:        MIT
URL:            https://github.com/bachya/pyairvisual
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pyairvisual is a simple library for interacting with AirVisual to retrieve
air quality information.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyairvisual is a simple library for interacting with AirVisual to retrieve
air quality information.

%prep
%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.2-1
- Update to latest upstream release 5.0.2 (#1880002)

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.1-2
- Update to latest upstream release 5.0.1

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.0-1
- Initial package for Fedora