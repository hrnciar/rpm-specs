Name:       gnome-shell-extension-freon
Summary:    GNOME Shell extension to display system temperature, voltage, and fan speed
Epoch:      2
Version:    43
Release:    1%{?dist}
URL:        https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki
License:    GPLv2
BuildArch:  noarch

# You can see the latest source releases here:
# https://github.com/UshakovVasilii/gnome-shell-extension-freon/releases
Source0: https://github.com/UshakovVasilii/%{name}/archive/EGO-%{version}/%{name}-EGO-%{version}.tar.gz

BuildRequires: glib2

# Dependencies described here:
# https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki/Dependency
Requires: gnome-shell >= 3.36
Requires: gnome-shell-extension-common
Requires: lm_sensors

Recommends: gnome-tweaks
Recommends: ( %{_bindir}/gnome-shell-extension-prefs  or  gnome-extensions-app )
Recommends: nvme-cli
Recommends: ( udisks2  or  smartmontools  or ( nc and hddtemp ))


%description
Freon is a GNOME Shell extension for displaying the temperature of your
CPU, hard disk, solid state, and video card (NVIDIA, Catalyst, and
Bumblebee supported), as well as power supply voltage, and fan
speed. You can choose which HDD/SSD or other devices to include, what
temperature units to use, and how often to refresh the sensors readout,
and they will appear in the GNOME Shell top bar.

**NOTE** that if you want to see GPU temperature, you will need to
install the vendor's driver and any related packages. (Nouveau
unfortunately won't work for Nvidia cards.)

* hard drive temperatures requires udisks2, or smartmontools, or both
  hddtemp and GNU netcat. (udisks2 should already be installed by
  default on Fedora Workstation, but if you want to use hddtemp instead,
  you will need to install it and netcat yourself, and enable the
  hddtemp daemon.)
* Nvidia GPU temperatures require the `nvidia-settings` application,
  typically installed with the proprietary Nvidia drivers.
* Bumblebee + Nvidia requires `optirun`.
* AMD GPU temperatures requires `aticonfig`, part of AMD Radeon Software
  (formerly known as AMD Catalyst).



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  freon@UshakovVasilii_Github.yahoo.com
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
%autosetup -n %{name}-EGO-%{version}

cat > ./README-fedora.md << EOF
**NOTE** that if you want to see GPU temperature, you will need to
install the vendor's official driver and any related packages. (Nouveau
unfortunately won't work for Nvidia cards.)

- hard drive temperatures requires udisks2, or smartmontools, or both
  hddtemp and GNU netcat. (udisks2 should already be installed by
  default on Fedora Workstation, but if you want to use hddtemp instead,
  you will need to install it and netcat yourself, and enable the
  hddtemp daemon.)
- Nvidia GPU temperatures require the `nvidia-settings` application,
  typically installed with the proprietary Nvidia drivers
- AMD GPU temperatures requires `aticonfig`, part of AMD Radeon Software
  (formerly known as AMD Catalyst)
- Bumblebee + Nvidia requires `optirun`

You can read more about this and other tips
**on the Freon [wiki](https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki)**.

Also, after installing this GNOME Shell extension, each user that wants
it must still manually enable Freon before it will take effect. You can
do so a few different ways.

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
# No compilation necessary.



%install
mkdir -p %{final_install_dir}
cp --recursive --preserve=mode,timestamps  %{UUID}/*  %{final_install_dir}

# RPM will take care of gschemas, but they should be installed to system-wide directory.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.sensors.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rmdir %{final_install_dir}/schemas/

# Remove source .po localization files, move binary .mo to system directory.
rm --recursive %{final_install_dir}/po/
mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/

%find_lang freon



%files -f freon.lang
%doc README.md  README-fedora.md
%license LICENSE
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.sensors.gschema.xml



%changelog
* Fri Oct 16 2020 Andrew Toskin <andrew@tosk.in> - 2:43-1
- Bump to upstream version 43, which fixes support for GNOME 3.38.

* Tue Oct 06 2020 Andrew Toskin <andrew@tosk.in> - 2:42-1
- Bump to upstream version 42, which updates some translations, icons,
  and how average temperatures are calculated.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Andrew Toskin <andrew@tosk.in> - 2:40-1
- Bump to upstream version 40, which adjusts to keep up with GNOME API
  changes, and adds Italian and Hungarian translations.

* Tue Mar 31 2020 Andrew Toskin <andrew@tosk.in> - 2:39-4
- Add explicit Recommend for the gnome-shell-extension-prefs tool.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
