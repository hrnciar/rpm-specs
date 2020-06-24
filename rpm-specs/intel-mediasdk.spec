%global mfx_abi 1
%global mfx_version %{mfx_abi}.32

Summary: Hardware-accelerated video processing on Intel integrated GPUs library
Name: intel-mediasdk
Version: 20.1.0
Release: 1%{?dist}
URL: http://mediasdk.intel.com
Source0: https://github.com/Intel-Media-SDK/MediaSDK/archive/%{name}-%{version}.tar.gz
# don't require Intel ICD at build time
Patch0: %{name}-no-icd.patch
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

%prep
%setup -q -n MediaSDK-%{name}-%{version}
%patch0 -p1 -b .no-icd
mkdir build

%build
pushd build
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
    ..
%make_build
popd

%install
pushd build
%make_install
popd

%check
pushd build
%make_build test
popd

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

%changelog
* Fri Apr 10 2020 Dominik Mierzejewski <rpm@greysector.net> 20.1.0-1
- update to 20.1.0 (#1786892)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-2
- Add missing Obsoletes: and Requires:
- Add license text and docs

* Fri Oct 11 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-1
- initial build
