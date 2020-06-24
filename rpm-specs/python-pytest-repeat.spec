%global srcname pytest-repeat

Name:           python-%{srcname}
Version:        0.8.0
Release:        6%{?dist}
Summary:        A pytest plugin for repeating test execution

License:        MPLv2.0
URL:            https://github.com/pytest-dev/%{srcname}
Source0:        https://github.com/pytest-dev/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
pytest-repeat is a plugin for py.test that makes it easy to repeat a single
test, or multiple tests, a specific number of times.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.6
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined python_disable_dependency_generator}
Requires:       python%{python3_pkgversion}-pytest >= 3.6
%endif # python_disable_dependency_generator

%description -n python%{python3_pkgversion}-%{srcname}
pytest-repeat is a plugin for py.test that makes it easy to repeat a single
test, or multiple tests, a specific number of times.


%prep
%autosetup -N -n %{srcname}-%{version}


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %py3_build


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  py.test-%{python3_version} test_repeat.py


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python3_sitelib}/pytest_repeat.py
%{python3_sitelib}/__pycache__/pytest_repeat.cpython-*
%{python3_sitelib}/pytest_repeat-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.8.0-1
- Update to 0.8.0
- Require pytest 3.6
- Drop python3_other subpackage

* Tue Feb 12 2019 Scott K Logan <logans@cottsay.net> - 0.7.0-1
- Initial package
