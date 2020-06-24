Name:           Field3D
Version:        1.7.3
Release:        2%{?dist}
Summary:        Library for storing voxel data

License:        BSD
URL:            https://sites.google.com/site/field3d/

Source0:        https://github.com/imageworks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake gcc-c++ doxygen
BuildRequires:  hdf5-devel
BuildRequires:  boost-devel
BuildRequires:  ilmbase-devel

Requires:       hdf5 = %{_hdf5_version}


%description
Field3D is an open source library for storing voxel data. It provides C++
classes that handle in-memory storage and a file format based on HDF5 that
allows the C++ objects to be written to and read from disk.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and documentation for %{name}.

# Need devel-docs subpackage.

%prep
%autosetup -p1


%build
mkdir build && pushd build
%cmake -DINSTALL_DOCS=OFF \
       ../

%make_build


%install
pushd build
%make_install
popd

install -D -m 0644 man/f3dinfo.1 %{buildroot}%{_mandir}/man1/f3dinfo.1


%check
pushd build
./unitTest


%files
%doc CHANGES README
%license COPYING
%{_bindir}/f3dinfo
%{_libdir}/libField3D.so.*
%{_mandir}/man1/f3dinfo.1*

%files devel
%doc docs/html/
%{_includedir}/Field3D/
%{_libdir}/libField3D.so


%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-2
- Rebuilt for Boost 1.73

* Thu Mar 12 2020 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-1
- Update to 1.7.3.

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 1.7.2-18
- Avoid hardcoding man page compression

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-15
- Rebuild for OpenEXR 2.3.0.

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.7.2-14
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-12
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-9
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-6
- Rebuilt for Boost 1.64

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-5
- Rebuilt for Boost 1.63

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-4
- Rebuild for hdf5 1.8.18

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-3
- Add patch to fix unit tests on big endian systems.

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-2
- Rebuild for hdf5 1.8.17

* Mon Jun 20 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-1
- Update to latest upstream release.

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7.1-2
- Rebuilt for linker errors in boost (#1331983)

* Wed Mar  2 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.1-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-10
- Rebuild for hdf5 1.8.16

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6.1-6
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-4
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for gcc 5 C++11 ABI

* Tue Feb 10 2015 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-1
- Update to latest upstream release.

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.4.3-4
- Rebuild for boost 1.57.0

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.3-3
- Rebuild for hdf5 1.8.4

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-2
- rebuild (ilmbase), add matching/missing popd's

* Fri Sep  5 2014 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-1
- Update to latest upstream release.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-18
- Rebuild for hdf 1.8.13

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.3.2-16
- Rebuild for boost 1.55.0

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-15
- Rebuild for hdf5 1.8.12

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-14
- rebuild (ilmbase)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-13
- rebuild (ilmbase)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.3.2-11
- Rebuild for boost 1.54.0

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-10
- Rebuild for hdf5 1.8.11

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.3.2-9
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.3.2-8
- Rebuild for Boost-1.53.0

* Mon Dec  3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-7
- Rebuild for hdf5 1.8.10

* Wed Aug  8 2012 David Malcolm <dmalcolm@redhat.com> - 1.3.2-6
- rebuild against boost-1.50

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-3
- Rebuild for hdf5 1.8.9
- Explicitly require the version of hdf5 built with

* Fri Mar 23 2012 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-2
- Bump EVR for oops with F17 package to make sure rawhide package is newer.

* Tue Feb 28 2012 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-1
- Update to latest release.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-2
- Fixed building under GCC 4.7.0.

* Sat Nov 12 2011 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-1
- Initial release.
