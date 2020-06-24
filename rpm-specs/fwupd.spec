%global glib2_version 2.45.8
%global libxmlb_version 0.1.3
%global libgusb_version 0.2.11
%global libsoup_version 2.51.92
%global libjcat_version 0.1.0
%global systemd_version 231
%global json_glib_version 1.1.1

# PPC64 is too slow to complete the tests under 3 minutes...
%ifnarch ppc64le
%global enable_tests 1
%endif

%global enable_dummy 1

# fwupd.efi is only available on these arches
%ifarch x86_64 aarch64
%global have_uefi 1
%endif

# flashrom is only available on these arches
%ifarch i686 x86_64 armv7hl aarch64 ppc64le
%global have_flashrom 1
%endif

# redfish is only available on this arch
%ifarch x86_64
%global have_redfish 1
%endif

# libsmbios is only available on x86
%ifarch x86_64
%global have_dell 1
%endif

# only available recently
%if 0%{?fedora} >= 30
%global have_modem_manager 1
%endif

Summary:   Firmware update daemon
Name:      fwupd
Version:   1.4.4
Release:   1%{?dist}
License:   LGPLv2+
URL:       https://github.com/fwupd/fwupd
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libxmlb-devel >= %{libxmlb_version}
BuildRequires: libgcab1-devel
BuildRequires: libgudev1-devel
BuildRequires: libgusb-devel >= %{libgusb_version}
BuildRequires: libsoup-devel >= %{libsoup_version}
BuildRequires: libjcat-devel >= %{libjcat_version}
BuildRequires: polkit-devel >= 0.103
BuildRequires: sqlite-devel
BuildRequires: gpgme-devel
BuildRequires: systemd >= %{systemd_version}
BuildRequires: libarchive-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gcab
%ifarch %{valgrind_arches}
BuildRequires: valgrind
BuildRequires: valgrind-devel
%endif
BuildRequires: elfutils-libelf-devel
BuildRequires: gtk-doc
BuildRequires: gnutls-devel
BuildRequires: gnutls-utils
BuildRequires: meson
BuildRequires: help2man
BuildRequires: json-glib-devel >= %{json_glib_version}
BuildRequires: vala
BuildRequires: bash-completion
BuildRequires: git-core
%if 0%{?have_flashrom}
BuildRequires: flashrom-devel >= 1.2-2
%endif

%if 0%{?have_modem_manager}
BuildRequires: ModemManager-glib-devel >= 1.10.0
BuildRequires: libqmi-devel >= 1.22.0
%endif

%if 0%{?have_redfish}
BuildRequires: efivar-devel >= 33
%endif

%if 0%{?have_uefi}
BuildRequires: efivar-devel >= 33
BuildRequires: python3 python3-cairo python3-gobject python3-pillow
BuildRequires: pango-devel
BuildRequires: cairo-devel cairo-gobject-devel
BuildRequires: freetype
BuildRequires: fontconfig
BuildRequires: google-noto-sans-cjk-ttc-fonts
BuildRequires: gnu-efi-devel
BuildRequires: tpm2-tss-devel >= 2.2.3
BuildRequires: pesign
%endif

%if 0%{?have_dell}
BuildRequires: efivar-devel >= 33
BuildRequires: libsmbios-devel >= 2.3.0
%endif

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: libxmlb%{?_isa} >= %{libxmlb_version}
Requires: libgusb%{?_isa} >= %{libgusb_version}
Requires: libsoup%{?_isa} >= %{libsoup_version}
Requires: bubblewrap
Requires: shared-mime-info

Obsoletes: fwupd-sign < 0.1.6
Obsoletes: libebitdo < 0.7.5-3
Obsoletes: libdfu < 1.0.0
Obsoletes: fwupd-labels < 1.1.0-1

%description
fwupd is a daemon to allow session software to update device firmware.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libebitdo-devel < 0.7.5-3
Obsoletes: libdfu-devel < 1.0.0

%description devel
Files for development with %{name}.

%package tests
Summary: Data files for installed tests

%description tests
Data files for installed tests.

%prep
%autosetup -p1

%build

%meson \
    -Dgtkdoc=true \
%if 0%{?enable_tests}
    -Dtests=true \
%else
    -Dtests=false \
%endif
%if 0%{?enable_dummy}
    -Dplugin_dummy=true \
%else
    -Dplugin_dummy=false \
%endif
%if 0%{?have_flashrom}
    -Dplugin_flashrom=true \
%else
    -Dplugin_flashrom=false \
%endif
    -Dplugin_thunderbolt=true \
%if 0%{?have_redfish}
    -Dplugin_redfish=true \
%else
    -Dplugin_redfish=false \
%endif
%if 0%{?have_uefi}
    -Dplugin_uefi=true \
    -Dplugin_nvme=true \
    -Dplugin_tpm=true \
%else
    -Dplugin_uefi=false \
    -Dplugin_nvme=false \
    -Dplugin_tpm=false \
%endif
%if 0%{?have_dell}
    -Dplugin_dell=true \
    -Dplugin_synaptics=true \
%else
    -Dplugin_dell=false \
    -Dplugin_synaptics=false \
%endif
%if 0%{?have_modem_manager}
    -Dplugin_modem_manager=true \
%else
    -Dplugin_modem_manager=false \
%endif
    -Dman=true

%meson_build

%if 0%{?enable_tests}
%check
%meson_test
%endif

%install
%meson_install

# sign fwupd.efi loader
%if 0%{?have_uefi}
%ifarch x86_64
%global efiarch x64
%endif
%ifarch aarch64
%global efiarch aa64
%endif
%global fwup_efi_fn $RPM_BUILD_ROOT%{_libexecdir}/fwupd/efi/fwupd%{efiarch}.efi
%pesign -s -i %{fwup_efi_fn} -o %{fwup_efi_fn}.signed
%endif

mkdir -p --mode=0700 $RPM_BUILD_ROOT%{_localstatedir}/lib/fwupd/gnupg

# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1757948
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/fwupd

%find_lang %{name}

%post
%systemd_post fwupd.service

%preun
%systemd_preun fwupd.service

%postun
%systemd_postun_with_restart fwupd.service
%systemd_postun_with_restart pesign.service

%files -f %{name}.lang
%doc README.md AUTHORS
%license COPYING
%config(noreplace)%{_sysconfdir}/fwupd/ata.conf
%config(noreplace)%{_sysconfdir}/fwupd/daemon.conf
%config(noreplace)%{_sysconfdir}/fwupd/upower.conf
%if 0%{?have_uefi}
%config(noreplace)%{_sysconfdir}/fwupd/uefi.conf
%endif
%if 0%{?have_redfish}
%config(noreplace)%{_sysconfdir}/fwupd/redfish.conf
%endif
%config(noreplace)%{_sysconfdir}/fwupd/thunderbolt.conf
%dir %{_libexecdir}/fwupd
%{_libexecdir}/fwupd/fwupd
%{_libexecdir}/fwupd/fwupdoffline
%if 0%{?have_uefi}
%{_libexecdir}/fwupd/efi/*.efi
%{_libexecdir}/fwupd/efi/*.efi.signed
%{_bindir}/fwupdate
%{_bindir}/fwupdtpmevlog
%endif
%{_bindir}/dfu-tool
%{_bindir}/fwupdmgr
%{_bindir}/fwupdtool
%{_bindir}/fwupdagent
%dir %{_sysconfdir}/fwupd
%dir %{_sysconfdir}/fwupd/remotes.d
%if 0%{?have_dell}
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/dell-esrt.conf
%endif
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/lvfs.conf
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/lvfs-testing.conf
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/vendor.conf
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/vendor-directory.conf
%config(noreplace)%{_sysconfdir}/pki/fwupd
%{_sysconfdir}/pki/fwupd-metadata
%{_datadir}/dbus-1/system.d/org.freedesktop.fwupd.conf
%{_datadir}/bash-completion/completions/fwupdmgr
%{_datadir}/bash-completion/completions/fwupdtool
%{_datadir}/bash-completion/completions/fwupdagent
%{_datadir}/fish/vendor_completions.d/fwupdmgr.fish
%{_datadir}/fwupd/metainfo/org.freedesktop.fwupd*.metainfo.xml
%if 0%{?have_dell}
%{_datadir}/fwupd/remotes.d/dell-esrt/metadata.xml
%endif
%{_datadir}/fwupd/remotes.d/vendor/firmware/README.md
%{_datadir}/dbus-1/interfaces/org.freedesktop.fwupd.xml
%{_datadir}/polkit-1/actions/org.freedesktop.fwupd.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.fwupd.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.fwupd.service
%{_datadir}/man/man1/fwupdtool.1.gz
%{_datadir}/man/man1/fwupdagent.1.gz
%{_datadir}/man/man1/dfu-tool.1.gz
%{_datadir}/man/man1/fwupdmgr.1.gz
%if 0%{?have_uefi}
%{_datadir}/man/man1/fwupdate.1.gz
%{_datadir}/man/man1/fwupdtpmevlog.1.gz
%endif
%{_datadir}/metainfo/org.freedesktop.fwupd.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.fwupd.svg
%{_datadir}/fwupd/firmware_packager.py
%{_datadir}/fwupd/simple_client.py
%{_datadir}/fwupd/add_capsule_header.py
%{_datadir}/fwupd/install_dell_bios_exe.py
%{_unitdir}/fwupd-offline-update.service
%{_unitdir}/fwupd.service
%{_unitdir}/fwupd-refresh.service
%{_unitdir}/fwupd-refresh.timer
%{_presetdir}/fwupd-refresh.preset
%{_unitdir}/system-update.target.wants/
%dir %{_localstatedir}/lib/fwupd
%dir %{_localstatedir}/cache/fwupd
%dir %{_datadir}/fwupd/quirks.d
%{_datadir}/fwupd/quirks.d/*.quirk
%{_localstatedir}/lib/fwupd/builder/README.md
%{_libdir}/libfwupd*.so.*
%{_libdir}/girepository-1.0/Fwupd-2.0.typelib
%{_libdir}/girepository-1.0/FwupdPlugin-1.0.typelib
/usr/lib/udev/rules.d/*.rules
/usr/lib/systemd/system-shutdown/fwupd.shutdown
%dir %{_libdir}/fwupd-plugins-3
%{_libdir}/fwupd-plugins-3/libfu_plugin_altos.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_amt.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_ata.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_ccgx.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_colorhug.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_coreboot.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_csr.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_cpu.so
%if 0%{?have_dell}
%{_libdir}/fwupd-plugins-3/libfu_plugin_dell.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_dell_esrt.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_dell_dock.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_dfu.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_ebitdo.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_emmc.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_ep963x.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_fastboot.so
%if 0%{?have_flashrom}
%{_libdir}/fwupd-plugins-3/libfu_plugin_flashrom.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_fresco_pd.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_jabra.so
%if 0%{?have_modem_manager}
%{_libdir}/fwupd-plugins-3/libfu_plugin_modem_manager.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_nitrokey.so
%if 0%{?have_uefi}
%{_libdir}/fwupd-plugins-3/libfu_plugin_nvme.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_optionrom.so
%if 0%{?have_redfish}
%{_libdir}/fwupd-plugins-3/libfu_plugin_redfish.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_rts54hid.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_rts54hub.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_solokey.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_steelseries.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_superio.so
%if 0%{?have_dell}
%{_libdir}/fwupd-plugins-3/libfu_plugin_synaptics_mst.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_synaptics_cxaudio.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_synaptics_prometheus.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_synaptics_rmi.so
%if 0%{?enable_dummy}
%{_libdir}/fwupd-plugins-3/libfu_plugin_test.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_invalid.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_thelio_io.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_thunderbolt.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_thunderbolt_power.so
%if 0%{?have_uefi}
%{_libdir}/fwupd-plugins-3/libfu_plugin_tpm.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_tpm_eventlog.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_uefi.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_uefi_recovery.so
%endif
%{_libdir}/fwupd-plugins-3/libfu_plugin_logind.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_logitech_hidpp.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_upower.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_vli.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_wacom_raw.so
%{_libdir}/fwupd-plugins-3/libfu_plugin_wacom_usb.so
%ghost %{_localstatedir}/lib/fwupd/gnupg
%if 0%{?have_uefi}
%{_datadir}/locale/*/LC_IMAGES/fwupd*
%endif

%files devel
%{_datadir}/gir-1.0/Fwupd-2.0.gir
%{_datadir}/gir-1.0/FwupdPlugin-1.0.gir
%{_datadir}/gtk-doc/html/fwupd
%{_datadir}/vala/vapi
%{_includedir}/fwupd-1
%{_libdir}/libfwupd*.so
%{_libdir}/pkgconfig/fwupd.pc
%{_libdir}/pkgconfig/fwupdplugin.pc

%files tests
%if 0%{?enable_tests}
%dir %{_datadir}/installed-tests/fwupd
%{_datadir}/installed-tests/fwupd/fwupd-tests.xml
%{_datadir}/installed-tests/fwupd/*.test
%{_datadir}/installed-tests/fwupd/*.cab
%{_datadir}/installed-tests/fwupd/*.sh
%dir %{_sysconfdir}/fwupd/remotes.d
%config(noreplace)%{_sysconfdir}/fwupd/remotes.d/fwupd-tests.conf
%endif

%changelog
* Wed Jun 10 2020 Richard Hughes <richard@hughsie.com> 1.4.4-1
- New upstream release
- Fix refreshing when checking for downgraded metadata

* Tue Jun 09 2020 Richard Hughes <richard@hughsie.com> 1.4.3-1
- New upstream release
- Add support for HP DMC dock devices
- Always enforce the metadata signature has a valid timestamp
- Capture the dock SKU in metadata
- Check the device requirements when returning from GetDetails
- Prevent Dell dock updates to occur via synaptics-mst plugin

* Fri May 22 2020 Richard Hughes <richard@hughsie.com> 1.4.2-2
- Backport a patch to fix the synaptics fingerprint reader update.

* Mon May 18 2020 Richard Hughes <richard@hughsie.com> 1.4.2-1
- New upstream release
- Add several more ATA OUI quirks
- Avoid communicating with DFU devices when bitManifestationTolerant is off
- Correct the display of final calculated PCRs
- Delay activation for Dell Thunderbolt updates
- Do not use synaptics-rmi on the Dell K12A
- Fix switching wacom-raw to bootloader mode
- Switch the default of EnumerateAllDevices to false
- Use GPIOB to reset the VL817 found in two Lenovo products

* Mon Apr 27 2020 Richard Hughes <richard@hughsie.com> 1.4.1-1
- New upstream release
- Allow specifying the device on the command line by GUID
- Correctly format firmware version of Dynabook X30 and X40
- Do not show safe mode errors for USB4 host controllers
- Do not show the USB 2 VLI recovery devices for USB 3 hubs
- Fix the correct DeviceID set by GetDetails
- Only update the FW2 partition of the ThinkPad USB-C Dock Gen2
- Prefer to update the child device first if the order is unspecified
- Refresh device name and format before setting supported flag
- Reset the progressbar time estimate if the percentage is invalid
- Set the CCGX device name and summary from quirk files
- Wait for the cxaudio device to reboot after writing firmware

* Tue Apr 14 2020 Richard Hughes <richard@hughsie.com> 1.4.0-1
- New upstream release
- Actually reload the DFU device after upgrade has completed
- Add plugin for CPU microcode
- Add plugin for Cypress CCGX hardware
- Add plugin for EP963x hardware
- Add STM32F745 DfuSe version quirk
- Allow server metadata to set the device name and version format
- Always check for 'PLAIN' when doing vercmp() operations
- Apply version format to releases and devices at same time
- Check the firmware requirements before adding 'SUPPORTED'
- Correctly attach VL103 after a firmware update
- Do not allow devices that have no vendor ID to be 'UPDATABLE'
- Do not use shim for non-secure boot configurations
- Export the device state, release creation time and urgency
- Fix a crash when removing device parents
- Fix a difficult-to-trigger daemon hang when replugging devices
- Fix a runtime error when detaching MSP430
- Fix CounterpartGuid when there is more than one supported device
- Fix reporting Synaptics cxaudio version number
- Introduce a new VersionFormat of 'hex'
- Load the signature to get the aliased CDN-safe version of the metadata
- Never add USB hub devices that are not upgradable
- Only auto-add counterpart GUIDs when required
- Parse the CSR firmware as a DFU file
- Set the protocol when updating logitech HID++ devices
- Use Jcat files in firmware archives and for metadata
- When TPM PCR0 measurements fail, query if secure boot is available and enabled

* Thu Mar 05 2020 Nicolas Mailhot <nim@fedoraproject.org> 1.3.9-2
- Rebuild against the new Gusb.

* Wed Mar 04 2020 Richard Hughes <richard@hughsie.com> 1.3.9-1
- New upstream release
- Added completion script for fish shell
- Always check for PLAIN when doing vercmp() operations
- Always return AppStream markup for remote agreements
- Apply UEFI capsule update even with single valid capsule
- Check the device protocol before de-duping devices
- Copy the version and format from donor device in get-details
- Correctly append the release to devices in `fwupdtool get-details`
- Decrease minimum battery requirement to 10%
- Discard the reason upgrades aren't available
- Do not fail loading in /etc/machine-id is not available
- Fix a critical warning when installing some firmware
- For the `get-details` command make sure to always show devices
- Inhibit all power management actions using logind when updating
- Set the MSP430 version format to pair
- Switch off the ATA verbose logging by default
- Use unknown for version format by default on get-details

* Thu Feb 13 2020 Richard Hughes <richard@hughsie.com> 1.3.8-1
- New upstream release
- Add an extra instance ID to disambiguate USB hubs
- Add a plugin to update PD controllers by Fresco Logic
- Correctly reset VL100 PD devices
- Do not rewrite BootOrder in the EFI helper
- Do not use vercmp when the device version format is plain
- Fix firmware regression in the EFI capsule helper
- Fix updating Synaptics MST devics with no PCI parent
- Ignore Unifying detach failures
- Make the cxaudio version match that of the existing Windows tools
- Replay the TPM event log to get the PCRx values
- Set up more parent devices for various Lenovo USB hubs
- Support the new gnuefi file locations
- Use the correct command to get the VLI device firmware version

* Fri Jan 31 2020 Richard Hughes <richard@hughsie.com> 1.3.7-1
- New upstream release
- Add 'get-remotes' and 'refresh' to fwupdtool
- Add support for standalone VIA PD devices
- Allow applying all releases to get to a target version
- Correctly delete UEFI variables
- Correctly import PKCS-7 remote metadata
- Discourage command line metadata refreshes more than once per day
- Do not always get the vendor ID for udev devices using the parent
- Get the list of updates in JSON format from fwupdagent
- Show the device parent if there is an interesting child
- Shut down automatically when there is system memory pressure
- Use a different protocol ID for VIA i2c devices
- Use the correct timeout for Logitech IO channel writes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Richard Hughes <richard@hughsie.com> 1.3.6-1
- New upstream release
- Add a dell-bios version format to match what is shown on the vendor website
- Add a new plugin that exposes the TPM device
- Allow incremental version major and minor number for Synaptics Prometheus devices
- Clarify error messages when no upgrades are available
- Correct the default prompt for reboot/shutdown
- Do not expose bootloader version errors to users
- Enforce that device protocol matches the metadata value
- Export the device protocol and raw device version to the client --verbose output
- Fix the quirk for the legacy VIA 813 usbhub chip
- Only check the vendor ID if the device has one set
- Return exit status success if there is no firmware to be updated
- Set the correct vendor eMMC ID prefix
- Use the baseboard vendor as the superio vendor ID
- Use the BIOS vendor as the coreboot and flashrom vendor ID

* Fri Nov 29 2019 Richard Hughes <richard@hughsie.com> 1.3.5-1
- New upstream release
- Convert libfwupdprivate to a shared library libfwupdplugin
- Create a REV_00 instance ID as this may be what the vendor needs to target
- Improve coreboot version detection
- Invert default behavior to be safer for reboot and shutdown prompts
- Reload the Synaptics prometheus device version after update
- Use the correct unlocker when using GRWLock
- Whitelist VIA USB hub PD and I²C devices

* Fri Nov 22 2019 Richard Hughes <richard@hughsie.com> 1.3.4-1
- New upstream release
- Add support for Foxconn T77W968 and DW5821e eSIM
- Add support for matching firmware requirements on device parents
- Add support for writing VIA PD and I2C devices
- Add versions formats for the Microsoft Surface devices
- Correct Wacom panel HWID support
- Fix a fastboot regression when updating modem firmware
- Fix regression when coldplugging superio devices
- Fix the linking of the UEFI update binary
- Fix the vendor id of hidraw devices
- Make loading USB device strings non-fatal
- Reject invalid Synaptics MST chip IDs
- Skip cleanup after device is done updating if required

* Fri Nov 01 2019 Richard Hughes <richard@hughsie.com> 1.3.3-1
- New upstream release
- Add a plugin for systems running coreboot
- Add a plugin to update eMMC devices
- Add a plugin to update Synaptics RMI4 devices
- Add a plugin to update VIA USB hub hardware
- Add several quirks for Realtek webcams
- Add some success messages when CLI tasks have completed
- Add support for automatically uploading reports
- Add support for `fwupdmgr reinstall`
- Add support for the 8bitdo SN30Pro+
- Add support for the ThinkPad USB-C Dock Gen2 audio device
- Allow fwupdtool to dump details of common firmware formats
- Always report the update-error correctly for multiple updates
- Create a unique GUID for the Thunderbolt controller path
- Fix a regression for Wacom EMR devices
- Recognize new 'generation' Thunderbolt sysfs attribute for USB4
- Rework ESP path detection and lifecycle to auto-unmount when required
- Show a useful error for Logitech devices that cannot self-reset
- Use correct method for stopping systemd units
- Use device safety flags to show prompts before installing updates
- Use will-disappear flag for 8bitdo SF30/SN30 controllers
- Use XMLb to query quirks to reduce the RSS when running

* Tue Oct 08 2019 Richard Hughes <richard@hughsie.com> 1.3.2-2
- Manually create /var/cache/fwupd to work around #1757948

* Thu Sep 26 2019 Richard Hughes <richard@hughsie.com> 1.3.2-1
- New upstream release
- Add aliases for get-upgrades and upgrade
- Add support for Conexant audio devices
- Add support for the Minnowboard Turbot
- Add support for the SoloKey Secure
- Add support for the Thelio IO board
- Add support to integrate into the motd
- Allow disabling SSL strict mode for broken corporate proxies
- Allow filtering devices when using the command line tools
- Allow specifying a firmware GUID to check any version exists
- Be more accepting when trying to recover a failed database migration
- Display more helpful historical device information
- Do not ask the user to upload a report if ReportURI is not set
- Do not segfault when trying to quit the downgrade selection
- Ensure HID++ v2.0 peripheral devices get added
- Never show AppStream markup on the console
- Only write the new UEFI device path if different than before
- Partially rewrite the Synapticsmst plugin to support more hardware
- Print devices, remotes, releases using a tree
- Support issues in AppStream metadata
- Use tpm2-tss library to read PCR values

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Richard Hughes <richard@hughsie.com> 1.2.10-1
- New upstream release
- Add a specific error code for the low battery case
- Add support for 8bitdo USB Retro Receiver
- Export new API to build objects from GVariant blobs
- Fix installing synaptics-prometheus config updates
- Prompt for reboot when unlocking on the command line if applicable
- Show a warning when running in UEFI legacy mode
- Show devices with an UpdateError in get-devices output
- Support a UEFI quirk to disable the use of the UX capsule
- Support empty proxy server strings
- Try harder to find duplicate UEFI boot entries

* Mon May 20 2019 Richard Hughes <richard@hughsie.com> 1.2.9-1
- New upstream release
- Add support for Synaptics Prometheus fingerprint readers
- Check the daemon version is at least the client version
- Correctly identify DFU firmware that starts at offset zero
- Display the remote warning on the console in an easy-to-read way
- Export the version-format used by devices to clients
- Fix a libasan failure when reading a UEFI variable
- Never guess the version format from the version string
- Only use class-based instance IDs for quirk matching
- Prompt the user to shutdown if required when installing by ID
- Reset the forced version during DFU attach and detach
- Set the version format for more device types

* Tue Apr 23 2019 Richard Hughes <richard@hughsie.com> 1.2.8-1
- New upstream release
- Allow the fwupdmgr tool to modify the daemon config
- Correctly parse DFU interfaces with extra vendor-specific data
- Do not report transient or invalid system failures
- Fix problems with the version format checking for some updates

* Wed Apr 17 2019 Richard Hughes <richard@hughsie.com> 1.2.7-3
- Revert a patch from upstream that was causing problems with Dell hardware

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.2.7-2
- Rebuild with Meson fix for #1699099

* Thu Apr 11 2019 Richard Hughes <richard@hughsie.com> 1.2.7-1
- New upstream release
- Add a component categories to express the firmware type
- Add support for 8BitDo M30
- Add support for the not-child extension from Logitech
- Blacklist the synapticsmst plugin when using amdgpu
- Correct ATA activation functionality to work for all vendors
- Implement QMI PDC active config selection for modems
- Make an error message clearer when there are no updates available
- Match the old or new version number when setting NEEDS_REBOOT
- More carefully check the output from tpm2_pcrlist
- Recreate the history database if migration failed
- Require AC power when updating Thunderbolt devices
- Require --force to install a release with a different version format
- Shut down the daemon if the on-disk binary is replaced

* Wed Mar 27 2019 Richard Hughes <richard@hughsie.com> 1.2.6-2
- Enable the ModemManager plugin

* Tue Mar 26 2019 Richard Hughes <richard@hughsie.com> 1.2.6-1
- New upstream release
- Add support for delayed activation of docks and ATA devices
- Add support for reading the SuperIO device checksum and writing to e-flash
- Add the fwupdagent binary for use in shell scripts
- Allow restricting firmware updates for enterprise use
- Allow running offline updates when in system-update.target
- Allow signing the fwupd report with a client certificate
- Ask to reboot after scheduling an offline firmware update
- Correctly check the new version for devices that replug
- Do not fail to start the daemon if tpm2_pcrlist hangs
- Do not fail when scheduling more than one update to be run offline
- Do not schedule an update on battery power if it requires AC power
- Include all device checksums in the LVFS report
- Rename the shimx64.efi binary for known broken firmware
- Upload the UPDATE_INFO entry for the UEFI UX capsule
- Use Plymouth when updating offline firmware

* Mon Feb 25 2019 Richard Hughes <richard@hughsie.com> 1.2.5-1
- New upstream release
- Allow a device to be updated using more than one plugin
- Call composite prepare and cleanup using fwupdtool
- Detect and special case Dell ATA hardware
- Fix flashing failure with latest Intuos Pro tablet
- Fix potential segfault when applying UEFI updates
- Fix unifying regression when recovering from failed flash
- Report the DeviceInstanceIDs from fwupdmgr when run as root

* Tue Feb 12 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.4-2
- Remove obsolete scriptlets

* Fri Feb 01 2019 Richard Hughes <richard@hughsie.com> 1.2.4-1
- New upstream release
- Add a directory remote that generates metadata
- Add a plugin to update Wacom embedded EMR and AES panels
- Add a plugin to upgrade firmware on ATA-ATAPI hardware
- Add a quirk to use the legacy bootmgr description
- Add SuperIO IT89xx device support
- Add support for Dell dock passive flow
- Add the needs-shutdown quirk to Phison NVMe drives
- Add 'update' and 'get-updates' commands to fwupdtool
- Allow Dell dock flashing Thunderbolt over I2C
- Check the battery percentage before flashing
- Correct Nitrokey Storage invalid firmware version read
- Do not check the BGRT status before uploading a UX capsule
- Do the UEFI UX checksum calculation in fwupd
- Fix flashing various Jabra devices
- Fix the parser to support extended segment addresses
- Flash the fastboot partition after downloading the file
- Show a console warning if loading an out-of-tree plugin
- Show a per-release source and details URL
- Show a `UpdateMessage` and display it in tools
- Support FGUID to get the SKU GUID for NVMe hardware

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Richard Hughes <richard@hughsie.com> 1.2.3-1
- New upstream release
- Correctly migrate the history database

* Sun Dec 30 2018 Richard Hughes <richard@hughsie.com> 1.2.2-1
- New upstream release
- Add support for devices that support fastboot
- Add more standard USB identifier GUIDs
- Add the PCR0 value as the device checksum for system firmware
- Add Dell TB18DC to the supported devices list
- Allow replacing the last byte in the image when using 'dfu-tool replace-data'
- Append the UEFI capsule header in userspace rather than in the loader
- Check the device checksum as well as the content checksum during verify
- Correctly parse format the version numbers correctly using old metadata
- Fix a crash if AMT returns an empty response
- Fix a regression when doing GetReleases on unsupported hardware
- Remove the Wacom DTH generation hardware from the whitelist
- Sanitize the version if the version format has been specified

* Tue Nov 27 2018 Richard Hughes <richard@hughsie.com> 1.2.1-1
- New upstream release
- Add per-release install duration values
- Fix a use-after-free when using --immediate-exit
- Fix flashing the 8bitdo SF30
- Fix showing the custom remote agreements
- Include the os-release information in the release metadata
- Shut down the daemon after 2h of inactivity when possible
- Speed up startup by loading less thunderbolt firmware
- Speed up startup by using a silo index for GUID queries
- Use less memory and fragment the heap less when starting

* Wed Nov 07 2018 Richard Hughes <richard@hughsie.com> 1.2.0-1
- New upstream release
- Add a standalone installer creation script
- Add version format quirks for several Lenovo machines
- Adjust synapticsmst EVB board handling
- Allow setting the version format from a quirk entry
- Port from libappstream-glib to libxmlb for a large reduction in RSS
- Set the full AMT device version including the BuildNum
- Sort the firmware sack by component priority
- Stop any running daemon over dbus when using fu-tool
- Support the Intel ME version format
- Use HTTPS_PROXY if set

* Fri Oct 12 2018 Richard Hughes <richard@hughsie.com> 1.1.3-1
- New upstream release
- Add a plugin for an upcoming Dell USB-C dock
- Add support for devices to show an estimated flash time
- Add support for Realtek USB devices using vendor HID and HUB commands
- Adjust panamera ESM update routine for some reported issues
- Allow firmware files to depend on versions from other devices
- Check the amount of free space on the ESP before upgrading
- Don't show devices pending a reboot in GetUpgrades
- Fix possible crash in the thunderbolt-power plugin
- Make various parts of the daemon thread-safe
- Redirect all debugging output to stderr instead of stdout
- Run the Dell plugin initialization after the UEFI plugin
- Update all sub-devices for a composite update

* Mon Sep 10 2018 Richard Hughes <richard@hughsie.com> 1.1.2-1
- New upstream release
- Add a new plugin to enumerate EC firmware
- Add a new plugin to update NVMe hardware
- Allow updating just one specific device from the command line
- Always use the same HardwareIDs as Windows
- Download firmware if the user specifies a URI
- Implement the systemd recommendations for offline updates
- Improve performance when reading keys from the quirk database
- Rewrite the unifying plugin to use the new daemon-provided functionality
- Show a time estimate on the progressbar after an update has started

* Mon Aug 13 2018 Richard Hughes <richard@hughsie.com> 1.1.1-1
- New upstream release
- Add support for the Synaptics Panamera hardware
- Add validation for Alpine and Titan Ridge
- Allow flashing unifying devices in recovery mode
- Allow running synapticsmst on non-Dell hardware
- Check the ESP for sanity at at startup
- Do not hold hidraw devices open forever
- Fix a potential segfault in smbios data parsing
- Fix encoding the GUID into the capsule EFI variable
- Fix various bugs when reading the thunderbolt version number
- Improve the Redfish plugin to actually work with real hardware
- Reboot synapticsmst devices at the end of flash cycle
- Show the correct title when updating devices

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Richard Hughes <richard@hughsie.com> 1.1.0-2
- Rebuild to get the EFI executable signed with the Red Hat key

* Wed Jul 11 2018 Richard Hughes <richard@hughsie.com> 1.1.0-1
- New upstream release
- Add a initial Redfish support
- Allow devices to assign a plugin from the quirk subsystem
- Detect the EFI system partition location at runtime
- Do not use 8bitdo bootloader commands after a successful flash
- Fix a potential buffer overflow when applying a DFU patch
- Fix downgrading older releases to devices
- Fix flashing devices that require a manual replug
- Fix unifying failure to detach when using a slow host controller
- Merge fwupdate functionality into fwupd
- Support more Wacom tablets

* Thu Jun 07 2018 Richard Hughes <richard@hughsie.com> 1.0.8-1
- New upstream release
- Adjust all licensing to be 100% LGPL 2.1+
- Add a firmware diagnostic tool called fwupdtool
- Add an plugin to update some future Wacom tablets
- Add support for Motorola S-record files
- Add the Linux Foundation public GPG keys for firmware and metadata
- Allow installing more than one firmware using 'fwupdmgr install'
- Allow specifying hwids with OR relationships
- Fix a potential DoS in libdfu by limiting holes to 1MiB
- Fix Hardware-ID{0,1,2,12} compatibility with Microsoft
- Hide devices that aren't updatable by default in fwupdmgr
- Stop matching Nintendo Switch Pro in the 8bitdo plugin

* Mon Apr 30 2018 Richard Hughes <richard@hughsie.com> 1.0.7-1
- New upstream release
- Add enable-remote and disable-remote commands to fwupdmgr
- Allow requiring specific versions of libraries for firmware updates
- Don't recoldplug thunderbolt to fix a flashing failure
- Fix SQL error when running 'fwupdmgr clear-offline'
- Only enumerate Dell Docks if the type is known
- Reboot after scheduling using logind not systemd
- Show a warning with interactive prompt when enabling a remote

* Mon Mar 12 2018 Richard Hughes <richard@hughsie.com> 1.0.6-1
- New upstream release
- Add bash completion for fwupdmgr
- Add support for newest Thunderbolt chips
- Allow devices to use the runtime version when in bootloader mode
- Allow overriding ESP mount point via conf file
- Correct handling of unknown Thunderbolt devices
- Correctly detect new remotes that are manually copied
- Delete any old fwupdate capsules and efivars when launching fwupd
- Fix a crash related to when passing device to downgrade in CLI
- Fix Unifying signature writing and parsing for Texas bootloader
- Generate Vala bindings

* Fri Feb 23 2018 Richard Hughes <richard@hughsie.com> 1.0.5-2
- Use the new CDN for metadata.

* Wed Feb 14 2018 Richard Hughes <richard@hughsie.com> 1.0.5-1
- New upstream release
- Be more careful deleting and modifying device history
- Fix crasher with MST flashing
- Fix DFU detach with newer releases of libusb
- Offer to reboot when processing an offline update
- Show the user a URL when they report a known problem
- Stop matching 8bitdo DS4 controller VID/PID
- Support split cabinet archives as produced by Windows Update

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Richard Hughes <richard@hughsie.com> 1.0.4-1
- New upstream release
- Add a device name for locked UEFI devices
- Add D-Bus methods to get and modify the history information
- Allow the user to share firmware update success or failure
- Ask the user to refresh metadata when it is very old
- Never add two devices to the daemon with the same ID
- Rescan supported flags when refreshing metadata
- Store firmware update success and failure to a local database

* Fri Jan 12 2018 Richard Hughes <richard@hughsie.com> 1.0.3-2
- Backport a patch that fixes applying firmware updates using gnome-software.

* Tue Jan 09 2018 Richard Hughes <richard@hughsie.com> 1.0.3-1
- New upstream release
- Add a new plugin to add support for CSR "Driverless DFU"
- Add initial SF30/SN30 Pro support
- Block owned Dell TPM updates
- Choose the correct component from provides matches using requirements
- Do not try to parse huge compressed archive files
- Handle Thunderbolt "native" mode
- Use the new functionality in libgcab >= 1.0 to avoid writing temp files

* Tue Nov 28 2017 Richard Hughes <richard@hughsie.com> 1.0.2-1
- New upstream release
- Add a plugin for the Nitrokey Storage device
- Add quirk for AT32UC3B1256 as used in the RubberDucky
- Add support for the original AVR DFU protocol
- Allow different plugins to claim the same device
- Disable the dell plugin if libsmbios fails
- Fix critical warning when more than one remote fails to load
- Ignore useless Thunderbolt device types
- Set environment variables to allow easy per-plugin debugging
- Show a nicer error message if the requirement fails
- Sort the output of GetUpgrades correctly
- Use a SHA1 hash for the internal DeviceID

* Thu Nov 09 2017 Kalev Lember <klember@redhat.com> 1.0.1-3
- Rebuild against libappstream-glib 0.7.4

* Thu Nov 09 2017 Kalev Lember <klember@redhat.com> 1.0.1-2
- Fix libdfu obsoletes versions

* Thu Nov 09 2017 Richard Hughes <richard@hughsie.com> 1.0.1-1
- New upstream release
- Add support for HWID requirements
- Add support for programming various AVR32 and XMEGA parts using DFU
- Add the various DFU quirks for the Jabra Speak devices
- Catch invalid Dell dock component requests
- Correctly output Intel HEX files with > 16bit offset addresses
- Do not try to verify the element write if upload is unsupported
- Fix a double-unref when updating any 8Bitdo device
- Fix uploading large firmware files over DFU
- Format the BCD USB revision numbers correctly
- Guess the DFU transfer size if it is not specified
- Include the reset timeout as wValue to fix some DFU bootloaders
- Move the database of supported devices out into runtime loaded files
- Support devices with truncated DFU interface data
- Use the correct wDetachTimeOut when writing DFU firmware
- Verify devices with legacy VIDs are actually 8Bitdo controllers

* Mon Oct 09 2017 Richard Hughes <richard@hughsie.com> 1.0.0-1
- New upstream release
- This release breaks API and ABI to remove deprecated symbols
- libdfu is now not installed as a shared library
- Add FuDeviceLocker to simplify device open/close lifecycles
- Add functionality to blacklist Dell HW with problems
- Disable the fallback USB plugin
- Do not fail to load the daemon if cached metadata is invalid
- Do not use system-specific infomation for UEFI PCI devices
- Fix various printing issues with the progressbar
- Never fallback to an offline update from client code
- Only set the Dell coldplug delay when we know we need it
- Parse the SMBIOS v2 and v3 DMI tables directly
- Support uploading the UEFI firmware splash image
- Use the intel-wmi-thunderbolt kernel module to force power

* Fri Sep 01 2017 Richard Hughes <richard@hughsie.com> 0.9.7-1
- New upstream release
- Add a FirmwareBaseURI parameter to the remote config
- Add a firmware builder that uses bubblewrap
- Add a python script to create fwupd compatible cab files from .exe files
- Add a thunderbolt plugin for new kernel interface
- Fix an incomplete cipher when using XTEA on data not in 4 byte chunks
- Show a bouncing progress bar if the percentage remains at zero
- Use the new bootloader PIDs for Unifying pico receivers

* Fri Sep 01 2017 Kalev Lember <klember@redhat.com> 0.9.6-2
- Disable i686 UEFI support now that fwupdate is no longer available there
- Enable aarch64 UEFI support now that all the deps are available there

* Thu Aug 03 2017 Richard Hughes <richard@hughsie.com> 0.9.6-1
- New upstream release
- Add --version option to fwupdmgr
- Display all errors recorded by efi_error tracing
- Don't log a warning when an unknown unifying report is parsed
- Fix a hang on 32 bit machines
- Make sure the unifying percentage completion goes from 0% to 100%
- Support embedded devices with local firmware metadata
- Use new GUsb functionality to fix flashing Unifying devices

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Richard Hughes <richard@hughsie.com> 0.9.5-1
- New upstream release
- Add a plugin to get the version of the AMT ME interface
- Allow flashing Unifying devices in bootloader modes
- Filter by Unifying SwId when making HID++2.0 requests
- Fix downgrades when version_lowest is set
- Fix the self tests when running on PPC64 big endian
- Use the UFY DeviceID prefix for Unifying devices

* Thu Jun 15 2017 Richard Hughes <richard@hughsie.com> 0.9.4-1
- New upstream release
- Add installed tests that use the daemon
- Add the ability to restrict firmware to specific vendors
- Compile with newer versions of meson
- Fix a common crash when refreshing metadata
- Generate a images for status messages during system firmware update
- Show progress download when refreshing metadata
- Use the correct type signature in the D-Bus introspection file

* Wed Jun 07 2017 Richard Hughes <richard@hughsie.com> 0.9.3-1
- New upstream release
- Add a 'downgrade' command to fwupdmgr
- Add a 'get-releases' command to fwupdmgr
- Add support for Microsoft HardwareIDs
- Allow downloading metadata from more than just the LVFS
- Allow multiple checksums on devices and releases
- Correctly open Unifying devices with original factory firmware
- Do not expect a Unifying reply when issuing a REBOOT command
- Do not re-download firmware that exists in the cache
- Fix a problem when testing for a Dell system
- Fix flashing new firmware to 8bitdo controllers

* Tue May 23 2017 Richard Hughes <richard@hughsie.com> 0.9.2-2
- Backport several fixes for updating Unifying devices

* Mon May 22 2017 Richard Hughes <richard@hughsie.com> 0.9.2-1
- New upstream release
- Add support for Unifying DFU features
- Do not spew a critial warning when parsing an invalid URI
- Ensure steelseries device is closed if it returns an invalid packet
- Ignore spaces in the Unifying version prefix

* Thu Apr 20 2017 Richard Hughes <richard@hughsie.com> 0.8.2-1
- New upstream release
- Add a config option to allow runtime disabling plugins by name
- Add DFU quirk for OpenPICC and SIMtrace
- Create directories in /var/cache as required
- Fix the Requires lines in the dfu pkg-config file
- Only try to mkdir the localstatedir if we have the right permissions
- Support proxy servers in fwupdmgr

* Thu Mar 23 2017 Bastien Nocera <bnocera@redhat.com> - 0.8.1-2
+ fwupd-0.8.1-2
- Release claimed devices on error, fixes unusable input devices

* Mon Feb 27 2017 Richard Hughes <richard@hughsie.com> 0.8.1-1
- New upstream release
- Adjust systemd confinement restrictions
- Don't initialize libsmbios on unsupported systems
- Fix a crash when enumerating devices

* Wed Feb 08 2017 Richard Hughes <richard@hughsie.com> 0.8.0-1
- New upstream release
- Add support for Intel Thunderbolt devices
- Add support for Logitech Unifying devices
- Add support for Synaptics MST cascades hubs
- Add support for the Altus-Metrum ChaosKey device
- Always close USB devices before error returns
- Return the pending UEFI update when not on AC power
- Use a heuristic for the start address if the firmware has no DfuSe footer
- Use more restrictive settings when running under systemd

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-2
- Rebuild for gpgme 1.18

* Wed Oct 19 2016 Richard Hughes <richard@hughsie.com> 0.7.5-1
- New upstream release
- Add quirks for HydraBus as it does not have a DFU runtime
- Don't create the UEFI dummy device if the unlock will happen on next boot
- Fix an assert when unlocking the dummy ESRT device
- Fix writing firmware to devices using the ST reference bootloader
- Match the Dell TB16 device

* Mon Sep 19 2016 Richard Hughes <richard@hughsie.com> 0.7.4-1
- New upstream release
- Add a fallback for older appstream-glib releases
- Allow the argument to 'dfu-tool set-release' be major.minor
- Fix a possible crash when uploading firmware files using libdfu
- Fix libfwupd self tests when a host-provided fwupd is not available
- Load the Altos USB descriptor from ELF files
- Show the human-readable version in the 'dfu-tool dump' output
- Support writing the IHEX symbol table
- Write the ELF files with the correct section type

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> 0.7.3-2
- Fix an unexpanded macro in the spec file
- Tighten libebitdo-devel requires with the _isa macro
- Add ldconfig scripts for libdfu and libebitdo subpackages

* Mon Aug 29 2016 Richard Hughes <richard@hughsie.com> 0.7.3-1
- New upstream release
- Add Dell TPM and TB15/WD15 support via new Dell provider
- Add initial ELF reading and writing support to libdfu
- Add support for installing multiple devices from a CAB file
- Allow providers to export percentage completion
- Don't fail while checking versions or locked state
- Show a progress notification when installing firmware
- Show the vendor flashing instructions when installing
- Use a private gnupg key store
- Use the correct firmware when installing a composite device

* Fri Aug 19 2016 Peter Jones <pjones@redhat.com> - 0.7.2-6
- Rebuild to get libfwup.so.1 as our fwupdate dep.  This should make this the
  last time we need to rebuild for this.

* Wed Aug 17 2016 Peter Jones <pjones@redhat.com> - 0.7.2-5
- rebuild against new efivar and fwupdate

* Fri Aug 12 2016 Adam Williamson <awilliam@redhat.com> - 0.7.2-4
- rebuild against new efivar and fwupdate

* Thu Aug 11 2016 Richard Hughes <richard@hughsie.com> 0.7.2-3
- Use the new CDN for firmware metadata

* Thu Jul 14 2016 Kalev Lember <klember@redhat.com> - 0.7.2-2
- Tighten subpackage dependencies

* Mon Jun 13 2016 Richard Hughes <richard@hughsie.com> 0.7.2-1
- New upstream release
- Allow devices to have multiple assigned GUIDs
- Allow metainfo files to match only specific revisions of devices
- Only claim the DFU interface when required
- Only return updatable devices from GetDevices()
- Show the DFU protocol version in 'dfu-tool list'

* Fri May 13 2016 Richard Hughes <richard@hughsie.com> 0.7.1-1
- New upstream release
- Add device-added, device-removed and device-changed signals
- Add for a new device field "Flashes Left"
- Fix a critical warning when restarting the daemon
- Fix BE issues when reading and writing DFU files
- Make the device display name nicer
- Match the AppStream metadata after a device has been added
- Return all update descriptions newer than the installed version
- Set the device description when parsing local firmware files

* Fri Apr 01 2016 Richard Hughes <richard@hughsie.com> 0.7.0-1
- New upstream release
- Add Alienware to the version quirk table
- Add a version plugin for SteelSeries hardware
- Do not return updates that require AC when on battery
- Return the device flags when getting firmware details

* Mon Mar 14 2016 Richard Hughes <richard@hughsie.com> 0.6.3-1
- New upstream release
- Add an unlock method for devices
- Add ESRT enable method into UEFI provider
- Correct the BCD version number for DFU 1.1
- Ignore the DFU runtime on the DW1820A
- Only read PCI OptionROM firmware when devices are manually unlocked
- Require AC power before scheduling some types of firmware update

* Fri Feb 12 2016 Richard Hughes <richard@hughsie.com> 0.6.2-1
- New upstream release
- Add 'Created' and 'Modified' properties on managed devices
- Fix get-results for UEFI provider
- Support vendor-specific UEFI version encodings

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Richard Hughes <richard@hughsie.com> 0.6.1-1
- New upstream release
- Do not misdetect different ColorHug devices
- Only dump the profiling data when run with --verbose

* Mon Dec 07 2015 Richard Hughes <richard@hughsie.com> 0.6.0-1
- New upstream release
- Add support for automatically updating USB DFU-capable devices
- Emit the changed signal after doing an update
- Export the AppStream ID when returning device results
- Use the same device identification string format as Microsoft

* Wed Nov 18 2015 Richard Hughes <richard@hughsie.com> 0.5.4-1
- New upstream release
- Use API available in fwupdate 0.5 to avoid writing temp files
- Fix compile error against fwupdate 0.5 due to API bump

* Thu Nov 05 2015 Richard Hughes <richard@hughsie.com> 0.5.3-1
- New upstream release
- Avoid seeking when reading the file magic during refresh
- Do not assume that the compressed XML data will be NUL terminated
- Use the correct user agent string for fwupdmgr

* Wed Oct 28 2015 Richard Hughes <richard@hughsie.com> 0.5.2-1
- New upstream release
- Add the update description to the GetDetails results
- Clear the in-memory firmware store only after parsing a valid XML file
- Ensure D-Bus remote errors are registered at fwupdmgr startup
- Fix verify-update to produce components with the correct provide values
- Show the dotted-decimal representation of the UEFI version number
- Support cabinet archives files with more than one firmware

* Mon Sep 21 2015 Richard Hughes <richard@hughsie.com> 0.5.1-1
- Update to 0.5.1 to fix a bug in the offline updater

* Tue Sep 15 2015 Richard Hughes <richard@hughsie.com> 0.5.0-1
- New upstream release
- Do not reboot if racing with the PackageKit offline update mechanism

* Thu Sep 10 2015 Richard Hughes <richard@hughsie.com> 0.1.6-3
- Do not merge the existing firmware metadata with the submitted files

* Thu Sep 10 2015 Kalev Lember <klember@redhat.com> 0.1.6-2
- Own system-update.target.wants directory
- Make fwupd-sign obsoletes versioned

* Thu Sep 10 2015 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream release
- Add application metadata when getting the updates list
- Remove fwsignd, we have the LVFS now

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> 0.1.5-3
- Disable fwupd offline update service

* Wed Aug 19 2015 Richard Hughes <richard@hughsie.com> 0.1.5-2
- Use the non-beta download URL prefix

* Wed Aug 12 2015 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream release
- Add a Raspberry Pi firmware provider
- Fix validation of written firmware
- Make parsing the option ROM runtime optional
- Use the AppStream 0.9 firmware specification by default

* Sat Jul 25 2015 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream release
- Actually parse the complete PCI option ROM
- Add a 'fwupdmgr update' command to update all devices to latest versions
- Add a simple signing server that operates on .cab files
- Add a 'verify' command that verifies the cryptographic hash of device firmware

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Richard Hughes <richard@hughsie.com> 0.1.3-2
- Compile with libfwupdate for UEFI firmware support.

* Thu May 28 2015 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream release
- Coldplug the devices before acquiring the well known name
- Run the offline actions using systemd when required
- Support OpenHardware devices using the fwupd vendor extensions

* Wed Apr 22 2015 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream release
- Only allow signed firmware to be upgraded without a password

* Mon Mar 23 2015 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream release
- Add a 'get-updates' command to fwupdmgr
- Add and document the offline-update lifecycle
- Create a libfwupd shared library
- Create runtime directories if they do not exist
- Do not crash when there are no devices to return

* Mon Mar 16 2015 Richard Hughes <richard@hughsie.com> 0.1.0-1
- First release
