%global srcname traitlets

Name:           python-%{srcname}
Version:        4.3.3
Release:        3%{?dist}
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects

License:        BSD
URL:            https://github.com/ipython/traitlets
Source0:        https://github.com/ipython/traitlets/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# Fix SyntaxWarnings with python 3.8
# https://bugzilla.redhat.com/show_bug.cgi?id=1750843
Patch0:         python-traitlets-py38.patch

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-decorator
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-ipython_genutils
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-decorator
Requires:       python%{python3_pkgversion}-ipython_genutils
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
py.test-%{python3_version} -v %{srcname}/tests/

 
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license COPYING.md
%{python3_sitelib}/*


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct  5 2019 Orion Poplawski <orion@cora.nwra.com> - 4.3.3-1
- Update to 4.3.3

* Wed Sep 11 2019 Orion Poplawski <orion@nwra.com> - 4.3.2-12
- Fix SyntaxWarnings with python 3.8 (bugz#1750843)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Orion Poplawski <orion@nwra.com> - 4.3.2-9
- Drop python2 (Bugz #1677957)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.3.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Orion Poplawski <orion@cora.nwra.com> - 4.3.2-2
- Really build for python3

* Fri Feb 24 2017 Orion Poplawski <orion@cora.nwra.com> - 4.3.2-1
- Update to 4.3.2
- Build for python3 on EPEL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-3
- Rebuild for Python 3.6

* Thu Oct 13 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-2
- Properly ship python2-traitlets

* Thu Oct 13 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-1
- Update to 4.3.1
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 10 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-1
- Initial package
