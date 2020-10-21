Name:           bubblemail
Version:        1.3
Release:        1%{?dist}
Summary:        Extensible mail notification service

License:        GPLv2
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  folks-devel
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
BuildRequires:  python3-pyxdg
BuildRequires:  vala
Requires:       folks
Requires:       gnome-keyring
Requires:       hicolor-icon-theme
Requires:       libsecret
Requires:       python3
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-requests
Requires:       python3-gstreamer1
Requires:       python3-pyxdg
Recommends:     gnome-online-accounts

%description
Bubblemail is a D-Bus service providing a list of the new and unread user's mail
from local mailboxes, pop, imap, and gnome online accounts. It include a
libnotify frontend to create notifications and can be used by other frontends as
well.

%prep
%autosetup -p1 -n %{name}-v%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' \
        bubblemail/plugins/spamfilterplugin.py \
        bubblemail/plugins/userscriptplugin.py

%build
%py3_build

%install
%py3_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSE.txt
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}d.1*
%{_sysconfdir}/xdg/autostart/%{name}d.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-avatar-provider
%{_bindir}/%{name}d
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%{python3_sitelib}/%{name}/
%{_datadir}/applications/bubblemail.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Sat Oct 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3-1
- Update to 1.3

* Thu Aug 27 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.2-1
- Update to 1.2
- New icon
- Bugfixes
- Fix typo in changelog

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.1-1
- Update to 1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.0-1
- Update to 1.0

* Tue Apr 14 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7-1
- Update to 0.7

* Sat Feb 22 01:31:11 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5-1
- Update to 0.5

* Thu Jan 30 19:59:15 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4-3
- Fix #1796406

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 02:38:48 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4-1
- Initial packaging
