%global modname zope.i18nmessageid

Summary: Message Identifiers for internationalization
Name: python-zope-i18nmessageid
Version: 4.0.3
Release: 21%{?dist}
Source0: http://pypi.python.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
License: ZPLv2.1
URL: http://pypi.python.org/pypi/zope.i18nmessageid

# Drop the use of the deprecated setuptools Features
# https://github.com/zopefoundation/zope.i18nmessageid/pull/19
Patch1: new-setuptools.patch

%description
This module provides message identifiers for internationalization.

%package -n python3-zope-i18nmessageid
Summary:    Message Identifiers for internationalization
%{?python_provide:%python_provide python3-zope-i18nmessageid}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-zope-i18nmessageid
This module provides message identifiers for internationalization.


%prep
%autosetup -p1 -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

# remove contained source file(s)
find $RPM_BUILD_ROOT -name '*.c' -type f -print0 | xargs -0 rm -fv

%check
%{__python3} setup.py test

%files -n python3-zope-i18nmessageid
%doc CHANGES.rst README.rst COPYRIGHT.txt
%license LICENSE.txt
# Co-own %%{python3_sitearch}/zope/
%dir %{python3_sitearch}/zope/
%{python3_sitearch}/zope/i18nmessageid/
%{python3_sitearch}/%{modname}-*.egg-info
%{python3_sitearch}/%{modname}-*-nspkg.pth


%changelog
* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 4.0.3-21
- Rebuild after unretiring

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-20
- Rebuilt for Python 3.9

* Mon May 11 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-19
- Fix build with setuptools 46+ (#1817775)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-17
- Subpackage python2-zope-i18nmessageid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.0.3-8
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.0.3-5
- Modernize python macros.
- Create an explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-1
- Latest upstream.
- Modernize python macros.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream
- Added Python3 subpackage

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 3.5.3-3
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.3-2
- Filter private shared library provides

* Wed Sep 15 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.3-1
- Update to 3.5.3
- Requires: python-zope-filesystem and python-setuptools removed
- Add %%check section and run tests
- Co-own %%{python_sitearch}/zope/
- Spec cleaned up

* Tue Jun 22 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.2-2
- don't move the text files

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.2-1
- Initial packaging
