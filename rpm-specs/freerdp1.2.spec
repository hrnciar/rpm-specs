Name:           freerdp1.2
Version:        1.2.0
Release:        14%{?dist}
Summary:        Compatibility version of the FreeRDP client libraries
License:        ASL 2.0
URL:            http://www.freerdp.com/

Source0:        https://github.com/FreeRDP/FreeRDP/archive/%{version}-beta1+android9.tar.gz

Patch0:         freerdp-aarch64.patch
# https://github.com/FreeRDP/FreeRDP/commit/1b663ceffe51008af7ae9749e5b7999b2f7d6698
Patch1:         freerdp-cmake-list.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1150349
# https://github.com/FreeRDP/FreeRDP/pull/2310
Patch2:         freerdp-args.patch
Patch3:         freerdp-rpmlint.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  gsm-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXv-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  xmlto

%if 0%{?fedora} >= 26
BuildRequires:  compat-openssl10-devel
%else
BuildRequires:  openssl-devel
%endif

Obsoletes:      compat-freerdp12 < %{version}-%{release}
Provides:       compat-freerdp12 = %{version}-%{release}

%description
Free implementation of the Remote Desktop Protocol (RDP) protocol.
This compatibility package only contains client libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8

Obsoletes:      compat-freerdp12-devel < %{version}-%{release}
Provides:       compat-freerdp12-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}-libs.

%prep
%autosetup -p1 -n FreeRDP-%{version}-beta1-android9

# Rpmlint fixes
find . -name "*.h" -exec chmod 664 {} \;

%build
export CFLAGS="%{optflags} -Wl,--as-needed"
%cmake %{?_cmake_skip_rpath} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DWITH_ALSA=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON -DSTATIC_CHANNELS=OFF \
    -DWITH_DIRECTFB=OFF \
    -DWITH_FFMPEG=OFF \
    -DWITH_GSM=ON \
    -DWITH_GSTREAMER_1_0=ON \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64
    -DWITH_SSE2=ON \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch armv7hl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
%ifarch armv7hnl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=ON \
%endif
%ifarch armv5tel armv6l armv7l
    -DARM_FP_ABI=soft \
    -DWITH_NEON=OFF \
%endif
    .

%make_build

%install
%make_install
find %{buildroot} -name "*.a" -delete

rm -fr %{buildroot}%{_bindir} %{buildroot}%{_mandir}

%ldconfig_scriptlets

%files
%license LICENSE
%doc README ChangeLog
%{_libdir}/freerdp/
%{_libdir}/*.so.*

%files devel
%{_libdir}/cmake/FreeRDP
%{_libdir}/cmake/WinPR
%{_includedir}/freerdp
%{_includedir}/winpr
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.0-9
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-6
- Update build options.
- Update build requirements.

* Thu Mar 16 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-5
- Rename package according to November 2016 packaging guidelines.

* Mon Mar 06 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-3
- rpmlint fixes, use make_build macro.

* Fri Mar 03 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-2
- Link libraries as needed, add license macro, use autosetup macro.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- First build based on the last useful commit of the 1.2.0 packages.
