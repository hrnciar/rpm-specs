%global srcname nbformat

Name:           python-%{srcname}
Version:        5.0.7
Release:        1%{?dist}
Summary:        The Jupyter Notebook format

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%description
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        The Jupyter Notebook format
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

 
%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.md
%license COPYING.md
%{_bindir}/jupyter-trust

%changelog
* Wed Sep 09 2020 Lumír Balhar <lbalhar@redhat.com> - 5.0.7-1
- Update to 5.0.7 (#1425643)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.5-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Orion Poplawski <orion@nwra.com> - 5.0.5-1
- Update to 5.0.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Orion Poplawski <orion@nwra.com> - 5.0.4-1
- Update to 5.0.4

* Sun Jan 12 2020 Orion Poplawski <orion@nwra.com> - 5.0.3-1
- Update to 5.0.3 (bz#1789213)

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-9
- Correct the BR of python3-jupyter-core

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-6
- Subpackage python2-nbformat has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Tue Aug  8 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.3.0-3
- Fix %%python_provide invocation

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Rebuild for Python 3.6

* Sat Dec 17 2016 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Update to 4.2.0
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-2
- Fixup BRs and EL7 build

* Mon Jul 13 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-1
- Initial package
