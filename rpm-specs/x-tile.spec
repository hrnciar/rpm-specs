Name:           x-tile
Version:        3.2
Release:        1%{?dist}
Summary:        A GTK application to tile windows in different ways

License:        GPLv2+
URL:            https://www.giuspen.com/x-tile/
Source0:        https://github.com/giuspen/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
Requires:       %{py3_dist pygobject}
Requires:       %{py3_dist pycairo}
Requires:       gtk3
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
X-tile is an application that allows you to select a number of windows and tile
them in different ways.  X-tile works on any X desktop (GNOME, KDE, XFCE,
LXDE...).
The main features are: many tiling geometries, undo tiling, invert tiling order,
optional system tray docking and menu, filter to avoid listing some windows,
filter to check some windows by default, command line interface.


%prep
%autosetup

# Remove bundled egg-info
rm -rf *.egg-info


%build
mkdir -p build/scripts-%{python3_version}/
%py3_build


%install
%py3_install
install -Dpm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%license license
%{_bindir}/%{name}
%{python3_sitelib}/X_Tile-*.egg-info
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*


%changelog
* Mon Sep 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2-1
- Update to 3.2

* Mon Aug 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1-1
- Initial RPM release, from previously retired package (with contribution of
  Vlastimil Holer)
