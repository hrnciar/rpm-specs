%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-network

%global plug_type network
%global plug_name networking
%global plug_rdnn io.elementary.switchboard.network

Name:           switchboard-plug-networking
Summary:        Switchboard Networking plug
Version:        2.3.3
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       network-manager-applet%{?_isa}
Requires:       switchboard%{?_isa}
Requires:       NetworkManager%{?_isa}

Supplements:    (switchboard%{?_isa} and NetworkManager%{?_isa})


%description
A switchboard plug for configuring available networks.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-1
- Update to version 2.3.3.

* Fri Sep 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-1
- Update to version 2.3.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-3
- Add missing dependency on network-manager-applet.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-5.20180218.gitc52183a
- Remove extraneous BR: libnm-gtk.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-4.20180218.gitc52183a
- Bump to commit c52183a to switch away from libnm-glib.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Rebuild for granite soname bump.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-3
- Refine Supplements.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-2
- Clean up spec file.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3-1
- Update to version 0.1.0.3.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2-2
- Mass rebuild.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2-1
- Update to version 0.1.0.2.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1-1
- Update to version 0.1.0.1.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.

