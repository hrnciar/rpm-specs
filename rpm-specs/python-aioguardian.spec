%global pypi_name aioguardian

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Python library for Elexa Guardian devices

License:        MIT
URL:            https://github.com/bachya/aioguardian
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library for Elexa Guardian devices (water valves and sensors).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library for Elexa Guardian devices (water valves and sensors).

%prep
%autosetup -n %{pypi_name}-%{version}

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
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.2-1
- LICENSE file was added by upstream

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
