# Created by pyp2rpm-3.3.2
%global pypi_name jaraco.functools
%global pkg_name jaraco-functools
# Fedora doesn't have all the docs deps yet
%bcond_with docs

Name:           python-%{pkg_name}
Version:        3.0.1
Release:        3%{?dist}
Summary:        Functools like those found in stdlib

License:        MIT
URL:            https://github.com/jaraco/jaraco.functools
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch
 
%description
Functools like those found in stdlib

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python3-jaraco
Requires:  python3dist(toml)

BuildRequires:  python3-devel
BuildConflicts: python3dist(pytest) = 3.7.3
BuildRequires:  python3-jaraco-classes
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest) >= 3.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(toml)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Functools like those found in stdlib

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-functools documentation

BuildRequires:  python3dist(jaraco.packaging) >= 3.2
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(sphinx)

%description -n python-%{pkg_name}-doc
Documentation for jaraco-functools
%endif

%prep
%autosetup -n jaraco.functools-%{version}
# Remove bundled egg-info
rm -rf jaraco.functools.egg-info

%build
%py3_build

%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# disabled for right now, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
# LANG=C.utf-8 %%{__python3} -m pytest --ignore=build

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%{python3_sitelib}/jaraco/functools*
%{python3_sitelib}/jaraco/__pycache__/functools*
%{python3_sitelib}/jaraco.functools-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Dan Radez <dradez@redhat.com> - 3.0.1-1
- updating to 3.0.1-1
- added toml dep

* Wed Feb 12 2020 Dan Radez <dradez@redhat.com> - 3.0.0-1
- updating to 3.0.0-1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Dan Radez <dradez@redhat.com> - 2.0-4
- Rebuilding to resolve dep issues

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Dan Radez <dradez@redhat.com> - 2.0-1
- Initial package.
