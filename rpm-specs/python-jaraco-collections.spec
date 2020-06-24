%global pypi_name jaraco.collections

Name:           python-jaraco-collections
Version:        3.0.0
Release:        2%{?dist}
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

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(jaraco.classes)
Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       python3dist(jaraco.text)
Requires:       python3dist(six) >= 1.7.0
%description -n python3-%{pypi_name}
%{summary}

%package -n python-%{pypi_name}-doc
Summary:        jaraco.collections documentation
%description -n python-%{pypi_name}-doc
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jun 19 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-2
- review feedback: fix license, remove (wrong) conflict

* Fri Mar 13 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-1
- Initial package.
