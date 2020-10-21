Name:           pycmd
Version:        1.2
Release:        22%{?dist}
Summary:        Tools for managing/searching Python related files
License:        MIT
URL:            https://pypi.python.org/pypi/pycmd
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
Pycmd is a collection of command line tools for helping with Python
development.

%package -n python%{python3_pkgversion}-pycmd
Summary:        Tools for managing/searching Python related files
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-py >= 1.4.0
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-py >= 1.4.0
%{?python_provide:%python_provide python%{python3_pkgversion}-pycmd}


%description -n python%{python3_pkgversion}-pycmd
Pycmd is a collection of command line tools for helping with Python
development.


%prep
%setup -q


%build
%py3_build


%install
%py3_install

# remove shebangs from all scripts
find %{buildroot}%{python3_sitelib} -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;


%files -n python%{python3_pkgversion}-pycmd
%doc README.txt
%doc CHANGELOG
%license LICENSE
%{_bindir}/py.cleanup
%{_bindir}/py.convert_unittest
%{_bindir}/py.countloc
%{_bindir}/py.lookup
%{_bindir}/py.svnwcrevert
%{_bindir}/py.which
%{python3_sitelib}/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-18
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.2-17
- Drop Python2 subpackage.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-13
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2-8
- Ship python2-pycmd
- Build python3 for EPEL
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.2-2
- Remove extra %%setup command.

* Thu Apr 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.2-1
- Update to 1.2.

* Mon Apr 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-2
- Apply updated Python packaging guidelines.
- Mark LICENSE with %%license.

* Fri Jul 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-1
- Update to 1.1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Aug 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-10
- Update distribute_setup.py (fixes rhbz#992844).
- Modernize spec file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.0-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-4
- Fix: python3 dependencies.

* Thu Aug 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-3
- Update Requires and BuildRequires tags.

* Tue Jul  5 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-2
- Python3 subpackage.

* Sun Jan 16 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-1
- New package.
