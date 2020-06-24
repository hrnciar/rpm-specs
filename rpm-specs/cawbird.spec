%global uuid    uk.co.ibboard.%{name}

Name:           cawbird
Version:        1.1.0
Release:        2%{?dist}
Summary:        Fork of the Corebird GTK Twitter client that continues to work with Twitter

License:        GPLv3+
URL:            https://github.com/IBBoard/cawbird
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/IBBoard/cawbird/issues/157
Patch0:         https://github.com/IBBoard/cawbird/commit/781e6061fa1e9be59751e732bf6e45393db4c7f8.patch#/fix-parsing-error-in-app-data.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)

Requires:       dbus-common
Requires:       hicolor-icon-theme

%description
Cawbird is a fork of the Corebird Twitter client from Baedert, which became
unsupported after Twitter disabled the streaming API.

Cawbird works with the new APIs and includes a few fixes and modifications that
have historically been patched in to IBBoard's custom Corebird build on his
personal Open Build Service account.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/locale/es_419
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md notes.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/cawbird.1*
%{_metainfodir}/*.xml


%changelog
* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-2
- Fix parsing error in app-data | GH-157

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Mon Nov 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3.1-1
- Update to 1.0.3.1

* Sun Oct 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-2
- Update to 1.0.2

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-2.20191002git870f127
- Initial package

