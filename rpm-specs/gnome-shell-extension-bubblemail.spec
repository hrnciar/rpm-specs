%global upname bubblemail-gnome-shell

Name:           gnome-shell-extension-bubblemail
Version:        1.3
Release:        1%{?dist}
Summary:        GNOME Shell indicator for new and unread mail using Bubblemail 

License:        GPLv2+
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{upname}/-/archive/v%{version}/%{upname}-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext

Requires:       bubblemail >= 1.0
Requires:       gnome-shell >= 3.34

BuildArch:      noarch

%description
%{name} relies on the Bubblemail service to display
notifications in GNOME shell about new and unread messages in local (mbox,
Maildir) and remote (POP3, IMAP) mailboxes.


%prep
%autosetup -n %{upname}-v%{version}
mv src/LICENSE ./

%build	
%meson -Dgnome_shell_libdir=%{_datadir}/gnome-shell/extensions/ \
       -Dgsettings_schemadir=%{_datadir}/glib-2.0/schemas/
%meson_build

%install
%meson_install
%find_lang %{upname}

%files -f %{upname}.lang
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.bubblemail.gschema.xml
%{_datadir}/gnome-shell/extensions/bubblemail@razer.framagit.org/

%changelog
* Sat Oct 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3-1
- Update to v1.3

* Thu Aug 27 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.2-1
- Update to v1.2
- Fix typo in changelog

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.1-1
- Update to v1.1

* Sun May 24 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.0-1
- Update to v1.0

* Tue Apr 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.71-1
- Initial release for Fedora
