%global commit 24ddaecfc6e1099f96330757181174e7054d6cd6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           librealsense1
Version:        1.12.4
Release:        5.%{shortcommit}%{?dist}
Summary:        Cross-platform camera capture for Intel RealSense

License:        ASL 2.0 and BSD
URL:            https://github.com/IntelRealSense/librealsense
Source0:        https://github.com/IntelRealSense/librealsense/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Remove custom CFLAGS that override ours.
# This was discussed with upstream, but upstream wants to keep those flags.
# See https://github.com/IntelRealSense/librealsense/pull/422 for the
# discussion.
Patch0:         librealsense.remove-cflags.patch
Patch1:         librealsense.v1-paths.patch
Patch2:         librealsense.do-not-throw-on-usberror.patch

Obsoletes:      librealsense < 1.12.1-11

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libusb-devel
BuildRequires:  systemd

%description
This project is a cross-platform library (Linux, OSX, Windows) for capturing
data from the Intel RealSense F200, SR300 and R200 cameras. This is a legacy
package to provide support for older camera hardware. For newer hardware, use
librealsense.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Obsoletes:      librealsense-devel < 1.12.1-11

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
BuildArch:      noarch
Summary:        Documentation for %{name}

Obsoletes:      librealsense-doc < 1.12.1-11

%description    doc
The %{name}-doc package contains documentation for developing applications
with %{name}.


%prep
%autosetup -p1 -n librealsense-%{commit}


%build
%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}
%cmake_build

sed -i "s:/usr/local/bin:%{_datadir}/realsense1:" config/*
sed -i "s/plugdev/users/g" config/*rules

pushd doc/Doxygen_API
# Do not generate Windows help files
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  Doxyfile
doxygen
popd


%install
%cmake_install

mkdir -p %{buildroot}/%{_udevrulesdir}
install -p -m644 config/99-realsense-libusb.rules \
  %{buildroot}/%{_udevrulesdir}/99-realsense1-libusb.rules
mkdir -p %{buildroot}/%{_datadir}/realsense1
install -p -m755 config/usb-R200-in{,_udev} %{buildroot}/%{_datadir}/realsense1


%files
%license LICENSE
%doc readme.md
%{_libdir}/librealsense1.so.*
%{_datadir}/realsense1
%{_udevrulesdir}/*

%files devel
%{_includedir}/librealsense1
%{_libdir}/librealsense1.so
%{_libdir}/cmake/realsense1

%files doc
%license LICENSE
%doc doc/Doxygen_API/html/*


%changelog
* Fri Sep 04 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.12.4-5.24ddaec
- Adapt to CMake out-of-source builds
  https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-4.24ddaec
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-3.24ddaec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2.24ddaec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.4-1.24ddaec
- Update to 1.12.4
- Remove upstreamed patch for recent kernels

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-b7a6fb9.5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.3-b7a6fb9.5
- Switch to better patch for recent kernel bug fix (upstream PR #3929)

* Sat Apr 27 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.3-b7a6fb9.4
- Add patch so no exception is thrown when an USB error occurs while polling

* Mon Apr 15 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.3-b7a6fb9.3
- Remove libuvc patch, fix v2l2 backend instead (updated upstream PR #3749)

* Fri Apr 12 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.3-b7a6fb9.2
- Add patch to switch to libuvc (upstream PR #3749)

* Fri Apr 12 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.12.3-b7a6fb9.1
- Move to git snapshots (upstream no longer provides proper releases)
- Update to 1.12.3
- Remove upstreamed patches

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.1-16
- Add patch to fix missing includes of sys/sysmacros.h

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.1-14
- Rename all install paths from librealsense to librealsense1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.12.1-12
- Add license file to doc subpackage

* Sun Dec 24 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.12.1-11
- Rename to librealsense1
- Add Obsoletes: for old package versions

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-7
- Add missing BR: gcc-c++

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-6
- Add patch for missing include of sys/time.h to fix build error on ppc64

* Wed Mar 22 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-5
- Add patch for missing include of functional header

* Sat Jan 21 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-4
- Add patch to remove any CFLAGS modification in cmake
- Change License to "ASL 2.0 and BSD"
- Remove trademarks from description

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-3
- Install bash scripts into datadir, not into libdir

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-2
- Add patch to fix build flags on arm

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.12.1-1
- Update to 1.12.1
- Switch to cmake for building the package

* Mon Jan 16 2017 Till Hofmann <till.hofmann@posteo.de> - 1.9.7-2
- Fix paths in udev rules

* Mon Aug 29 2016 Till Hofmann <till.hofmann@posteo.de> - 1.9.7-1
- Initial package
