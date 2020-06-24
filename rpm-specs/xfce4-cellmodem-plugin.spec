# Review: https://bugzilla.redhat.com/show_bug.cgi?id=499279

%global _hardened_build 1
%global majorversion 0.0
%global panelversion 4.12

Name:           xfce4-cellmodem-plugin
Version:        0.0.5
Release:        27%{?dist}
Summary:        Cell Modem monitor plugin for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{majorversion}/%{name}-%{version}.tar.gz
# fixes path of the desktop file for xfce4-panel 4.7
# Port over to libxfce4ui
Patch1:         xfce4-cellmodem-plugin-0.0.5-port-to-libxfce4ui.patch

# From Xfce: Fix crash on removing the plugin from the panel
# Fedora bug:   https://bugzilla.redhat.com/show_bug.cgi?id=874042
# Upstream bug: https://bugzilla.xfce.org/show_bug.cgi?id=6747
Patch2:         xfce4-cellmodem-plugin-0.0.5-fix-callback-prototype.patch

BuildRequires:  xfce4-panel-devel >= 4.3.22, libxfce4ui-devel >= 4.4.0
BuildRequires:  libusb-devel
BuildRequires:  gettext, intltool
BuildRequires:  libtool, xfce4-dev-tools
Requires:       xfce4-panel >= %{panelversion}
 
%description
The cellmodem plugin is a monitoring plugin for cellular modems. It reports 
provider and signal quality for GPRS/UMTS(3G)/HSDPA(3.5G) modem cards. It 
works with (mostly) all cards which support an out-of-band channel for 
monitoring purposes. Current features include:
* Display the current network type (GPRS/UMTS)
* Display the current signal level
* Configure the maximum signal level
* Configure the low and critical signal level
* Asking for PIN if modem needs it
* Quick visual feedback on modem and registration status via LEDs


%prep
%autosetup -p1

# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=xfce-mouse|Icon=phone|g' panel-plugin/cellmodem.desktop.in.in


%build
# Xfce has its own autotools-running-script thingy, if you use autoreconf
# it'll fall apart horribly
xdt-autogen

%configure --disable-static
%make_build


%install
%make_install
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_libexecdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.0.5-23
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Kevin Fenzi <kevin@scrye.com> 0.0.5-16
- Add patch porting to libxfceui4

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.0.5-15
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.5-11
- Fix crash on removing the plugin from the panel (#874042)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.0.5-9
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.0.5-8
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.5-6
- Rebuild for new libpng

* Fri Apr 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.5-5
- Fix icon in 'Add new panel item' dialog (#694903)
- Fix Source0 URL
- Update translations from Xfce Transifex

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 0.0.5-3
- 01_typo-linking.patch: fix a typo (from Debian)
- 02_explicit-linking-to-libxfcegui4.patch: fix linking (from Debian)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.5-1
- Initial Fedora package
