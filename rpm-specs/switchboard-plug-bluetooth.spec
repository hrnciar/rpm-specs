%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name bluetooth
%global plug_rdnn io.elementary.switchboard.bluetooth

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        2.3.2
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       bluez
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and bluez)

%description
The Bluetooth plug is a section in the Switchboard (System Settings)
that allows the user to manage bluetooth settings and connected
devices.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-1
- Update to version 2.3.2.

* Thu Feb 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.2-2
- Rebuild with Meson fix for #1699099

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Update to version 2.1.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1-6
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1-5
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Add upstream patch to fix compilation with vala 0.35+.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

