%global pypi_name sortedcollections

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        3%{?dist}
Summary:        Python Sorted Collections

License:        ASL 2.0
URL:            http://www.grantjenks.com/docs/sortedcollections
Source0:        https://github.com/grantjenks/python-sortedcollections/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sortedcontainers)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Sep 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-3
- Add missing BR

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-2
- Change source to GitHub
- Run tests (rhbz#1876911)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Initial package for Fedora