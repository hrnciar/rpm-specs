%global majorversion %(cut -d "." -f 1-2 <<<%{version})

Name:           gnome-tweaks
Version:        3.34.0
Release:        5%{?dist}
Summary:        Customize advanced GNOME 3 options

# Software is GPLv3, Appdata file is CC0-1.0
License:        GPLv3 and CC0
URL:            https://wiki.gnome.org/action/show/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/%{majorversion}/%{name}-%{version}.tar.xz

# Fix opening system installed extensions in gnome-software
# https://gitlab.gnome.org/GNOME/gnome-tweaks/merge_requests/25
Patch0:         0001-extensions-Fix-opening-system-installed-extensions-i.patch
# Fix extension preferences with gnome-extensions instead of
# gnome-shell-extension-prefs
# https://bugzilla.redhat.com/show_bug.cgi?id=1820396#c2
Patch1:         0002-extensions-Fix-preferences-opening.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
Requires:       gnome-desktop3
Requires:       gnome-settings-daemon
Requires:       gnome-shell
Requires:       gnome-shell-extension-user-theme
Requires:       gobject-introspection
Requires:       gsettings-desktop-schemas
Requires:       gtk3
Requires:       libhandy
Requires:       libnotify
Requires:       libsoup
Requires:       mutter
Requires:       pango
Requires:       python3dist(pygobject)
Provides:       gnome-tweak-tool = %{version}-%{release}
Obsoletes:      gnome-tweak-tool < 3.27.3-4
BuildArch:      noarch

%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-tweak-tool/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-tweak-tool/b.png

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/
%{_bindir}/%{name}
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{python3_sitelib}/gtweak/
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.tweaks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.34.0-5
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-4
- Fix extension preferences opening (RHBZ #1820396)

* Sat Mar 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-3
- Add dependency on gnome-extensions-app (RHBZ #1812779)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.90-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.32.0-2
- Fix typo in Provides version (RHBZ #1721864)

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Wed Dec 19 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2
- Fix opening system installed extensions in gnome-software

* Fri Sep 28 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.30.0-1
- Update to 3.30.0

* Wed Aug 29 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.92-1
- Update to 3.29.92

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.91.1-1
- Update to 3.29.91.1

* Fri Aug 03 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.90.1-1
- Update to 3.29.90.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.29.2-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.2-1
- Update to 3.29.2

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.27.92-1
- Initial RPM release, based on gnome-tweak-tool.spec
