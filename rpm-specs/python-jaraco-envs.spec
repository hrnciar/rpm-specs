%global pypi_name jaraco.envs
%global pkg_name jaraco-envs

# Not all test dependencies are available yet
%bcond_with tests
%bcond_without docs

Name:           python-%{pkg_name}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Classes for orchestrating Python (virtual) environments

License:        MIT
URL:            https://github.com/jaraco/jaraco.envs
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(toml)


%if %{with tests}
BuildRequires:       python3dist(pytest)
BuildRequires:       python3dist(pytest-cov)
BuildRequires:       python3-path
BuildRequires:       python3dist(pytest-checkdocs)
BuildRequires:       python3dist(pytest-flake8)
BuildRequires:       python3dist(pytest-black-multipy)
%endif # with tests

%description
Classes for orchestrating Python (virtual) environments.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pkg_name}}

Requires:       python3-path
Requires:       python3-jaraco

%description -n python3-%{pkg_name}
Classes for orchestrating Python (virtual) environments.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-envs documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco.packaging)
BuildRequires:  python3dist(rst.linker)

%description -n python-%{pkg_name}-doc
Documentation for jaraco-envs
%endif # with docs

%prep
%autosetup -n jaraco.envs-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove path and tox-venv dependencies as to not
# automatically generate requires metadata for those.
# path does not provide the python3dist namespace
# and tox-venv is a deprecated package not recommended
# for use.
sed -i '/path/d; /tox-venv/d' setup.cfg

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif # with docs

%install
%py3_install

%if %{with tests}
%check
%pytest
%endif # with tests

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%{python3_sitelib}/jaraco/envs*
%{python3_sitelib}/jaraco/__pycache__/envs*
%{python3_sitelib}/jaraco.envs-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
%endif # with docs

%changelog
* Fri Jun 05 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-2
- Packaging fixes

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-1
- Initial package.