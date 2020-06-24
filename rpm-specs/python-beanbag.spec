Name:           python-beanbag
Version:        1.9.2
Release:        17%{?dist}
Summary:        A helper module for accessing REST APIs
License:        MIT
URL:            https://github.com/ajtowns/beanbag
BuildArch:      noarch

Source0:        https://pypi.python.org/packages/source/b/beanbag/beanbag-%{version}.tar.gz
# Python 3.6 changed the way it was handling the initialization of classes in a metaclass
# thus making tests to fail. This patch addresses the issue.
# Relevant info:
# http://bugs.python.org/issue23722
# https://docs.python.org/3/reference/datamodel.html#class-object-creation
# Patch sent upstream: https://github.com/ajtowns/beanbag/pull/10
Patch0:			py36-metaclass-compatibility.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-requests


%description
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])

See http://beanbag.readthedocs.org/ for more information.

%package -n python3-beanbag
Summary:        A helper module for accessing REST APIs
%{?python_provide:%python_provide python3-beanbag}
Requires:  python3-requests

%description -n python3-beanbag
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])
See http://beanbag.readthedocs.org/ for more information.

%prep
%setup -q -n beanbag-%{version}
%patch0 -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py nosetests || exit 1

%files -n python3-beanbag
%doc README.rst
%license LICENSE
%{python3_sitelib}/beanbag*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-15
- Subpackage python2-beanbag has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-10
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Ralph Bean <rbean@redhat.com> - 1.9.2-2
- Some changes during package review.

* Fri Jan 08 2016 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.9.2-1
- Initial version
