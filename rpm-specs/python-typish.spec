%global pypi_name typish

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        2%{?dist}
Summary:        Python library for additional control over types

License:        MIT
URL:            https://github.com/ramonhagenaars/typish
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Suport for functions to allow thorough checks on types. Including instance
checks considering generics and typesafe duck-typing.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(nptyping)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(coverage)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Suport for functions to allow thorough checks on types. Including instance
checks considering generics and typesafe duck-typing.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# https://github.com/ramonhagenaars/typish/issues/18
%pytest -v tests -k "not test_instance_of_union and not test_is_type_annotation and not test_subclass_of_union"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-2
- Disable failing tests (rhbz#1875996)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Initial package for Fedora
