%global srcname extension-helpers
%global modname extension_helpers

%bcond_with doc

Name:           python-%{srcname}
Version:        0.1
Release:        2%{?dist}
Summary:        A build time package to simplify C/Cython extensions

License:        BSD
URL:            https://pypi.python.org/pypi/extension-helpers
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
The extension-helpers package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed
by the Astropy project but is intended to be general and usable by any
Python package.

This is not a traditional package in the sense that it is not intended to be
installed directly by users or developers. Instead, it is meant to be accessed
when the setup.py command is run and should be defined as a build-time
dependency in pyproject.toml files.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Test requirements
BuildRequires:  gcc
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %_description

%if %{with doc}
%package doc
Summary:        Documentation for %{srcname}
BuildRequires:  python3-sphinx

%description doc %_description
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with doc}
pushd docs
PYTHONPATH=.. make html
rm -f _build/html/.buildinfo
popd
%endif

%check
pushd %{buildroot}/%{python3_sitelib}
# For skipped tests check issue filed upstream by Debian packager:
# https://github.com/astropy/extension-helpers/issues/17
py.test-%{python3_version} -k "not (test_add_openmp_flags_if_available or test_generate_openmp_enabled_py)" %{modname}
# Remove pytest remnants
rm -f .coverage.subprocess %{modname}/__pycache__/conftest.cpython*pytest*.pyc
rm -rf .pytest_cache %{modname}/tests/__pycache__
popd

%files -n python3-%{srcname}
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%if %{with doc}
%files doc
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst docs/_build/html
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.1-1
- Initial package (review: RHBZ #1858376)

