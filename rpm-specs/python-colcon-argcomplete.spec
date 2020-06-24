%global srcname colcon-argcomplete

Name:           python-%{srcname}
Version:        0.3.3
Release:        6%{?dist}
Summary:        Completion for colcon command lines using argcomplete

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Taken from sources - disables install of data files per setuptools version
Patch0:         %{name}-0.3.0-data-files.patch
# Submitted upstream - uses the 'root' argument to setup.py install properly
Patch1:         %{name}-0.3.1-use-root-argument.patch

BuildArch:      noarch

%description
An extension for colcon-core to provide command line completion using
argcomplete.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-argcomplete
Requires:       python%{python3_pkgversion}-colcon-core
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide command line completion using
argcomplete.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
BUILD_DEBIAN_PACKAGE=1 \
    %py3_build


%install
BUILD_DEBIAN_PACKAGE=1 \
    %py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_argcomplete/
%{python3_sitelib}/colcon_argcomplete-%{version}-py%{python3_version}.egg-info/
%{_datadir}/colcon_argcomplete/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.3.3-1
- Update to 0.3.3

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-2
- Fix changelog version

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-1
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Thu Jan 17 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-1
- Update to 0.3.2

* Mon Jan 14 2019 Scott K Logan <logans@cottsay.net> - 0.3.1-1
- Update to 0.3.1

* Wed Jan 09 2019 Scott K Logan <logans@cottsay.net> - 0.3.0-1
- Update to 0.3.0

* Fri Dec 28 2018 Scott K Logan <logans@cottsay.net> - 0.2.4-1
- Update to 0.2.4

* Fri Dec 14 2018 Scott K Logan <logans@cottsay.net> - 0.2.3-1
- Update to 0.2.3

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.2-2
- Fix requires and argcomplete file provides

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.2-1
- Initial package
