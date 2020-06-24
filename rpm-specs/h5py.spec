Summary:        A Python interface to the HDF5 library
Name:           h5py
Version:        2.10.0
Release:        2%{?dist}
License:        BSD
URL:            http://www.h5py.org/
Source0:        https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
# patch to use a system liblzf rather than bundled liblzf
Patch0:         h5py-system-lzf.patch
Patch1:         h5py-2.10.x-branch.patch
BuildRequires:  gcc
BuildRequires:  hdf5-devel
BuildRequires:  liblzf-devel
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.23
BuildRequires:  python%{python3_pkgversion}-devel >= 3.2
BuildRequires:  python%{python3_pkgversion}-numpy >= 1.7
BuildRequires:  python%{python3_pkgversion}-pkgconfig
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sphinx

%global _description\
The h5py package provides both a high- and low-level interface to the\
HDF5 library from Python. The low-level interface is intended to be a\
complete wrapping of the HDF5 API, while the high-level component\
supports access to HDF5 files, data sets and groups using established\
Python and NumPy concepts.\
\
A strong emphasis on automatic conversion between Python (Numpy)\
data types and data structures and their HDF5 equivalents vastly\
simplifies the process of reading and writing data from Python.

%description %_description

%package     -n python%{python3_pkgversion}-h5py
Summary:        %{summary}
Requires:       hdf5%{_isa} = %{_hdf5_version}
Requires:       python%{python3_pkgversion}-numpy >= 1.7
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-h5py}
%description -n python%{python3_pkgversion}-h5py %_description

%prep
%setup -q
# use system libzlf and remove private copy
%patch0 -p1 -b .lzf
%patch1 -p1 -b .2.10.x
rm -rf lzf/lzf
%{__python3} api_gen.py

%build
export CFLAGS="%{optflags} -fopenmp"
%py3_build

%install
%py3_install

%check
# https://github.com/h5py/h5py/issues/1337
%ifnarch %ix86
%{__python3} setup.py test
%else
%{__python3} setup.py test || :
%endif

%files -n python%{python3_pkgversion}-h5py
%license licenses/*.txt
%doc ANN.rst README.rst examples
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.10.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.10.0-1
- Add commits from 2.10.x branch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-4
- Rebuild for hdf5 1.10.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-2
- Subpackage python2-h5py has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jan 7 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-1
- Update to 2.9.0
- Drop python2 for Fedora 30+ (bug #1663834)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.8.0-1
- Update to 2.8.0

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.7.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
- Minor clean up

* Tue Feb 13 2018 Christian Dersch <lupinix@mailbox.org> - 2.7.1-3
- Added patch h5py-Dont-reorder-compound-types (required for new numpy>=1.14)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 04 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.7.1-1
- Update to 2.7.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.0-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Mar 20 2017 Orion Poplawski <orion@cora.nwra.com> - 2.7.0-1
- Update to 2.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-6
- Rebuild for Python 3.6

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-5
- Rebuild for hdf5 1.8.18

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-4
- Rebuild for hdf5 1.8.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-2
- Rebuild for hdf5 1.8.17

* Sun Apr 10 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-1
- Update to 2.6.0
- Modernize spec and ship python2-h5py package

* Wed Mar 23 2016 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-8
- Tests run okay now

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-6
- Rebuild for hdf5 1.8.16

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-3
- Add six and pkgconfig dep (thanks Orion!)

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-2
- Rebuild for hdf5 1.8.15

* Mon Apr 13 2015 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-1
- Update to 2.5.0

* Wed Jan 7 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-1
- Update to 2.4.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.1-1
- Update to 2.3.1

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-4
- Rebuild for hdf 1.8.13

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-2
- Rebuild for Python 3.4

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-1
- Update to 2.3.0

* Sun Jan 5 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-2
- Rebuild for hdf5 1.8.12
- Add requires for hdf5 version

* Thu Dec 19 2013 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- 2.2.1

* Thu Sep 26 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.1.3-1
- 2.1.3
- add Python 3 import patches (#962250)

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- rebuild for hdf5 1.8.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.1.0-1
- 2.1.0
- add Python 3 subpackage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- 2.0.1
- docs is removed
- rebase patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 23 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-4
- add patch from Steve Traylen (thanks!) to use system liblzf
 
* Thu Jan 13 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-3
- fix buildroot
- add filter
- don't remove egg-info files
- remove explicit hdf5 req

* Sun Jan  2 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-2
- build and ship docs as html

* Mon Dec 27 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-1
- 1.3.1
- license is BSD only
- run tests
- new url

* Sat Jul  4 2009 Joseph Smidt <josephsmidt@gmail.com> - 1.2.0-1
- initial RPM release
