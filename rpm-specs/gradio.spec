# Note: Gradio version 8.0 was rewritten in Rust and renamed to Shortwave

%global uuid    de.haeckerfelix.%{name}

Name:           gradio
Version:        7.3
Release:        5%{?dist}
Summary:        Find and listen to internet radio stations

License:        GPLv3+
URL:            https://github.com/haecker-felix/Gradio
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Adding multiple translations which not included by upstream:
# hi, hu, ca, cmn, fi, ga, id, ja, ko, pt_PT, ru
Patch0:         %{name}-translations.patch

# Regression in 0.55: Compiling Vala requires C
# * https://github.com/mesonbuild/meson/issues/7495
Patch1:         regression-in-0.55-compiling-vala-requires-c.patch

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)

Requires:       dconf
Requires:       hicolor-icon-theme

%description
A GTK3 app for finding and listening to internet radio stations.


%prep
%autosetup -n Gradio-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gnome-shell/search-providers/*.search-provider.ini
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml


%changelog
* Thu Aug 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 7.3-5
- Fix regression in Meson 0.55: Compiling Vala requires C

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.3-1
- Update to 7.3
- Switch upstream URL - https://gitlab.gnome.org/World/Shortwave/issues/391

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-13
- Cosmetic spec file fixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 7.2-11
- Rebuild with Meson fix for #1699099

* Wed Mar 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-10
- Removed unnecessary buildrequires dependency

* Sun Feb 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-9
- Updated spec file

* Mon Feb 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-4
- Removed gnome-shell dependency

* Sun Feb 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-3
- Updated spec file
- Added multiple translations: ca, cmn, fi, ga, hi, hu, id, ja, ko, pt_PT

* Fri Feb 1 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-2
- Spec file fixes

* Thu Jan 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-1
- Added Russian translation
