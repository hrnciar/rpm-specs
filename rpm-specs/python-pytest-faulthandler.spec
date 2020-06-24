%global srcname pytest-faulthandler

Name:           python-%{srcname}
Version:        1.6.0
Release:        6%{?dist}
Summary:        py.test plugin that activates the fault handler module for tests

License:        MIT
URL:            https://github.com/pytest-dev/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools_scm

%description
Plugin for pytest that automatically enables the faulthandler
module during tests. Inspired by the nose faulthandler plugin.

%package -n python3-%{srcname}
Summary:    %{summary}
Requires:   python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Plugin for pytest that automatically enables the faulthandler
module during tests. Inspired by the nose faulthandler plugin.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=$(pwd) py.test-3 ./test_pytest_faulthandler.py

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pytest_faulthandler.py
%{python3_sitelib}/pytest_faulthandler-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/pytest_faulthandler.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Lumír Balhar <lbalhar@redhat.com> - 1.6.0-1
- New upstream version 1.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Lumír Balhar <lbalhar@redhat.com> - 1.5.0-4
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Lumír Balhar <lbalhar@redhat.com> - 1.5.0-1
- New upstream version and build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuild for Python 3.6

* Tue Oct 04 2016 Dominika Krejci <dkrejci@redhat.com> - 1.3.0-1
- Inital release

