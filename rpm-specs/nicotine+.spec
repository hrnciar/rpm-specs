%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine

Name:           nicotine+
Version:        2.1.2
Release:        1%{?dist}
Summary:        A graphical client for Soulseek

# - IP2Location Country Database (pynicotine/geoip/ipcountrydb.bin) is CC-BY-SA
#   (see pynicotine/geoip/README.md)
# - some icons are LPGPLv3+, GPLv3+ and MIT (see img/CREDITS.md)
License:        GPLv3+ and CC-BY-SA and LGPLv3+ and MIT
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytaglib}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
Requires:       %{py3_dist dbus-python}
Requires:       %{py3_dist miniupnpc}
Requires:       %{py3_dist pygobject}
Requires:       %{py3_dist pytaglib}
Requires:       gobject-introspection
Requires:       gspell
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       libnotify
Requires:       xdg-utils
BuildArch:      noarch

%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.


%prep
%autosetup -n nicotine-plus-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install

# Remove installed documentation/license files. Useful ones are installed using
# %%doc/%%license
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{altname}/
rm $RPM_BUILD_ROOT%{python3_sitelib}/pynicotine/*/README.md

%find_lang %{altname}


%check
# Tests requiring an Internet connection are disabled
%pytest --deselect=test/unit/test_version.py

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{appdata_id}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appdata_id}.appdata.xml


%files -f %{altname}.lang
%doc AUTHORS.md NEWS.md README.md TRANSLATORS.md
%license COPYING img/CREDITS.md pynicotine/geoip/README.md
%{_bindir}/%{altname}
%{python3_sitelib}/pynicotine/
%{python3_sitelib}/%{altname}-*.egg-info
%{_datadir}/applications/%{appdata_id}.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_metainfodir}/%{appdata_id}.appdata.xml
%{_mandir}/man1/%{altname}.1.*


%changelog
* Tue Oct 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Sun Sep 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Update License tag

* Sat Sep 12 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.1-1
- Initial RPM release
