%global modname zope.schema


Summary: Zope 3 schemas
Name: python-zope-schema
Version: 4.4.2
Release: 18%{?dist}
Source0: http://pypi.python.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
License: ZPLv2.1
BuildArch: noarch
URL: http://pypi.python.org/pypi/zope.schema


%description
This package is a zope.interface extension for defining data schemas.

%package -n python3-zope-schema
Summary:        Zope 3 schemas
%{?python_provide:%python_provide python3-zope-schema}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For docs
BuildRequires: python3-sphinx
# For tests
BuildRequires: python3-zope-testing
BuildRequires: python3-zope-interface
BuildRequires: python3-zope-event

Requires: python3-zope-interface
Requires: python3-zope-event

%description -n python3-zope-schema
This package is a zope.interface extension for defining data schemas.

%prep
%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info


%build
%py3_build

# build Sphinx documents
sphinx-build-%{python3_version} -b html docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -fr html/{.buildinfo,.doctrees}

%install
%py3_install

%check
# the test setup and runner are rather, ahem, 'special' (see setup.py
# all_tests). This silly hack makes it fly on recent Python 3.
ln -s %{python3_sitelib}/zope/* src/zope
# this can fail if sitelib and sitearch are the same on the host doing
# the build, it's no problem
ln -s %{python3_sitearch}/zope/* src/zope >/dev/null || :
%{__python3} setup.py test

%files -n python3-zope-schema
%doc CHANGES.rst COPYRIGHT.txt README.rst
%doc html/
%license LICENSE.txt
%{python3_sitelib}/zope/schema/
%exclude %{python3_sitelib}/zope/schema/tests/
%exclude %{python3_sitelib}/zope/schema/*.txt
%{python3_sitelib}/%{modname}-*.egg-info
%{python3_sitelib}/%{modname}-*-nspkg.pth


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-16
- Subpackage python2-zope-schema has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.2-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Adam Williamson <awilliam@redhat.com> - 4.4.2-6
- Fix Sphinx doc generation
- Fix (in a stupid way, but it works) test running on recent Python 3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.4.2-5
- Modernize python macros.
- Add an explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 4.4.2-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 4.4.1-1
- Latest upstream.
- Modernized python macros.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 4.4.0-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.3.2-1
- Latest upstream.
- README and CHANGES renamed from .txt to .rst.

* Wed Feb 13 2013 Ralph Bean <rbean@redhat.com> - 4.2.2-1
- Latest upstream.
- Added Python3 subpackage.
- Removed dos2unix references.  No longer needed.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1 (#741003)
- Fix ends of lines

* Thu Mar 31 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#689215)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Build Sphinx documents

* Thu Sep 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.7.0-1
- Update to 3.7.0
- Move the documents to proper place
- Exclude the tests

* Sat Sep 11 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.4-2
- Spec cleaned up
- Requires: python-zope-filesystem and python-setuptools removed
- Add %%check section and run tests
- BR: python-zope-testing and runtime requirements added
- Don't move the text files

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.4-1
- Initial packaging
