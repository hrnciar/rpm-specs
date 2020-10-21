%global debug_package %{nil}

Name:		python-zope-interface
Version:	5.1.2
Release:	1%{?dist}
Summary:	Zope 3 Interface Infrastructure
License:	ZPLv2.1
URL:		https://pypi.io/project/zope.interface
Source0:	https://pypi.io/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%package -n python3-zope-interface
Summary:	Zope 3 Interface Infrastructure
%{?python_provide:%python_provide python3-zope-interface}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-event
BuildRequires:  python3-zope-testing

Requires:       python3-zope-event

%description -n python3-zope-interface
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%prep
%setup -n zope.interface-%{version} -q
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install
# Will put docs in %%{_docdir} instead
%{__rm} -f %{buildroot}%{python3_sitearch}/zope/interface/*.txt
# C files don't need to be packaged
%{__rm} -f %{buildroot}%{python3_sitearch}/zope/interface/_zope_interface_coptimizations.c

%check
# We have to run tests installed together with the package
# https://github.com/zopefoundation/zope.interface/issues/196
pushd %{buildroot}%{python3_sitearch}
PURE_PYTHON=1 python3 -m unittest discover -s zope/interface -t .
popd

%files -n python3-zope-interface
%doc README.rst CHANGES.rst COPYRIGHT.txt docs/
%license LICENSE.txt
%{python3_sitearch}/zope/interface/
# Co-own %%{python3_sitearch}/zope/
%dir %{python3_sitearch}/zope/
%exclude %{python3_sitearch}/zope/interface/tests/
%exclude %{python3_sitearch}/zope/interface/common/tests/
%{python3_sitearch}/zope.interface-*.egg-info
%{python3_sitearch}/zope.interface-*-nspkg.pth

%changelog
* Fri Oct 02 2020 Lumír Balhar <lbalhar@redhat.com> - 5.1.2-1
- Update to 5.1.2 (#1883998)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.9

* Thu Apr 09 2020 Lumír Balhar <lbalhar@redhat.com> - 5.1.0-1
- Update to 5.1.0 (#1822171)

* Fri Mar 20 2020 Lumír Balhar <lbalhar@redhat.com> - 5.0.2-1
- Update to 5.0.2 (#1815086)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Lumír Balhar <lbalhar@redhat.com> - 4.7.1-1
- Update to 4.7.1 (#1771185)

* Fri Oct 25 2019 Lumír Balhar <lbalhar@redhat.com> - 4.6.0-5
- Python 2 subpackage removed

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Lumír Balhar <lbalhar@redhat.com> - 4.6.0-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Lumír Balhar <lbalhar@redhat.com> - 4.5.0-1
- New upstream version
- Specfile cleanup

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.3-2
- Rebuilt for Python 3.7

* Tue Feb 06 2018 Lumír Balhar <lbalhar@redhat.com> - 4.4.3-1
- New upstream release

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 4.3.3-7
- Cleanup spec file conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.3.3-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Jerry James <loganjerry@gmail.com> - 4.3.3-2
- Rebuild for Python 3.6 again

* Wed Dec 14 2016 Ralph Bean <rbean@redhat.com> - 4.3.3-1
- new version

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 4.3.2-2
- Rebuild for Python 3.6

* Tue Sep 27 2016 Ralph Bean <rbean@redhat.com> - 4.3.2-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.2.0-1
- new version

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.1.3-5
- Modernize python macros.
- Provide an explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Dan Horák <dan[at]danny.cz> - 4.1.3-3
- make Python3 support more modular

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 4.1.3-2
- Rebuilt for Python 3.5

* Mon Oct 05 2015 Ralph Bean <rbean@redhat.com> - 4.1.3-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 4.1.2-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 4.1.1-1
- Latest upstream.
- Modernized python macros.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- Latest upstream.
- Change .zip back to .tar.gz.
- Drop fedora 12 conditional.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 4.0.5-1
- Update to 4.0.5 (#891046)
- Run the unit tests with nose

* Tue Mar 26 2013 David Malcolm <dmalcolm@redhat.com> - 4.0.4-2
- remove rhel clause from python3 guard

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.0.4-1
- Latest upstream
- README and CHANGES moved from .txt to .rst.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Ralph Bean <rbean@redhat.com> - 4.0.2-4
- Wrap files section in a python3 conditional.

* Thu Nov 29 2012 Ralph Bean <rbean@redhat.com> - 4.0.2-3
- Typofix to python-zope-event requirement.

* Thu Nov 29 2012 Ralph Bean <rbean@redhat.com> - 4.0.2-2
- Added dependency on python-zope-event.

* Wed Nov 28 2012 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream release.
- Python3 subpackage.
- Rearrange the way we package docs.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Robin Lee <cheeselee@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0 (ZTK 1.1.3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct  4 2010 Robin Lee <cheeselee@fedoraproject.org> - 3.6.1-7
- Obsoletes python-zope-filesystem

* Wed Sep 29 2010 jkeating - 3.6.1-6
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.1-5
- Move the texts files to %%doc
- Exclude the tests from installation
- Filter private shared library provides

* Wed Sep 15 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.1-4
- Run the test suite
- Don't move the text files

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.1-3
- Remove python-zope-filesystem from requirements
- Own %%{python_sitearch}/zope/
- BR: python-setuptools-devel renamed to python-setuptools
- Spec cleaned up

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 22 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.1-1
- update to 3.6.1
- License provided in the source package
- include the tests

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.2-1
- update to 3.5.2

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> 3.5.1-3
- Add python-setuptools-devel to the BuildRequires, so we generate egg-info

* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.1-2
- use correct source filename (upstream switched from zip to tar.gz)

* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.1-1
- update to 3.5.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 3.5.0-3
- Make compatible with the new python-zope-filesystem.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.5.0-2
- Rebuild for Python 2.6

* Sat Nov 15 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.0-1
- update to 3.5.0

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 3.4.1-1
- update to 3.4.1
- incorporate suggestions from Felix Schwarz:
  - new summary and description
  - new upstream URL (old one out of date)
  - don't package test files
  - include more documentation

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 3.3.0-1
- update to 3.3.0
- update source URL to include versioned directory and new tarball name
- drop the gcc 4.x compatibility patch, no longer needed
- don't run the test suite as it now depends on zope.testing
- exclude _zope_interface_coptimizations.c source from the binary package

* Thu Feb 14 2008 Paul Howarth <paul@city-fan.org> 3.0.1-10
- rebuild with gcc 4.3.0 for Fedora 9

* Fri Jan  4 2008 Paul Howarth <paul@city-fan.org> 3.0.1-9
- tweak %%files list to pull in egg info file when necessary
- fix permissions on shared objects (silence rpmlint)

* Wed Aug 29 2007 Paul Howarth <paul@city-fan.org> 3.0.1-8
- update license tag to ZPLv2.1 in anticipation of this tag being approved

* Sat Dec  9 2006 Paul Howarth <paul@city-fan.org> 3.0.1-7
- rebuild against python 2.5 for Rawhide

* Tue Oct 31 2006 Paul Howarth <paul@city-fan.org> 3.0.1-6
- add %%check section

* Wed Sep 20 2006 Paul Howarth <paul@city-fan.org> 3.0.1-5
- dispense with %%{pybasever} macro and python-abi dependency, not needed from
  FC4 onwards
- include ZPL 2.1 license text
- add reference in %%description to origin of patch
- change License: tag from "ZPL 2.1" to "Zope Public License" to shut rpmlint up

* Thu Aug 31 2006 Paul Howarth <paul@city-fan.org> 3.0.1-4
- files list simplified as .pyo files are no longer %%ghost-ed

* Tue May  9 2006 Paul Howarth <paul@city-fan.org> 3.0.1-3
- import from PyVault Repository
- rewrite in Fedora Extras style

* Tue Aug 23 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 3.0.1-2
- add bug fix for gcc 4

* Mon Feb 07 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 3.0.1-1
- new rpm

