%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.datetime

Name:           wingpanel-indicator-datetime
Summary:        Datetime Indicator for wingpanel
Version:        2.2.5
Release:        2%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/wingpanel-indicator-datetime
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A datetime indicator for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang datetime-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f datetime-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libdatetime.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.datetime.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.5-1
- Update to version 2.2.5.

* Thu May 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Wed May 20 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Mon Mar 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-2
- Include upstream patch for libecal-2.0 support.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-4
- Drop unnecessary granite/datetime patch.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-2
- Add patch to move some gsettings to granite itself.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-2
- Rebuild for libedataserver soname bump.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Add missing BR: gcc, gcc-c++.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-8
- Rebuild for granite5 soname bump.

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 2.0.2-7
- Rebuilt for evolution-data-server soname bump

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-6
- Add patch to fix undefined symbols.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-5
- Rebuild for libical soname bump.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Remove explicit BR: pkgconfig.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Clean up spec file.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Spec file cleanups.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

