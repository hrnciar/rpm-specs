%global gvc_commit 468022b708fc1a56154f3b0cc5af3b938fb3e9fb

Name:           phosh
Version:        0.3.1
Release:        1%{?dist}
Summary:        Graphical shell for mobile devices

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/phosh
Source0:        https://source.puri.sm/Librem5/phosh/-/archive/v%{version}/%{name}-v%{version}.tar.gz

	
# This library doesn't compile into a DSO or ever has had any releases.
# Other projects, such as gnome-shell use it this way.
Source1:        https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz

Source2:        phosh

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  dbus-daemon
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gcr-3) >= 3.7.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.12
BuildRequires:  pkgconfig(libnm) >= 1.14
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.105
BuildRequires:  pkgconfig(upower-glib) >= 0.99.1
BuildRequires:  pkgconfig(wayland-client) >= 1.14
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  feedbackd-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  at-spi2-core
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth
BuildRequires:  desktop-file-utils
BuildRequires:  git

Requires:       gnome-session
Requires:       lato-fonts

%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nighlight
* the gcr system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi


%prep
%setup -a1 -q -n %{name}-v%{version}
rmdir subprojects/gvc
ln -s ../libgnome-volume-control-%{gvc_commit} subprojects/gvc


%build
%meson
%meson_build


%install
mkdir -p $RPM_BUILD_ROOT/etc/pam.d/
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/
%meson_install
%find_lang %{name}


%check
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/sm.puri.Phosh.desktop
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH


%files -f %{name}.lang
%{_bindir}/phosh
%{_bindir}/phosh-osk-stub
%{_libexecdir}/phosh
%{_datadir}/applications/sm.puri.Phosh.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.gschema.xml
%{_datadir}/gnome-session/sessions/phosh.session
%{_datadir}/applications/sm.puri.OSK0.desktop
%{_datadir}/wayland-sessions/phosh.desktop
%{_datadir}/phosh
%{_sysconfdir}/pam.d/phosh
%doc README.md
%doc debian/phosh.service
%license COPYING


%changelog
* Tue Jun 23 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.3.1-1
- Update to phosh 0.3.1
- Adding dbus-daemon

* Tue May 19 2020 Nikhil Jha <hi@nikhiljha.com> - 0.3.0-1
- Update to phosh 0.3.0

* Thu Mar 05 2020 Nikhil Jha <hi@nikhiljha.com> - 0.2.1-1
- Update to phosh 0.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 0.1.0-3
- Rebuilt for libgnome-desktop soname bump

* Wed Oct 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Fixes from review (thanks Robert-André Mauchin):
- Corrected the License tag
- Validate the Desktop Entry file

* Tue Oct 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging

