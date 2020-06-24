%global modname bleach

Name:           python-%{modname}
Version:        3.1.4
Release:        3%{?dist}
Summary:        An easy whitelist-based HTML-sanitizing tool

License:        ASL 2.0
URL:            https://github.com/mozilla/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         python-bleach-3.1.4-html5lib-prerel-compat.patch

BuildArch:      noarch

%global _description \
Bleach is an HTML sanitizing library that escapes or strips markup and\
attributes based on a white list.

%description %{_description}

%package -n python3-%{modname}
Summary:        An easy whitelist-based HTML-sanitizing tool
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-six
BuildRequires:  python3-html5lib
Requires:       python3-six
Requires:       python3-html5lib

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1 -S gendiff

sed -i 's/pytest-runner>=2.0,<3dev/pytest-runner/' setup.py

# Remove vendored libraries which were added for https://github.com/mozilla/bleach/issues/386
rm -r bleach/_vendor/
# Bleach has a shim layer that references the vendored html5lib we just deleted. Let's patch up the
# imports to use the real html5lib.
sed -i "s/bleach._vendor.html5lib/html5lib/g" bleach/html5lib_shim.py tests/test_clean.py


%build
%py3_build

%install
%py3_install

%check
! find %{buildroot}%{python3_sitelib}/bleach/ -type d | grep vendor

if [ $? -ne 0 ]; then
    echo "Detected vendored libraries; please remove them."
    /usr/bin/false
fi;

# skip failing tests until this is fixed:
# https://github.com/mozilla/bleach/issues/503
# https://bugs.python.org/issue27657
%{__python3} -m pytest -k 'not test_uri_value_allowed_protocols or not ("example.com:8000" or "localhost:8000" or "192.168.100.100:8000")'

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Nils Philippsen <nils@redhat.com> - 3.1.4-2
- skip failing tests regardless of Python version

* Wed Apr 22 2020 Nils Philippsen <nils@redhat.com> - 3.1.4-1
- version 3.1.4
- use pythonhosted.org source URL as the tarballs match published hashes
- only skip failing tests and only on Python 3.9
- cope with html5lib prerelease on EL8

* Wed Feb 19 2020 Matthias Runge <mrunge@redhat.com> - 3.1.0-5
- skip tests for python 3.9 

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-4
- Drop python2-bleach (#1746757).

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0.
- https://github.com/mozilla/bleach/blob/v3.1.0/CHANGES

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2 (#1641626).
- https://github.com/mozilla/bleach/blob/v3.0.2/CHANGES

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4.
- https://github.com/mozilla/bleach/blob/v2.1.4/CHANGES

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-2
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild