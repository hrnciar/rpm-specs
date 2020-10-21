Name:           smesh
Version:        8.3.0.3
Release:        4%{?dist}
Summary:        OpenCascade based MESH framework

License:        LGPLv2
URL:            https://github.com/LaughlinResearch/SMESH

Source0:        https://github.com/LaughlinResearch/SMESH/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         https://github.com/LaughlinResearch/SMESH/pull/21.patch#/smesh-netgen.patch
Patch1:         smesh-install.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  doxygen graphviz
BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  opencascade-devel
BuildRequires:  libXmu-devel
# /builddir/build/BUILD/SMESH-8.3.0.3/inc/DriverMED_Family.h:37:10: fatal
# error: MED_Common.hxx: No such file or directory
#BuildRequires:  med-devel
BuildRequires:  vtk-devel

# Dependencies for optional NETGENPlugin library.
BuildRequires:  netgen-mesher-devel
BuildRequires:  netgen-mesher-devel-private

# Documentation is no longer built
Obsoletes:      %{name}-doc < 6.7.5-9


%description
A complete OpenCascade based MESH framework.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for %{name}.


%prep
%autosetup -p1 -n SMESH-%{version}


%build
LDFLAGS='-Wl,--as-needed'; export LDFLAGS
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DENABLE_NETGEN=ON \
       -DNEW_NETGEN_INTERFACE=ON \
       -DENABLE_MED=OFF \
       -DBUILD_TESTS=TRUE

%cmake_build


%install
%cmake_install


%check
%ctest


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/smesh/
%{_libdir}/*.so
%{_libdir}/cmake/*.cmake


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 8.3.0.3-2
- Rebuilt for Boost 1.73

* Tue May 05 2020 Richard Shaw <hobbes1069@gmail.com> - 8.3.0.3-1
- Update to 8.3.0.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 6.7.5-5
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 6.7.5-2
- Rebuilt for Boost 1.66

* Thu Aug 24 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.5-1
- Update to latest upstream release.

* Thu Jun  1 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.4-1
- Update to latest upstream release.

* Sat May 13 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.3-1
- Update to latest upstream release.

* Wed May 10 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.2-1
- Update to latest upstream release.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.6-2
- Rebuilt for Boost 1.63

* Mon Jul 18 2016 Richard Shaw <hobbes1069@gmail.com> - 6.7-1
- Update to latest upstream release.

* Tue Apr  5 2016 Richard Shaw <hobbes1069@gmail.com> - 6.6-1
- Update to latest upstream release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 6.5.3.1-10
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 6.5.3.1-9
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 6.5.3.1-7
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.5.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 29 2015 Jiri Kastner <jkastner@redhat.com> - 6.5.3.1-4
- fix build for ppc64 on rhel6 and OCE-0.16.1

* Wed Apr 29 2015 Jiri Kastner <jkastner@redhat.com> - 6.5.3.1-3
- fix problems with boost on rhel6

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 6.5.3.1-2
- Rebuild for boost 1.57.0

* Tue Dec  9 2014 Richard Shaw <hobbes1069@gmail.com> - 6.5.3.1-1
- Update to latest upstream release.

* Fri Nov 28 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.4-1
- Move to forked project as original is no longer maintained.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-13
- Add patch for freecad specific tweaks.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 5.1.2.2-11.svn55
- Rebuild for boost 1.55.0

* Thu May 15 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-10.svn55
- Fix license reference in spec file.

* Fri Feb 14 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-9.svn55
- Bump revision to update package license reference.

* Thu Oct 10 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-8.svn55
- Rebuild for OCE-0.13.

* Mon Jul 15 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-7.svn55
- Rebuild for updated OCE.

* Fri Jun 21 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-6.svn55
- Rebuild for OCE 0.12.

* Fri Feb 15 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-1.svn55
- Update for compatibility with new OCE.

* Mon Oct 22 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-5.svn54
- Remove build requirement for fortran (f2c).
- Initial packaging for EPEL 6.

* Wed Sep 26 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-4.svn54
- Rebuild due to package not being signed in F-18 repo.

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.1.2.2-3.svn54
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-2.svn54
- Minor updates to spec file.

* Tue Dec 20 2011 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-1.svn54
- Initial release.
