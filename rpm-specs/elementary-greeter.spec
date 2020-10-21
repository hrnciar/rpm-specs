%global srcname greeter
%global appname io.elementary.greeter

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        5.0.4
Release:        4%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        40-%{appname}.conf
Source2:        %{appname}.whitelist

# upstreamed patch for mutter 3.38 / libmutter-7 support
# https://github.com/elementary/greeter/commit/a571deb
Patch0:         %{url}/commit/a571deb.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(mutter-clutter-7)
BuildRequires:  pkgconfig(mutter-cogl-7)
BuildRequires:  pkgconfig(mutter-cogl-pango-7)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(x11)

Provides:       pantheon-greeter = %{version}-%{release}
Obsoletes:      pantheon-greeter < 3.2.0-7


Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# Runtime requirement for numlock capture
Requires:       numlockx

# Requirements for default artwork
Requires:       elementary-icon-theme
Requires:       elementary-theme-gtk3
Requires:       elementary-wallpapers

# Requirements for accountsservice extension
Requires:       pantheon-session-settings >= 30.90

# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# Alternate, more descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}


%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dubuntu-patched-gsd=false
%meson_build


%install
%meson_install

%find_lang %{appname}

# Install LightDM configuration file
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/

# Install wingpanel overrides for the greeter
mkdir -p %{buildroot}%{_sysconfdir}/wingpanel.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/wingpanel.d


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/%{appname}.whitelist

%{_bindir}/%{appname}-compositor
%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Aug 27 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-4
- Include upstreamed patch for mutter 3.38 / libmutter-7 support.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-1
- Update to version 5.0.4.

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Update to version 5.0.3.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-220200402.git671dd75
- Bump to commit 671dd75.

* Wed Feb 26 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-1
- Update to version 5.0.2.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Update to version 5.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1-3
- Hard-code GTK and icon theme to fix visual glitches.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1-1
- Update to version 3.3.1.
- Switch to upstreamed version of my GSettings fixes patch.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-2
- Update GSettings patch to fix gnome-settings-daemon.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-1
- Initial package renamed from pantheon-greeter.

