%undefine __cmake_in_source_build
%global mfx_abi 1
%global mfx_version %{mfx_abi}.34

Summary: Hardware-accelerated video processing on Intel integrated GPUs library
Name: intel-mediasdk
Version: 20.3.0
Release: 2%{?dist}
URL: http://mediasdk.intel.com
Source0: https://github.com/Intel-Media-SDK/MediaSDK/archive/%{name}-%{version}.tar.gz
# don't require Intel ICD at build time
Patch0: %{name}-no-icd.patch
Patch1: %{name}-gcc11.patch
License: MIT
ExclusiveArch: x86_64
BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: gmock-devel
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
BuildRequires: libva-devel
BuildRequires: libX11-devel
BuildRequires: ocl-icd-devel
BuildRequires: wayland-devel
Obsoletes: libmfx < %{mfx_version}
Provides: libmfx = %{mfx_version}
Provides: libmfx%{_isa} = %{mfx_version}

%global __provides_exclude_from ^%{_libdir}/mfx/libmfx_.*\\.so$

%description
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition

%package devel
Summary: SDK for hardware-accelerated video processing on Intel integrated GPUs
Provides: libmfx-devel = %{mfx_version}
Provides: libmfx%{_isa}-devel = %{mfx_version}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition

%package tracer
Summary: Dump the calls of an application to the Intel Media SDK library
Requires: %{name}%{_isa} = %{version}-%{release}

%description tracer
Media SDK Tracer is a tool which permits to dump logging information from the
calls of the application to the Media SDK library. Trace log obtained from this
tool is a recommended information to provide to Media SDK team on submitting
questions and issues.

%prep
%setup -q -n MediaSDK-%{name}-%{version}
%patch0 -p1 -b .no-icd
%patch1 -p1 -b .gcc11

%build
%cmake3 \
    -DBUILD_DISPATCHER=ON \
    -DBUILD_SAMPLES=OFF \
    -DBUILD_TESTS=ON \
    -DBUILD_TOOLS=OFF \
    -DENABLE_OPENCL=ON \
    -DENABLE_WAYLAND=ON \
    -DENABLE_X11=ON \
    -DENABLE_X11_DRI3=ON \
    -DUSE_SYSTEM_GTEST=ON \

%cmake3_build

%install
%cmake3_install

%check
%cmake3_build -- test

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_libdir}/libmfx.so.%{mfx_abi}
%{_libdir}/libmfx.so.%{mfx_version}
%{_libdir}/libmfxhw64.so.%{mfx_abi}
%{_libdir}/libmfxhw64.so.%{mfx_version}
%{_libdir}/mfx/libmfx_*_hw64.so
%{_datadir}/mfx/plugins.cfg

%files devel
%dir %{_includedir}/mfx
%{_includedir}/mfx/mfx*.h
%{_libdir}/libmfx.so
%{_libdir}/libmfxhw64.so
%{_libdir}/pkgconfig/libmfx.pc
%{_libdir}/pkgconfig/libmfxhw64.pc
%{_libdir}/pkgconfig/mfx.pc

%files tracer
%{_bindir}/mfx-tracer-config
%{_libdir}/libmfx-tracer.so
%{_libdir}/libmfx-tracer.so.%{mfx_abi}
%{_libdir}/libmfx-tracer.so.%{mfx_version}

%changelog
* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 20.3.0-2
- Add missing #includes for gcc-11

* Fri Oct 02 2020 Dominik Mierzejewski <rpm@greysector.net> - 20.3.0-1
- update to 20.3.0 (#1884321)

* Fri Aug 07 2020 Dominik Mierzejewski <rpm@greysector.net> - 20.2.1-1
- update to 20.2.1 (#1827296)
- fix build with recent cmake macro changes
- put the new Media SDK Tracer in a separate subpackage

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Dominik Mierzejewski <rpm@greysector.net> 20.1.1-1
- update to 20.1.1

* Fri Apr 10 2020 Dominik Mierzejewski <rpm@greysector.net> 20.1.0-1
- update to 20.1.0 (#1786892)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-2
- Add missing Obsoletes: and Requires:
- Add license text and docs

* Fri Oct 11 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-1
- initial build
