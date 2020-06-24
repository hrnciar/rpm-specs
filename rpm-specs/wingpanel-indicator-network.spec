%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.network

Name:           wingpanel-indicator-network
Summary:        Network Indicator for wingpanel
Version:        2.2.4
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       network-manager-applet%{?_isa}
Requires:       wingpanel%{?_isa}

Supplements:    wingpanel%{?_isa}


%description
A network indicator for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang network-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f network-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Sat Mar 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-3
- Add missing dependency on network-manager-applet.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.
- Drop backported patch included in this release.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-2
- Include upstream patch to fix libnm.vapi for vala 0.44.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-2
- Rebuild for granite5 soname bump.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-5.20171231.gitedd2b7a
- Remove unnecessary libnm-util dependency.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-4.20171231.gitedd2b7a
- Bump to commit edd2b7a to switch away from libnm-glib amd libnm-gtk.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-2
- Rebuild for granite soname bump.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-3
- Remove explicit BR: pkgconfig.

* Sun Jan 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-2
- Clean up spec file.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Spec file cleanups.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0.

