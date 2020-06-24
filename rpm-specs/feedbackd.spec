Name:           feedbackd
Version:        0.0.0+git20200527
Release:        1%{?dist}
Summary:        Feedback library for GNOME

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/feedbackd
Source0:        https://source.puri.sm/Librem5/feedbackd/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  vala-tools
BuildRequires:  dbus-daemon

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%{_bindir}/fbcli
%{_libdir}/girepository-1.0/Lfb-0.0.typelib
%{_libdir}/libfeedback-0.0.so.0
%{_libexecdir}/feedbackd
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%{_datadir}/dbus-1/services/org.sigxcpu.Feedback.service
%{_datadir}/feedbackd
%{_datadir}/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml

%files devel
%{_libdir}/libfeedback-0.0.so
%dir %{_includedir}/libfeedback-0.0
%{_includedir}/libfeedback-0.0/lfb-enums.h
%{_includedir}/libfeedback-0.0/lfb-event.h
%{_includedir}/libfeedback-0.0/lfb-gdbus.h
%{_includedir}/libfeedback-0.0/libfeedback.h
%{_datadir}/vala/vapi/libfeedback-0.0.deps
%{_datadir}/vala/vapi/libfeedback-0.0.vapi
%{_datadir}/gir-1.0/Lfb-0.0.gir
%{_libdir}/pkgconfig/libfeedback-0.0.pc

%changelog
* Fri Jun 12 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.0.0+git20200527-1
- Update to 0.0.0+git20200527

* Sat Feb 29 2020 Nikhil Jha <hi@nikhiljha.com> - 0.0.0+git20200305-1
- Initial packaging
