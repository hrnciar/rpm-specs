%global pypi_name gekitchen

Name:           python-%{pypi_name}
Version:        0.2.19
Release:        1%{?dist}
Summary:        Python SDK for GE Kitchen Appliances

License:        MIT
URL:            https://github.com/ajmarks/gekitchen
Source0:        %{pypi_source}
BuildArch:      noarch

%description
gekitchen is a Python SDK for GE WiFi-enabled kitchen appliances.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
gekitchen is a Python SDK for GE WiFi-enabled kitchen appliances.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

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
* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.19-1
- Update to latest upstream release 0.2.19

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.14-1
- Update to latest upstream release 0.2.14 (#1877859)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.12-1
- Initial package for Fedora