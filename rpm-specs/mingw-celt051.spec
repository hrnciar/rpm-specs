%?mingw_package_header

Name:           mingw-celt051
Version:        0.5.1.3
Release:        24%{?dist}
Summary:        An audio codec for use in low-delay speech and audio communication

License:        BSD
# Files without license header are confirmed to be BSD. Will be fixed in later release
# http://lists.xiph.org/pipermail/celt-dev/2009-February/000063.html
URL:            http://www.celt-codec.org/
Source0:        http://downloads.us.xiph.org/releases/celt/celt-%{version}.tar.gz

# Some tests need libcelt but are not explicitly linked against it.
# Windows cross builds fail because of that (native linux builds
# don't for some mysterious reason).  Fix it.
Patch1:         celt051-tests-makefile-fix.patch

# Fixes "libtool: link: warning: undefined symbols not allowed in
# i686-pc-mingw32 shared libraries"
Patch2:         celt051-build-a-dll-for-win32.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libogg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libogg

BuildRequires:  pkgconfig autoconf automake libtool
BuildRequires:  libogg-devel


%description
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio 
codec designed for realtime transmission of high quality speech and audio. 
This is meant to close the gap between traditional speech codecs 
(such as Speex) and traditional audio codecs (such as Vorbis). 

# Win32
%package -n mingw32-celt051
Summary:        An audio codec for use in low-delay speech and audio communication
Requires:       pkgconfig

%description -n mingw32-celt051
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio
codec designed for realtime transmission of high quality speech and audio.
This is meant to close the gap between traditional speech codecs
(such as Speex) and traditional audio codecs (such as Vorbis).

%package -n mingw32-celt051-static
Summary:        Static version of the CELT ultra-low delay audio codec library
Requires:       mingw32-celt051 = %{version}-%{release}

%description -n mingw32-celt051-static
Static version of the CELT ultra-low delay audio codec library.

# Win64
%package -n mingw64-celt051
Summary:        An audio codec for use in low-delay speech and audio communication
Requires:       pkgconfig

%description -n mingw64-celt051
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio
codec designed for realtime transmission of high quality speech and audio.
This is meant to close the gap between traditional speech codecs
(such as Speex) and traditional audio codecs (such as Vorbis).

%package -n mingw64-celt051-static
Summary:        Static version of the CELT ultra-low delay audio codec library
Requires:       mingw64-celt051 = %{version}-%{release}

%description -n mingw64-celt051-static
Static version of the CELT ultra-low delay audio codec library.


%?mingw_debug_package


%prep
%setup -q -n celt-%{version}
%patch1 -p1
%patch2 -p1


%build
autoreconf -i -f
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-celt051
%doc COPYING README TODO
%{mingw32_bindir}/celtenc051.exe
%{mingw32_bindir}/celtdec051.exe
%{mingw32_bindir}/libcelt051-0.dll
%{mingw32_includedir}/celt051
%{mingw32_libdir}/libcelt051.dll.a
%{mingw32_libdir}/pkgconfig/celt051.pc

%files -n mingw32-celt051-static
%{mingw32_libdir}/libcelt051.a

# Win64
%files -n mingw64-celt051
%doc COPYING README TODO
%{mingw64_bindir}/celtenc051.exe
%{mingw64_bindir}/celtdec051.exe
%{mingw64_bindir}/libcelt051-0.dll
%{mingw64_includedir}/celt051
%{mingw64_libdir}/libcelt051.dll.a
%{mingw64_libdir}/pkgconfig/celt051.pc

%files -n mingw64-celt051-static
%{mingw64_libdir}/libcelt051.a


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.5.1.3-9
- Added win64 support (contributed by Marc-Andre Lureau)
- Added -static subpackages
- Removed the redundant R: mingw32-libogg
- Automatically generate debuginfo package

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.1.3-8
- Remove the .la file

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.5.1.3-7
- Renamed the source package to mingw-celt051 (RHBZ #800851)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.5.1.3-6
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.1.3-3
- Fix dll build, drop static library from package.

* Tue Aug 3 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.1.3-2
- Don't use wildcards in the file list.
- Use %%global instead of %%define.
- Do parallel builds.
- Add patch comment.

* Tue Jul 13 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.1.3-1
- Initial package.
