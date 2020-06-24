%global modname traitsui 
Name:           python-%{modname}
Version:        7.0.0
Release:        2%{?dist}
Summary:        User interface tools designed to complement Traits

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file. Except traitsui/editors_gen.py
# which is GPLv2+ all remaining source or image files are in BSD
# 3-clause license
License:        BSD and EPL and LGPLv2 and GPLv2+
URL:            https://github.com/enthought/traitsui
# Current release is missing files
#Source0:        http://www.enthought.com/repo/ets/traitsui-%{version}.tar.gz
Source0:        https://github.com/enthought/traitsui/archive/%{version}/traitsui-%{version}.tar.gz
Obsoletes:      %{name}-doc <= 5.0.0-2
BuildArch:      noarch
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  mesa-dri-drivers

%description
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pyface
BuildRequires:  python%{python3_pkgversion}-pyface-qt
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-Traits >= 6.0.0
# For demo
BuildRequires:  python%{python3_pkgversion}-configobj
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-pyface
Requires:       python%{python3_pkgversion}-Traits >= 6.0.0
Requires:       python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{modname}
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
pushd build/lib/traitsui/tests/
  PYTHONPATH=%{buildroot}%{python3_sitelib} xvfb-run nosetests-%{python3_version} -v
popd

%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE.txt image_LICENSE*.txt
%doc README.rst CHANGES.txt examples
%{python3_sitelib}/%{modname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Orion Poplawski <orion@nwra.com> - 7.0.0-1
- Update to 7.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 6.1.3-1
- Update to 6.1.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  8 2019 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Subpackage python2-traitsui has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 6.0.0-1
- Update to 6.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-2
- Add python3 subpackage

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Update to 5.0.0

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.5.1-1
- Update to 4.5.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 1 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Split documentation in to doc sub-package
- Add requires numpy
- More explicit file listing
- Drop sitelib macro

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Tue Dec 18 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-5
- Change BR to python2-devel

* Wed Dec 5 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-4
- Add upstream patch to move to UTF-8 and remove hidden directories

* Sat Oct 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-3
- Add BR python-setuptools

* Sat Oct 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-2
- Drop CFLAGS comment
- Drop buildroot cleanup
- Add docs and examples to %%doc

* Wed Jun 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Initial package
