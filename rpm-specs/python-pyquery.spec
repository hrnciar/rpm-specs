%global real_name pyquery

%bcond_without tests

Name:           python-%{real_name}
Version:        1.4.1
Release:        4%{?dist}
Summary:        A jQuery-like library for python
License:        BSD
URL:            http://pypi.python.org/pypi/pyquery
Source0:        %pypi_source pyquery

# skip some tests that need network
Patch1:         python-pyquery-skip-test-requiring-net-connection.patch

BuildArch:      noarch


%global _description\
python-pyquery allows you to make jQuery queries on XML documents. The API is\
as much as possible the similar to jQuery. python-pyquery uses lxml for fast\
XML and HTML manipulation.

%description %_description

%package -n python3-pyquery
Summary:        A jQuery-like library for python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# test deps
BuildRequires:  python3-cssselect
BuildRequires:  python3-lxml >= 2.1
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-webob
%if %{with tests}
BuildRequires:  python3-webtest
%endif

Requires:       python3-lxml >= 2.1
Requires:       python3-cssselect

%description -n python3-pyquery
python3-pyquery allows you to make jQuery queries on XML documents. The API is 
as much as possible the similar to jQuery. python-pyquery uses lxml for fast 
XML and HTML manipulation.


%prep
%autosetup -n %{real_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
%if %{with tests}
nosetests-%{python3_version}

%endif

%files -n python3-pyquery
%doc CHANGES.rst README.rst
%{python3_sitelib}/pyquery/
%{python3_sitelib}/pyquery*.egg-info/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Bootstrap for Python 3.9

* Fri Apr 03 2020 Clement Verna <cverna@tutanota.com> - 1.4.1-1
- Update to 1.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Subpackage python2-pyquery has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.4.0-1
- Update to 1.4.0

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.3.0-7
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Bootstrap for Python 3.7

* Wed Feb 28 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3.0-4
- Use /usr/bin/python2 instead of /usr/bin/python when building and installing.

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Kevin Fenzi <kevin@scrye.com> - 1.3.0-1
- Update to 1.3.0. Fixes bug #1505136

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.2.17-7
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.17-6
- Python 2 binary package renamed to python2-pyquery
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
