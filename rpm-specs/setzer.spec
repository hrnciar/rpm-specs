%global forgeurl    https://github.com/cvfosammmm/Setzer
%global uuid        org.cvfosammmm.Setzer

Name:           setzer
Version:        0.2.8
Release:        3%{?dist}
Summary:        LaTeX editor written in Python with Gtk

%forgemeta

License:        GPLv3+
URL:            https://www.cvfosammmm.org/setzer/
Source0:        %{forgesource}
BuildArch:      noarch


BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  gspell-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  python3-pyxdg
BuildRequires:  python3-gobject
Requires:       gtk3
Requires:       gtksourceview4
Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       poppler-glib
Requires:       python3-pyxdg
Requires:       python3-gobject

Requires:       texlive
Requires:       texlive-synctex

# LaTeX engines
Requires:       texlive-xetex
Recommends:     latexmk
Recommends:     texlive-pdftex
Recommends:     texlive-luatex

%description
Write LaTeX documents with an easy to use yet full-featured editor.

- Buttons and shortcuts for many LaTeX elements and special characters.
- Document creation wizard.
- Dark mode.
- Helpful error messages in the build log.
- Looks great on the Gnome desktop.
- Good screen to content ratio.
- Arguably the best .pdf viewer of any LaTeX editor.

%prep
%forgeautosetup -p1

%build
# Removing unnecessary shebangs
find ./setzer -name "*.py" -type f -exec sed -i '1d' {} \;
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/Setzer/
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{uuid}.svg
%{_metainfodir}/%{uuid}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%{python3_sitelib}/%{name}/


%changelog
* Fri Jun 26 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-3
- Fix #1851601

* Fri Jun 26 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-2
- Correcting License from GPLv3 -> GPLv3+

* Sat May 30 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-1
- Updating to 0.2.8

* Tue May 19 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.6-1
- Updating to 0.2.6

* Tue May 05 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.5-1
- Updating to 0.2.5

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-3
- Removing shebangs and changing poppler-glib dependency

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-2
- Adding synctex dependency

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-1
- Initial package
