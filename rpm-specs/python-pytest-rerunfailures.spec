%global srcname pytest-rerunfailures

Name:           python-%{srcname}
Version:        9.0
Release:        1%{?dist}
Summary:        A py.test plugin that re-runs failed tests to eliminate flakey failures

License:        MPLv2.0
URL:            https://github.com/pytest-dev/%{srcname}
Source0:        https://github.com/pytest-dev/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
pytest-rerunfailures is a plugin for py.test that re-runs tests to eliminate
intermittent failures.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest >= 5.0
BuildRequires:  python%{python3_pkgversion}-setuptools >= 40.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-pytest >= 5.0
Requires:       python%{python3_pkgversion}-setuptools >= 40.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
pytest-rerunfailures is a plugin for py.test that re-runs tests to eliminate
intermittent failures.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} test_pytest_rerunfailures.py


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python3_sitelib}/pytest_rerunfailures.py
%{python3_sitelib}/__pycache__/pytest_rerunfailures.cpython-*
%{python3_sitelib}/pytest_rerunfailures-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri May 29 2020 Scott K Logan <logans@cottsay.net> - 9.0-1
- Update to 9.0 (rhbz#1773599)

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 8.0-1
- Update to 8.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Scott K Logan <logans@cottsay.net> - 7.0-1
- Update to 7.0 (rhbz#1693860)

* Tue Feb 12 2019 Scott K Logan <logans@cottsay.net> - 6.0-1
- Initial package
