%global pypi_name aionotion

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        2%{?dist}
Summary:        Python library for Notion Home Monitoring

License:        MIT
URL:            https://github.com/bachya/aionotion
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A asyncio-friendly library for Notion Home Monitoring devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A asyncio-friendly library for Notion Home Monitoring devices.

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
* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-2
- Use pyproject-rpm-macros (rhbz#1875865)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Initial package for Fedora
