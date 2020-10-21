%global appname YACReader

Name:           yacreader
Version:        9.7.1
Release:        1%{?dist}
Summary:        Cross platform comic reader and library manager

# The entire source code is GPLv3+ except:
# BSD:          QsLog
#               folder_model
# MIT:          pictureflow
License:        GPLv3+ and BSD and MIT
URL:            https://www.yacreader.com
Source0:        https://github.com/YACReader/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(libunarr)
BuildRequires:  pkgconfig(poppler-qt5)

Requires:       hicolor-icon-theme
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols%{?_isa}

%{?systemd_requires}

%description
Best comic reader and comic manager with support for .cbr .cbz .zip .rar comic
files.


%prep
%autosetup -p1

# wrong-file-end-of-line-encoding fix
sed -i 's/\r$//' INSTALL.md

# file-not-utf8 fix
iconv -f iso8859-1 -t utf-8 README.md > README.md.conv && mv -f README.md.conv README.md


%build
%qmake_qt5
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
%find_lang %{name}library --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang -f %{name}library.lang
%license COPYING.txt
%doc CHANGELOG.md README.md INSTALL.md
%{_bindir}/%{appname}
%{_bindir}/%{appname}Library
%{_bindir}/%{appname}LibraryServer
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*
%{_userunitdir}/*.service


%changelog
* Sat Sep 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 9.7.1-1
- Update to 9.7.1

* Fri Sep  4 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 9.7.0-1
- Update to 9.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 9.6.2-3
- Add dep: qt5-qtgraphicaleffects
- Add dep: qt5-qtquickcontrols

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 9.6.2-1
- Update to 9.6.2
- Enable LTO

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 9.6.0-2
- Rebuild for poppler-0.84.0

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 9.6.0-1
- Update to 9.6.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 9.5.0-6
- Initial package.
