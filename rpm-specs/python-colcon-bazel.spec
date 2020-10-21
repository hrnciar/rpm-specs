%global srcname colcon-bazel

Name:           python-%{srcname}
Version:        0.1.0
Release:        10%{?dist}
Summary:        Extension for colcon to support Bazel packages

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as colcon/colcon-bazel#15
Patch0:         %{name}-0.1.0-python-39.patch
# Submitted upstream as colcon/colcon-bazel#16
Patch1:         %{name}-0.1.0-regex-escapes.patch

BuildArch:      noarch

%description
An extension for colcon-core to support Bazel projects.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-argcomplete
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.9
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.9
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-pyparsing
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support Bazel projects.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/colcon_bazel/
%{python3_sitelib}/colcon_bazel-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Aug 03 2020 Scott K Logan <logans@cottsay.net> - 0.1.0-10
- Add a patch to fix a test with Python 3.9
- Add a patch to resolve some deprecation warnings
- Add a 'pytest_asyncio' build dependency where supported

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.1.0-2
- Fix changelog version

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Fri Nov 09 2018 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
