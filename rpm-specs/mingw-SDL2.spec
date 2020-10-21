%{?mingw_package_header}

Name:           mingw-SDL2
Version:        2.0.12
Release:        2%{?dist}
Summary:        MinGW Windows port of SDL2 cross-platform multimedia library

License:        LGPLv2+
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/SDL2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

# Not required at the moment, but SDL does contain plenty of C++ code,
# I just haven't worked out how to enable it.
#BuildRequires:  mingw32-gcc-c++

%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


# Win32
%package -n mingw32-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw32-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32 (static)
%package -n mingw32-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw32-SDL2 = %{version}-%{release}

%description -n mingw32-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64
%package -n mingw64-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw64-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64 (static)
%package -n mingw64-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw64-SDL2 = %{version}-%{release}

%description -n mingw64-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


%?mingw_debug_package


%prep
%setup -q -n SDL2-%{version}
dos2unix COPYING.txt README.txt


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove test library.
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libSDL2_test.a
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libSDL2_test.a

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-SDL2
%doc README.txt COPYING.txt
%{mingw32_bindir}/SDL2.dll
%{mingw32_bindir}/sdl2-config
%{mingw32_libdir}/libSDL2.dll.a
%{mingw32_libdir}/libSDL2main.a
%{mingw32_libdir}/cmake/SDL2/
%{mingw32_libdir}/pkgconfig/sdl2.pc
%{mingw32_datadir}/aclocal/sdl2.m4
%{mingw32_includedir}/SDL2

# Win32 (static)
%files -n mingw32-SDL2-static
%{mingw32_libdir}/libSDL2.a

# Win64
%files -n mingw64-SDL2
%doc README.txt COPYING.txt
%{mingw64_bindir}/SDL2.dll
%{mingw64_bindir}/sdl2-config
%{mingw64_libdir}/libSDL2.dll.a
%{mingw64_libdir}/libSDL2main.a
%{mingw64_libdir}/cmake/SDL2/
%{mingw64_libdir}/pkgconfig/sdl2.pc
%{mingw64_datadir}/aclocal/sdl2.m4
%{mingw64_includedir}/SDL2

# Win64 (static)
%files -n mingw64-SDL2-static
%{mingw64_libdir}/libSDL2.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Pete Walter <pwalter@fedoraproject.org> - 2.0.12-1
- Update to 2.0.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 2.0.10-1
- Update to 2.0.10

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.0.9-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Kalev Lember <klember@redhat.com> - 2.0.9-1
- Update to 2.0.9

* Thu Sep 27 2018 Kalev Lember <klember@redhat.com> - 2.0.8-1
- Update to 2.0.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.0.5-1
- Update to 2.0.5
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Anonymous Maarten <anonymous.maarten@gmail.com> - 2.0.3-7
- Added static package.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.3-5
- Don't try to re-implement D3D11 pieces which are already part of mingw-w64
- Workaround a gcc compatibility issue

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-3
- Fix rpmlint warnings

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-1
- Initial rpm
