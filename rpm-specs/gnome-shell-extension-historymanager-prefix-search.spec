%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  UUID                  historymanager-prefix-search@sustmidown.centrum.cz
%global  install_destination   %{buildroot}/%{gnome_extensions_dir}/%{UUID}

Name:       gnome-shell-extension-historymanager-prefix-search
Summary:    Use PageUp and PageDown to search for previous GNOME Shell commands
Version:    12
Release:    5%{?dist}
URL:        https://github.com/sustmi/gnome-shell-extension-historymanager-prefix-search
License:    GPLv3+
BuildArch:  noarch

# See the latest releases here:
# https://github.com/sustmi/gnome-shell-extension-historymanager-prefix-search/releases
Source0: https://github.com/sustmi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: glib2

Requires: gnome-shell >= 3.8
Requires: gnome-shell-extension-common

# (CentOS 7 build environment doesn't have new enough version of RPM to support Recommends tag.)
%if 0%{?fedora}  ||  0%{?rhel} >= 8
Recommends: ( gnome-tweaks  or  gnome-tweak-tool )
Recommends: %{_bindir}/gnome-shell-extension-prefs
%endif

Obsoletes: gnome-shell-extension-sustmi-historymanager-prefix-search <= 3.0-17



%description
The GNOME Shell Run Command dialog (Alt-F2) and Looking Glass let you
cycle through the history of previous commands with the arrow keys, but
there's currently no built-in way to search or do autocompletion for
commands. With HistoryManager Prefix Search, you can type the beginning
of a command, and then hit the PageUp and PageDown keys to cycle through
previous commands which match the prefix you typed.



%prep
%autosetup

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
HistoryManager Prefix Search before it will take effect. You can do so a
few different ways.

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
cp --recursive --preserve=mode,timestamps  ./*  %{install_destination}/
# Remove duplicate copies of license and README.
rm  %{install_destination}/README.md  %{install_destination}/COPYING
# Makefile is only used in upstream's builds for the GNOME Extensions website.
rm %{install_destination}/Makefile

# RPM will take care of gschemas, we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{install_destination}/schemas/org.gnome.shell.extensions.historymanager-prefix-search.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{install_destination}/schemas/

# Localizations.
for file in $( ls ./po/*.po ); do
    locale=$( basename $file .po )
    mkdir -p  %{buildroot}/%{_datadir}/locale/$locale/LC_MESSAGES
    msgfmt $file  --output-file %{buildroot}/%{_datadir}/locale/$locale/LC_MESSAGES/historymanager-prefix-search.mo
done
rm --recursive  %{install_destination}/po/  %{install_destination}/locale/
%find_lang historymanager-prefix-search



%files -f historymanager-prefix-search.lang
%license COPYING
%doc README.md  README-fedora.md
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.historymanager-prefix-search.gschema.xml





%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Andrew Toskin <andrew@tosk.in> - 12-4
- Add explicit Recommend for GNOME Shell Extensions preferences tool.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Andrew Toskin <andrew@tosk.in> - 12-1
- Bump to upstream version 12, which adds an option to change the key
  bindings.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Andrew Toskin <andrew@tosk.in> - 11-1
- Bump to upstream version 11, which fixes a bug that could multiply
  user keypresses.
