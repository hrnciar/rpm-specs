%global pypi_name jaraco.text
%global pkg_name jaraco-text

# Not all test dependencies are available yet
%bcond_with tests
%bcond_without docs

Name:           python-%{pkg_name}
Version:        3.2.0
Release:        2%{?dist}
Summary:        Module for text manipulation

License:        MIT
URL:            https://github.com/jaraco/jaraco.text
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
#
#BuildRequires:  python3dist(jaraco.functools)

%if %{with tests}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-checkdocs)
BuildRequires: python3dist(pytest-flake8)
BuildRequires: python3dist(pytest-black-multipy)
BuildRequires: python3dist(pytest-cov)
# with tests
%endif

%description
%{summary}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Requires:       python3dist(jaraco.functools)
Requires:       python3dist(six)
Requires:       python3-jaraco

%description -n python3-%{pkg_name}
%{summary}

%package -n python-%{pkg_name}-doc
Summary:        jaraco.text documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(jaraco.packaging)

%description -n python-%{pkg_name}-doc
Documentation for jaraco.text

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# with docs
%endif

%install
%py3_install
install jaraco/text/Lorem\ ipsum.txt \
    %{buildroot}%{python3_sitelib}/jaraco/text/

%if %{with tests}
%check
%pytest
# with tests
%endif

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%{python3_sitelib}/jaraco/text/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
# with docs
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Matthias Runge <mrunge@redhat.com> - 3.2.0-1
- Initial package.
