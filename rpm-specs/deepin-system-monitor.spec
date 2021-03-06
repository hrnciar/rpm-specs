Name:           deepin-system-monitor
Version:        5.0.0
Release:        5%{?dist}
Summary:        A more user-friendly system monitor
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml
Patch0:         0001-Fix-build-with-Qt-5.14.patch
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(dtkwm) >= 2.0
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  libpcap-devel
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%setup -q
%patch0 -p1

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc README.md
%license LICENSE
%caps(cap_kill,cap_net_raw,cap_dac_read_search,cap_sys_ptrace=+ep) %{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/

%changelog
* Wed Sep  2 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-5
- Rebuild for libprocps

* Thu Aug  6 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-4
- Applied a patch to fix build with Qt 5.14

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.4.8.1-1
- Update to 1.4.8.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.4.8-1
- Update to 1.4.8

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.4.7-1
- Update to 1.4.7

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 1.4.6-1
- Update to 1.4.6

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 1.4.5-1
- Update to 1.4.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.7-4
- Rebuild for procps-ng-3.3.15

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.7-2
- Remove obsolete scriptlets

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 1.3.7-1
- Update to 1.3.7

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 1.3-1
- Update to 1.3

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Sat Jul 15 2017 mosquito <sensor.wen@gmail.com> - 0.0.4-1.gita73357d
- Initial build
