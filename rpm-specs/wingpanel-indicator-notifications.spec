%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.notifications

Name:           wingpanel-indicator-notifications
Summary:        Notifications Indicator for wingpanel
Version:        2.1.4
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A notifications indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang notifications-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f notifications-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnotifications.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Rebuild for granite5 soname bump.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-2
- Rebuild for granite soname bump.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0-6
- Add upstream patch to fix compilation with vala 0.35+.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0-4
- Remove explicit BR: pkgconfig.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Clean up spec file.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

