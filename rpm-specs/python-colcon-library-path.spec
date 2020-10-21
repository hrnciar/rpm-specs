%global srcname colcon-library-path

Name:           python-%{srcname}
Version:        0.2.1
Release:        9%{?dist}
Summary:        Extension for colcon adding an environment variable to find libraries

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to set an environment variable to find shared
libraries at runtime.


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
An extension for colcon-core to set an environment variable to find shared
libraries at runtime.


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
%{python3_sitelib}/colcon_library_path/
%{python3_sitelib}/colcon_library_path-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-3
- Drop obsolte Group

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Thu Jan 17 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Initial package
