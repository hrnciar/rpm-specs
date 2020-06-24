%{?mingw_package_header}

%global pkgname openal-soft

# Disable qtgui by default for now
%bcond_with qtgui

Name:           mingw-%{pkgname}
Version:        1.18.2
Release:        6%{?dist}
Summary:        Open Audio Library

License:        LGPLv2+
URL:            http://kcat.strangesoft.net/openal.html
Source0:        http://kcat.strangesoft.net/openal-releases/openal-soft-%{version}.tar.bz2
Patch0:         openal-soft-arm_neon-only-for-32bit.patch
# Fixed in a different manner upstream
Patch1:         openal-soft-1.18.2-fix-check_include_file-for-windows.patch
BuildArch:      noarch

BuildRequires:  cmake

# Win32 BRs
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qmake
%endif

# Win64 BRs
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qmake
%endif

%description
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

# Win32
%package -n mingw32-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win32 target
Provides:       mingw32-openal = %{version}-%{release}

%description -n mingw32-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win64 target
Provides:       mingw64-openal = %{version}-%{release}

%description -n mingw64-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n %{pkgname}-%{version} -p1

%build
%mingw_cmake . -DALSOFT_CPUEXT_NEON:BOOL=OFF

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -Dpm644 alsoftrc.sample %{buildroot}%{mingw32_sysconfdir}/openal/alsoft.conf
install -Dpm644 alsoftrc.sample %{buildroot}%{mingw64_sysconfdir}/openal/alsoft.conf

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/OpenAL32.dll
%{mingw32_bindir}/alrecord.exe
%{mingw32_bindir}/altonegen.exe
%{mingw32_bindir}/bsincgen.exe
%{mingw32_bindir}/makehrtf.exe
%{mingw32_bindir}/openal-info.exe
%if %{with qtgui}
%{mingw32_bindir}/alsoft-config.exe
%endif
%{mingw32_sysconfdir}/openal
%{mingw32_includedir}/AL
%{mingw32_libdir}/libOpenAL32.dll.a
%{mingw32_libdir}/cmake/OpenAL/
%{mingw32_libdir}/pkgconfig/openal.pc
%{mingw32_datadir}/openal

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/OpenAL32.dll
%{mingw64_bindir}/alrecord.exe
%{mingw64_bindir}/altonegen.exe
%{mingw64_bindir}/bsincgen.exe
%{mingw64_bindir}/makehrtf.exe
%{mingw64_bindir}/openal-info.exe
%if %{with qtgui}
%{mingw64_bindir}/alsoft-config.exe
%endif
%{mingw64_sysconfdir}/openal
%{mingw64_includedir}/AL
%{mingw64_libdir}/libOpenAL32.dll.a
%{mingw64_libdir}/cmake/OpenAL/
%{mingw64_libdir}/pkgconfig/openal.pc
%{mingw64_datadir}/openal

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.18.2-5
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 1.18.2-1
- Update to 1.18.2
- Fix CMakeLists to build correctly (#1582930)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Neal Gompa <ngompa13@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Neal Gompa <ngompa13@gmail.com> - 1.17.2-1
- Initial import (#1396748)
- Initial packaging based on native Fedora version
