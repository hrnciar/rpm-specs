%{?mingw_package_header}

%global pkgname eigen3

Name:           mingw-%{pkgname}
Version:        3.3.8
Release:        2%{?dist}
Summary:        MinGW lightweight C++ template library for vector and matrix math
BuildArch:      noarch
# See COPYING.README
License:        MPLv2.0 and LGPLv2+ and BSD
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.bz2
# Since we are crosscompiling, read the comment in the file for details
Source1:        TryRunResults.cmake

# Fix cmake error due to buggy FindCUDA.cmake
# CMake Error at /usr/share/cmake/Modules/FindCUDA.cmake:675 (find_host_program):
#  Unknown CMake command "find_host_program".
# See https://gitlab.kitware.com/cmake/cmake/issues/16509
Patch0:         eigen_disable-cuda.patch

# Drop reference to undefined Eigen::eigen_assert_exception (FIXME??)
Patch1:         eigen_assert_exception.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw32-fftw
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-mpfr

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gcc-gfortran
BuildRequires:  mingw64-fftw
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-mpfr

BuildRequires:  cmake

%description
%{summary}

# Mingw32
%package -n mingw32-%{pkgname}
Summary:                %{summary}

%description -n mingw32-%{pkgname}
%{summary}

# Mingw64
%package -n mingw64-%{pkgname}
Summary:                %{summary}

%description -n mingw64-%{pkgname}
%{summary}


%prep
%autosetup -p1 -n eigen-%{version}


%build
mkdir build_win32
pushd build_win32
%mingw32_cmake -C%{SOURCE1} -DEIGEN_BUILD_PKGCONFIG:BOOL=ON -DINCLUDE_INSTALL_DIR=include/%{pkgname} -DCMAKEPACKAGE_INSTALL_DIR=share/cmake/%{pkgname} -DEIGEN_TEST_CXX11=ON
popd

mkdir build_win64
pushd build_win64
%mingw64_cmake -C%{SOURCE1} -DEIGEN_BUILD_PKGCONFIG:BOOL=ON -DINCLUDE_INSTALL_DIR=include/%{pkgname} -DCMAKEPACKAGE_INSTALL_DIR=share/cmake/%{pkgname} -DEIGEN_TEST_CXX11=ON
popd
# Just as a sanity check
#mingw_make #{?_smp_mflags} buildtests


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license COPYING.BSD COPYING.LGPL COPYING.MPL2 COPYING.README
%{mingw32_includedir}/%{pkgname}
%{mingw32_datadir}/pkgconfig/%{pkgname}.pc
%{mingw32_datadir}/cmake/%{pkgname}/

%files -n mingw64-%{pkgname}
%license COPYING.BSD COPYING.LGPL COPYING.MPL2 COPYING.README
%{mingw64_includedir}/%{pkgname}
%{mingw64_datadir}/pkgconfig/%{pkgname}.pc
%{mingw64_datadir}/cmake/%{pkgname}/


%changelog
* Mon Oct 05 2020 Sandro Mani <manisandro@gmail.com> - 3.3.8-2
- Drop reference to undefined Eigen::eigen_assert_exception

* Mon Oct 05 2020 Sandro Mani <manisandro@gmail.com> - 3.3.8-1
- Update to 3.3.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Sandro Mani <manisandro@gmail.com> - 3.3.7-1
- Update to 3.3.7

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 3.3.6-1
- Update to 3.3.6

* Thu Jul 26 2018 Sandro Mani <manisandro@gmail.com> - 3.3.5-1
- Update to 3.3.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 3.3.4-3
- Rebuild for ppc64le binutils bug

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Sandro Mani <manisandro@gmail.com> - 3.3.4-1
- Update to 3.3.4

* Wed Feb 22 2017 Sandro Mani <manisandro@gmail.com> - 3.3.3-1
- Update to 3.3.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Sandro Mani <manisandro@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Sun Jan 01 2017 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 3.2.10-1
- Update to 3.2.10

* Tue Jul 19 2016 Sandro Mani <manisandro@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Sat Feb 20 2016 Sandro Mani <manisandro@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-3
- Again: Fix incorrect include path in pkgconfig file

* Fri Nov 06 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-2
- Fix incorrect include path in pkgconfig file

* Thu Nov 05 2015 Sandro Mani <manisandro@gmail.com> - 3.2.7-1
- Update to release 3.2.7

* Thu Oct 01 2015 Sandro Mani <manisandro@gmail.com> - 3.2.6-1
- Update to release 3.2.6

* Tue Jun 16 2015 Sandro Mani <manisandro@gmail.com> - 3.2.5-1
- Update to release 3.2.5

* Sat Jan 24 2015 Sandro Mani <manisandro@gmail.com> - 3.2.4-1
- Update to release 3.2.4

* Thu Dec 18 2014 Sandro Mani <manisandro@gmail.com> - 3.2.3-1
- Update to release 3.2.3

* Mon Aug 04 2014 Sandro Mani <manisandro@gmail.com> - 3.2.2-1
- Update to release 3.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Sandro Mani <manisandro@gmail.com> - 3.2.1-1
- Update to release 3.2.1

* Mon Aug 05 2013 Sandro Mani <manisandro@gmail.com> - 3.2-3
- Add patch to work around gcc bug 58087

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Sandro Mani <manisandro@gmail.com> - 3.2-1
- Update to release 3.2

* Fri Apr 19 2013 Sandro Mani <manisandro@gmail.com> - 3.1.3-1
- Update to release 3.1.3

* Tue Mar 05 2013 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Initial fedora package
