Name:       gnome-shell-extension-activities-configurator
Summary:    Configure the top bar and Activities button in GNOME Shell
URL:        https://extensions.gnome.org/extension/358/activities-configurator/
Version:    85
Release:    1%{?dist}
License:    GPLv2
BuildArch:  noarch

# You can see the latest source releases here:
# https://nls1729.github.io/activities_config_zip.html
# With the changelog here:
# https://nls1729.github.io/latestupdate.html
Source0: https://extensions.gnome.org/extension-data/activities-confignls1729.v%{version}.shell-extension.zip
Source1: ./README.md

BuildRequires: glib2

Requires: gnome-shell >= 3.36
Requires: gnome-shell-extension-common

Recommends: gnome-tweaks
Recommends: %{_bindir}/gnome-shell-extension-prefs



%description
Activities Configurator gives you all sorts of options to control the
look and feel of the top bar and Activities button in GNOME Shell,
possibly even overriding your current Shell theme. You can change or
remove the Activities button text, add an icon, move it to right corner,
change the top bar's background color and transparency... You can toggle
the Overview if no applications are running (at login and whenever the
last application window is closed). You can also adjust the "pressure"
threshold for the hot corner, or disable it altogether.



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  activities-config@nls1729
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
%autosetup -c %{name}-%{version}

%build
# No compilation necessary.

%install
mkdir -p %{final_install_dir}
cp --recursive --preserve=mode,timestamps  ./*  %{final_install_dir}
cp --recursive --preserve=mode,timestamps  %{SOURCE1}  ./README-fedora.md

# License and README get copied to system directories for docs and license.
rm  %{final_install_dir}/COPYING  %{final_install_dir}/README.txt

# RPM will take care of gschemas, we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.activities-config.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{final_install_dir}/schemas/

mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/
%find_lang activities-config-extension



%files -f activities-config-extension.lang
%doc README.txt  README-fedora.md
%license COPYING
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.activities-config.gschema.xml



%changelog
* Tue Jun 16 2020 Andrew Toskin <andrew@tosk.in> - 85-1
- Bump to upstream version 85, which fixes a cosmetic bug on the lock
  screen.

* Tue Mar 31 2020 Andrew Toskin <andrew@tosk.in> - 84-1
- Bump to upstream version 84, which fixes remaining compatibility
  issues on GNOME 3.36.

* Fri Mar 27 2020 Andrew Toskin <andrew@tosk.in> - 80-1
- Bump to upstream version 80, which fixes support for GNOME 3.36.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Andrew Toskin <andrew@tosk.in> - 78-1
- Bump to upstream version 78, which fixes support in GNOME 3.34.

* Tue Nov 05 2019 Andrew Toskin <andrew@tosk.in> - 77-1
- Bump to upstream version 77, which adds a fix for changed APIs around
  the hot corner.
