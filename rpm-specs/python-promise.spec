%global pypi_name promise

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        4%{?dist}
Summary:        Promises/A+ implementation for Python

License:        MIT
URL:            https://github.com/syrusakbary/promise
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide just the
extensions that are absolutely necessary for using promises in Python.
It's fully compatible with the Promises/A+ spec.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-coveralls
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide just the
extensions that are absolutely necessary for using promises in Python.
It's fully compatible with the Promises/A+ spec.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-3
- Fix changelog entry

* Thu Jul 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-2
- Add major release to BR (rhzb#1836559)

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Initial package for Fedora
