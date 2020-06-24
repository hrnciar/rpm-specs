%global srcname code
%global appname io.elementary.code

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-code
Summary:        Code editor from elementary
Version:        3.4.1
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.24
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libvala-0.48)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

Provides:       scratch-text-editor = %{version}-%{release}
Obsoletes:      scratch-text-editor < 2.4.1-13.20180825.gitdf6691c


%description
%{summary}.


%package        devel
Summary:        The text editor that works (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

This package contains the development headers.


%prep
%autosetup -n %{srcname}-%{version} -p1


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
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/
%{_libdir}/libcodecore.so.0
%{_libdir}/libcodecore.so.0.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%doc README.md
%license COPYING

%{_includedir}/codecore.h

%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%{_datadir}/vala/vapi/codecore.deps
%{_datadir}/vala/vapi/codecore.vapi


%changelog
* Fri Jun 12 2020 Fabio Valentini <decathorpe@gmail.com> - 3.4.1-1
- Update to version 3.4.1.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 3.4.0-1
- Update to version 3.4.0.

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-1
- Update to version 3.3.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Kalev Lember <klember@redhat.com> - 3.2.0-2
- Rebuilt for vala 0.48

* Sat Jan 11 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.1.1-3
- Rebuilt for vala 0.46

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.1.1-2
- Rebuild with Meson fix for #1699099

* Sun Mar 17 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1-1
- Update to version 3.1.1.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0-1
- Update to version 3.1.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2-1
- Update to version 3.0.2.

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.0.1-2
- Rebuilt for vala 0.44

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-1
- Update to version 3.0.1.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0-1
- Update to version 3.0.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1-13.20180825.gitdf6691c
- Initial package renamed from scratch-text-editor.

