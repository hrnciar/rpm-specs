%{?mingw_package_header}

%global         gstreamer       gstreamer
%global         majorminor      0.10
%global         gstreamer_version %{majorminor}.36

Name:           mingw-gstreamer-plugins-good
Version:        0.10.31
Release:        22%{?dist}
Summary:        Cross compiled GStreamer plug-ins good

License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  pkgconfig
BuildRequires:  perl-File-Temp

# For glib-genmarshal
BuildRequires:  glib2-devel

BuildRequires:  mingw32-%{gstreamer} >= %{gstreamer_version}
BuildRequires:  mingw64-%{gstreamer} >= %{gstreamer_version}
BuildRequires:  mingw32-gstreamer-plugins-base  >= %{gstreamer_version}
BuildRequires:  mingw64-gstreamer-plugins-base  >= %{gstreamer_version}
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
# BuildRequires:  mingw32-orc
# BuildRequires:  mingw64-orc


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plug-ins is a collection of well-supported plug-ins of
good quality and under the LGPL license.


# Mingw32
%package -n mingw32-gstreamer-plugins-good
Summary:        %{summary}
Requires:       mingw32-gstreamer >= %{gstreamer_version}
Requires:       mingw32-gstreamer-plugins-base
Obsoletes:      mingw32-gstreamer-plugins-good-static < 0.10.30-5

%description -n mingw32-gstreamer-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plug-ins is a collection of well-supported plug-ins of
good quality and under the LGPL license.


# Mingw64
%package -n mingw64-gstreamer-plugins-good
Summary:        %{summary}
Requires:       mingw64-gstreamer >= %{gstreamer_version}
Requires:       mingw64-gstreamer-plugins-base
Obsoletes:      mingw64-gstreamer-plugins-good-static < 0.10.30-5

%description -n mingw64-gstreamer-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plug-ins is a collection of well-supported plug-ins of
good quality and under the LGPL license.


%{?mingw_debug_package}


%prep
%setup -q -n gst-plugins-good-%{version}


%build
%mingw_configure \
    --with-package-name='Fedora Mingw gstreamer-plugins-good package' \
    --with-package-origin='http://download.fedora.redhat.com/fedora' \
    --enable-experimental \
    --disable-gtk-doc \
    --disable-monoscope \
    --disable-aalib \
    --disable-esd \
    --disable-libcaca \
    --with-default-visualizer=autoaudiosink \
    --disable-shout2 \
    --disable-flac \
    --disable-jack

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{majorminor}/*.a

%mingw_find_lang gstreamer-plugins-good --all-name


# Mingw32
%files -n mingw32-gstreamer-plugins-good -f mingw32-gstreamer-plugins-good.lang
%doc AUTHORS COPYING README REQUIREMENTS

# Equaliser presets
%{mingw32_datadir}/gstreamer-%{majorminor}/presets/

# non-core plugins without external dependencies
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstalaw.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstalpha.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstalphacolor.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstannodex.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstapetag.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudiofx.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudioparsers.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstauparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstautodetect.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstavi.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcutter.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdebug.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsteffectv.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstequalizer.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstflv.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstflxdec.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgoom.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsticydemux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstid3demux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstinterleave.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstlevel.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmatroska.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmulaw.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmultifile.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmultipart.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstisomp4.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstreplaygain.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrtp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrtsp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstshapewipe.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsmpte.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstspectrum.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstudp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideobox.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideocrop.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideofilter.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideomixer.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstwavenc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstwavparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsty4menc.dll

# gstreamer-plugins with external dependencies but in the main package
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcairo.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdirectsoundsink.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgdkpixbuf.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstpng.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsouphttpsrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstjpeg.dll


# Mingw64
%files -n mingw64-gstreamer-plugins-good -f mingw64-gstreamer-plugins-good.lang
%doc AUTHORS COPYING README REQUIREMENTS

# Equaliser presets
%{mingw64_datadir}/gstreamer-%{majorminor}/presets/

# non-core plugins without external dependencies
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstalaw.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstalpha.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstalphacolor.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstannodex.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstapetag.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudiofx.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudioparsers.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstauparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstautodetect.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstavi.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcutter.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdebug.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsteffectv.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstequalizer.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstflv.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstflxdec.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgoom.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsticydemux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstid3demux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstinterleave.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstisomp4.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstlevel.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmatroska.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmulaw.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmultifile.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmultipart.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstreplaygain.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrtp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrtsp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstshapewipe.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsmpte.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstspectrum.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstudp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideobox.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideocrop.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideofilter.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideomixer.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstwavenc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstwavparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsty4menc.dll

# gstreamer-plugins with external dependencies but in the main package
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcairo.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdirectsoundsink.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgdkpixbuf.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstpng.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsouphttpsrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstjpeg.dll


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.10.31-22
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.10.31-20
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.31-9
- Rebuild against libpng 1.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-6
- Enable orc.

* Mon Apr 30 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-5
- Spec fixes for FPC changes.

* Tue Apr 24 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-4
- Obsoletes static package.

* Mon Apr 16 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-3
- Drop static package.

* Sun Apr 15 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-2
- Spec file changes for review.

* Sat Apr 14 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.31-1
- New upstream release.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 2 2011 Levente Farkas <lfarkas@lfarkas.org> - 0.10.30-1
- Update to 0.10.30

* Sat May 14 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.29-1
- Updated to 0.10.29
- Updated to newer mingw instructions (with mingw64 support)

* Wed Dec 29 2010 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.26-1
- Build with mingw32
