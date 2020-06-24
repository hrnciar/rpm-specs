Name:               studio-controls
Version:            1.99.1
Release:            1%{?dist}
Summary:            Studio control for audio devices
BuildArch:          noarch


# The entire source code is GPLv2+

License:            GPLv2+
URL:                https://launchpad.net/ubuntustudio-controls
Source:             https://github.com/ovenwerks/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:      desktop-file-utils
BuildRequires:      systemd-rpm-macros
Requires:           jack-audio-connection-kit
Requires:           jack-audio-connection-kit-dbus
Requires:           jack-audio-connection-kit-example-clients
Requires:           a2jmidid
Requires:           dbus-tools
Requires:           psmisc
Requires:           pulseaudio-utils
Requires:           pulseaudio-module-jack
Requires:           python3-dbus
Requires:           python3-gobject
Requires:           python3
Requires:           python-jack-client
Requires:           zita-ajbridge
Requires:           qasmixer
Requires:           pavucontrol
Requires:           hicolor-icon-theme
Requires:           shared-mime-info
Requires:           kernel-tools
Requires:           polkit
Recommends:         Carla

%description
Studio Controls is a small application that enables/disables realtime privilege
for users and controls jackdbus. It allows Jackdbus to be run from session
start. It also will detect USB audio devices getting plugged in after session
start and optionally connect them to jackdbus as a client or switch them in as
jackdbus master.

%prep
%autosetup -p 1 -n studio-controls-%{version}

%build
#Intentionally blank

%install
cp -r usr %{buildroot} --preserve=mode,timestamps
cp -r lib/systemd %{buildroot}/usr/lib --preserve=mode,timestamps
rm -rf %{buildroot}/usr/lib/systemd/system/ondemand.service.d

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_post studio-system.service
%systemd_user_post studio.service

%preun
%systemd_preun studio-system.service
%systemd_user_preun studio.service

%postun
%systemd_postun_with_restart studio-system.service

%files
%doc AUTHORS
%doc README
%doc ROADMAP
%license COPYING
%{_bindir}/autojack
%{_bindir}/studio-controls
%{_sbindir}/studio-system
%{_prefix}/lib/systemd/studio
%{_unitdir}/studio-system.service
%exclude %{_userunitdir}/session-monitor.service
%{_userunitdir}/studio.service
%dir %{_userunitdir}/default.target.wants/
%{_userunitdir}/default.target.wants/studio.service
%exclude %{_userunitdir}/indicator-messages.service.wants/session-monitor.service
%{_datadir}/applications/studio-controls.desktop
%{_datadir}/studio-controls/
%{_datadir}/icons/hicolor/*/apps/studio-controls.*
%{_datadir}/man/man1/studio-controls.1.gz
%{_datadir}/man/man2/autojack.2.gz
%{_datadir}/man/man2/studio-system.2.gz
%{_datadir}/polkit-1/actions/com.studiocontrols.pkexec.studio-controls.policy

%changelog
* Sun May 10 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.1-1
- New version 1.99.1, removes tablet interface code for now

* Thu May 07 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.0-1
- New version 1.99.0, removes Ubuntu branding from icon

* Tue May 05 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.5-1
- New version 1.12.5

* Sun Apr 12 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.4-1
- New verison 1.12.4

* Wed Mar 04 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-3
- Remove ondemand.service files, add studio-system.service system file

* Wed Mar 04 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-2
- Add missing systemd files

* Mon Mar 02 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-1
- Fix symbolic links (actually add them)

* Sun Mar 01 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.2-1
- Temporarily remove unused tablet configuration gui for wacom

* Sun Feb 23 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.1-1
- Fix for bad adduser call (should be usermod)

* Sat Feb 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12-1
- Initial release for Fedora
