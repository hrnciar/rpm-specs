Summary:        Modular SIP user-agent with audio and video support
Name:           baresip
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.creytiv.com/baresip.html
Source0:        https://github.com/baresip/baresip/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        com.creytiv.baresip.desktop
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libre-devel >= 1.0.0
BuildRequires:  librem-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
Recommends:     %{name}-pulse%{?_isa} = %{version}-%{release}
%else
Requires:       %{name}-pulse%{?_isa} = %{version}-%{release}
%endif

%description
A modular SIP user-agent with support for audio and video, and many IETF
standards such as SIP, RTP, STUN, TURN, and ICE for both, IPv4 and IPv6.

Additional modules provide support for audio codecs like G.711, G.722,
G.726, GSM, L16, MPA, and Opus, audio drivers like ALSA, GStreamer, JACK
Audio Connection Kit, Portaudio, and PulseAudio, video codecs like VP8 or
VP9, video sources like Video4Linux and X11 grabber, video outputs like
SDL2 or X11, NAT traversal via STUN, TURN, ICE, NATBD, and NAT-PMP, media
encryption via SRTP or DTLS-SRTP, management features like embedded web-
server with HTTP interface, command-line console and interface, and MQTT.

%package alsa
Summary:        ALSA audio driver for baresip
BuildRequires:  alsa-lib-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description alsa
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Advanced Linux Sound Architecture (ALSA) audio
driver.

%package cairo
Summary:        Video source driver for baresip to draw demo graphics
BuildRequires:  pkgconfig(cairo)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cairo
Baresip is a modular SIP user-agent with audio and video support.

This module provides a video source driver to draw graphics for testing
and demo purposes into a frame buffer using the Cairo library.

%package g722
Summary:        G.722 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description g722
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.722 audio codec, often used for HD voice.

%package g726
Summary:        G.726 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description g726
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.726 audio codec.

%package gsm
Summary:        GSM audio codec module for baresip
BuildRequires:  gsm-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gsm
Baresip is a modular SIP user-agent with audio and video support.

This module provides the GSM audio codec.

%package gst
Summary:        GStreamer audio source driver for baresip
BuildRequires:  pkgconfig(gstreamer-1.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gst
Baresip is a modular SIP user-agent with audio and video support.

This module uses the GStreamer 1.0 framework to play external media and
provides them as an internal audio source.

%package gst_video
Summary:        Video codec support using GStreamer for baresip
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gst_video
Baresip is a modular SIP user-agent with audio and video support.

This module implements video codecs using GStreamer 1.0 framework.

%package gtk
Summary:        GTK+ menu-based user interface module for baresip
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.22
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  desktop-file-utils
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
Requires:       (gnome-shell-extension-topicons-plus if gnome-shell)
%endif

%description gtk
Baresip is a modular SIP user-agent with audio and video support.

This module provides a GTK+ menu-based user interface.

%package jack
Summary:        JACK audio driver for baresip
BuildRequires:  pkgconfig(jack)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jack
Baresip is a modular SIP user-agent with audio and video support.

This module provides the JACK Audio Connection Kit audio driver.

# RHEL 8 doesn't have twolame-devel, see RHBZ#1843275
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} < 8)
%package mpa
Summary:        MPA speech and audio codec module for baresip
BuildRequires:  twolame-devel
BuildRequires:  lame-devel
BuildRequires:  mpg123-devel
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  speexdsp-devel
%else
BuildRequires:  speex-devel
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mpa
Baresip is a modular SIP user-agent with audio and video support.

This module provides the MPA speech and audio codec.
%endif

%package mqtt
Summary:        MQTT management module for baresip
BuildRequires:  mosquitto-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mqtt
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Message Queue Telemetry Transport (MQTT)
management module.

%package opus
Summary:        Opus speech and audio codec module for baresip
BuildRequires:  opus-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description opus
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Opus speech and audio codec module.

%package plc
Summary:        Packet Loss Concealment module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description plc
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Packet Loss Concealment (PLC) module.

%package portaudio
Summary:        Portaudio audio driver for baresip
BuildRequires:  portaudio-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description portaudio
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Portaudio audio driver.

%package pulse
Summary:        PulseAudio audio driver for baresip
BuildRequires:  pkgconfig(libpulse-simple)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description pulse
Baresip is a modular SIP user-agent with audio and video support.

This module provides the PulseAudio audio driver.

%package rst

Summary:        Radio streamer audio/video source driver for baresip
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libmpg123)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description rst
Baresip is a modular SIP user-agent with audio and video support.

This module uses mpg123 to play streaming media (MP3) and provide them as
an internal audio/video source.

%package sdl
Summary:        SDL2 video output driver for baresip
BuildRequires:  SDL2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sdl
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Simple DirectMedia Layer 2.0 (SDL2) video output
driver.

%package sndfile
Summary:        Audio dumper module using libsndfile for baresip
BuildRequires:  libsndfile-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sndfile
Baresip is a modular SIP user-agent with audio and video support.

This module provides an audio dumper to write WAV audio sample files
using libsndfile.

%package speex_pp
Summary:        Audio pre-processor module using libspeexdsp for baresip
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  speexdsp-devel
%else
BuildRequires:  speex-devel
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description speex_pp
Baresip is a modular SIP user-agent with audio and video support.

This module provides an audio pre-processor using libspeexdsp.

%package vp8
Summary:        VP8 video codec module for baresip
BuildRequires:  libvpx-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vp8
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP8 video codec, which is compatible with the
WebRTC standard.

%package vp9
Summary:        VP9 video codec module for baresip
BuildRequires:  pkgconfig(vpx) >= 1.3.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vp9
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP9 video codec, which is compatible with the
WebRTC standard.

%package v4l2
Summary:        Video4Linux video source and codec modules for baresip
BuildRequires:  libv4l-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description v4l2
Baresip is a modular SIP user-agent with audio and video support.

These modules provide the Video4Linux video source and codec, where
latter is for devices that support compressed formats such as H.264.

%package x11
Summary:        X11 video output driver for baresip
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x11
Baresip is a modular SIP user-agent with audio and video support.

This module provides the X11 video output driver.

%package x11grab
Summary:        X11 grabber video source driver for baresip
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x11grab
Baresip is a modular SIP user-agent with audio and video support.

This module provides the X11 grabber video source driver.

%prep
%setup -q

%build
%if 0%{?rhel} == 7
sed -e 's|\(openssl\)|openssl11/\1|g' -i mk/modules.mk
%endif

%make_build \
  SHELL='sh -x' \
  RELEASE=1 \
  PREFIX=%{_prefix} \
  MOD_PATH=%{_libdir}/%{name}/modules \
  EXTRA_CFLAGS="$RPM_OPT_FLAGS -DDEFAULT_CAFILE='\"%{_sysconfdir}/pki/tls/certs/ca-bundle.crt\"' -DDEFAULT_AUDIO_DEVICE='\"pulse\"'" \
  EXTRA_LFLAGS="$RPM_LD_FLAGS"

%install
%make_install LIBDIR=%{_libdir}

# Correct module permissions to add executable bit
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.so

# Install com.creytiv.baresip.desktop file
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ %{SOURCE1}

%check
make test

%files
%license docs/COPYING
%doc docs/ChangeLog docs/THANKS docs/examples
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%{_libdir}/%{name}/modules/account.so
%{_libdir}/%{name}/modules/aubridge.so
%{_libdir}/%{name}/modules/aufile.so
%{_libdir}/%{name}/modules/auloop.so
%{_libdir}/%{name}/modules/ausine.so
%{_libdir}/%{name}/modules/b2bua.so
%{_libdir}/%{name}/modules/cons.so
%{_libdir}/%{name}/modules/contact.so
%{_libdir}/%{name}/modules/ctrl_tcp.so
%{_libdir}/%{name}/modules/debug_cmd.so
%{_libdir}/%{name}/modules/dtls_srtp.so
%{_libdir}/%{name}/modules/ebuacip.so
%{_libdir}/%{name}/modules/echo.so
%{_libdir}/%{name}/modules/evdev.so
%{_libdir}/%{name}/modules/fakevideo.so
%{_libdir}/%{name}/modules/g711.so
%{_libdir}/%{name}/modules/httpd.so
%{_libdir}/%{name}/modules/ice.so
%{_libdir}/%{name}/modules/l16.so
%{_libdir}/%{name}/modules/menu.so
%{_libdir}/%{name}/modules/mwi.so
%{_libdir}/%{name}/modules/natpmp.so
%{_libdir}/%{name}/modules/oss.so
%{_libdir}/%{name}/modules/presence.so
%{_libdir}/%{name}/modules/selfview.so
%{_libdir}/%{name}/modules/srtp.so
%{_libdir}/%{name}/modules/stdio.so
%{_libdir}/%{name}/modules/stun.so
%{_libdir}/%{name}/modules/syslog.so
%{_libdir}/%{name}/modules/turn.so
%{_libdir}/%{name}/modules/uuid.so
%{_libdir}/%{name}/modules/vidbridge.so
%{_libdir}/%{name}/modules/vidinfo.so
%{_libdir}/%{name}/modules/vidloop.so
%{_libdir}/%{name}/modules/vumeter.so
%{_datadir}/%{name}/

%files alsa
%{_libdir}/%{name}/modules/alsa.so

%files cairo
%{_libdir}/%{name}/modules/cairo.so

%files g722
%{_libdir}/%{name}/modules/g722.so

%files g726
%{_libdir}/%{name}/modules/g726.so

%files gsm
%{_libdir}/%{name}/modules/gsm.so

%files gst
%{_libdir}/%{name}/modules/gst.so

%files gst_video
%{_libdir}/%{name}/modules/gst_video.so

%files gtk
%{_libdir}/%{name}/modules/gtk.so
%{_datadir}/applications/com.creytiv.baresip.desktop

%files jack
%{_libdir}/%{name}/modules/jack.so

%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} < 8)
%files mpa
%{_libdir}/%{name}/modules/mpa.so
%endif

%files mqtt
%{_libdir}/%{name}/modules/mqtt.so

%files opus
%{_libdir}/%{name}/modules/opus.so
%{_libdir}/%{name}/modules/opus_multistream.so

%files plc
%{_libdir}/%{name}/modules/plc.so

%files portaudio
%{_libdir}/%{name}/modules/portaudio.so

%files pulse
%{_libdir}/%{name}/modules/pulse.so

%files rst
%{_libdir}/%{name}/modules/rst.so

%files sdl
%{_libdir}/%{name}/modules/sdl.so

%files sndfile
%{_libdir}/%{name}/modules/sndfile.so

%files speex_pp
%{_libdir}/%{name}/modules/speex_pp.so

%files v4l2
%{_libdir}/%{name}/modules/v4l2.so
%{_libdir}/%{name}/modules/v4l2_codec.so

%files vp8
%{_libdir}/%{name}/modules/vp8.so

%files vp9
%{_libdir}/%{name}/modules/vp9.so

%files x11
%{_libdir}/%{name}/modules/x11.so

%files x11grab
%{_libdir}/%{name}/modules/x11grab.so

%changelog
* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1887059)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Robert Scheck <robert@fedoraproject.org> 0.6.6-2
- Include latest features and fixes from upstream
- Changes to match the Fedora Packaging Guidelines (#1843279 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.6-1
- Upgrade to 0.6.6 (#1843279)
- Initial spec file for Fedora and Red Hat Enterprise Linux
