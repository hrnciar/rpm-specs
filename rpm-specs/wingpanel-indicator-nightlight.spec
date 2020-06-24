%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.nightlight

Name:           wingpanel-indicator-nightlight
Summary:        Night Light Indicator for wingpanel
Version:        2.0.3
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A wingpanel indicator for Night Light.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang nightlight-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f nightlight-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnightlight.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Initial package.

