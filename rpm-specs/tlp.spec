%global gittag 1.3.1
Name:           tlp
Version:        1.3.1
Release:        2%{?dist}
Summary:        Advanced power management tool for Linux
License:        GPLv2+
URL:            http://linrunner.de/en/tlp/tlp.html
Source0:        https://github.com/linrunner/TLP/archive/%{gittag}.tar.gz#/%{name}-%{gittag}.tar.gz
#Provided by Andreas Roederer <tlp~at~warpnine~dot~de>:
Source1:        50-tlp.preset

BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  libappstream-glib

#The following requires are not detected:
Requires:       ethtool
Requires:       hdparm
Requires:       iw
Requires:       redhat-lsb-core
Requires:       rfkill
Requires:       systemd
Requires:       udev
Requires:       usbutils
Requires:       pciutils
Recommends:     kernel-tools

#Note: Conflicts with laptop-mode-tools
#Makes sure laptop_mode isn't being used:
Conflicts:      %{_sbindir}/laptop_mode
BuildArch:      noarch

%description
TLP is an advanced power management tool for Linux. It comes with a
default configuration already optimized for battery life. At the same
time it is highly customizable to fulfill specific user requirements.

TLP supplies separate settings profiles for AC and battery power and can
enable or disable Bluetooth, WiFi and WWAN radio devices upon system start-up.

For ThinkPads it provides a unified way to configure charging thresholds and
re-calibrate the battery for all models which support it (via tp-smapi or
acpi-call).

TLP is a pure command line tool with automated background tasks, it
does not contain a GUI.

%package rdw
Summary:        Radio Device Wizard for TLP
Requires:       NetworkManager >= 1.20
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of:
 - Bluetooth, WiFi, WWAN radio devices
 - upon network connect/disconnect
 - and dock/undock

%prep
%autosetup -n TLP-%{gittag}

%build
%make_build

%install
%make_install \
  TLP_SDSL=%{_unitdir}/../system-sleep \
  TLP_NMDSP=%{_prefix}/lib/NetworkManager/dispatcher.d \
  TLP_NO_INIT=1 \
  TLP_WITH_ELOGIND=0 \
  TLP_SYSD=%{_unitdir} \
  TLP_ULIB=%{_udevrulesdir}/..
#Install manpages:
make install-man DESTDIR=%{buildroot}
make install-man-rdw DESTDIR=%{buildroot}
#Install preset (source 1):
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_presetdir}/50-tlp.preset

%check
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/*.xml

%files
%config(noreplace) %{_sysconfdir}/tlp.conf
%config(noreplace) %{_sysconfdir}/tlp.d
%license LICENSE
%doc COPYING README.md changelog
%{_bindir}/*
%exclude %{_bindir}/tlp-rdw
%{_sbindir}/*
%{_mandir}/man*/*
%exclude %{_mandir}/man*/tlp-rdw*
%{_datadir}/tlp
%{_udevrulesdir}/85-tlp.rules
%{_udevrulesdir}/../tlp-usb-udev
%{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/bash-completion/completions/tlp-rdw
%{_presetdir}/50-tlp.preset
%{_unitdir}/*.service
%{_unitdir}/../system-sleep
%{_datadir}/metainfo/*.metainfo.xml
%{_sharedstatedir}/tlp

%files rdw
%doc COPYING README.md changelog
%{_bindir}/tlp-rdw
%{_mandir}/man*/tlp-rdw*
%{_prefix}/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%{_udevrulesdir}/85-tlp-rdw.rules
%{_udevrulesdir}/../tlp-rdw-udev
%{_datadir}/bash-completion/completions/tlp-rdw

%post
%systemd_post tlp.service
systemctl mask systemd-rfkill.service

%preun
%systemd_preun tlp.service

%postun
%systemd_postun_with_restart tlp.service
if [ $1 -eq 0 ] ; then
    systemctl unmask systemd-rfkill.service
fi

%post rdw
/bin/systemctl enable NetworkManager-dispatcher.service >/dev/null 2>&1 || :

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 6 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.3.1-1
- Update to 1.3.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.3.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.3.0-0.2.beta.3
- Drop sleep service scriptlets, as they were dropped in 1.3.0

* Fri Jan 17 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.3.0-0.1.beta.3
- Update to 1.3.0 beta 3

* Fri Jan 3 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.2-4
- Fix suspend issue, missing var directory creation

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.2.2-3
- Move the NetworkManager dispatcher script out of /etc

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.2-1
- Update to 1.2.2

* Mon Mar 18 2019 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.1-1
- Update to 1.2.1
- Modernize SPEC file

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-1
- Update to 1.1
- Add weak require for kernel-tools

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 03 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0-3
- Remove kernel-tools require, fixes s390x

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0-1
- Update to 1.0

* Mon Mar 20 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-5
- Cherry-pick upstream fix for mitigate slow shutdown

* Thu Mar 02 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-4
- Cherry-pick upstream fix for tlp-stat

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-2
- Fix rfkill service masking

* Sun Aug 28 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-1
- Update to 0.9

* Wed Feb 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 0.8-3
- Fix rpmlint warnings/errors

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.8-1
- Update to 0.8

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-4
- Use workaround to avoid conflict with systemd

* Mon May 11 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-3
- Fix rfkill conflict

* Tue Feb 3 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-2
- Fix a typo in the spec file

* Sat Jan 31 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-1
- New Version

* Mon Nov 17 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-3
- Wireless-tools removed as a dependency

* Tue Nov 04 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-2
- Missing Dependancy

* Mon Oct 27 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-1
- New Upstream Version

* Mon Apr 21 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.5-2
- Various tweaking
- Move bashcompletion file to silence rpmlint warning

* Sun Apr 20 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.5-1
- Initial fedora package
