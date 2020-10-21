%global pypi_name aioeafm

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Python wrapper for the UK Environment Agency Flood Monitoring API

License:        ASL 2.0
URL:            https://github.com/Jc2k/aioeafm
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a thin Python wrapper for the Real Time flood
monitoring API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a thin Python wrapper for the Real Time flood
monitoring API.

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
%doc README.md
%license LICENSE

%changelog
* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora