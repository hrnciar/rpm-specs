%global srcname plaster-pastedeploy
%global sum A PasteDeploy binding to the plaster configuration loader

Name: python-%{srcname}
Version: 0.7
Release: 7%{?dist}
BuildArch: noarch

License: MIT
Summary: %{sum}
URL:     https://github.com/Pylons/plaster_pastedeploy
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-paste-deploy >= 2.0.0
BuildRequires: python3-plaster >= 0.5
BuildRequires: python3-pytest


%description
plaster_pastedeploy is a plaster plugin that provides a
plaster.Loader that can parse ini files according to the standard set
by PasteDeploy. It supports the wsgi plaster protocol, implementing
the plaster.protocols.IWSGIProtocol interface.


%package -n python3-%{srcname}
Summary: %{sum}

Requires: python3-paste-deploy >= 1.5.0
Requires: python3-plaster >= 0.5
Requires: python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{description}


%prep
%autosetup -n plaster_pastedeploy-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="./src" py.test-3


%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst
%{python3_sitelib}/plaster_pastedeploy
%{python3_sitelib}/*.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.7-4
- Drop python2-plaster-pastedeploy (#1745067).

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.7-1
- Update to 0.7 (#1699275).
- https://github.com/Pylons/plaster_pastedeploy/blob/0.7/CHANGES.rst

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6-1
- Update to 0.6 (#1562465).
- https://github.com/Pylons/plaster_pastedeploy/blob/0.6/CHANGES.rst

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2 (#1469107).
- https://github.com/Pylons/plaster_pastedeploy/blob/0.4.2/CHANGES.rst

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-2
- Depend on python2-paste-deploy instead of python-paste-deploy.

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-1
- Initial release.
