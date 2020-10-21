%global altname optimus-indicator

Name:           mate-optimus
Version:        20.04.0
Release:        2%{?dist}
Summary:        NVIDIA Optimus GPU switcher

License:        GPLv3+
URL:            https://github.com/ubuntu-mate/mate-optimus
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       glew
Requires:       hicolor-icon-theme
Requires:       libappindicator-gtk3
Requires:       libnotify
Requires:       python3-gobject
Requires:       python3-setproctitle

# For Fedora Workstation (GNOME)
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)

# Not available in official Fedora repos
#Recommends:     xorg-x11-drv-nvidia >= 435.17

%description
This applet provides means to display the active GPU and lets you switch between
the Intel and Nvidia GPUs on NVIDIA Optimus equipped computers.

Requires at least:

  NVIDIA 435.17 (beta driver release) and now the 435.21 (stable driver).

How to run:

  $ %{name}-applet


%prep
%autosetup -p1
sed -i 's!/usr/bin/env python3!%{__python3}!' usr/bin/%{name}-applet


%install
install -Dpm0644 etc/xdg/autostart/%{name}.desktop          %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm0644 etc/xdg/autostart/%{name}.desktop          %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
install -Dpm0644 usr/share/pixmaps/%{altname}-intel.svg     %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{altname}-intel.svg
install -Dpm0644 usr/share/pixmaps/%{altname}-nvidia.svg    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{altname}-nvidia.svg
install -Dpm0644 usr/share/pixmaps/%{altname}-unknown.svg   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{altname}-unknown.svg
install -Dpm0755 usr/bin/%{name}-applet                     %{buildroot}%{_bindir}/%{name}-applet
ln -s %{name}-applet                                        %{buildroot}%{_bindir}/offload-glx
ln -s %{name}-applet                                        %{buildroot}%{_bindir}/offload-vulkan


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING.txt
%doc README.md
%{_bindir}/%{name}-applet
%{_bindir}/offload-glx
%{_bindir}/offload-vulkan
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_sysconfdir}/xdg/autostart/*.desktop


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.0-1
- Update to 20.04.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.4-1
- Update to 19.10.4

* Sun Sep 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.3-4
- Update to 19.10.3

* Sat Sep 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.2-7
- Initial package
- Thanks to Vitaly Zaitsev <vitaly@easycoding.org> for help with packaging and review
