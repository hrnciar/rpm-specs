%global pypi_name aioopenssl

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        TLS-capable transport using OpenSSL for asyncio

License:        ASL 2.0
URL:            https://github.com/horazont/aioopenssl
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aioopenssl provides a asyncio Transport which uses PyOpenSSL instead of
the built-in ssl module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyopenssl)
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pyopenssl)
%description -n python3-%{pypi_name}
aioopenssl provides a asyncio Transport which uses PyOpenSSL instead of
the built-in ssl module.

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
%doc README.rst
# https://github.com/horazont/aioopenssl/pull/11
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Initial package for Fedora