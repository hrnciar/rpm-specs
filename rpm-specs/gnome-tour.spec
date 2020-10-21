%global debug_package %{nil}

# Use bundled deps as we don't ship the exact right versions for all the
# required rust libraries
%global bundled_rust_deps 1

Name:           gnome-tour
Version:        3.38.0
Release:        2%{?dist}
Summary:        GNOME Tour and Greeter

# * gnome-tour source code is GPLv3+
# * fedora-initial-intro.webm is CC-BY-SA
# * bundled rust crates all include either MIT or GPLv3+ as one of the possible
#   licenses, which when compiled into gnome-tour binary together with GPLv3+
#   gnome-tour source code results in effective GPLv3+ for the resulting binary
License:        GPLv3+ and CC-BY-SA
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/gnome-tour/3.38/gnome-tour-%{version}.tar.xz
# https://pagure.io/fedora-workstation/issue/175
Source1:        fedora-initial-intro.webm

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%if 0%{?bundled_rust_deps}
BuildRequires:  cargo
BuildRequires:  rust
%else
BuildRequires:  rust-packaging
%endif

%if 0%{?bundled_rust_deps}
# bundled crates list updated for gnome-tour 3.37.91
Provides: bundled(crate(aho-corasick/default)) = 0.7.13
Provides: bundled(crate(anyhow/default)) = 1.0.32
Provides: bundled(crate(atk/default)) = 0.9.0
Provides: bundled(crate(atk-sys/default)) = 0.10.0
Provides: bundled(crate(atty/default)) = 0.2.14
Provides: bundled(crate(autocfg/default)) = 1.0.0
Provides: bundled(crate(bitflags/default)) = 1.2.1
Provides: bundled(crate(cairo-rs/default)) = 0.9.1
Provides: bundled(crate(cairo-sys-rs/default)) = 0.10.0
Provides: bundled(crate(cc/default)) = 1.0.58
Provides: bundled(crate(cfg-if/default)) = 0.1.10
Provides: bundled(crate(either/default)) = 1.6.0
Provides: bundled(crate(env_logger/default)) = 0.7.1
Provides: bundled(crate(futures/default)) = 0.3.5
Provides: bundled(crate(futures-channel/default)) = 0.3.5
Provides: bundled(crate(futures-core/default)) = 0.3.5
Provides: bundled(crate(futures-executor/default)) = 0.3.5
Provides: bundled(crate(futures-io/default)) = 0.3.5
Provides: bundled(crate(futures-macro/default)) = 0.3.5
Provides: bundled(crate(futures-sink/default)) = 0.3.5
Provides: bundled(crate(futures-task/default)) = 0.3.5
Provides: bundled(crate(futures-util/default)) = 0.3.5
Provides: bundled(crate(gdk/default)) = 0.13.1
Provides: bundled(crate(gdk-pixbuf/default)) = 0.9.0
Provides: bundled(crate(gdk-pixbuf-sys/default)) = 0.10.0
Provides: bundled(crate(gdk-sys/default)) = 0.10.0
Provides: bundled(crate(gettext-rs/default)) = 0.4.4
Provides: bundled(crate(gettext-sys/default)) = 0.19.9
Provides: bundled(crate(gio/default)) = 0.9.0
Provides: bundled(crate(gio-sys/default)) = 0.10.0
Provides: bundled(crate(glib/default)) = 0.10.1
Provides: bundled(crate(glib-macros/default)) = 0.10.1
Provides: bundled(crate(glib-sys/default)) = 0.10.0
Provides: bundled(crate(gobject-sys/default)) = 0.10.0
Provides: bundled(crate(gstreamer/default)) = 0.16.2
Provides: bundled(crate(gstreamer-base/default)) = 0.16.0
Provides: bundled(crate(gstreamer-base-sys/default)) = 0.9.0
Provides: bundled(crate(gstreamer-player/default)) = 0.16.0
Provides: bundled(crate(gstreamer-player-sys/default)) = 0.9.0
Provides: bundled(crate(gstreamer-sys/default)) = 0.9.0
Provides: bundled(crate(gstreamer-video/default)) = 0.16.0
Provides: bundled(crate(gstreamer-video-sys/default)) = 0.9.0
Provides: bundled(crate(gtk/default)) = 0.9.1
Provides: bundled(crate(gtk-sys/default)) = 0.10.0
Provides: bundled(crate(heck/default)) = 0.3.1
Provides: bundled(crate(humantime/default)) = 1.3.0
Provides: bundled(crate(itertools/default)) = 0.9.0
Provides: bundled(crate(lazy_static/default)) = 1.4.0
Provides: bundled(crate(libc/default)) = 0.2.74
Provides: bundled(crate(libhandy/default)) = 1.0.0~alpha
Provides: bundled(crate(libhandy-sys/default)) = 1.0.0~alpha
Provides: bundled(crate(locale_config/default)) = 0.2.3
Provides: bundled(crate(log/default)) = 0.4.11
Provides: bundled(crate(memchr/default)) = 2.3.3
Provides: bundled(crate(muldiv/default)) = 0.2.1
Provides: bundled(crate(num-integer/default)) = 0.1.43
Provides: bundled(crate(num-rational/default)) = 0.3.0
Provides: bundled(crate(num-traits/default)) = 0.2.12
Provides: bundled(crate(once_cell/default)) = 1.4.1
Provides: bundled(crate(pango/default)) = 0.9.1
Provides: bundled(crate(pango-sys/default)) = 0.10.0
Provides: bundled(crate(paste/default)) = 0.1.18
Provides: bundled(crate(paste-impl/default)) = 0.1.18
Provides: bundled(crate(pin-project/default)) = 0.4.23
Provides: bundled(crate(pin-project-internal/default)) = 0.4.23
Provides: bundled(crate(pin-utils/default)) = 0.1.0
Provides: bundled(crate(pkg-config/default)) = 0.3.18
Provides: bundled(crate(pretty_env_logger/default)) = 0.4.0
Provides: bundled(crate(pretty-hex/default)) = 0.1.1
Provides: bundled(crate(proc-macro2/default)) = 1.0.19
Provides: bundled(crate(proc-macro-crate/default)) = 0.1.5
Provides: bundled(crate(proc-macro-error/default)) = 1.0.4
Provides: bundled(crate(proc-macro-error-attr/default)) = 1.0.4
Provides: bundled(crate(proc-macro-hack/default)) = 0.5.18
Provides: bundled(crate(proc-macro-nested/default)) = 0.1.6
Provides: bundled(crate(quick-error/default)) = 1.2.3
Provides: bundled(crate(quote/default)) = 1.0.7
Provides: bundled(crate(regex/default)) = 1.3.9
Provides: bundled(crate(regex-syntax/default)) = 0.6.18
Provides: bundled(crate(serde/default)) = 1.0.115
Provides: bundled(crate(slab/default)) = 0.4.2
Provides: bundled(crate(strum/default)) = 0.18.0
Provides: bundled(crate(strum_macros/default)) = 0.18.0
Provides: bundled(crate(syn/default)) = 1.0.38
Provides: bundled(crate(system-deps/default)) = 1.3.2
Provides: bundled(crate(termcolor/default)) = 1.1.0
Provides: bundled(crate(thiserror/default)) = 1.0.20
Provides: bundled(crate(thiserror-impl/default)) = 1.0.20
Provides: bundled(crate(thread_local/default)) = 1.0.1
Provides: bundled(crate(toml/default)) = 0.5.6
Provides: bundled(crate(unicode-segmentation/default)) = 1.6.0
Provides: bundled(crate(unicode-xid/default)) = 0.2.1
Provides: bundled(crate(version_check/default)) = 0.9.2
Provides: bundled(crate(version-compare/default)) = 0.0.10
%endif

Requires: gstreamer1-plugins-good-gtk%{?_isa}

%description
A guided tour and greeter for GNOME.


%prep
%autosetup -p1

%if ! 0%{?bundled_rust_deps}
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson -Dvideo_path=%{_datadir}/gnome-tour/fedora-initial-intro.webm
%meson_build

%if ! 0%{?bundled_rust_deps}
%cargo_build
%endif


%install
%meson_install

%if ! 0%{?bundled_rust_deps}
%cargo_install
%endif

# Install Fedora video
install -p -m 0644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-tour/fedora-initial-intro.webm

%find_lang gnome-tour


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tour.desktop


%files -f gnome-tour.lang
%license LICENSE.md
%doc NEWS README.md
%{_bindir}/gnome-tour
%{_datadir}/applications/org.gnome.Tour.desktop
%dir %{_datadir}/gnome-tour
%{_datadir}/gnome-tour/fedora-initial-intro.webm
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tour.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml


%changelog
* Tue Oct 20 2020 Kalev Lember <klember@redhat.com> - 3.38.0-2
- Add missing gstreamer1-plugins-good-gtk dep (#1889657)

* Wed Sep 16 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.37.92-2
- Use a lower res video to improve the layout (thanks jimmac!)

* Tue Sep 08 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Thu Aug 27 2020 Kalev Lember <klember@redhat.com> - 3.37.91-2
- Add provides for bundled rust crates (#1873108)
- Clarify licensing for bundled rust crates (#1873108)

* Thu Aug 27 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Initial Fedora packaging
