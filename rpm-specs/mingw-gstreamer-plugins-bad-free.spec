%{?mingw_package_header}

%global         gstreamer       gstreamer
%global         majorminor      0.10
%global         gstreamer_version %{majorminor}.36

Name:           mingw-gstreamer-plugins-bad-free
Version:        0.10.23
Release:        23%{?dist}
Summary:        Cross compiled GStreamer plug-ins "bad"

# The freeze and nfs plugins are LGPLv2 (only)
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-free-%{version}.tar.xz
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
# modified with gst-p-bad-cleanup.sh from SOURCE1
Source1:        gst-p-bad-cleanup.sh
Patch1:         0001-build-fix-librfb-linking-on-win32.patch

BuildArch:      noarch

BuildRequires:  perl-File-Temp
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gstreamer >= %{gstreamer_version}
BuildRequires:  mingw64-gstreamer >= %{gstreamer_version}
BuildRequires:  mingw32-gstreamer-plugins-base >= %{gstreamer_version}
BuildRequires:  mingw64-gstreamer-plugins-base >= %{gstreamer_version}
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-pthreads
BuildRequires:  mingw64-pthreads
BuildRequires:  mingw32-SDL
BuildRequires:  mingw64-SDL
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
#BuildRequires: mingw32-libcelt
#BuildRequires:	mingw32-libvpx
#BuildRequires:	mingw32-xvidcore

# For glib-genmarshal
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw32
%package -n mingw32-gstreamer-plugins-bad-free
Summary:        %{summary}
Obsoletes:      mingw32-gstreamer-plugins-bad-free-static < 0.10.22-5
Requires:       mingw32-gstreamer >= %{gstreamer_version}

%description -n mingw32-gstreamer-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw64
%package -n mingw64-gstreamer-plugins-bad-free
Summary:        %{summary}
Obsoletes:      mingw64-gstreamer-plugins-bad-free-static < 0.10.22-5
Requires:       mingw64-gstreamer >= %{gstreamer_version}

%description -n mingw64-gstreamer-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


%{?mingw_debug_package}


%prep
%setup -q -n gst-plugins-bad-%{version}
%patch1 -p1


%build
%mingw_configure \
    --with-package-name='Fedora Mingw gstreamer-plugins-bad package' \
    --with-package-origin='http://download.fedora.redhat.com/fedora' \
    --enable-debug \
    --disable-gtk-doc \
    --enable-experimental \
    --disable-divx \
    --disable-acm \
    --disable-apexsink \
    --disable-dvdspu \
    --disable-real \
    --disable-siren

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*%{majorminor}.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*%{majorminor}.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{majorminor}/*.a

%mingw_find_lang gstreamer-plugins-bad-free --all-name


# Mingw32
%files -n mingw32-gstreamer-plugins-bad-free -f mingw32-gstreamer-plugins-bad-free.lang
%doc AUTHORS COPYING README REQUIREMENTS

# libraries
%{mingw32_bindir}/libgstbasecamerabinsrc-%{majorminor}-23.dll
%{mingw32_bindir}/libgstbasevideo-%{majorminor}-23.dll
%{mingw32_bindir}/libgstcodecparsers-%{majorminor}-23.dll
%{mingw32_bindir}/libgstphotography-%{majorminor}-23.dll
%{mingw32_bindir}/libgstsignalprocessor-%{majorminor}-23.dll

# bad plugins
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaiff.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstasfmux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstautoconvert.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstbayer.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstbz2.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcamerabin.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcog.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstcolorspace.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdccp.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdirectdrawsink.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstd3dvideosink.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdirectsoundsrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstdtmf.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfestival.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfragmented.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfreeverb.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfreeze.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstfrei0r.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstgsettingselements.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsth264parse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsthdvparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstid3tag.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstinter.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstinterlace.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstivfparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstjp2k.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstjpegformat.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstlegacyresample.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstliveadder.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmpegdemux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmve.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstmxf.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstnsf.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstpatchdetect.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstpcapparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstpnm.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrawparse.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstremovesilence.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrtpmux.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstrtpvp8.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstscaletempoplugin.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsdi.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsdl.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsdpelem.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsmooth.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstspeed.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgststereo.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstsubenc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsttta.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideomaxrate.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideomeasure.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvideosignal.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstvmnc.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgstwininet.dll
%{mingw32_libdir}/gstreamer-%{majorminor}/libgsty4mdec.dll

# %files devel
# plugin helper library headers
%dir %{mingw32_includedir}/gstreamer-%{majorminor}/gst/interfaces
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstbasecamerasrc.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabin-enum.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabinpreview.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gsth264parser.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpeg4parser.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpegvideoparser.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvc1parser.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography-enumtypes.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/signalprocessor/gstsignalprocessor.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideocodec.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideodecoder.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideoencoder.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideoutils.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstsurfacebuffer.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/gstsurfaceconverter.h
%{mingw32_includedir}/gstreamer-%{majorminor}/gst/video/videocontext.h

%{mingw32_libdir}/libgstbasecamerabinsrc-%{majorminor}.dll.a
%{mingw32_libdir}/libgstbasevideo-%{majorminor}.dll.a
%{mingw32_libdir}/libgstcodecparsers-%{majorminor}.dll.a
%{mingw32_libdir}/libgstphotography-%{majorminor}.dll.a
%{mingw32_libdir}/libgstsignalprocessor-%{majorminor}.dll.a

%{mingw32_libdir}/pkgconfig/gstreamer-basevideo-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-codecparsers-0.10.pc
%{mingw32_libdir}/pkgconfig/gstreamer-plugins-bad-0.10.pc
%{mingw32_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml


# Mingw64
%files -n mingw64-gstreamer-plugins-bad-free -f mingw64-gstreamer-plugins-bad-free.lang
%doc AUTHORS COPYING README REQUIREMENTS

# libraries
%{mingw64_bindir}/libgstbasecamerabinsrc-%{majorminor}-23.dll
%{mingw64_bindir}/libgstbasevideo-%{majorminor}-23.dll
%{mingw64_bindir}/libgstcodecparsers-%{majorminor}-23.dll
%{mingw64_bindir}/libgstphotography-%{majorminor}-23.dll
%{mingw64_bindir}/libgstsignalprocessor-%{majorminor}-23.dll

# bad plugins
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaiff.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstasfmux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstautoconvert.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstbayer.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstbz2.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcamerabin.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcog.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstcolorspace.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdccp.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdirectdrawsink.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstd3dvideosink.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdirectsoundsrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstdtmf.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfestival.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfragmented.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfreeverb.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfreeze.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstfrei0r.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstgsettingselements.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsth264parse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsthdvparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstid3tag.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstinter.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstinterlace.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstivfparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstjp2k.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstjpegformat.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstlegacyresample.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstliveadder.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmpegdemux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmve.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstmxf.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstnsf.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstpatchdetect.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstpcapparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstpnm.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrawparse.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstremovesilence.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrtpmux.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstrtpvp8.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstscaletempoplugin.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsdi.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsdl.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsdpelem.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsmooth.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstspeed.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgststereo.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstsubenc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsttta.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideomaxrate.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideomeasure.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvideosignal.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstvmnc.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgstwininet.dll
%{mingw64_libdir}/gstreamer-%{majorminor}/libgsty4mdec.dll

# %files devel
# plugin helper library headers
%dir %{mingw64_includedir}/gstreamer-%{majorminor}/gst/interfaces
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstbasecamerasrc.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabin-enum.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabinpreview.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gsth264parser.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpeg4parser.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpegvideoparser.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvc1parser.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography-enumtypes.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/signalprocessor/gstsignalprocessor.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideocodec.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideodecoder.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideoencoder.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstbasevideoutils.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstsurfacebuffer.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/gstsurfaceconverter.h
%{mingw64_includedir}/gstreamer-%{majorminor}/gst/video/videocontext.h

%{mingw64_libdir}/libgstbasecamerabinsrc-%{majorminor}.dll.a
%{mingw64_libdir}/libgstbasevideo-%{majorminor}.dll.a
%{mingw64_libdir}/libgstcodecparsers-%{majorminor}.dll.a
%{mingw64_libdir}/libgstphotography-%{majorminor}.dll.a
%{mingw64_libdir}/libgstsignalprocessor-%{majorminor}.dll.a

%{mingw64_libdir}/pkgconfig/gstreamer-basevideo-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-codecparsers-0.10.pc
%{mingw64_libdir}/pkgconfig/gstreamer-plugins-bad-0.10.pc
%{mingw64_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.10.23-23
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.10.23-21
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Michael Cronenworth <mike@cchtml.com> - 0.10.23-14
- Rebuilt for mingw-jasper update

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.23-10
- Rebuild against winpthreads

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.23-8
- Rebuild against libpng 1.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.23-5
- Update file list
- Missing BR for bzip2

* Fri May 04 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.23-4
- Apply librfb patch. (gnome bz 675415)

* Mon Apr 30 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.23-3
- Spec fixes for FPC changes.
- Remove and obsoletes static package.

* Sun Apr 15 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.23-2
- Spec file changes for review.

* Sat Apr 14 2012 Michael Cronenworth <mike@cchtml.com> - 0.10.23-1
- New upstream release

* Fri Feb 24 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.10.22-4
- Rebuild against winpthreads
- Dropped the use of the mingw_pkg_name macro

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 24 2011 Levente Farkas <lfarkas@lfarkas.org> 0.10.22-2
- Add d3dvideo component patch (already upstream) and rename to bad-free as in fedora

* Sat May 14 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.22-1
- Updated to 0.10.22
- Updated to newer mingw instructions (with mingw64 support)

* Tue Jan 04 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.20-1
- Build with mingw32
