%global pypi_name pytest-venv

Name:           python-%{pypi_name}
Version:        0.2
Release:        1%{?dist}
Summary:        py.test fixture for creating a virtual environment

License:        MIT
URL:            https://github.com/mmerickel/pytest-venv
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%generate_buildrequires
%pyproject_buildrequires -r -x testing

%description
pytest-venv is a simple pytest plugin that exposes a venv fixture.
The fixture is used to create a new virtual environment which can be used to
install packages and run commands inside tests.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(pytest)

%description -n python3-%{pypi_name}
pytest-venv is a simple pytest plugin that exposes a venv fixture.
The fixture is used to create a new virtual environment which can be used to
install packages and run commands inside tests.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_venv

%check
%pytest -k "not test_it_installs_dep and not test_it_upgrades_dep"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Thu Jul 09 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2-1
- Initial package.
