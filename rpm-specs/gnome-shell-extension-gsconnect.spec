%global debug_package %{nil}

%global app_id org.gnome.Shell.Extensions.GSConnect

Name:           gnome-shell-extension-gsconnect
Version:        43
Release:        1%{?dist}
Summary:        KDE Connect implementation for GNOME Shell

License:        GPLv2
URL:            https://github.com/andyholmes/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        nautilus-gsconnect.metainfo.xml
Source2:        nemo-gsconnect.metainfo.xml
# Fix Firewalld path
Patch0:         %{name}-42-firewalld.patch

BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
Requires:       firewalld-filesystem
Requires:       gnome-shell >= 3.36
Requires:       openssh
Requires:       openssh-clients
Requires:       openssl
Requires(post): firewalld-filesystem
Suggests:       evolution-data-server
Suggests:       gsound
Suggests:       libcanberra-gtk3

%description
The KDE Connect project allows devices to securely share content such as
notifications and files as well as interactive features such as SMS messaging
and remote input. The KDE Connect team maintains cross-desktop, Android and
Sailfish applications as well as an interface for KDE Plasma.

GSConnect is a complete implementation of KDE Connect especially for GNOME Shell
with Nautilus, Chrome and Firefox integration. It is does not rely on the KDE
Connect desktop application and will not work with it installed.


%package -n nautilus-gsconnect
Summary:        Nautilus extension for GSConnect
Requires:       gobject-introspection
Requires:       nautilus-extensions
Requires:       nautilus-python
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n nautilus-gsconnect
The nautilus-gsconnect package provides a Nautilus context menu for sending
files to devices that are online, paired and have the "Share and receive" plugin
enabled.


%package -n nemo-gsconnect
Summary:        Nemo extension for GSConnect
Requires:       gobject-introspection
Requires:       nemo-extensions
Requires:       python3-nemo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n nemo-gsconnect
The nemo-gsconnect package provides a Nemo context menu for sending files to
devices that are online, paired and have the "Share and receive" plugin enabled.


%package -n webextension-gsconnect
Summary:        Web browser integration for GSConnect
Requires:       mozilla-filesystem
Requires:       %{name} = %{version}-%{release}

%description -n webextension-gsconnect
The webextension-gsconnect package allows Google Chrome/Chromium, Firefox,
Vivaldi, Opera (and other Browser Extension, Chrome Extension or WebExtensions
capable browsers) to interact with GSConnect, using the Share plugin to open
links in device browsers and the Telephony plugin to share links with contacts
by SMS.


%prep
%autosetup -p0 -n %{name}-%{version}%{?prerelease:-%{prerelease}}


%build
%meson \
    -Dfirewalld=true \
    -Dinstalled_tests=false \
    -Dnemo=true
%meson_build


%install
%meson_install

# Install AppData files
install -Dpm 0644 %{SOURCE1} %{SOURCE2} -t $RPM_BUILD_ROOT%{_metainfodir}/

%find_lang %{app_id}


%check
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.desktop \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.Preferences.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_metainfodir}/nautilus-gsconnect.metainfo.xml \
    $RPM_BUILD_ROOT%{_metainfodir}/nemo-gsconnect.metainfo.xml \
    $RPM_BUILD_ROOT%{_metainfodir}/%{app_id}.metainfo.xml


%post
%firewalld_reload


%files -f %{app_id}.lang
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/gsconnect@andyholmes.github.io/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/applications/%{app_id}.Preferences.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_prefix}/lib/firewalld/services/*.xml
%{_metainfodir}/%{app_id}.metainfo.xml


%files -n nautilus-gsconnect
%{_datadir}/nautilus-python/extensions/nautilus-gsconnect.py
%{_metainfodir}/nautilus-gsconnect.metainfo.xml


%files -n nemo-gsconnect
%{_datadir}/nemo-python/extensions/nemo-gsconnect.py
%{_metainfodir}/nemo-gsconnect.metainfo.xml


%files -n webextension-gsconnect
%{_libdir}/mozilla/native-messaging-hosts/
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/


%changelog
* Tue Sep 22 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 43-1
- Update to 43

* Sun Sep 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42-1
- Update to 42

* Wed Aug 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 41-1
- Update to 41

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 39-1
- Update to 39

* Fri May 15 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 38-1
- Update to 38

* Fri Apr 17 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 37-1
- Update to 37

* Sat Mar 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 36-1
- Update to 36

* Tue Mar 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 35-1
- Update to 35

* Wed Mar 11 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 34-1
- Update to 34

* Wed Mar 04 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 33-1
- Update to 33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 31-1
- Update to 31

* Mon Dec 02 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 30-1
- Update to 30

* Wed Oct 16 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 27-1
- Update to 27

* Tue Sep 10 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 26-1
- Update to 26

* Tue Sep 10 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 25-1
- Update to 25

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 24-1
- Update to 24

* Thu May 02 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 23-1
- Update to 23

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 21-2
- Rebuild with Meson fix for #1699099

* Mon Mar 18 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 21-1
- Update to 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20-1
- Update to 20

* Tue Nov 27 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16-1
- Initial RPM release
