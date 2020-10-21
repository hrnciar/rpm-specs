%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  UUID                  windowoverlay-icons@sustmidown.centrum.cz
%global  install_destination   %{buildroot}/%{gnome_extensions_dir}/%{UUID}

Name:       gnome-shell-extension-windowoverlay-icons
Summary:    Show app icons on top of the windows thumbnails in Activities Overview
Version:    35
Release:    1%{?dist}
URL:        https://github.com/sustmi/gnome-shell-extension-windowoverlay-icons
License:    GPLv3+
BuildArch:  noarch

# You can see the latest releases here:
# https://github.com/sustmi/gnome-shell-extension-windowoverlay-icons/releases
Source0: https://github.com/sustmi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: glib2

Requires: gnome-shell >= 3.32
Requires: gnome-shell-extension-common

# (CentOS 7 build environment doesn't have new enough version of RPM to support Recommends tag.)
%if 0%{?fedora}  ||  0%{?rhel} >= 8
Recommends: ( gnome-tweaks  or  gnome-tweak-tool )
Recommends: %{_bindir}/gnome-shell-extension-prefs
%endif

Obsoletes: gnome-shell-extension-sustmi-windowoverlay-icons <= 3.0-18



%description
Sometimes when you have many open windows, especially if they all
contain a lot of text, the windows all start to look the same in the
Activities Overview. WindowOverlay Icons adds the application icon to
every window thumbnail, making it easier to tell them apart.



%prep
%autosetup

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
WindowOverlay Icons before it will take effect. You can do so a few
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
# Nothing to build.



%install
mkdir -p %{install_destination}
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
cp --recursive --preserve=mode,timestamps  ./*  %{install_destination}/

# Remove duplicates of README and license.
rm  %{install_destination}/README.md  %{install_destination}/COPYING

# Make file is only used by upstream's packaging for GNOME Shell Extensions website.
rm %{install_destination}/Makefile

# Move gschemas to the system directory.
mv  %{install_destination}/schemas/org.gnome.shell.extensions.windowoverlay-icons.gschema.xml  \
  %{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{install_destination}/schemas/

# Localizations.
for file in $( ls ./po/*.po ); do
    locale=$( basename $file .po )
    mkdir -p  %{buildroot}/%{_datadir}/locale/$locale/LC_MESSAGES
    msgfmt $file  --output-file %{buildroot}/%{_datadir}/locale/$locale/LC_MESSAGES/windowoverlay-icons.mo
done
rm --recursive  %{install_destination}/po/  %{install_destination}/locale/
%find_lang windowoverlay-icons



%if 0%{?rhel} && 0%{?rhel} <= 7
%posttrans
# The latest versions of Fedora compile gschemas automatically, but CentOS 7
# does not.
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas/  &> /dev/null || :
%endif


%files -f windowoverlay-icons.lang
%license COPYING
%doc  README.md  README-fedora.md
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.windowoverlay-icons.gschema.xml



%changelog
* Mon Aug 03 2020 Andrew Toskin <andrew@tosk.in> - 35-1
- Bump to upstream version 35.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Andrew Toskin <andrew@tosk.in> - 34-4
- Add Recommended packages for EPEL8+.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Andrew Toskin <andrew@tosk.in> - 34-1
- Bump to upstream version 34, which updated to keep up with
  backwards-incompatible changes to the shell API in GNOME 3.32
