%global srcname coloredlogs

Name:           python-%{srcname}
Version:        14.0
Release:        3%{?dist}
Summary:        Colored terminal output for Python's logging module

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal.


%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-capturer >= 2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-humanfriendly >= 7.1
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-verboselogs >= 1.7
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-humanfriendly >= 7.1
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal.


%prep
%autosetup -p1


%build
%py3_build

# Don't install tests.py
rm build/lib/%{srcname}/tests.py

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo


%install
%py3_install


%check
# Some hacking to get the pth file to get processed outside
# of the build host's site dir. This sitecustomize.py needs
# to be somewhere in the path.
mkdir -p fakesite
echo "import site; site.addsitedir(site.USER_SITE)" > fakesite/sitecustomize.py

PATH=%{buildroot}%{_bindir}:$PATH \
    PYTHONPATH=$PWD/fakesite \
    PYTHONUSERBASE=%{buildroot}%{_prefix} \
    PYTHONUNBUFFERED=1 \
    py.test-%{python3_version} \
    %{srcname}/tests.py


%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}.pth
%{_bindir}/%{srcname}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 14.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 14.0-1
- Update to 14.0 (rhbz#1803324)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 10.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 10.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 10.0-7
- Drop python2 and python3_other
- Deselect plain_text test on Python >= 3.7 (xolox/python-coloredlogs#66)

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 10.0-6
- Pattern conformance

* Fri Sep 28 2018 Scott K Logan <logans@cottsay.net> - 10.0-5
- Disable python2 for Fedora 30+
- Better conditionals in spec
- Enable tests

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 10.0-4
- Enable both python34 and python36 for EPEL

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 10.0-3
- Add missing setuptools BR for EPEL

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 10.0-2
- Enable python34 builds for EPEL

* Thu Sep 20 2018 Scott K Logan <logans@cottsay.net> - 10.0-1
- Initial package
