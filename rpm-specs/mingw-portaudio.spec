%{?mingw_package_header}
%global datetag 20161030

Name:           mingw-portaudio
Version:        19
Release:        5.%{datetag}%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library

License:        LGPLv2+
URL:            http://www.portaudio.com/
Source0:        http://www.portaudio.com/archives/pa_stable_v%{version}0600_%{datetag}.tgz

# from main portaudio package
Patch3:         portaudio-audacity.patch
# MinGW-specific patches
# Otherwise the library is unusable due to configure assumes MSVC instead of
# MinGW gcc
Patch100:       portaudio-mingw64.patch
Patch101:       portaudio-win-headers.patch

BuildArch:      noarch

BuildRequires:  autoconf automake libtool

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib


%description
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

%package -n mingw32-portaudio
Summary:       %{summary}

%description -n mingw32-portaudio
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

# Win64
%package -n mingw64-portaudio
Summary:       MinGW compiled portaudio for the Win64 target

%description -n mingw64-portaudio
MinGW compiled portaudio for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n portaudio -p1
autoreconf -fiv


%build
%mingw_configure \
  --enable-shared --disable-static \
  --with-winapi=directx,wdmks,wmme,wasapi
%mingw_make_build


%install
%mingw_make_install

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-portaudio
%{mingw32_bindir}/libportaudio-2.dll
%{mingw32_includedir}/portaudio.h
%{mingw32_includedir}/pa_win_*.h
%{mingw32_libdir}/libportaudio.dll.a
%{mingw32_libdir}/pkgconfig/portaudio-2.0.pc

%files -n mingw64-portaudio
%{mingw64_bindir}/libportaudio-2.dll
%{mingw64_includedir}/portaudio.h
%{mingw64_includedir}/pa_win_*.h
%{mingw64_libdir}/libportaudio.dll.a
%{mingw64_libdir}/pkgconfig/portaudio-2.0.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-5.20161030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Richard Shaw <hobbes1069@gmail.com> - 19-4.20161030
- Update per reviewer comments.

* Wed May 13 2020 Richard Shaw <hobbes1069@gmail.com> - 19-3.20161030
- Fix library install location again the right way.

* Wed May 13 2020 Richard Shaw <hobbes1069@gmail.com> - 19-2.20161030
- Give up on making portaudio use the right directories for mingw.

* Sun May 13 2018 Richard Shaw <hobbes1069@gmail.com> - 19-1
- Initial packaging.
