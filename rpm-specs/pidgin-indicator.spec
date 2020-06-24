
Name:    pidgin-indicator
Summary: StatusNotifierItem tray icon plugin for Pidgin
Version: 1.0.1
Release: 5%{?dist}

License: GPLv2+
URL:     https://github.com/philipl/pidgin-indicator
Source0: https://github.com/philipl/pidgin-indicator/releases/download/%{version}/pidgin-indicator-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: pkgconfig(appindicator-0.1)
BuildRequires: pkgconfig(pidgin)
BuildRequires: perl(XML::Parser)

Requires: pidgin

%if 0%{?fedora} > 23
Supplements: (pidgin and plasma-workspace)
%endif

%description
This plugin provides a StatusNotifierItem tray icon, for use in
KDE Plasma 5, Unity, Elementary and other environments.

It provides all the same functionality as the original tray icon
but not in exactly the same way:
* The smart click behavior that either shows the buddy list or
unread messages is now activated by a middle-click because
left click on an libappindicator always opens the menu.
* As the SNI-icon is a separate process from pidgin itself, there
are sometimes conflicts with Focus Stealing Prevention when you
use the indicator to go to unread messages. You may need to
disable FSP for Pidgin to get around this.
* Due to how libappindicator work, the middle-click action must
also be a menu item, so it's the new Show/Hide item at the top
of the menu.
* Due to libappindicator limitations, some of the special icons
cannot be shown next to menu items any more.


%prep
%autosetup


%build
%configure

%make_build


%install
%make_install

%find_lang pidgin-indicator

## unpackaged files
rm -fv %{buildroot}%{_libdir}/pidgin/indicator.la

%files -f pidgin-indicator.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/pidgin/indicator.*
%{_datadir}/icons/hicolor/*/status/pidgin-indicator-nothing.png


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- 1.0.1 (#1574489)

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0-7
- BR: gcc, use %%make_build %%make_install

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.0-1
- 1.0

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-2
- Supplements: (pidgin and plasma-workspace), f24+

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- 0.9

* Mon Jun 15 2015 Radek Vokal <rvokal@redhat.com> - 0.1-1
- Initial package build
