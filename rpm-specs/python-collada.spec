%global realname pycollada

Name:           python-collada
Version:        0.6
Release:        8%{?dist}
Summary:        A python module for creating, editing and loading COLLADA

License:        BSD
URL:            https://github.com/pycollada/pycollada
Source0:        https://github.com/pycollada/pycollada/archive/v0.6/%{realname}-%{version}.tar.gz
# Disable pypi downloads in setup.py to guarantee use of only system libs
Patch0:         python-collada-0.4-disable_unittest_downloads.patch
Patch1:         python-collada-py39.patch

BuildArch:      noarch

# Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# unit test requirements
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-numpy


%description
pycollada is a python module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.


%package -n python%{python3_pkgversion}-collada
Summary:        A python 3 module for creating, editing and loading COLLADA
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-numpy
%{?python_provide: %python_provide python%{python3_pkgversion}-collada}

%description -n python%{python3_pkgversion}-collada
pycollada is a python 3 module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%py3_build


%install
%py3_install

 
%check
%{__python3} setup.py test


%files -n python%{python3_pkgversion}-collada
%license COPYING
%doc AUTHORS.md CHANGELOG.rst README.markdown
%{python3_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-2
- Subpackage python2-collada has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Apr 08 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6-1
- Update to 0.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-19
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Richard Shaw <hobbes1069@gmail.com> - 0.4-17
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Richard Shaw <hobbes1069@gmail.com> - 0.4-15
- Fix FTBFS by disabling python3 tests for now, fixes RHBZ#1424133.
- Fix build requirements for python 3 for EPEL 7 so proper package is built.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-13
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul  6 2015 Richard Shaw <hobbes1069@gmail.com> - 0.4-9
- Fix FTBFS on rawhide, fixes BZ#1239822.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct  1 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4-7
- Fix error for Python 3.4.

* Mon Sep  8 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4-6
- Add Python 3 support.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  9 2013 John Morris <john@zultron.com> - 0.4-3
- Rename disable_unittest_downloads patch to silence fedora-review
  warning and add patch description in a comment

* Fri Jan 25 2013 John Morris <john@zultron.com> - 0.4-2
- Add check section
- Add extra BRs for check and build
- Remove unneeded python site{lib,arch} macros

* Wed Jan 23 2013 Richard Shaw <hobbes1069@gmail.com> - 0.4-1
- Initial packaging.
