%global srcname apptools

Name:           python-AppTools
Version:        4.5.0
Release:        3%{?dist}
Summary:        Enthought Tool Suite Application Tools
License:        BSD and LGPLv2+
URL:            http://code.enthought.com/projects/app_tools/
Source0:        https://github.com/enthought/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source1:        README.fedora.%{name}
BuildArch:      noarch

%description
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.


%package -n python-%{srcname}-doc
Summary:        Documentation for %{name}
BuildRequires:  /usr/bin/sphinx-build-3
Obsoletes:      python-AppTools-doc < 4.4.0-1
Provides:       python-AppTools-doc = %{version}-%{release}

%description -n python-%{srcname}-doc
Documentation and examples for %{name}.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Enthough Tool Suite Application Tools
BuildRequires:  /usr/bin/2to3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-traits
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-configobj
Requires:       python%{python3_pkgversion}-pyface
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.


%prep
%setup -q -n %{srcname}-%{version}
# remove exec permission
find examples -type f -exec chmod 0644 {} ";"
cp -p %{SOURCE1} README.fedora
2to3 --write .


%build
%py3_build

pushd docs
make html SPHINXBUILD=%{_bindir}/sphinx-build-3
popd


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license *LICENSE*.txt
%doc CHANGES.txt TODO.txt
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{srcname}/

%files -n python-%{srcname}-doc
%license *LICENSE*.txt
%doc docs/build/html examples README.fedora

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Orion Poplawski <orion@nwra.com> - 4.5.0-1
- Update to 4.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-13
- Subpackage python-apptools-doc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-6
- Make sure we build docs with python2-sphinx

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-3
- Build python3 package

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-2
- Fix requires

* Mon Feb 29 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0
- Ship python2-apptools

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-2
- BR /usr/bin/sphinx-build instead of python-sphinx

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-1
- Update to 4.2.1

* Tue Aug 6 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-3
- Drop BR on python-setupdocs, no longer used

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Update to 4.2.0
- Split off documentation into a separate package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Rakesh Pandit <rakesh@fedoraproject.org> 3.4.0-1
- Updated to 3.4.0

* Fri Aug 13 2010 Chen Lei <supercyper@163.com> 3.3.2-1
- Update spec to match latest guidelines w.r.t %%clean
- Fix several rpmlint warnings

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jan 31 2010 Rakesh Pandit <rakesh@fedoraproject.org> 3.3.0-1
- Updated to 3.3.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-1
- Updated

* Thu Jun 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-4
- Added README.fedora

* Fri Apr 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-3
- Removed AppTools.egg-info directory

* Fri Mar 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Included examples in %%doc, added python-TraitsGUI & python-EnthoughtBase
- as Requires. Added html folder.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Initial package
