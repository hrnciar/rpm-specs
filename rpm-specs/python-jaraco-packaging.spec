# Created by pyp2rpm-3.2.2
%global pypi_name jaraco.packaging
%global pkg_name jaraco-packaging
# This package is interdependant on rst-linker to build docs
# will build both with out docs and add docs in later
%bcond_with docs 

Name:           python-%{pkg_name}
Version:        8.1.0
Release:        2%{?dist}
Summary:        Tools to supplement packaging Python releases

License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.

%package -n python3-jaraco
Summary: A Parent package for jaraco's parent dir and init file.
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-jaraco}

%description -n python3-jaraco
A Parent package for jaraco's parent dir and init file.

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python3-jaraco
Requires:       python3dist(rst.linker)
Requires:       python3dist(six) >= 1.4
Requires:       python3dist(setuptools)

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-setuptools_scm >= 1.15.0
BuildRequires:  python3dist(six) >= 1.4
BuildRequires:  python3dist(toml)

%if 0%{?python3_version_nodots} < 38
Requires:       python3dist(importlib-metadata) >= 0.18
%endif
BuildRequires:  (python3dist(importlib-metadata) >= 0.18 if python3 < 3.8)

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.


%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco.packaging documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(rst.linker)

%description -n python-%{pkg_name}-doc
Documentation for jaraco.packaging
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if %{with docs}
# generate html docs 
# This package requires itself to build docs :/
PYTHONPATH=./ sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-jaraco
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%exclude %{python3_sitelib}/jaraco/packaging

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{_bindir}/dependency-tree
%{python3_sitelib}/jaraco/packaging
%{python3_sitelib}/jaraco.packaging-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc html 
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.1.0-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Dan Radez <dradez@redhat.com> - 8.1.0-1
- Update to 8.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2-5
- Fix dependency on rst.linker

* Tue Aug 20 2019 Dan Radez <dradez@redhat.com> - 6.2-4
- removing the sed . to _ it's confusing and not needed

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Dan Radez <dradez@redhat.com> - 6.2-1
- updating to 6.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 6.1-7
- fixing egg info

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 6.1-6
- Updating doc reqs in prep to enable doc build

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-5
- fixing python-jaraco-packaging requires... again

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-4
- fixing python-jaraco-packaging requires.

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-3
- adding python-jaraco subpackage.

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-2
- adding py3 subpackage.

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 6.1-1
- Initial package.
