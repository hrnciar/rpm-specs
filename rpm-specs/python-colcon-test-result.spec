%global srcname colcon-test-result

Name:           python-%{srcname}
Version:        0.3.8
Release:        3%{?dist}
Summary:        Extension for colcon to provide information about the test results

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to provide information about the test results.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide information about the test results.


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
%{python3_sitelib}/colcon_test_result/
%{python3_sitelib}/colcon_test_result-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Scott K Logan <logans@cottsay.net> - 0.3.8-1
- Update to 0.3.8 (rhbz#1757635)

* Wed Sep 18 2019 Scott K Logan <logans@cottsay.net> - 0.3.7-1
- Update to 0.3.7 (rhbz#1753409)

* Thu Aug 29 2019 Scott K Logan <logans@cottsay.net> - 0.3.6-1
- Update to 0.3.6 (rhbz#1747251)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Scott K Logan <logans@cottsay.net> - 0.3.5-1
- Update to 0.3.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.3.4-1
- Update to 0.3.4

* Sat May 18 2019 Scott K Logan <logans@cottsay.net> - 0.3.3-1
- Update to 0.3.3

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-1
- Update to 0.3.2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Thu Jan 17 2019 Scott K Logan <logans@cottsay.net> - 0.3.1-1
- Update to 0.3.1

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.3.0-1
- Initial package
