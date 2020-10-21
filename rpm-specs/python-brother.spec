%global pypi_name brother

Name:           python-%{pypi_name}
Version:        0.1.17
Release:        1%{?dist}
Summary:        Python wrapper for getting data from Brother printers

License:        ASL 2.0
URL:            https://github.com/bieniu/brother
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python wrapper for getting data from Brother laser and inkjet printers
via SNMP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pysnmp)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for getting data from Brother laser and inkjet printers
via SNMP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.17-1
- Upstream adjusted BRs (rhbz#1875834)
- LICENSE file is now available 

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.15-1
- Initial package for Fedora
