%global pypi_name aiosasl

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Protocol agnostic SASL Python library

License:        LGPLv3+
URL:            https://github.com/horazont/aiosasl
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiosasl, pure Python generic asyncio SASL library aiosasl provides a generic,
asyncio-based SASL library. It can be used with any protocol, provided the
necessary interface code is provided by the application or protocol
implementation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyopenssl)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiosasl, pure Python generic asyncio SASL library aiosasl provides a generic,
asyncio-based SASL library. It can be used with any protocol, provided the
necessary interface code is provided by the application or protocol
implementation.

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
%license LICENSES COPYING.LESSER COPYING.gpl3
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-2
- Implement review comments (rhbz#1876901)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora
