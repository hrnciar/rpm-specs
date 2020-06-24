%global srcname colcon-common-extensions

Name:           python-%{srcname}
Version:        0.2.1
Release:        3%{?dist}
Summary:        Meta package aggregating colcon-core and common extensions

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A meta package aggregating colcon-core as well as a set of common extensions.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-argcomplete
Requires:       python%{python3_pkgversion}-colcon-bash
Requires:       python%{python3_pkgversion}-colcon-cd
Requires:       python%{python3_pkgversion}-colcon-cmake
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-colcon-defaults
Requires:       python%{python3_pkgversion}-colcon-devtools
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-colcon-metadata
Requires:       python%{python3_pkgversion}-colcon-notification
Requires:       python%{python3_pkgversion}-colcon-output
Requires:       python%{python3_pkgversion}-colcon-package-information
Requires:       python%{python3_pkgversion}-colcon-package-selection
Requires:       python%{python3_pkgversion}-colcon-parallel-executor
Requires:       python%{python3_pkgversion}-colcon-powershell
Requires:       python%{python3_pkgversion}-colcon-python-setup-py
Requires:       python%{python3_pkgversion}-colcon-recursive-crawl
Requires:       python%{python3_pkgversion}-colcon-ros
Requires:       python%{python3_pkgversion}-colcon-test-result
Requires:       python%{python3_pkgversion}-colcon-zsh
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
A meta package aggregating colcon-core as well as a set of common extensions.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_common_extensions/
%{python3_sitelib}/colcon_common_extensions-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1 (rhbz#1763100)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.0-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Initial package
