%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.session

Name:           wingpanel-indicator-session
Summary:        Session Indicator for wingpanel
Version:        2.2.8
Release:        4%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# upstream patch to fix vala / gee API issue
# backported from https://github.com/elementary/wingpanel-indicator-session/commit/85347e6
Patch0:         00-vala-gee-api-fix.patch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A session Indicator for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang session-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f session-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libsession.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Aug 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.8-4
- Include patch to fix gee API issues with latest vala.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.8-1
- Update to version 2.2.8.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7-1
- Update to version 2.2.7.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6-1
- Update to version 2.2.6.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5-1
- Update to version 2.2.5.

* Wed Jul 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Rebuild for granite5 soname bump.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-1
- Update to version 2.0.4.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-2
- Rebuild for granite soname bump.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-4
- Remove explicit BR: pkgconfig.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Filter Provides.

* Fri Jan 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Clean up spec file.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-2
- Mass rebuild.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to latest snapshot.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com>
- Weak inverse require wingpanel.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

