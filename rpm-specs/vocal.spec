%global appname com.github.needle-and-thread.vocal

Name:           vocal
Summary:        Powerful, beautiful, and simple podcast client
Version:        2.4.1
Release:        3%{?dist}
License:        GPLv3

URL:            https://github.com/needle-and-thread/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26.2

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme


%description
Vocal is a powerful, fast, and intuitive application that helps users
find new podcasts, manage their libraries, and enjoy the best that
independent audio and video publishing has to offer. Vocal features full
support for both episode downloading and streaming, native system
integration, iTunes store search and top 100 charts (with international
results support), iTunes link parsing, OPML importing and exporting, and
so much more. Plus, it has great smart features like automatically
keeping your library clean from old files, and the ability to set custom
skip intervals.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang vocal


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f vocal.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/vocal/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1-1
- Update to version 2.4.1.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-2
- Rebuild for granite5 soname bump.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-1
- Update to version 2.1.6.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Remove icon cache scriptlets, replaced by file triggers.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-1
- Update to version 2.0.20.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.19-1
- Initial package.

