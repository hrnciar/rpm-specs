Name:           qdirstat
Version:        1.7
Release:        1%{?dist}
Summary:        Qt-based directory statistics

License:        GPLv2
URL:            https://github.com/shundhammer/qdirstat
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       qt5-qtbase
Requires:       hicolor-icon-theme

%description
QDirStat is a graphical application to show where your disk space has gone
and to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
 latest Qt 5. It does not need any KDE libs or infrastructure. It runs on
 every X11-based desktop on Linux, BSD and other Unix-like systems.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{qmake_qt5}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/qdirstat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%{_docdir}/%{name}/
%{_bindir}/qdirstat
%{_bindir}/qdirstat-cache-writer
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Mon Aug 24 22:14:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.7-1
- Update to 1.7 (#1860727)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 00:59:03 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 00:10:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6-1
- Release 1.6

* Fri Jul 05 16:13:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.90-1
- Release 1.5.90 (#1727120)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Robert-André Mauchin <zebob.m@gmail.com> 1.5-1
- Update to version 1.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-7
- Add a svg icon for Appstream

* Sun Feb 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-6
- Add missing BR for gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-4
- Remove obsolete scriptlets

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-3
- Fix for Fedora Review

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-2
- Update to Fedora Packaging Guidelines specification

* Sat Jun 24 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-1
- Update to version 1.4

* Tue Mar 07 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.3-1
- Update to version 1.3

* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.2-1
- Update to version 1.2

* Sat Dec 03 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.1-1
- First RPM release
