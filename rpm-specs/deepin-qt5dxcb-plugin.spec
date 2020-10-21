%global repo qt5platform-plugins

Name:           deepin-qt5dxcb-plugin
Version:        5.0.17
Release:        1%{?dist}
Summary:        Qt platform integration plugin for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(mtdev)
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
%{repo} is the
%{summary}.

%prep
%setup -q -n %{repo}-%{version}
rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev

# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro

sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += %{_qt5_includedir}/QtXcb|' xcb/linux.pri

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/platforms/libdxcb.so

%changelog
* Wed Sep 16 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.17-1
- Update to 5.0.17

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.1-7
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.0-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.0-2
- rebuild (qt5)

* Wed May 15 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (BZ#1701436)

* Thu Apr 11 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.25-1
- Separated from deepin-qt5integration
