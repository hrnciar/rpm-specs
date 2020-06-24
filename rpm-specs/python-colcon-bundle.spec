%global srcname colcon-bundle

Name:           python-%{srcname}
Version:        0.0.20
Release:        2%{?dist}
Summary:        Plugin to bundle built software for the colcon command line tool

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as colcon/colcon-bundle#163
Patch0:         %{name}-0.0.20-relax-distro-req.patch

BuildArch:      noarch

%description
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.15
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.15
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.1
Requires:       python%{python3_pkgversion}-distro >= 1.2.0
Requires:       python%{python3_pkgversion}-setuptools >= 30.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc NOTICE README.md
%{python3_sitelib}/colcon_bundle/
%{python3_sitelib}/colcon_bundle-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.0.20-1
- Update to 0.0.20 (rhbz#1818496)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Scott K Logan <logans@cottsay.net> - 0.0.18-1
- Update to 0.0.18 (rhbz#1742142)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.15-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Scott K Logan <logans@cottsay.net> - 0.0.15-1
- Update to 0.0.15 (rhbz#1722296)
- Ignore a test due to known Python 3.8 incompatibility (rhbz#1721930)

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.0.13-1
- Update to 0.0.13
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.0.10-1
- Update to 0.0.10

* Mon Nov 26 2018 Scott K Logan <logans@cottsay.net> - 0.0.8-1
- Update to 0.0.8

* Wed Nov 21 2018 Scott K Logan <logans@cottsay.net> - 0.0.6-1
- Update to 0.0.6

* Thu Nov 01 2018 Scott K Logan <logans@cottsay.net> - 0.0.5-1
- Update to 0.0.5

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.0.4-1
- Initial package
