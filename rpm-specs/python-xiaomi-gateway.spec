%global pypi_name PyXiaomiGateway
%global pkg_name xiaomi-gateway
%bcond_with device

Name:           python-%{pkg_name}
Version:        0.13.3
Release:        1%{?dist}
Summary:        Python library to communicate with the Xiaomi Gateway

License:        MIT
URL:            https://github.com/Danielhiversen/PyXiaomiGateway/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python library to communicate with the Xiaomi Gateway.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pkg_name}
A Python library to communicate with the Xiaomi Gateway.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
%pytest -v tests
%endif

%files -n python3-%{pkg_name}
%doc README.md
%license License.txt
%{python3_sitelib}/xiaomi_gateway/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.3-1
- Update to latest upstream release 0.13.3

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.2-1
- Initial package for Fedora
