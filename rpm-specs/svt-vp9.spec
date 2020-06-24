# %global gitcommit_full a34e143c22ca99107c4b4efac0ce266f5e93d79a
# %global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
# %global date 20200117

Name:           svt-vp9
Version:        0.2.0
Release:        2%{?dist}
Summary:        Scalable Video Technology for VP9 Encoder

# ISC license for Source/Lib/ASM_SSE2/x86inc.asm
License:        BSD-2-Clause-Patent and ISC
URL:            https://github.com/OpenVisualCloud/SVT-VP9
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0:        %url/tarball/%{gitcommit_full}

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  yasm
BuildRequires:  meson
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

ExclusiveArch:  x86_64

%description
The Scalable Video Technology for VP9 Encoder (SVT-VP9 Encoder)
is a VP9-compliant encoder library core. The SVT-VP9 Encoder development
is a work-in-progress targeting performance levels applicable to both VOD
and Live encoding/transcoding video applications.

%package        libs
Summary:        Libraries for svt-hevc

%description    libs
Libraries for development svt-hevc.

%package        devel
Summary:        Include files and mandatory libraries for development svt-vp9
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development svt-vp9.

%package -n     gstreamer1-%{name}
Summary:        GStreamer 1.0 %{name}-based plug-in
Requires:       gstreamer1-plugins-base%{?_isa}

%description -n gstreamer1-%{name}
This package provides %{name}-based GStreamer plug-in.

%prep
%autosetup -p1 -n SVT-VP9-%{version}
#-n OpenVisualCloud-SVT-VP9-%{gitcommit}
# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtVp9Enc',|" \
-e "/svtvp9enc_dep =/d" -e 's|, svtvp9enc_dep||' -e "s|svtvp9enc_dep.found()|true|" -i gstreamer-plugin/meson.build


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_SKIP_BUILD_RPATH=TRUE \
    ..
popd
%ninja_build -C %{_target_platform}

pushd gstreamer-plugin
    export LIBRARY_PATH="$PWD/../Bin/Release:$LIBRARY_PATH"
    %meson
    %meson_build
popd


%install
%ninja_install -C %{_target_platform}
pushd gstreamer-plugin
    %meson_install
popd

%files
%{_bindir}/SvtVp9EncApp

%files libs
%license LICENSE.md
%doc README.md Docs/svt-vp9_encoder_user_guide.md
%{_libdir}/libSvtVp9Enc.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/libSvtVp9Enc.so
%{_libdir}/pkgconfig/*.pc

%files -n gstreamer1-%{name}
%{_libdir}/gstreamer-1.0/libgstsvtvp9enc.so

%changelog
* Thu May 07 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.2.0-2
- Update from upstream

* Tue May 05 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Fri Jan 31 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 0.1.1-0.3.20200117gita34e143
- Update to latest git

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.1.1-1
- Update to 0.1.1

* Mon Sep 23 2019 Vasiliy Glazov <vascom2@gmail.com> - 0-1.20190919git68b81bd
- Fixed exit call and executable stack
- Added libs subpackage

* Fri Sep 13 2019 Vasiliy Glazov <vascom2@gmail.com> - 0-1.20190906gite9653d9
- Initial release
