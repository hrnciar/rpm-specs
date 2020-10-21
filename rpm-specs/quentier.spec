%undefine __cmake_in_source_build

%global commit          48fa2ccedfebcffa7f41dfa29ffaf8d7758518b3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20200617

Name:       quentier
Summary:    Cross-platform desktop Evernote client
Version:    0.5.0
Release:    0.2.%{snapshotdate}git%{shortcommit}%{?dist}

License:    GPLv3
URL:        https://github.com/d1vanov/quentier
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Libquentier-qt5)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(libxml2)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: boost-devel
BuildRequires: libtidy-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires:      hicolor-icon-theme
Requires:      oxygen-icon-theme
Requires:      tango-icon-theme

%description
Quentier is a cross-platform desktop note taking app capable of working as
Evernote client. You can also use Quentier for local notes without any
connection to Evernote and synchronization.

%prep
%autosetup -p1 -n %{name}-%{commit}

sed -i "/tango.qrc/d; /oxygen.qrc/d" CMakeLists.txt
sed -i "s/QStringLiteral(\"tango\")/QStringLiteral(\"Tango\")/" bin/quentier/src/MainWindow.cpp

%build
%cmake -DQt5_LUPDATE_EXECUTABLE=%{_bindir}/lupdate-qt5 \
       -DQt5_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt5
%cmake_build
%cmake_build --target lupdate
%cmake_build --target lrelease

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/icons/hicolor/1024x1024

for size in "16x16" "22x22" "32x32" ; do
    for icon in "actions/mail-send.png" \
                "actions/checkbox.png" \
                "actions/format-list-ordered.png" \
                "actions/format-list-unordered.png" \
                "actions/tools-check-spelling.png" \
                "actions/insert-horizontal-rule.png" \
                "actions/format-text-color.png" \
                "actions/fill-color.png" \
                "actions/insert-table.png" \
                "mimetypes/application-pdf.png" \
                "mimetypes/application-enex.png" ; do
        install -Dpm 0644 resource/icons/themes/tango/$size/$icon %buildroot%{_datadir}/icons/Tango/$size/$icon
    done
done
for size in "16x16" "22x22" "32x32" ; do
    install -Dpm 0644 resource/icons/themes/oxygen/$size/mimetypes/application-enex.png %buildroot%{_datadir}/icons/oxygen/$size/mimetypes/application-enex.png
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.quentier.Quentier.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.quentier.Quentier.appdata.xml

%files
%doc CONTRIBUTING.md CodingStyle.md README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-%{version}
%{_datadir}/applications/org.quentier.Quentier.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/oxygen/
%{_datadir}/icons/Tango/
%{_metainfodir}/org.quentier.Quentier.appdata.xml
%dir %{_datadir}/quentier
%{_datadir}/quentier/translations

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.2.20200617git48fa2cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 19:31:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-0.1.20200617git48fa2cc
- Bump to commit 48fa2ccedfebcffa7f41dfa29ffaf8d7758518b3

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-0.14.20190730gitad95ab4
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.13.20190730gitad95ab4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 18:59:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.12.20190730gitad95ab4
- Bump to commit ad95ab4e30127d1c0c444224a29a897406c51a9e

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.11.20190311git594128d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.10.20190311git594128d
- Bump to 594128de97ad818a3b013f71b1b7dac920afe044

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.9.20180903.git5342a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-0.8.20180903.git5342a4f
- Rebuilt for Boost 1.69

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 0.4.0-0.7.20180903git5342a4f
- rebuild for hunspell-1.7.0

* Mon Sep 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.6.20180903git5342a4f
- Bump to 5342a4f72a7f0f9d1b77391c8ec7bedf41a3613c

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.5.20180622.git5a92775
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.4.20180622git5a92775
- Bump to 5a9277504a6a68da0a490f755e036561270094c7

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.3.20180301git8226e31
- Bump to 8226e3174607c2ef0ed3e32e57fe09484e6d2c0e

* Tue Feb 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.2.20180227gite72d0e4
- Bump to e72d0e45d908b4246dba79939db01931504e9d0a

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.1.20180128git442947d
- Initial RPM release.
