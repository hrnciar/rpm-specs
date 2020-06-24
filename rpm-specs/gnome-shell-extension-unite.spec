%global extuuid		unite@hardpixel.eu
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		unite-shell
%global giturl		https://github.com/hardpixel/%{gitname}


Name:		gnome-shell-extension-unite
Version:	8
Release:	6%{?dist}
Summary:	GNOME Shell Extension Unite by hardpixel

License:	GPLv3+
URL:		https://extensions.gnome.org/extension/1287/unite
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	gnome-shell-extension-common
Requires:	xorg-x11-utils

%description
Unite is a GNOME Shell extension which makes a few layout tweaks to the
top panel and removes window decorations to make it look like Ubuntu
Unity Shell.

  * Adds window buttons to the top panel for maximized windows.
  * Shows current window title in the app menu for maximized windows.
  * Removes titlebars on maximized windows.
  * Hides window controls on maximized windows with headerbars.
  * Moves the date to the right, fixes icons spacing and removes
    dropdown arrows.
  * Moves legacy tray icons to the top panel.
  * Moves notifications to the right.
  * Hides activities button.


%prep
%autosetup -n %{gitname}-%{version} -p 1


%build
# noop


%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}


%files
%license LICENSE
%doc README.md
%{extdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 8-1
- Initial import (rhbz#1520153)

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 8-0.1
- Initial rpm release (rhbz#1520153)
