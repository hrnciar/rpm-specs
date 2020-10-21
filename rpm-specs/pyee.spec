Name:      pyee
Version:   7.0.2
Release:   2%{?dist}
Summary:   A port of node.js's EventEmitter to python
License:   MIT
URL:       https://pypi.python.org/pypi/pyee
Source0:   https://github.com/jfhbrook/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:    pyee-not-vcs.patch
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-flake8
BuildRequires: python3-mock
BuildRequires: python3-sphinx
BuildRequires: python3-tox
BuildRequires: python3-twisted
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-pytest-runner
BuildRequires: python3-pytest-trio

%description
A port of node.js's EventEmitter to python.

%package -n python3-ee
Summary:       A port of node.js's EventEmitter to python
%{?python_provide:%python_provide python3-ee}

%description -n python3-ee
A port of node.js's EventEmitter to python.

%prep
%setup -q
%patch1 -p1 -b .vcs

%build
%py3_build

%install
%py3_install

%check
# %{__python3} setup.py test

%files -n python3-ee
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> 7.0.2-1
- Update to 7.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.1-2
- Rebuilt for Python 3.9

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 7.0.1-1
- Update to 7.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-4
- Rebuilt for Python 3.7

* Thu May 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 5.0-3
- Fix FTBFS, drop python2 support

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb  5 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.0-1
- initial packaging
