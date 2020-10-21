%global pypi_name pytenable

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Python library to interface with Tenable's products and applications

License:        MIT
URL:            https://github.com/tenable/pytenable
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(restfly)
BuildRequires:  python3-dateutil
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(requests-pkcs12)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-vcr)
BuildRequires:  python3dist(pytest-datafiles)
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(marshmallow)
BuildRequires:  python3-box
BuildRequires:  python3dist(responses)
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n pyTenable-%{version}
rm -rf %{pypi_name}.egg-info
# Remove standard lib
sed -i -e '42d' setup.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%py3_install

%check
%pytest -v tests -k "not docker"

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/tenable/
%{python3_sitelib}/pyTenable-%{version}-py*.egg-info
%exclude %{python3_sitelib}/tests

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2 (#1875252)

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-2
- Update to latest upstream release 1.2.1 (#1875252)

* Mon Aug 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Fix FTBFS (#1865309)
- Update to latest upstream release 1.1.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Remove configuration file for publishing
- Remove standard library (#1815272)
- Update to latest upstream release 1.1.1

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
