Name:           ckb-next
Version:        0.4.2
Release:        4%{?dist}
Summary:        Unofficial driver for Corsair RGB keyboards

# ckb-next is GPLv2
# The kissfft library (src/libs/kissfft) is BSD
License:        GPLv2 and BSD

URL:            https://github.com/ckb-next/ckb-next
Source0:        %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# Upstream provides none of the following files
Source1:        ckb-next.appdata.xml
Source2:        ckb-next.1
Source3:        99-ckb-next.preset

Patch0:         ckb-next-0.4.2--missing-extern-qualifiers.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappindicator-devel
BuildRequires:  libappstream-glib
BuildRequires:  libgudev-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qtbase-devel >= 5.2.0
BuildRequires:  quazip-qt5-devel >= 0.7.3
BuildRequires:  zlib-devel

BuildRequires:  systemd-devel
%{?systemd_requires}

Requires:       qt5-qtbase >= 5.2.0
Requires:       qt5ct

Provides:       bundled(kissfft)

# ckb-next, as the name suggests, is a re-activation and continuation of "ckb"
Obsoletes:      ckb


%description
ckb-next is an open-source driver for Corsair keyboards and mice. It aims to
bring the features of their proprietary CUE software to the Linux operating
system. This project is currently a work in progress, but it already
supports much of the same functionality, including full RGB animations.


%prep
%setup -q
%patch0 -p1

# Remove the bundled quazip library
rm -rf src/libs/quazip

# Fedora uses /usr/libexec for daemons
sed -e '/^ExecStart/cExecStart=%{_libexecdir}/ckb-next-daemon' -i linux/systemd/ckb-next-daemon.service.in


%build
%cmake -H. -Bbuild \
  -DCMAKE_BUILD_TYPE=Release \
  -DSAFE_INSTALL=OFF \
  -DSAFE_UNINSTALL=OFF \
  -DWITH_SHIPPED_QUAZIP=OFF \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBEXECDIR=libexec \
  -DDISABLE_UPDATER=1
%cmake --build build --target all -- -j build

pushd build
%make_build
popd

# Color freeze fix
sed -e '/^Exec=/cExec=env QT_QPA_PLATFORMTHEME=qt5ct %{_bindir}/ckb-next' -i build/src/gui/ckb-next.desktop


%install
install -Dp -m 755 build/bin/ckb-next  %{buildroot}%{_bindir}/ckb-next
install -Dp -m 755 build/bin/ckb-next-daemon  %{buildroot}%{_libexecdir}/ckb-next-daemon

install -d -m 755 %{buildroot}%{_libexecdir}/ckb-next-animations
for ANIM in $(find src/animations/ -mindepth 1 -maxdepth 1 -type d -printf '%%f '); do
    install -p -m 755 "build/bin/${ANIM}"  "%{buildroot}%{_libexecdir}/ckb-next-animations/${ANIM}"
done

install -Dp -m 0644 %{SOURCE3} %{buildroot}/%{_presetdir}/99-ckb-next.preset
install -Dp -m 644 linux/udev/99-ckb-next-daemon.rules %{buildroot}%{_udevrulesdir}/99-ckb-next-daemon.rules
install -Dp -m 644 linux/systemd/ckb-next-daemon.service.in %{buildroot}%{_unitdir}/ckb-next-daemon.service

install -Dp -m 644 build/src/gui/ckb-next.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/ckb-next.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ build/src/gui/ckb-next.desktop

install -Dp -m 0644 %{SOURCE1}  %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml

install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/ckb-next.1


%post
%systemd_post ckb-next-daemon.service
if [ $1 -eq 1 ]; then
    # starting daemon also at install
    systemctl start ckb-next-daemon.service >/dev/null 2>&1 || :
fi
udevadm control --reload-rules 2>&1 > /dev/null || :


%preun
%systemd_preun ckb-next-daemon.service


%postun
%systemd_postun_with_restart ckb-next-daemon.service
udevadm control --reload-rules 2>&1 > /dev/null || :


%files
%license LICENSE
%doc CHANGELOG.md FIRMWARE README.md
%{_bindir}/ckb-next
%{_libexecdir}/ckb-next-daemon
%{_libexecdir}/ckb-next-animations/
%{_datadir}/applications/ckb-next.desktop
%{_datadir}/metainfo/ckb-next.appdata.xml
%{_datadir}/icons/hicolor/**/apps/ckb-next.png
%{_mandir}/man1/ckb-next.1*
%{_presetdir}/99-ckb-next.preset
%{_udevrulesdir}/*.rules
%{_unitdir}/ckb-next-daemon.service


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.2-3
- Add a patch to fix build failures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.2-1
- Update to latest upstream release

* Tue Aug 27 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.1-1
- Update to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Artur Iwicki <fedora@svgames.pl> - 0.4.0-1
- Update to latest upstream release

* Sat Feb 16 2019 Artur Iwicki <fedora@svgames.pl> - 0.3.2-4
- Use "install -p" (preserve timestamps)
- Do not use the bundled quazip library

* Sat Jan 26 2019 Artur Iwicki <fedora@svgames.pl> - 0.3.2-3
- Tidy up the spec file
- Remove obsolete scriptlets

* Tue Oct 16 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.2-2
- Fixed animations dir

* Sat Oct 13 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.2-1
- Update to 0.3.2 release

* Sun Oct 7 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.1-1
- Update to 0.3.1 release

* Sat Jun 16 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.0-2
- Fixed Epel build
- Fixed animations dir

* Fri Jun 15 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.3.0-1
- Update to 0.3.0 release
- set QT_QPA_PLATFORMTHEME only for binary

* Mon Jan 22 2018 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.9-0.1.20180122git2316518
- Update to latest snapshot.

* Sun Dec 17 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.9.20171217git142b307
- Update to latest snapshot.
- Disable debugsource due to build error with empty file debugsourcefiles.list.

* Fri Nov 17 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.8.20171111gitb88d8be
- Update to latest snapshot.

* Fri Oct 20 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.7.20171014gitda28864
- Update to latest snapshot.

* Sun Aug 20 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.6.20170820git6af2773
- Update to latest snapshot.

* Wed Jul 26 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.5.20170726git9dc8216
- Update to latest snapshot.
- Color change freeze workaround by requiring qt5ct and adding to environment.

* Fri Jul 07 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.4.20170707git1331253
- Update to latest snapshot.

* Fri Jun 23 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.3.20170621gitae7346b
- Update to latest snapshot.

* Thu May 25 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.2.20170525gite54c911
- Fix animation path.
- Update to latest snapshot.

* Thu May 18 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.8-0.1.20170518git5a34841
- Update to 0.2.8 latest snapshot.

* Fri Apr 14 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.7.20170414git565add5
- Added systemd preset.
- Update to latest snapshot.

* Sun Feb 19 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.6.20170219gitb59d179
- Changed package name to ckb-next.
- Update to latest snapshot.

* Sun Jan 22 2017 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.7-0.2.20170120git89e8750
- Update to latest snapshot.

* Thu Dec 1 2016 Johan Heikkila <johan.heikkila@gmail.com> - 0.2.6-0.1
- Created spec file for Fedora based on the Suse spec file
- added appdata file
- added man page

* Thu Aug 25 2016 - aloisio@gmx.com
- Update to version 0.2.6
- Use external quazip only when available
- Replaced ckb-fix-desktop-file.patch with %suse_update_desktop_file
- Replaced ckb-daemon-path.patch and ckb-animations-path.patch with macros \
  for consistency.

* Sun Apr 17 2016 - herbert@graeber-clan.de
- Add hicolor folder, too

* Sun Apr 17 2016 - herbert@graeber-clan.de
- Fix icon folder

* Fri Apr 15 2016 - herbert@graeber-clan.de
- Initial package
- Use /var/run instead of /dev/input for communication with the daemon.
- move the daemon and the animations into the libexec folder
