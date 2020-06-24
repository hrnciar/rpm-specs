Name:           feedreader
Version:        2.11.0
Release:        1%{?dist}
Summary:        RSS desktop client

# Some of the source files are GPLv3+ and some are LGPLv3+, which makes the
# combined work GPLv3+.
License:        GPLv3+
URL:            https://github.com/jangernert/FeedReader
Source0:        https://github.com/jangernert/FeedReader/archive/v%{version}%{?pre:-%{pre}}/FeedReader-%{version}%{?pre:-%{pre}}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       dbus
Requires:       hicolor-icon-theme

%description
FeedReader is a modern desktop application designed to complement existing
web-based RSS accounts. It combines all the advantages of web based services
like synchronization across all your devices with everything you expect from a
modern desktop application.


%prep
%autosetup -p1 -n FeedReader-%{version}%{?pre:-%{pre}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang feedreader


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.FeedReader.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.FeedReader.desktop


%files -f feedreader.lang
%license LICENSE
%{_bindir}/feedreader
%{_libdir}/feedreader/
%{_libdir}/libFeedReader.so
%{_datadir}/feedreader/
%{_datadir}/applications/org.gnome.FeedReader.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.feedreader*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.FeedReader.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.FeedReader-symbolic.svg
%{_datadir}/metainfo/org.gnome.FeedReader.appdata.xml


%changelog
* Sat May 23 2020 Pete Walter <pwalter@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Pete Walter <pwalter@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0

* Thu May 30 2019 Pete Walter <pwalter@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2

* Mon May 27 2019 Pete Walter <pwalter@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1

* Fri May 24 2019 Pete Walter <pwalter@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0

* Mon Feb 11 2019 Pete Walter <pwalter@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Sun Feb 10 2019 Pete Walter <pwalter@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Fri Feb 01 2019 Pete Walter <pwalter@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Pete Walter <pwalter@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jan 25 2019 Pete Walter <pwalter@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Fri Dec 07 2018 Pete Walter <pwalter@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Tue Dec 04 2018 Pete Walter <pwalter@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Thu Nov 29 2018 Pete Walter <pwalter@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Mon Nov 26 2018 Pete Walter <pwalter@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Fri Nov 09 2018 Pete Walter <pwalter@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Fri Nov 02 2018 Pete Walter <pwalter@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Mon Oct 29 2018 Pete Walter <pwalter@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Pete Walter <pwalter@fedoraproject.org> - 2.2-1
- Update to 2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Mon Feb 20 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Mon Feb 13 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0-1
- Update to 2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0-0.1.beta1
- Update to 2.0 beta 1

* Thu Sep 22 2016 Pete Walter <pwalter@fedoraproject.org> - 1.6.2-2
- Add missing intltool build dependency

* Tue Aug 30 2016 Pete Walter <pwalter@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Thu Aug 04 2016 Pete Walter <pwalter@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Mon Aug 01 2016 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sun May 15 2016 Peter Walter <pwalter@fedoraproject.org> - 1.6-0.1.beta1
- Update to 1.6 beta 1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Pete Walter <pwalter@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sat Dec 12 2015 Pete Walter <pwalter@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Wed Nov 18 2015 Pete Walter <pwalter@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- Disable vilistextum support as we don't have that packaged in Fedora

* Sat Oct 10 2015 Pete Walter <pwalter@fedoraproject.org> - 1.4-0.1.beta
- Update to 1.4-beta

* Wed Sep 23 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-4
- Add missing html2text dependency

* Wed Sep 09 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-3
- Add update-desktop-database rpm scripts
- Add a comment explaining the licensing
- Depend on dbus for /usr/share/dbus-1/services directory

* Fri Sep 04 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-2
- Update to respinned 1.2.1 tarball
- Include app icon

* Fri Sep 04 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- Ship COPYING file
- Use American spelling of 'synchronization'
- Use autosetup macro
- Install appdata file

* Thu Sep 03 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2-1
- Initial packaging
