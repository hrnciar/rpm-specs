Name:           gnome-shell-extension-gamemode
Version:        1
Release:        4%{?dist}
Summary:        GameMode integration for GNOME Shell
License:        LGPLv2
URL:            https://github.com/gicmo/gamemode-extension
Source0:        %{url}/archive/v%{version}/gamemode-extension-%{version}.tar.gz
Patch0:         shell-master-changes.patch

BuildRequires:  meson
BuildRequires:  gettext >= 0.19.6
Requires:       gnome-shell >= 3.33
Suggests:       gamemode
BuildArch:      noarch

%description
GNOME Shell extension to integrate with GameMode. Can display
an icon when GameMode is active and also emit notifications
when the global GameMode status changes.


%prep
%autosetup -p1 -n gamemode-extension-%{version}%{?prerelease:-%{prerelease}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang gamemode-extension


%files -f gamemode-extension.lang
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/gamemode*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gamemode.gschema.xml


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Christian Kellner <christian@kellner.me> - 1-1
- Initial package
  Resolves rhbz#1725103
- Include patche to adapt for GNOME Shell 3.33 API changes.

