%global srcname colcon-ros

Name:           python-%{srcname}
Version:        0.3.21
Release:        1%{?dist}
Summary:        Extension for colcon to support ROS packages

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support ROS packages.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.5.3
BuildRequires:  python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.4.14
Requires:       python%{python3_pkgversion}-colcon-cmake >= 0.2.6
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.3
Requires:       python%{python3_pkgversion}-colcon-pkg-config
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
Requires:       python%{python3_pkgversion}-colcon-recursive-crawl
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       dpkg-dev
%else
Requires:       dpkg-dev
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support ROS packages.


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
%doc README.rst
%{python3_sitelib}/colcon_ros/
%{python3_sitelib}/colcon_ros-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat Oct 17 2020 Scott K Logan <logans@cottsay.net> - 0.3.21-1
- Update to 0.3.21 (rhbz#1889066)

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.3.20-1
- Update to 0.3.20 (rhbz#1881838)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Scott K Logan <logans@cottsay.net> - 0.3.19-1
- Update to 0.3.19 (rhbz#1858472)

* Fri Jun 12 2020 Scott K Logan <logans@cottsay.net> - 0.3.18-1
- Update to 0.3.18 (rhbz#1846603)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-2
- Rebuilt for Python 3.9

* Mon Apr 13 2020 Scott K Logan <logans@cottsay.net> - 0.3.17-1
- Update to 0.3.17 (rhbz#1775856)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Scott K Logan <logans@cottsay.net> - 0.3.13-1
- Update to 0.3.13

* Thu Aug 29 2019 Scott K Logan <logans@cottsay.net> - 0.3.12-1
- Update to 0.3.12 (rhbz#1747250)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.11-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Scott K Logan <logans@cottsay.net> - 0.3.11-1
- Update to 0.3.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.10-1
- Update to 0.3.10
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7

* Fri Mar 01 2019 Scott K Logan <logans@cottsay.net> - 0.3.8-1
- Update to 0.3.8
- Handle automatic dependency generation (f30+)

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.3.7-1
- Update to 0.3.7

* Wed Dec 26 2018 Scott K Logan <logans@cottsay.net> - 0.3.6-1
- Update to 0.3.6

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.3.5-1
- Initial package
