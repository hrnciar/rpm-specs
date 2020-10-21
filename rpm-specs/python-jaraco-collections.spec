%global pypi_name jaraco.collections

Name:           python-jaraco-collections
Version:        3.0.0
Release:        4%{?dist}
Summary:        Collection objects similar to those in stdlib by jaraco

License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(jaraco.classes)
BuildRequires:  python3dist(jaraco.packaging) >= 3.2

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15.0
BuildRequires:  python3dist(sphinx)

%if %{with tests}
# test requirements
BuildRequires:  python3dist(jaraco.text)
BuildRequires:  python3dist(pytest) >= 3.5
BuildRequires:  python3dist(pytest-black-multipy)
BuildRequires:  python3dist(pytest-checkdocs) >= 1.2.3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(six) >= 1.7.0
%endif

%description
%{summary}

%package -n     python3-jaraco-collections
Summary:        %{summary}
 
Requires:       python3-jaraco

# The package name was changed. Obsolete the previous
# name to provide a clean upgrade path.
# Remove in Fedora >= 36
Obsoletes:      python3-jaraco.collections < 3.0.0-3

%description -n python3-jaraco-collections
%{summary}

%package -n python-jaraco-collections-doc
Summary:        jaraco.collections documentation

# The package name was changed. Obsolete the previous
# name to provide a clean upgrade path.
# Remove in Fedora >= 36
Obsoletes:      python-jaraco.collections-doc < 3.0.0-3

%description -n python-jaraco-collections-doc
Documentation for jaraco.collections

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if %{with tests}
%check
%pytest
%endif

%install
%py3_install

%files -n python3-jaraco-collections
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%pycached %exclude %{python3_sitelib}/jaraco/__init__.py
%pycached %{python3_sitelib}/jaraco/collections.py
%{python3_sitelib}/jaraco.collections-%{version}-py%{python3_version}.egg-info/

%files -n python-jaraco-collections-doc
%doc html
%license LICENSE

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-3
- Fix a file conflict with python3-jaraco
- Rename the binary rpms to conform to the packaging guidelines
- Misc packaging fixes

* Fri Jun 19 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-2
- review feedback: fix license, remove (wrong) conflict

* Fri Mar 13 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-1
- Initial package.
