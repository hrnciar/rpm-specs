%global pypi_name hatasmota

Name:           python-%{pypi_name}
Version:        0.0.20
Release:        1%{?dist}
Summary:        Python module to help parse and construct Tasmota MQTT messages

License:        MIT
URL:            https://github.com/emontnemery/hatasmota
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python module to help parse and construct Tasmota MQTT messages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python module to help parse and construct Tasmota MQTT messages.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/HATasmota-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Oct 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20-1
- Update to latest upstream release 0.0.20 (#1889169)

* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.18-1
- Update to latest upstream release 0.0.18 (#1889106)

* Sat Oct 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.17-1
- Update to latest upstream release 0.0.17 (#1888814)

* Fri Oct 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.16-1
- Update to latest upstream release 0.0.16 (#1888814)

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.15-1
- Update to latest upstream release 0.0.15

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Initial package for Fedora