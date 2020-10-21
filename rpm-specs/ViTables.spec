Summary:        Viewer for Hierarchical Datafiles (HDF5)
Name:           ViTables
Version:        3.0.2
Release:        4%{?dist}
License:        GPLv3
URL:            https://www.vitables.org/

Source0:        https://github.com/uvemas/ViTables/archive/v%{version}/vitables-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-tables
BuildRequires:  hdf5-devel
BuildRequires:  python3-sphinx
BuildArch:      noarch

%global _description %{expand:
ViTables is a component of the PyTables family. It is a graphical tool
for browsing and editing files in both PyTables and HDF5 formats. It
is developed using Python and PyQt (the Python binding to the Qt
library), so it can run on any platform that supports these components.}

%description %_description

%package -n vitables
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 3.0.0-1
Requires:       hdf5
Requires:       python3-numpy
Requires:       python3-tables
Requires:       python3-qt5
Requires:       python3-QtPy

%description -n vitables %_description

%package -n vitables-doc
Summary:        vitables documentation and examples
Requires:       vitables = %{version}-%{release}

%description -n vitables-doc
This package contains the documentation and examples for vitables.

%prep
%setup -q

%build
%py3_build
make -C doc html

%install
%py3_install

# force the directory to be the same for ViTables and ViTables-doc
%global _docdir_fmt vitables

%files -n vitables
%license LICENSE.txt
%doc ANNOUNCE.txt README.txt TODO.txt
%{_bindir}/vitables
%{python3_sitelib}/vitables
%{python3_sitelib}/%{name}-%{version}-py*.egg-info

%files -n vitables-doc
%doc examples/
%doc doc/_build/html/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan  5 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-1
- Update to latest bugfix version (#1787834)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-10
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-9
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 3.0.0-7
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-1
- Update to latest version (#1457016)
- Binary packages are renamed to lowercase (vitables and vitables-doc)
- vitables now uses Qt5, so requirements are updated
- Documentation is built from source and provided in the html format

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1-17
- Rebuild for hdf5 1.8.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-16
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1-15
- Rebuild for hdf5 1.8.17

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1-13
- Rebuild for hdf5 1.8.16

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1-11
- Rebuild for hdf5 1.8.15

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1-10
- Rebuild for hdf5 1.8.14

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 2.1-8
- Rebuild for hdf5 1.8.12

* Wed Oct 16 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-7
- Fix for https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Thibault North <tnorth@fedoraproject.org> - 2.1-2
- Fixes

* Tue Nov 8 2011 Thibault North <tnorth@fedoraproject.org> - 2.1-1
- Initial package
