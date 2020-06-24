%global apiversion   0.2
%global spaversion   0.1

#global snap       20141103
#global gitrel     327
#global gitcommit  aec811798cd883a454b9b5cd82c77831906bbd2d
#global shortcommit %(c=%{gitcommit}; echo ${c:0:5})

# https://bugzilla.redhat.com/983606
%global _hardened_build 1

# where/how to apply multilib hacks
%global multilib_archs x86_64 %{ix86} ppc64 ppc s390x s390 sparc64 sparcv9 ppc64le

Name:           pipewire0.2
Summary:        Media Sharing Server compat libraries
Version:        0.2.7
Release:        2%{?snap:.%{snap}git%{shortcommit}}%{?dist}
License:        LGPLv2+
URL:            https://pipewire.org/
%if 0%{?gitrel}
# git clone git://anongit.freedesktop.org/gstreamer/pipewire
# cd pipewire; git reset --hard %{gitcommit}; ./autogen.sh; make; make distcheck
Source0:        pipewire-%{version}-%{gitrel}-g%{shortcommit}.tar.gz
%else
Source0:	https://github.com/PipeWire/pipewire/archive/%{version}/pipewire-%{version}.tar.gz
%endif

## upstream patches
Patch1:		0001-build-and-link-a2dp-codecs.c-as-well.patch
Patch2:		0001-bluez5-declare-factory-as-extern.patch

## upstreamable patches

BuildRequires:  meson >= 0.35.0
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-net-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-allocators-1.0) >= 1.10.0
BuildRequires:  systemd-devel >= 184
BuildRequires:  alsa-lib-devel
BuildRequires:  libv4l-devel
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  graphviz
BuildRequires:  sbc-devel

Requires(pre):  shadow-utils
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       systemd >= 184
Requires:       rtkit

# https://bugzilla.redhat.com/983606
%global _hardened_build 1

## enable systemd activation
%global systemd 1

%description
PipeWire is a multimedia server for Linux and other Unix like operating
systems.

%package libs
Summary:        Compatibility Libraries for PipeWire clients
License:        LGPLv2+
Recommends:     %{name}%{?_isa} = %{version}-%{release}

Provides:	pipewire-libs = %{version}
Conflicts:	pipewire-libs < %{version}

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PipeWire media server.

%package devel
Summary:        Compatibility Headers and libraries for PipeWire client development
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%prep
%setup -q -T -b0 -n pipewire-%{version}%{?gitrel:-%{gitrel}-g%{shortcommit}}

%patch1 -p1 -b .0001
%patch2 -p1 -b .0002

%build
%meson -D docs=false -D man=false -D gstreamer=disabled -D systemd=false
%meson_build

%install
%meson_install

rm -rf $RPM_BUILD_ROOT%{_bindir}/*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/*

%check
%meson_test

%pre
%ldconfig_scriptlets libs

%files libs
%license LICENSE GPL LGPL
%doc README
%{_libdir}/libpipewire-%{apiversion}.so.*
%{_libdir}/pipewire-%{apiversion}/
%{_libdir}/spa/

%files devel
%{_libdir}/libpipewire-%{apiversion}.so
%{_includedir}/pipewire/
%{_includedir}/spa/
%{_libdir}/pkgconfig/libpipewire-%{apiversion}.pc
%{_libdir}/pkgconfig/libspa-%{spaversion}.pc

%changelog
* Fri Feb 07 2020 Wim Taymans <wtaymans@redhat.com> - 0.2.7-2
- Add compat -devel package

* Wed Jan 29 2020 Wim Taymans <wtaymans@redhat.com> - 0.2.7-1
- First version
- Fix bluez5 plugins build
