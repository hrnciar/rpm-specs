%global srcname session-settings

Name:           pantheon-session-settings
Summary:        Pantheon session configuration files
Version:        32.1
Release:        1%{?dist}
License:        GPLv3

URL:            https://pagure.io/pantheon-fedora/session-settings
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

Requires:       gala
Requires:       gnome-disk-utility
Requires:       gnome-keyring
Requires:       gnome-session
Requires:       gnome-session-xsession
Requires:       gnome-settings-daemon
Requires:       orca
Requires:       pantheon-agent-geoclue2
Requires:       pantheon-agent-polkit
Requires:       plank
Requires:       xdg-user-dirs-gtk
Requires:       wingpanel

# experimental wayland session is not provided anymore
Obsoletes:      %{name}-wayland < 0.9.90-3

# cerbere is obsolete and retired on fedora 32+
Obsoletes:      cerbere < 2.5.0-5


%description
Configuration files for the Pantheon desktop session.


%package        overrides
Summary:        Pantheon session default settings overrides

Requires:       %{name} = %{version}-%{release}

Requires:       elementary-icon-theme
Requires:       elementary-sound-theme
Requires:       elementary-theme
Requires:       open-sans-fonts

%description    overrides
Configuration files for the Pantheon desktop session.

This subpackage contains system-wide overrides for Pantheon-specific
default settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%install
# Copy / create autostart entries for the Pantheon session
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp -p autostart/* %{buildroot}/%{_sysconfdir}/xdg/autostart/

# Copy Pantheon gnome-session configuration files
mkdir -p %{buildroot}/%{_datadir}/gnome-session/sessions
cp -p gnome-session/* %{buildroot}/%{_datadir}/gnome-session/sessions/

# Copy list of default application overrides for Pantheon
mkdir -p %{buildroot}/%{_datadir}/applications
cp -p applications/pantheon-mimeapps.list %{buildroot}/%{_datadir}/applications

# Copy Pantheon xsession configuration file
mkdir -p %{buildroot}/%{_datadir}/xsessions
cp -p xsessions/pantheon.desktop %{buildroot}/%{_datadir}/xsessions/

# Copy Overrides schema to appropriate location
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas
cp -p overrides/20-io.elementary.desktop.gschema.override %{buildroot}/%{_datadir}/glib-2.0/schemas/

# Install accountsservice extension files
mkdir -p %{buildroot}/%{_datadir}/dbus-1/interfaces
cp -p accountsservice/io.elementary.pantheon.AccountsService.xml \
    %{buildroot}/%{_datadir}/dbus-1/interfaces/

mkdir -p %{buildroot}/%{_datadir}/polkit-1/actions
cp -p accountsservice/io.elementary.pantheon.AccountsService.policy \
    %{buildroot}/%{_datadir}/polkit-1/actions/

mkdir -p %{buildroot}/%{_datadir}/accountsservice/interfaces
ln -s %{_datadir}/dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml \
    %{buildroot}/%{_datadir}/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml


# These scriptlets are needed because .override files don't trigger the schema recompilation
%postun    overrides
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans overrides
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/*.desktop

%{_datadir}/applications/pantheon-mimeapps.list
%{_datadir}/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml
%{_datadir}/dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml
%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/polkit-1/actions/io.elementary.pantheon.AccountsService.policy
%{_datadir}/xsessions/pantheon.desktop

%files overrides
%{_datadir}/glib-2.0/schemas/20-io.elementary.desktop.gschema.override


%changelog
* Thu Apr 30 2020 Fabio Valentini <decathorpe@gmail.com> - 32.1-1
- Update to version 32.1.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 32.0-1
- Update to version 32.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 31.0-2
- Include missing Requires: gnome-disk-utility.

* Mon Oct 28 2019 Fabio Valentini <decathorpe@gmail.com> - 31.0-1
- Update to version 31.0.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 30.92-1
- Update to version 30.92.

* Wed Sep 04 2019 Fabio Valentini <decathorpe@gmail.com> - 30.91-1
- Update to version 30.91.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 30.90-1
- Update to version 30.90.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Fabio Valentini <decathorpe@gmail.com> - 30.1-1
- Update to version 30.1.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 30.0-1
- Update to version 30.0.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 29.90-1
- Update to version 29.90.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 29.0-1
- Update to version 29.0.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 28.92-1
- Update to version 28.92.

* Tue Aug 07 2018 Fabio Valentini <decathorpe@gmail.com> - 28.91-1
- Update to version 28.91.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 28.90-1
- Update to version 28.90.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 28.1-2
- Add Requires on Pantheon polkit and geoclue 2 agents.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 28.1-1
- Update to version 28.1.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 28.0-1
- Update to version 28.0.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 27.90-1
- Update to version 27.90.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 27.0-1
- Update to version 27.0.

* Tue Aug 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.91-1
- Update to version 0.9.91.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.90-1
- Update to version 0.9.90.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.2-1
- Update to version 0.9.2.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com>
- Fix License tag to match upstream license.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.1-1
- Update to version 0.9.1.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9-1
- Initial package.

