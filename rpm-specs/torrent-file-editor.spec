Name:           torrent-file-editor
Version:        0.3.17
Release:        4%{?dist}
Summary:        Qt based GUI tool designed to create and edit .torrent files

License:        GPLv3+
URL:            https://torrent-file-editor.github.io
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
%if 0%{?fedora} > 21 || 0%{?rhel} > 7
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qttools-devel
%else
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QJson)
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Package puts icons to hicolor-icon-theme folders
Requires:       hicolor-icon-theme

%description
Qt based GUI tool designed to create and edit .torrent files.

Features
 - create .torrent file from scratch
 - edit .torrent file in user-friendly way
 - edit .torrent file in tree format
 - edit .torrent file in JSON format
 - add, remove and interchange files in .torrent file
 - support for codings

%prep
%setup -q

%build
%if 0%{?fedora} > 21 || 0%{?rhel} > 7
%cmake -DQT5_BUILD=ON -DDISABLE_DONATION=ON -DENABLE_PCH=OFF
%else 
%cmake -DDISABLE_DONATION=ON -DENABLE_PCH=OFF
%endif
%cmake_build

%install
%cmake_install

%check
# Menu file is being installed when make install
# so it need only to check this allready installed file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Check AppData file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Ivan Romanov <drizt72@zoho.eu> - 0.3.17-2
- Fix EPEL8 building
- Disable PCH

* Mon Jan  6 2020 Ivan Romanov <drizt72@zoho.eu> - 0.3.17-1
- Bump to v0.3.17

* Mon Sep 23 2019 Ivan Romanov <drizt72@zoho.eu> - 0.3.16-1
- Bump to v0.3.16

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Ivan Romanov <drizt72@zoho.eu> - 0.3.15-1
- Bump to v0.3.15
- Update URL and Source

* Fri Apr 12 2019 Ivan Romanov <drizt72@zoho.eu> - 0.3.14-1
- Bump to v0.3.14

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Ivan Romanov <drizt72@zoho.eu> - 0.3.13-1
- Bump to v0.3.13

* Sun Aug  5 2018 Ivan Romanov <drizt72@zoho.eu> - 0.3.12-1
- Bump to v0.3.12

* Sun Jul 15 2018 Ivan Romanov <drizt72@zoho.eu> - 0.3.11-1
- Bump to v0.3.11

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Ivan Romanov <drizt72@zoho.eu> - 0.3.10-1
- Bump to v0.3.10

* Mon Dec 11 2017 Ivan Romanov <drizt@land.ru> - 0.3.9-1
- Bump to v0.3.9

* Thu Nov 30 2017 Ivan Romanov <drizt@land.ru> - 0.3.8-1
- Bump to v0.3.8

* Tue Sep 26 2017 Ivan Romanov <drizt@land.ru> - 0.3.7-1
- Bump to v0.3.7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Ivan Romanov <drizt@land.ru> - 0.3.6-1
- Bump to v0.3.6

* Sun Jun  4 2017 Ivan Romanov <drizt@land.ru> - 0.3.5-1
- Bump to v0.3.5

* Mon Apr 17 2017 Ivan Romanov <drizt@land.ru> - 0.3.4-1
- Bump to v0.3.4

* Mon Apr 17 2017 Ivan Romanov <drizt@land.ru> - 0.3.3-1
- Bump to v0.3.3

* Thu Mar 23 2017 Ivan Romanov <drizt@land.ru> - 0.3.2-1
- Bump to v0.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Ivan Romanov <drizt@land.ru> - 0.3.1-1
- Bump to v0.3.1

* Wed Jun 29 2016 Ivan Romanov <drizt@land.ru> - 0.3.0-1
- Bump to v0.3.0

* Fri Jun  3 2016 Ivan Romanov <drizt@land.ru> - 0.2.2-1
- Bump to v0.2.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Ivan Romanov <drizt@land.ru> - 0.2.1-1
- Bump to v0.2.1
- Use %%license tag

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun  6 2015 Ivan Romanov <drizt@land.ru> - 0.2.0-2
- link against Qt5 on F22

* Tue May 12 2015 Ivan Romanov <drizt@land.ru> - 0.2.0-1
- update to v0.2.0
- dropped app file patch (went to upstream)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 25 2015 Ivan Romanov <drizt@land.ru> - 0.1.0-4
- Added AppData file

* Sun Dec 21 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-3
- corrected updating icon cache
- added updating MIME type database

* Sat Dec 20 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-2
- Corrected sf source path
- Corrected project url
- Added hicolor-icon-theme to requires
- Improved description
- Use check section for desktop file validation

* Sat Dec 20 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-1
- Initial version of package
