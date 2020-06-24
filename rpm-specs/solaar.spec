%global forgeurl https://github.com/pwr/Solaar
%global commit 563ef0d8ef45d6d7244a068a745a1788bfcf6a8a
%global date 20200322
#%%global tag 1.0.2

Name:           solaar
Version:        1.0.2
Release:        0.3.rc1%{?dist}
Summary:        Device manager for a wide range of Logitech devices
%forgemeta
URL:            %forgeurl
Source:         %forgesource

# Fedora-specific patch; remove udev-acl tag from upsteam udev rules as it only
# applies to some old version of ubuntu.
Patch1:         patch-udev-rules

BuildArch:      noarch
License:        GPLv2

BuildRequires:  desktop-file-utils python3-devel systemd

Requires:       hicolor-icon-theme
Requires:       python3-gobject python3-pyudev
Requires:       solaar-udev
Recommends:     gtk3

%description
Solaar is a device manager for Logitech's Unifying Receiver peripherals. It is
able to pair/unpair devices to the receiver and, for most devices, read battery
status.

gtk3 is recommended.  Without it, you can run solaar commands to view the
configuration of the devices and pair/unpair peripherals but you cannot use the
graphical interface.


%package doc
Summary:        Developer documentation for Solaar
Requires:       %name = %version-%release
BuildArch:      noarch

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.


%package udev
Summary:        Udev rules for Logitech receivers
BuildArch:      noarch
Obsoletes:      unifying-receiver-udev < 0.2-12
Provides:       unifying-receiver-udev = 0.2-12

%description udev
This package contains udev rules which grant users permission to access various
connected Logitech wireless receivers.  This includes Unifying receivers,
various types of Nano receivers and some other types which can be used by
Solaar.


%prep
%forgeautosetup -p1
rm docs/.gitignore


%build
%py3_build


%install
%py3_install

install -pm755 tools/hidconsole %{buildroot}%{_bindir}

# This just spews a warning; there is no real reason to install it.
rm %buildroot/%_bindir/solaar-cli

# Remove pointless shebangs
sed -i -e '1d' %buildroot/%python3_sitelib/solaar/{gtk,tasks}.py

# Fix shebang line
sed -i -e '1s,^#!.*$,#!/usr/bin/python3,' %buildroot/%_bindir/hidconsole

desktop-file-validate %buildroot/%_datadir/applications/solaar.desktop

install -pm644 -D -t %{buildroot}%{_udevrulesdir} rules.d/42-logitech-unify-permissions.rules


%posttrans udev
# This is needed to apply permissions to existing devices when the package is
# installed.
# Skip triggering udevd when it is note accessible, e.g. containers or
# rpm-ostree-based systems.
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=hidraw --action=add
fi

%files
%license COPYING
%doc COPYRIGHT share/README
%_bindir/solaar
%_bindir/hidconsole
%python3_sitelib/hidapi/
%python3_sitelib/logitech_receiver/
%python3_sitelib/solaar/
%python3_sitelib/solaar-%{version}*-py%{python3_version}.egg-info
%_datadir/solaar/
%_datadir/applications/solaar.desktop
%_datadir/icons/hicolor/scalable/apps/solaar.svg
%config(noreplace) %_sysconfdir/xdg/autostart/solaar.desktop


%files doc
%doc docs/


%files udev
%license COPYING
%_udevrulesdir/42-logitech-unify-permissions.rules


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-0.3.rc1
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-0.2.rc1.20200322git563ef0d
- Don't trigger udev if socket is not accessible (#1764565, patch by Stefano Figura)

* Tue Mar 24 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-0.1.rc1.20200322git563ef0d
- update to 1.0.2-rc1 + two recent commits
- drop obsolete patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.0.1-1
- update to 1.0.1
- preserve timestamps
- fix wrong version in setup.py
- add missing requires for unowned icons directory

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11.gitf0fc63e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-10.20180813gitf0fc63e
- Add optional gtk3 dependency.
- Document optional gtk3 dependency.
- Add patch for better output when gtk3 is not installed.

* Tue Aug 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-9.20180813gitf0fc63e
- Install the hidconsole executable.
- Fix permissions on the udev rules file.

* Mon Aug 13 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-8.20180813gitf0fc63e
- Update to latest git head.
- Drop upstreamed patch.

* Fri Jul 27 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-7.20180720git59b7285
- Include a subpackage containing the udev rules, and have it obsolete/provide
  unifying-receiver-udev.
- Add build dependency on systemd (for %%_udevrulesdir).
- Add %%posttranstrigger on the udev subpackage to auto-activate the rules.
- Drop solaar-cli executable.  It just spits out a warning to use solaar.

* Fri Jul 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-6.20180720git59b7285
- Update to new git snapshot.
- Use forge macros to simplify things.
- Convert to python3 and modern python macros.
- Add patch for python3.7 compatibility.
- Better way to fix shebang lines.

* Fri Jul 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-5.20150528gitcf27328
- Use versioned python macros.
- Remove icon-cache scriptlets which are not needed in Fedora.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.2-4.20150528gitcf27328.9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 0.9.2-4.20150528gitcf27328.7
- Remove unnecessary Group: tags

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Richard Fearn <richardfearn@gmail.com> - 0.9.2-4.20150528gitcf27328.4
- Add missing dependency on python-gobject (bug #1355869)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4.20150528gitcf27328.3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4.20150528gitcf27328.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-4.20150528gitcf27328
- Update to upstream git snapshot

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 24 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-2
- Changed files line for .egg-info to be less dependent on Python version,
  to build for EL6 which uses Python 2.6.

* Thu Jul 25 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-1
- Updated to latest upstream.

* Fri Jul 19 2013 Eric Smith <eric@brouhaha.com> 0.9.1-2
- Added scriptlets to update icon caches.
- Added BuildRequires for desktop-file-utils.

* Sun Jul 14 2013 Eric Smith <eric@brouhaha.com> 0.9.1-1
- Updated to latest upstream.
- Consistently use "solaar" rather than name macro.
- Removed extraneous dependency on pygtk2.
- Moved documentation into subpackage.

* Sun Apr 28 2013 Eric Smith <eric@brouhaha.com> 0.8.7-1
- initial version
