# git source
# https://cgit.kde.org/smb4k.git/
# bug tracker
# https://phabricator.kde.org/project/view/95/
%global optflags %(echo %{optflags} -Wl,--as-needed )
%global _kf5_iconsdir %{_datadir}/icons

Name:       smb4k
Version:    3.0.6
Release:    1%{?dist}
Summary:    The SMB/CIFS Share Browser for KDE

License:    GPLv2+
URL:        http://smb4k.sourceforge.net/
Source0:    http://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz

BuildRequires:  cmake3 >= 2.6.0
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  libsmbclient-devel
Requires:   samba-client
Requires:   cifs-utils

%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}

# on F15 we need remove old smb4k-devel
Obsoletes: smb4k-devel < 1.0.0
Obsoletes: kde-plasma-smb4k < 2.0.0


%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.


%prep
%autosetup -p 1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} -Wno-dev ..
popd

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
# delete devel .so
rm %{buildroot}%{_kf5_libdir}/libsmb4kcore.so

# Already have Categories=Qt;KDE;Utility;
# add-category Network, because is Network application, search and map SMB/CIFS shares of LAN.
desktop-file-install \
    --add-category Network \
    --delete-original \
    %{buildroot}%{_kf5_datadir}/applications/org.kde.smb4k.desktop

#workaround for bug https://bugzilla.redhat.com/show_bug.cgi?id=1584944
sed -i  %{buildroot}/%{_kf5_metainfodir}/*.appdata.xml -e 's/type="stock"//'

appstream-util validate-relax --nonet %{buildroot}/%{_kf5_metainfodir}/*.appdata.xml

# please look into kdenlive.spec to add --with-html on epel7
%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog README
%license COPYING
%{_kf5_datadir}/dbus-1/system.d/org.kde.%{name}.mounthelper.conf
%{_kf5_bindir}/%{name}*
%{_kf5_libdir}/libsmb4kcore.so.*
%{_kf5_datadir}/kconf_update/*
%{_kf5_datadir}/dbus-1/system-services/org.kde.%{name}.mounthelper.service
%{_kf5_datadir}/polkit-1/actions/org.kde.%{name}.mounthelper.policy
%{_qt5_plugindir}/*.so
%{_kf5_libexecdir}/kauth/mounthelper
%{_kf5_datadir}/applications/org.kde.smb4k.desktop
%{_kf5_datadir}/config.kcfg/%{name}.kcfg
%{_kf5_datadir}/kxmlgui5/%{name}/
%{_kf5_datadir}/knotifications5/%{name}.notifyrc
%{_kf5_datadir}/kservices5
%{_kf5_iconsdir}/hicolor/*/apps/smb4k.png
%{_kf5_iconsdir}/oxygen/*/apps/smb4k.png
%{_kf5_metainfodir}/*.appdata.xml
%{_kf5_qmldir}/org/kde/smb4k/
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/

%changelog
* Thu Jun 04 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6 (#1843775)

* Tue May 12 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.0.5-1
- Update to 3.0.5 (#1823635)

* Sun Mar 08 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3 (#1811413)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Sérgio Basto <sergio@serjux.com> - 3.0.2-1
- Update to 3.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Sérgio Basto <sergio@serjux.com> - 3.0.1-1
- Update smb4k to 3.0.1

* Sun Apr 28 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.1-3
- Rebuild for libQt5.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Sérgio Basto <sergio@serjux.com> - 2.1.1-1
- Update to 2.1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Sérgio Basto <sergio@serjux.com> - 2.1.0-1
- Update to 2.1.0 (#1515014)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-2
- Remove obsolete scriptlets

* Thu Aug 24 2017 Sérgio Basto <sergio@serjux.com> - 2.0.2-1
- Update smb4k to 2.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Sérgio Basto <sergio@serjux.com> - 2.0.1-2
- Obsolete the old kde-plasma-smb4k and require qt5-qtbase

* Sat May 20 2017 Sérgio Basto <sergio@serjux.com> - 2.0.1-1
- Update smb4k to 2.0.1, copied from Mageia rpm spec

* Fri May 19 2017 Sérgio Basto <sergio@serjux.com> - 1.2.3-1
- Update smb4k to 1.2.3

* Wed May 10 2017 Than Ngo <than@redhat.com> - 1.2.2-3
- security fix for CVE-2017-8849

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Sérgio Basto <sergio@serjux.com> - 1.2.2-1
- New upstream vesion, 1.2.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Sérgio Basto <sergio@serjux.com> - 1.2.1-2
- Only use update-desktop-database when a desktop entry has a MimeType key.
  http://fedoraproject.org/wiki/Packaging:ScriptletSnippets#desktop-database

* Fri Oct 16 2015 Sérgio Basto <sergio@serjux.com> - 1.2.1-1
- Update to 1.2.1

* Sun Jul 05 2015 Sérgio Basto <sergio@serjux.com> - 1.2.0-4
- Doesn't force installation of kde-plasma-smb4k in F22+ because only work with
  plasma 4 (F21) .

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Sérgio Basto <sergio@serjux.com> - 1.2.0-2
- Fix mixed-use-of-spaces-and-tabs.
- Fix desktop-file-install sriptlet.
- Fix license tag.
- Removed trailing spaces.
- Removed libsmb4kcore.so (devel-file) reverts fix of internal broken dependencies.
- Update smb4k.appdata.xml in smb4k-1.2.0_fixbuild.patch .
- Added a subpackage with kde-plasma-smb4k.
- Fixed unused-direct-shlib-dependency in cmake with global optflags.

* Sun Apr 19 2015 Sérgio Basto <sergio@serjux.com> - 1.2.0-1
- Update to 1.2.0
- Added AppData https://fedoraproject.org/wiki/Packaging:AppData
- Added patch to fix build already upstreamed.

* Mon Jan 05 2015 Sérgio Basto <sergio@serjux.com> - 1.1.4-1
- New bug fix release.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Sérgio Basto <sergio@serjux.com> - 1.1.2-1
- New upstream release.

* Fri Mar 28 2014 Sérgio Basto <sergio@serjux.com> - 1.1.1-2
- Fix internal broken dependencies.

* Thu Mar 27 2014 Sérgio Basto <sergio@serjux.com> - 1.1.1-1
- Update to Smb4K 1.1.1, the first bug fix release of the stable 1.1 branch.
  This release fixes a crash bug and a potential security issue (rhbz #1079820)

* Sat Nov 09 2013 Sérgio Basto <sergio@serjux.com> - 1.0.9-1
- Update 1.0.9, bugfix release.

* Sat Oct 26 2013 Sérgio Basto <sergio@serjux.com> - 1.0.8-1
- Update to 1.0.8, bugfix release.
- Fix some dates.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Sérgio Basto <sergio@serjux.com> - 1.0.7-1
- Update to 1.0.7, bugfix release.

* Sun Mar 10 2013 Sérgio Basto <sergio@serjux.com> - 1.0.6-1
- New upstream and bugfix release.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Sérgio Basto <sergio@serjux.com> - 1.0.5-1
- New upstream release.

* Wed Sep 26 2012 Sérgio Basto <sergio@serjux.com> - 1.0.4-1
- New upstream release.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Sérgio Basto <sergio@serjux.com> 1.0.2
- New upstream release.

* Thu May 31 2012 Sérgio Basto <sergio@serjux.com> 1.0.1-8
- add patch to fix several bugs, from upcoming release 1.0.2.

* Mon May 07 2012 Sérgio Basto <sergio@serjux.com> 1.0.1-7
- add requires cifs-utils, to have mount.cifs

* Thu Apr 19 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-6
- remove some assumptions about qreal = double

* Tue Apr 10 2012 Sérgio Basto <sergio@serjux.com> - 1.0.1-5
- Obsoletes: smb4k-devel for F15.

* Mon Apr 2 2012 Sérgio Basto <sergio@serjux.com> - 1.0.1-4
- a little review.

* Wed Mar 28 2012 Sérgio Basto <sergio@serjux.com> - 1.0.1-3
- new review.

* Tue Mar 27 2012 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- review
- remove devel subpackage

* Sat Mar 24 2012 Sérgio Basto <sergio@serjux.com> - 1.0.1-1
- New upstream version 1.0.1
- some cleanups for fedora-review.

* Sun Dec 4 2011 Sérgio Basto <sergio@serjux.com> - 0.10.12-1
- update to 0.10.12
- drop qtstring upstreamed patch.

* Thu Dec 1 2011 Sérgio Basto <sergio@serjux.com> - 0.10.11-1
- update to 0.10.11
- patch a qtstring to fix a compile error.
- update homepage project and url source.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Marcin Garski <mgarski[AT]post.pl> 0.10.7-1
- Update to 0.10.7 (fix #574904)

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.10.4-2
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sat Oct 24 2009 Marcin Garski <mgarski[AT]post.pl> 0.10.4-1
- Update to 0.10.4
- Proper update of sudoers (#527401)
- Add kdesu to Requires (#499720)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 0.10.2-1
- Update to 0.10.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Marcin Garski <mgarski[AT]post.pl> 0.10.1-1
- Update to 0.10.1

* Thu Sep 04 2008 Marcin Garski <mgarski[AT]post.pl> 0.10.0-2
- Update to 0.10.0

* Wed Jul 30 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.6-1
- Update to 0.9.6

* Mon Jun 02 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.5-1
- Update to 0.9.5

* Tue Apr 29 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.4-1
- Update to 0.9.4

* Sat Mar 01 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.3-2
- Include .la files (bug #435149)

* Tue Feb 26 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.3-1
- Update to 0.9.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-4
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.2-3
- Update to 0.9.2
- Don't compile Konqueror plugin

* Sat Dec 08 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-3
- Fix BR's to compile on rawhide

* Sun Dec 02 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-2
- Add qt-devel to BR

* Sun Dec 02 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-1
- Update to 0.8.7

* Sun Nov 11 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.6-1
- Update to 0.8.6

* Thu Sep 27 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.5-1
- Update to 0.8.5

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.4-2
- Fix license tag

* Fri Aug 03 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.4-1
- Update to 0.8.4
- Preserve upstream .desktop vendor

* Thu May 03 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.3-1
- Updated to version 0.8.3

* Tue May 01 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.2-1
- Updated to version 0.8.2
- Spec file cleanup

* Tue Apr 10 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.1-1
- Updated to version 0.8.1

* Mon Jan 01 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.0-1
- Updated to version 0.8.0

* Tue Nov 28 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.5-1
- Updated to version 0.7.5

* Tue Nov 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.4-1
- Updated to version 0.7.4

* Wed Sep 27 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.3-1
- Updated to version 0.7.3

* Fri Sep 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.2-2
- Rebuild for Fedora Core 6
- Spec tweak

* Fri Aug 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.2-1
- Updated to version 0.7.2

* Mon Jun 19 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.1-1
- Updated to version 0.7.1
- Drop smb4k-0.6.5-desktop.patch (merged upstream)

* Tue Apr 25 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.0-1
- Updated to version 0.7.0, comment --enable-final

* Tue Apr 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.10-1
- Updated to version 0.6.10

* Fri Mar 24 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.9-1
- Updated to version 0.6.9

* Fri Feb 24 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.8-1
- Updated to version 0.6.8

* Fri Feb 17 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-4
- Updated smb4k-0.6.8-mount.patch

* Fri Feb 17 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-3
- Add support of mount.cifs/umount.cifs (bug #181638)
- Remove smb4k-0.6.5-buff.patch

* Tue Feb 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-2
- Rebuild

* Wed Feb 08 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-1
- Updated to version 0.6.7

* Wed Feb 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-5
- Fix GCC warnings
- Don't own KDE directories

* Wed Jan 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-4
- Remove libxml2 from BR
- Add workaround for broken libtool archive (made by Dawid Gajownik)

* Sun Jan 15 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-3
- Get rid of desktop-file-utils
- Add --disable-dependency-tracking & --enable-final

* Thu Jan 12 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-2
- Add kdebase-devel to BuildRequires

* Wed Jan 11 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-1
- Updated to version 0.6.5 && spec cleanup for FE

* Sun Sep 05 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.1a-1.fc2
- Updated to version 0.4.1a

* Tue Aug 31 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.1-1.fc2
- Updated to version 0.4.1

* Wed Jun 02 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-3.fc2
- Rebuild for Fedora Core 2

* Thu May 06 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-2
- Convert pl.po to UTF-8

* Thu May 06 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-1
- Update to 0.4.0

* Wed Jan 21 2004 Marcin Garski <mgarski[AT]post.pl> 0.3.2-1
- Rebuild for Fedora Core 1

* Thu Dec 18 2003 Marcin Garski <mgarski[AT]post.pl> 0.3.1-3
- Cleanup specfile

* Fri Nov 28 2003 Marcin Garski <mgarski[AT]post.pl> 0.3.1-2
- Initial specfile based on specfile by Ian Geiser <geiseri[AT]msoe.edu>
