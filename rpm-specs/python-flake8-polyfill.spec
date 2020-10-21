%global srcname flake8-polyfill

Name:           python-%{srcname}
Version:        1.0.2
Release:        9%{?dist}
Summary:        Polyfill package for Flake8 plugins

License:        MIT
URL:            https://gitlab.com/pycqa/%{srcname}
Source0:        https://gitlab.com/pycqa/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as pycqa/flake8-polyfill#1
Patch0:         %{name}-1.0.2-pytest-4-compatibility.patch

BuildArch:      noarch

%description
flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-flake8
%endif

%description -n python%{python3_pkgversion}-%{srcname}
flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  py.test-%{python3_version} \
  --ignore=tests/test_stdin.py \
  tests


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python3_sitelib}/flake8_polyfill/
%{python3_sitelib}/flake8_polyfill-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Rebuilt for Python 3.9

* Thu Feb 20 2020 Scott K Logan <logans@cottsay.net> - 1.0.2-7
- Drop pep8 requirement and skip test which needs it
- Fix automatic python dependency conditional

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Scott K Logan <logans@cottsay.net> - 1.0.2-2
- Add patch for pytest 4 compatibility, pytest 3 deprecation (rhbz#1716494)

* Thu Mar 21 2019 Scott K Logan <logans@cottsay.net> - 1.0.2-1
- Initial package
