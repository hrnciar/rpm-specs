%global pypi_name mongomock

Name:           python-%{pypi_name}
Version:        3.20.0
Release:        1%{?dist}
Summary:        Module for testing MongoDB-dependent code

License:        BSD
URL:            https://github.com/mongomock/mongomock
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(sentinels)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not BulkOperationsWithPymongoTest and not CollectionComparisonTest \
  and not MongoClientCollectionTest and not MongoClientSortSkipLimitTest \
  and not test__insert_do_not_modify_input"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.20.0-1
- Initial package for Fedora