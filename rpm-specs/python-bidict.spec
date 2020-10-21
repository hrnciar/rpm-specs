%global pypi_name bidict

Name:           python-%{pypi_name}
Version:        0.21.2
Release:        1%{?dist}
Summary:        Bidirectional mapping library for Python

License:        MPLv2.0
URL:            https://bidict.readthedocs.io
Source0:        https://github.com/jab/bidict/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         bidict-remove-setuptools-scm.patch
BuildArch:      noarch

%description
Forward declarations for all the custom interpreted text roles that Sphinx
defines and that are used below. This helps Sphinx-unaware tools (e.g.
rst2html, PyPI's and GitHub's renderers, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-benchmark)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sortedcollections)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Forward declarations for all the custom interpreted text roles that Sphinx
defines and that are used below. This helps Sphinx-unaware tools (e.g.
rst2html, PyPI's and GitHub's renderers, etc.

%package -n python-%{pypi_name}-doc
Summary:        bidict documentation

BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for bidict.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v tests --ignore=tests/properties/test_properties.py --ignore=tests/properties/_strategies.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.2-1
- Initial package for Fedora
