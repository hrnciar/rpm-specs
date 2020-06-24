%?mingw_package_header

%global         majorminor      0.10
%global         gstreamer_version %{majorminor}.36

Name:    mingw-gstreamer-plugins-base
Version: %{gstreamer_version}
Release: 17%{?dist}
Summary: Cross compiled GStreamer media framework base plug-ins

License: LGPLv2+
URL:     http://gstreamer.freedesktop.org/
Source:  http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.bz2

# Fix FTBFS against mingw-gcc 4.9
Patch0:         daa194b71ea6f9e8ee522ab02e8c56150b7e62b3.patch
Patch1:         4e3d101aa854cfee633a9689efeb75e5001baa5e.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gstreamer >= %{gstreamer_version}
BuildRequires:  mingw32-libogg >= 1.0
BuildRequires:  mingw32-libvorbis >= 1.0
#BuildRequires:  mingw32-libtheora >= 1.0
#BuildRequires:  mingw32-orc >= 0.4.11
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-pango
#BuildRequires:  mingw32-libvisual

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gstreamer >= %{gstreamer_version}
BuildRequires:  mingw64-libogg >= 1.0
BuildRequires:  mingw64-libvorbis >= 1.0
#BuildRequires:  mingw64-libtheora >= 1.0
#BuildRequires:  mingw64-orc >= 0.4.11
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw64-pango
#BuildRequires:  mingw64-libvisual

# We need glib-mkenums
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.


# Win32
%package -n mingw32-gstreamer-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw32-gstreamer >= %{gstreamer_version}
# Fix upgrade path when upgrading from the testing repository
Obsoletes:      mingw32-gstreamer-plugins-base-static < 0.10.35-4
Provides:       mingw32-gstreamer-plugins-base-static = 0.10.35-4

%description  -n mingw32-gstreamer-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

# Win64
%package -n mingw64-gstreamer-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw64-gstreamer >= %{gstreamer_version}
# Fix upgrade path when upgrading from the testing repository
Obsoletes:      mingw64-gstreamer-plugins-base-static < 0.10.35-4
Provides:       mingw64-gstreamer-plugins-base-static = 0.10.35-4

%description  -n mingw64-gstreamer-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.


%?mingw_debug_package


%prep
%setup -q -n gst-plugins-base-%{version}
%patch0 -p1
%patch1 -p1


%build
%mingw_configure                                                        \
    --with-package-name='Fedora Mingw gstreamer-plugins-base package'   \
    --with-package-origin='http://download.fedora.redhat.com/fedora'    \
    --enable-experimental                                               \
    --disable-gtk-doc                                                   \
    --disable-gnome_vfs                                                 \
    --disable-static

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/gst-visualise*
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/gst-visualise*
rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/gst-visualise*
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/gst-visualise*
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%mingw_find_lang gst-plugins-base-0.10 --all-name


# Win32
%files -n mingw32-gstreamer-plugins-base -f mingw32-gst-plugins-base-0.10.lang
%doc AUTHORS COPYING README REQUIREMENTS

# libraries
%{mingw32_bindir}/gst-discoverer-0.10.exe
%{mingw32_bindir}/libgstapp-%{majorminor}-0.dll
%{mingw32_bindir}/libgstaudio-%{majorminor}-0.dll
%{mingw32_bindir}/libgstcdda-%{majorminor}-0.dll
%{mingw32_bindir}/libgstfft-%{majorminor}-0.dll
%{mingw32_bindir}/libgstinterfaces-%{majorminor}-0.dll
%{mingw32_bindir}/libgstnetbuffer-%{majorminor}-0.dll
%{mingw32_bindir}/libgstpbutils-%{majorminor}-0.dll
%{mingw32_bindir}/libgstriff-%{majorminor}-0.dll
%{mingw32_bindir}/libgstrtp-%{majorminor}-0.dll
%{mingw32_bindir}/libgstrtsp-%{majorminor}-0.dll
%{mingw32_bindir}/libgstsdp-%{majorminor}-0.dll
%{mingw32_bindir}/libgsttag-%{majorminor}-0.dll
%{mingw32_bindir}/libgstvideo-%{majorminor}-0.dll

# base plugins without external dependencies
%dir %{mingw32_libdir}/gstreamer-%{majorminor}
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstadder.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstapp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudiorate.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudioresample.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdecodebin.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdecodebin2.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstencodebin.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgdp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgio.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstplaybin.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsubparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideorate.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideoscale.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvolume.dll

# base plugins with dependencies
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstogg.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstpango.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvorbis.dll

# plugin helper library headers
%{mingw32_includedir}/gstreamer-%{majorminor}

%{mingw32_libdir}/libgstapp-%{majorminor}.dll.a
%{mingw32_libdir}/libgstaudio-%{majorminor}.dll.a
%{mingw32_libdir}/libgstcdda-%{majorminor}.dll.a
%{mingw32_libdir}/libgstfft-%{majorminor}.dll.a
%{mingw32_libdir}/libgstinterfaces-%{majorminor}.dll.a
%{mingw32_libdir}/libgstnetbuffer-%{majorminor}.dll.a
%{mingw32_libdir}/libgstpbutils-%{majorminor}.dll.a
%{mingw32_libdir}/libgstriff-%{majorminor}.dll.a
%{mingw32_libdir}/libgstrtp-%{majorminor}.dll.a
%{mingw32_libdir}/libgstrtsp-%{majorminor}.dll.a
%{mingw32_libdir}/libgstsdp-%{majorminor}.dll.a
%{mingw32_libdir}/libgsttag-%{majorminor}.dll.a
%{mingw32_libdir}/libgstvideo-%{majorminor}.dll.a

# pkg-config files
%{mingw32_libdir}/pkgconfig/*.pc

%{mingw32_datadir}/gst-plugins-base

# Win64
%files -n mingw64-gstreamer-plugins-base -f mingw64-gst-plugins-base-0.10.lang
%doc AUTHORS COPYING README REQUIREMENTS

# libraries
%{mingw64_bindir}/gst-discoverer-0.10.exe
%{mingw64_bindir}/libgstapp-%{majorminor}-0.dll
%{mingw64_bindir}/libgstaudio-%{majorminor}-0.dll
%{mingw64_bindir}/libgstcdda-%{majorminor}-0.dll
%{mingw64_bindir}/libgstfft-%{majorminor}-0.dll
%{mingw64_bindir}/libgstinterfaces-%{majorminor}-0.dll
%{mingw64_bindir}/libgstnetbuffer-%{majorminor}-0.dll
%{mingw64_bindir}/libgstpbutils-%{majorminor}-0.dll
%{mingw64_bindir}/libgstriff-%{majorminor}-0.dll
%{mingw64_bindir}/libgstrtp-%{majorminor}-0.dll
%{mingw64_bindir}/libgstrtsp-%{majorminor}-0.dll
%{mingw64_bindir}/libgstsdp-%{majorminor}-0.dll
%{mingw64_bindir}/libgsttag-%{majorminor}-0.dll
%{mingw64_bindir}/libgstvideo-%{majorminor}-0.dll

# base plugins without external dependencies
%dir %{mingw64_libdir}/gstreamer-%{majorminor}
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstadder.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstapp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudiorate.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudioresample.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdecodebin.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdecodebin2.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstencodebin.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgdp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgio.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstplaybin.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsubparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideorate.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideoscale.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvolume.dll

# base plugins with dependencies
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstogg.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstpango.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvorbis.dll

# plugin helper library headers
%{mingw64_includedir}/gstreamer-%{majorminor}

%{mingw64_libdir}/libgstapp-%{majorminor}.dll.a
%{mingw64_libdir}/libgstaudio-%{majorminor}.dll.a
%{mingw64_libdir}/libgstcdda-%{majorminor}.dll.a
%{mingw64_libdir}/libgstfft-%{majorminor}.dll.a
%{mingw64_libdir}/libgstinterfaces-%{majorminor}.dll.a
%{mingw64_libdir}/libgstnetbuffer-%{majorminor}.dll.a
%{mingw64_libdir}/libgstpbutils-%{majorminor}.dll.a
%{mingw64_libdir}/libgstriff-%{majorminor}.dll.a
%{mingw64_libdir}/libgstrtp-%{majorminor}.dll.a
%{mingw64_libdir}/libgstrtsp-%{majorminor}.dll.a
%{mingw64_libdir}/libgstsdp-%{majorminor}.dll.a
%{mingw64_libdir}/libgsttag-%{majorminor}.dll.a
%{mingw64_libdir}/libgstvideo-%{majorminor}.dll.a

# pkg-config files
%{mingw64_libdir}/pkgconfig/*.pc

%{mingw64_datadir}/gst-plugins-base

%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.10.36-17
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.10.36-15
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.36-5
- Fix FTBFS against mingw-gcc 4.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Paweł Forysiuk <tuxator@o2.pl> - 0.10.36-1
- Update to upstream version 0.10.36
- Drop obsolete patch

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.35-4
- Added win64 support (contributed by Marc-André Lureau)
- Use mingw macros without leading underscore
- Backported fix for GNOME bug #654816
- Use %%global instead of %%define

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.35-3
- Rebuild against the mingw-w64 toolchain

* Sun Feb 12 2012 - Paweł Forysiuk <tuxator@o2.pl> - 0.10.35-2
- Minor packaging cleanup

* Sun Feb 12 2012 - Paweł Forysiuk <tuxator@o2.pl> - 0.10.35-1
- Updated to 0.10.35
- Spec file updated to match Fedora guidelines

* Sat May 14 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.33-1
- Updated to 0.10.33
- Updated to newer mingw instructions (with mingw64 support)

* Wed Dec 29 2010 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.31-1
- Build with mingw32
