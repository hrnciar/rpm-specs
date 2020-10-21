Name:       gnome-shell-extension-do-not-disturb-button
Summary:    Hide desktop notifications until you're ready to look at them
Version:    39
Release:    2%{?dist}
URL:        https://extensions.gnome.org/extension/964/do-not-disturb-button/
License:    GPLv2
BuildArch:  noarch

# Norman L. Smith tracks a few different Shell extensions in the same GitHub
# repo, and does not tag commits for releases of any of them. So, see the latest
# source release of Do Not Disturb Button, with changelog, here:
# https://nls1729.github.io/DNDlatestupdate_332.html
Source0: https://extensions.gnome.org/extension-data/donotdisturb-buttonnls1729.v%{version}.shell-extension.zip

BuildRequires: glib2

Requires: gnome-shell >= 3.36
Requires: gnome-shell-extension-common

Recommends: gnome-tweaks
Recommends: %{_bindir}/gnome-shell-extension-prefs



%description
Do Not Disturb Button provides a panel button to temporarily hide
incoming notifications in GNOME Shell. A count of notifications appears
next to the panel button, and notifications remain hidden in the
notifications message tray, until you choose to show and dismiss
them. You can also assign a keyboard shortcut to toggle the Do Not
Disturb status.

(Do Not Disturb Button allows you to set the "available" or "busy"
status for desktop notifications only, not the status of chat or other
applications connected to GNOME's Online Accounts.)



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  donotdisturb-button@nls1729
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
%autosetup -c %{name}-%{version}

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
Do Not Disturb Button before it will take effect. You can do so a few
different ways.

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
# No compiling necessary.



%install
mkdir -p %{final_install_dir}
cp --recursive --preserve=mode,timestamps  ./*  %{final_install_dir}

# COPYING and README also get copied to standard documentation and license
# locations, so we don't need them here.
rm  %{final_install_dir}/COPYING  %{final_install_dir}/README.txt

# RPM will take care of gschemas, we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.donotdisturb-button.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{final_install_dir}/schemas/

mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/
%find_lang donotdisturb-button-extension



%files -f donotdisturb-button-extension.lang
%doc README.txt  README-fedora.md
%license COPYING
# Make gdm owner of the main extension files. Do Not Disturb Button
# modifies itself to suit the environment, so setting gdm as the owner
# allows this to work without requiring world-writable permissions.
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.donotdisturb-button.gschema.xml



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Andrew Toskin <andrew@tosk.in> - 39-1
- Bump to upstream version 39, which fixes a bug causing preferences not
  to appear at least on some distributions.

* Wed Apr 15 2020 Andrew Toskin <andrew@tosk.in> - 38-1
- Bump to upstream version 38, which changes how it launches the
  settings dialog.

* Tue Mar 31 2020 Andrew Toskin <andrew@tosk.in> - 36-1
- Bump to upstream version 36, which now requires GNOME 3.36+, and
  redesigns the preferences dialog.

* Thu Mar 19 2020 Andrew Toskin <andrew@tosk.in> - 35-1
- Bump to upstream version 35, which fixes minor bugs creating junk log
  messages.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
