%global pypi_name pytest-testmon

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        A py.test plug-in which executes only tests affected by recent changes
License:        MIT
URL:            http://testmon.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-coverage
#BuildRequires:  python3-unittest_mixins

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%package -n     python3-%{pypi_name}
Summary:        A py.test plug-in which executes only tests affected by recent changes
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pytest
Requires:       python3-coverage
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

This a Python 3 version of the package.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# Had to disable tests for now, missing coverage mixins rpm for tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1833407
# PYTHONPATH=$PWD py.test-3

%files -n python3-%{pypi_name} 
%license LICENSE
%doc README.rst
%{python3_sitelib}/testmon
%{python3_sitelib}/pytest_testmon-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 05 2020 Dan Radez <dradez@redhat.com> - 1.0.3-1
- updating to 1.0.3

* Thu Jul 30 2020 Dan Radez <dradez@redhat.com> - 1.0.2-1
- Updating to 1.0.2
- Had to disable tests for now, missing coverage mixins rpm for tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.19-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Dan Radez <dradez@redhat.com> - 0.9.19-9
- Updating to 0.9.19
- remove fix-py38-compat.patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 02 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.9.16-4
- Fix Python 3.8 compatibility

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradz@redhat.com> - 0.9.16-1
- updating to 0.9.16
- removing < 4 pytest req

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-1
- Update to 0.9.13
- Remove the python2 package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.9.6-1
- update to 0.9.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-1
- Update
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 0.8.2-3
- Add patch for pytest3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-1
- New upstream release (removes the need for old patch)
- Be consistent with Requires and BRs
- Add coverage_pth to Requires
- Run tests and BR on dependencies
- Use GitHub archive to get tests
- export PYTHONPATH before running tests
- Add LICENSE file to %%license

* Fri Mar 11 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-1
- Initial package
