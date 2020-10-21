%global pypi_name pyairnow

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Python wrapper for EPA AirNow Air Quality API

License:        MIT
URL:            https://github.com/asymworks/pyairnow
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyairnow is a simple and thin client library for interacting with the
AirNow United States EPA Air Quality Index API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aioresponses)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyairnow is a simple and thin client library for interacting with the
AirNow United States EPA Air Quality Index API.

%prep
%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
