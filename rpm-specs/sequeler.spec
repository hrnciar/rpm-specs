%global appname com.github.alecaddd.sequeler

Name:           sequeler
Summary:        SQL Client built in Vala
Version:        0.7.91
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/Alecaddd/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

Recommends:     libgda-mysql
Recommends:     libgda-postgres
Recommends:     libgda-sqlite


%description
Sequeler is a native Linux SQL client built in Vala and Gtk. It allows
you to connect to your local and remote databases, write SQL in a handy
text editor with language recognition, and visualize SELECT results in
a Gtk.Grid Widget.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{appname}.svg
%{_datadir}/icons/hicolor/16x16/status/table*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun May 24 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.91-1
- Update to version 0.7.91.

* Sun Apr 12 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.9-1
- Update to version 0.7.9.

* Fri Apr 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.5-1
- Update to version 0.7.5.

* Wed Apr 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.7.4-1
- Update to version 0.7.4.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.3-1
- Update to version 0.7.3.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.2-1
- Update to version 0.7.2.

* Sun Aug 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.1-1
- Update to version 0.7.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.7.0-2
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.0-1
- Update to version 0.7.0.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.9-1
- Update to version 0.6.9.

* Sun Mar 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Update to version 0.6.8.

* Wed Feb 27 2019 Fabio Valentini <decathorpe@gmail.com> - 0.6.7-1
- Update to version 0.6.7.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.5-1
- Update to version 0.6.5.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.4-1
- Update to version 0.6.4.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.3-1
- Update to version 0.6.3.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.2-1
- Update to version 0.6.2.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-1
- Update to version 0.6.1.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.0-1
- Update to version 0.6.0.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.9-1
- Update to version 0.5.9.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.7-1
- Update to version 0.5.7.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-2
- Rebuild for granite5 soname bump.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-1
- Update to version 0.5.5.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-1
- Update to version 0.5.4.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Update to version 0.5.3.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Update to version 0.5.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3-1
- Update to version 0.4.3.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-1
- Update to version 0.4.2.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Initial package for fedora.

