%global pypi_name sybil

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Automated testing for the examples in your documentation

License:        MIT
URL:            https://sybil.readthedocs.io/
Source0:        https://github.com/cjw296/sybil/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides a way to test examples in your documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of your normal test run. Integration is provided for the three main Python
test runners.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-nose
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides a way to test examples in your documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of your normal test run. Integration is provided for the three main Python
test runners.

%package doc
Summary:        Documentation for python3-%{pypi_name}

BuildRequires:  python3-sphinx

%description doc
This documentation for python3-%{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
pushd docs
PYTHONPATH=%{buildroot}/%{python3_sitelib} make html
rm _build/html/.buildinfo
popd

# nose tests are failing because they are not ported to Python 3 yet
%check
pytest-%{python3_version} tests -k "not nose"

%files -n python3-%{pypi_name}
%doc README.rst
%license docs/license.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%files doc
%doc docs/_build/html/

%changelog
* Thu Aug 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0 (rhbz#1861675)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> -  1.3.0-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.9

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (rhbz#1818465)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-2
- Enable tests
- Add documentation

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Initial package for Fedora
