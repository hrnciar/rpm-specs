%global  commit_date   20200414
%global  commit_short  bfa3fe3
%global  commit_long   bfa3fe30a56419224952f393a19648a6c13dc715

Name:       gnome-shell-extension-topicons-plus
Summary:    Move all legacy tray icons to the top panel
Version:    27
#Release:    8%%{?dist}.%%{commit_date}.%%{commit_short}
Release:    2%{?dist}
URL:        https://extensions.gnome.org/extension/1031/topicons/
License:    GPLv2
BuildArch:  noarch

# There haven't been any *tagged* releases in a long time, but this is where they would be:
# https://github.com/phocean/TopIcons-plus/releases
#Source0: https://github.com/phocean/TopIcons-plus/archive/%%{commit_short}/TopIcons-plus-%%{commit_short}.tar.gz
Source0: https://github.com/phocean/TopIcons-plus/archive/%{version}/TopIcons-plus-%{version}.tar.gz

BuildRequires: glib2

Requires: gnome-shell >= 3.34
Requires: gnome-shell-extension-common

Recommends: gnome-tweaks
Recommends: %{_bindir}/gnome-shell-extension-prefs



%description
Many applications, such as chat clients, downloaders, and some media
players, are meant to run long-term in the background even after you
close their window.  These applications remain accessible by adding an
icon to the GNOME Shell Legacy Tray. However, the Legacy Tray is hidden
until you push your mouse into the lower-left of the screen and click on
the small tab that appears. TopIcons Plus brings all icons back to the
top panel, so that it's easier to keep track of apps running in the
background. You also get some options to control the look and feel: You
can leave the icons in full color, or dynamically convert them to
grayscale, etc.



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  TopIcons@phocean.net
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
# %%autosetup -n TopIcons-plus-%%{commit_long}
%autosetup -n TopIcons-plus-%{version}

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
TopIcons Plus before it will take effect. You can do so a few different
ways.

First, restart GNOME Shell (Open the command dialog with Alt-F2, type
\`r\`, and hit enter), or log out and log back in. Then:

- If you've already set up the GNOME Shell web browser plugin, go to
  <https://extensions.gnome.org/local/>, find the extension, and click
  the switch to "ON."
- Open GNOME Tweaks, go to the Extensions tab, find the extension,
  and click the switch to "ON."
- Open a terminal or the desktop's command dialog, and (as your normal
  user account) run:
  \`gnome-extensions enable %{UUID}\`
EOF



%build
# `build` make target is included in `make install`.



%install
%make_install  INSTALL_PATH=%{buildroot}/%{gnome_extensions_dir}

rm %{final_install_dir}/locale/*/LC_MESSAGES/*.po
mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/
%find_lang TopIcons-Plus

# README also gets copied to the standard documentation directory, so we don't
# need it here.
rm  %{final_install_dir}/README.md

# RPM will take care of gschemas, so we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.topicons.gschema.xml  \
	%{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{final_install_dir}/schemas/



%files -f TopIcons-Plus.lang
%doc README.md  README-fedora.md
%license gpl-2.0.txt
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.topicons.gschema.xml



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 01 2020 Andrew Toskin <andrew@tosk.in> - 27-1
- Bump to upstream version 27.

* Wed Apr 15 2020 Andrew Toskin <andrew@tosk.in> - 22-8.20200414.bfa3fe3
- Merge upstream patches by Jean-Christophe Baptiste and vancez.
  Improves cross-platform builds and fixes oversized icons.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22-7.20191031.0a35713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 4 2019 Andrew Toskin <andrew@tosk.in> - 22-6.20191031.0a35713
- Merge changes by Robin A Meade, which brings better compatibility to
  GNOME both before *and* after v3.33.90.

* Mon Oct 14 2019 Andrew Toskin <andrew@tosk.in> - 22-5.20190929.ad2dd1a
- Patches from Hans de Goede were merged upstream.
- Added Dutch translations.
