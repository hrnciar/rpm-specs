%global srcname capturer

Name:           python-%{srcname}
Version:        3.0
Release:        2%{?dist}
Summary:        Easily capture stdout/stderr of the current process and subprocesses

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.


%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-humanfriendly >= 8.0
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-humanfriendly >= 8.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-humanfriendly >= 8.0
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.


%prep
%autosetup -p1


%build
%py3_build

# Don't install the tests.py
rm build/lib/%{srcname}/tests.py

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo


%install
%py3_install


%check
PYTHONUNBUFFERED=1 py.test-%{python3_version} %{srcname}/tests.py


%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 3.0-1
- Update to 3.0 (rhbz#1811288)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Scott K Logan <logans@cottsay.net> - 2.4-5
- Drop python2 and python3_other

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 2.4-4
- Fix EL7 python 3.6

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 2.4-3
- Pattern conformance

* Fri Sep 28 2018 Scott K Logan <logans@cottsay.net> - 2.4-2
- Add setuptools dependency to EPEL

* Mon Sep 24 2018 Scott K Logan <logans@cottsay.net> - 2.4-1
- Initial package
