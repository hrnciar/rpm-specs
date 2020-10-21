%global pypi_name httpx

Name:           python-%{pypi_name}
Version:        0.16.1
Release:        1%{?dist}
Summary:        Python HTTP client

License:        BSD
URL:            https://github.com/encode/httpx
Source0:        %{pypi_source}
BuildArch:      noarch

%description
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Oct 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.1-1
- Update to new upstream release 0.16.1 (#1884265)

* Wed Oct 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to new upstream release 0.16.0 (#1884265)

* Sun Oct 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.5-1
- Update to new upstream release 0.15.5 (#1884265)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.4-1
- Update to latest upstream release 0.15.4 (#1881434)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.3-1
- Update to latest upstream release 0.15.3 (#1881434)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.0-1
- Update to latest upstream release 0.15.0 (#1881434)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.3-2
- Run dependency genenerator

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.3-1
- Update to latest upstream release 0.14.3 (#1875281)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.3-1
- Initial package for Fedora
