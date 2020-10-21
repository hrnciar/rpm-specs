# When we are bootstrapping, we drop some dependencies, and/or build time tests.
# Set this to 0 after we've bootstrapped.
%{!?_with_bootstrap: %global bootstrap 1}

%global modname pyface

Name:           python-%{modname}
Version:        7.1.0
Release:        1%{?dist}
Summary:        Generic User Interface objects

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
License:        BSD and EPL and LGPLv2+ and Public Domain
URL:            https://github.com/enthought/pyface
# Current release is missing files
# https://github.com/enthought/pyface/issues/98
#Source0:        http://www.enthought.com/repo/ets/pyface-%{version}.tar.gz
Source0:        https://github.com/enthought/pyface/archive/%{version}/pyface-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  /usr/bin/xvfb-run

%description
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Traits
%if ! 0%{?bootstrap}
BuildRequires:  python%{python3_pkgversion}-traitsui
%endif
BuildRequires:  python%{python3_pkgversion}-pygments
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-six
# For tests
BuildRequires:  python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-Traits >= 6.0.0
%if ! 0%{?bootstrap}
Requires:       python%{python3_pkgversion}-traitsui
%endif
Requires:       python%{python3_pkgversion}-pygments
Requires:       python%{python3_pkgversion}-%{modname}-backend
Requires:       python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{modname}
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

Python 3 version.

%package doc
Summary:        Documentation for pyface

%description doc
Documentation and examples for pyface.

%package -n python%{python3_pkgversion}-%{modname}-qt
Summary:        Qt backend placeholder for pyface
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}-qt}
Requires:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}
%if 0%{?fedora} >= 32
BuildRequires:  python%{python3_pkgversion}-PyQt5
BuildRequires:  python%{python3_pkgversion}-qt5-webkit
BuildRequires:  python%{python3_pkgversion}-pyqt5-sip
Requires:       python%{python3_pkgversion}-PyQt5
Requires:       python%{python3_pkgversion}-qt5-webkit
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%else
BuildRequires:  python%{python3_pkgversion}-PyQt4
BuildRequires:  python%{python3_pkgversion}-PyQt4-webkit
BuildRequires:  python%{python3_pkgversion}-pyqt4-sip
Requires:       python%{python3_pkgversion}-PyQt4
Requires:       python%{python3_pkgversion}-PyQt4-webkit
%{?_sip_api:Requires: python3-pyqt4-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%endif
Provides:       python%{python3_pkgversion}-%{modname}-backend

%description -n python%{python3_pkgversion}-%{modname}-qt
Qt backend placeholder for pyface.

%prep
%autosetup -p1 -n pyface-%{version}
# file not utf-8
for f in image_LICENSE_{Eclipse,OOo}.txt
do
  iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && mv -f ${f}.conv ${f}
done


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} xvfb-run %{__python3} -s -m unittest discover -v

 
%files -n python%{python3_pkgversion}-%{modname}
%license image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst
%{python3_sitelib}/%{modname}*

%files doc
%doc docs/DockWindowFeature.pdf examples

%files -n python%{python3_pkgversion}-%{modname}-qt

%changelog
* Tue Oct 20 2020 Orion Poplawski <orion@nwra.com> - 7.1.0-1
- Update to 7.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Orion Poplawski <orion@nwra.com> - 7.0.1-1
- Update to 7.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Orion Poplawski <orion@nwra.com> - 7.0.0-1
- Update to 7.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 1 2019 Orion Poplawski <orion@nwra.com> - 6.1.2-2
- Upstream patch for PyQt4 4.12.2 support (bugz#1753414)
- Switch to Qt5 for Fedora 32+

* Thu Aug 22 2019 Orion Poplawski <orion@nwra.com> - 6.1.2-1
- Update to 6.1.2
- Enable bootstrap
- Require PyQt4-webkit

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  8 2019 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Add BR/R on python3-sip for PyQt4 backend
- Allow tests to fail build again

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Subpackages python2-pyface, python2-pyface-qt, python2-pyface-wx have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 6.0.0-1
- Update to 6.0.0

* Sun Jul 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.0-10
- De-bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- Bootstrap

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-8
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-2
- Disable bootstrap

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0
- Add bootstrap, and enable it for python 3.6 build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Robert Kuska <rkuska@redhat.com> - 5.0.0-8
- Rebuilt with traitsui

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 9 2015 Orion Poplawski <orion@cora.nra.com> - 5.0.0-6
- Restore doc sub-package, fix doc installs

* Mon Nov 9 2015 Orion Poplawski <orion@cora.nra.com> - 5.0.0-5
- Add %%python_provides to qt/wx sub-packages
- Use sub-dirs for build

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-4
- Rebuild against traitsui

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-3
- Fix BR/Rs

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-2
- Return back to PyQt4
- Add python3-subpackages (only qt backend supported)
- Fix license a bit

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Update to 5.0.0
- Switch qt requires to pyside

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.5.2-1
- Update to 4.5.2
- Add BR/R on python-pygments

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Mon Sep 16 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-4
- Create dummy backend packages to express dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Fix non-UTF-8 files
- Add doc sub-package
- Be more explicit with files

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Initial package
