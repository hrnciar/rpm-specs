%global srcname queuelib

Name:           python-queuelib
Version:        1.5.0
Release:        8%{?dist}
Summary:        Collection of persistent (disk-based) queues

License:        BSD
URL:            https://github.com/scrapy/queuelib
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
nosetests-%{python3_version} queuelib/tests

%files -n python3-%{srcname}
%doc NEWS README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0
- Use upstream source

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-10
- Subpackage python2-queuelib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015  Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Cleanup
- Upate to latest upstream release 1.4.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Jan 04 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Mon Oct 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-3
- Naming of Py3 package updated

* Mon Sep 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-2
- Python macro updated

* Wed Sep 04 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial spec file for Fedora
