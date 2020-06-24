%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  UUID                  windowoverlay-icons@sustmidown.centrum.cz
%global  install_destination   %{buildroot}/%{gnome_extensions_dir}/%{UUID}

Name:       gnome-shell-extension-windowoverlay-icons
Summary:    Show app icons on top of the windows thumbnails in Activities Overview
Version:    34
Release:    4%{?dist}
URL:        https://github.com/sustmi/gnome-shell-extension-windowoverlay-icons
License:    GPLv3+
BuildArch:  noarch

# You can see the latest releases here:
# https://github.com/sustmi/gnome-shell-extension-windowoverlay-icons/releases
Source0: https://github.com/sustmi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: ./README.md

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



%build
# Nothing to build.



%install
mkdir -p %{install_destination}
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
cp --recursive --preserve=mode,timestamps  ./*  %{install_destination}/
cp --recursive --preserve=mode,timestamps  %{SOURCE1}  ./README-fedora.md

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
* Tue Apr 21 2020 Andrew Toskin <andrew@tosk.in> - 34-4
- Add Recommended packages for EPEL8+.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Andrew Toskin <andrew@tosk.in> - 34-1
- Bump to upstream version 34, which updated to keep up with
  backwards-incompatible changes to the shell API in GNOME 3.32

* Mon Apr 22 2019 Andrew Toskin <andrew@tosk.in> - 33-1
- Bump to upstream version 33, which fixes a minor bug that was throwing
  junk messages into the error logs.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
