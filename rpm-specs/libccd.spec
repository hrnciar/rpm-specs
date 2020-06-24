%ifnarch s390 %{mips}
%global with_valgrind 1
%endif
%global soversion 2

Name:           libccd
Version:        2.1
Release:        1%{?dist}
Summary:        Library for collision detection between convex shapes

License:        BSD
URL:            http://libccd.danfis.cz
Source0:        https://github.com/danfis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch integrates additional programs that are present in
# the testsuites folder into CMake, via CTest.
# It also increments the version number to match the release.
# Not yet submitted  upstream
Patch0:         %{name}-2.1-ctest.patch
# This patch changes the ccd.pc file to point to the correct include
# directory.  Not yet submitted upstream
Patch1:         %{name}-2.1-pkgconfig.patch
# Convert check_regressions to python3
# Not submitted upstream
Patch2:         %{name}-2.1-py3.patch

BuildRequires:  gcc-c++
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  cmake28
%else
BuildRequires:  cmake
%endif
# These are required for executing the test suite
BuildRequires:  python3
%if 0%{?with_valgrind}
BuildRequires:  valgrind
%endif

%description
libccd implements variation on Gilbert-Johnson-Keerthi (GJK) algorithm + 
Expand Polytope Algorithm (EPA). It also implements Minkowski Portal 
Refinement (MPR, a.k.a. XenoCollide) algorithm as published in Game 
Programming Gems 7.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p0 -b .ctest
%patch1 -p0 -b .pkgconfig
%patch2 -p0 -b .py3

%build
mkdir build
pushd build
%if 0%{?rhel} && 0%{?rhel} < 7
%cmake28 \
%else
%cmake \
%endif
  -DBUILD_TESTS=ON \
  -DCMAKE_BUILD_TYPE=None \
  ..
popd
make -C build %{?_smp_mflags}

%install
rm -rf %{buildroot}
make -C build install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_docdir}/ccd


%check
%if 0%{?with_valgrind}
make -C build test ||exit 0
%endif

%ldconfig_scriptlets


%files
%doc BSD-LICENSE README.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%doc 
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/ccd

%changelog
* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 2.1-1
- Update to release 2.1
- Update test suite to use python 3 (rhbz#1807509)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 2.0-7
- No valgrind on MIPS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.0-5
- Valgrind is not available only on s/390 (rhbz#1257526)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <rmattes@fedoraproject.org> - 2.0-1
- Update to release 2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Dan Horák <dan[at]danny.cz> - 1.4-2
- build on platforms without valgrind

* Mon Oct 22 2012 Rich Mattes <richmattes@gmail.com> - 1.4-1
- Update to release 1.4

* Tue May 29 2012 Rich Mattes <richmattes@gmail.com> - 1.3-3
- Fixed pkgconfig file to point to correct include dir

* Sat May 26 2012 Rich Mattes <richmattes@gmail.com> - 1.3-2
- Convert test suite to CTest

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 1.3-1
- Update to release 1.3
- Remove upstreamed soname patch

* Sun May 06 2012 Rich Mattes <richmattes@gmail.com> - 1.2-3
- Removed -static subpackage.

* Mon Apr 30 2012 Rich Mattes <richmattes@gmail.com> - 1.2-2
- Update soname patch to match upstream implementation 

* Fri Apr 27 2012 Rich Mattes <richmattes@gmail.com> - 1.2-1
- Initial package
