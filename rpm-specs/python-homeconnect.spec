%global pypi_name homeconnect

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        1%{?dist}
Summary:        Python client for the BSH Home Connect REST API

License:        MIT
URL:            https://github.com/DavidMStraub/homeconnect
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python client for the BSH Home Connect REST API implementing OAuth 2
authentication, REST calls, and SSE event stream parsing.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python client for the BSH Home Connect REST API implementing OAuth 2
authentication, REST calls, and SSE event stream parsing.

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
* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Update to latest upstream release 0.6.3

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to latest upstream release 0.6.1 (#1877902)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Initial package for Fedora