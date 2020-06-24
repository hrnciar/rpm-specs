
#global snap 20180119
# include -updater applet subpkg or not
#global updater 1

Name:    apper
Summary: KDE interface for PackageKit
Version: 1.0.0
Release: 6%{?dist}

License: GPLv2+
%if 0%{?snap:1}
Source0: apper-%{version}-%{snap}git.tar.xz
%else
Source0: apper-%{version}.tar.xz
#Source0: http://download.kde.org/stable/apper/%{version}/src/apper-%{version}.tar.xz
%endif
URL:     https://cgit.kde.org/apper.git

## upstream patches
Patch1: 0001-Install-apper-binary-as-TARGET-instead-of-PROGRAM.patch
Patch2: 0002-Fix-build-without-AppStream.patch
Patch3: 0003-Fix-compilation-when-EDIT_ORIGNS_DESKTOP_NAME-is-def.patch
Patch4: 0004-Update-AppStream-metadata.patch

## upstreamable patches
Patch100: apper-1.0.0-qt511.patch

Obsoletes: kpackagekit < 0.7.0
Provides:  kpackagekit = %{version}-%{release}
# required because gnome-packagekit provides exactly the same interface
Provides: PackageKit-session-service

%if ! 0%{?updater}
Obsoletes: apper-updater < %{version}-%{release}
%endif

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: cmake(KDED)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5IconThemes)

BuildRequires: cmake(LibKWorkspace)

BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(AppStreamQt)
BuildRequires: cmake(packagekitqt5) >= 1.0.0

BuildRequires: pkgconfig(dbus-1)

Requires: PackageKit

%description
KDE interface for PackageKit.

%package updater
Summary: Apper plasma updater applet
Requires: %{name} = %{version}-%{release}
%description updater
%{summary}.


%prep
%autosetup -p1

%if 0%{?updater}
# disable update applet by default
sed -i \
  -e 's|X-KDE-PluginInfo-EnabledByDefault=.*|X-KDE-PluginInfo-EnabledByDefault=false|g' \
  plasmoid/package/metadata.desktop
%endif


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  %{?appstream:-DAPPSTREAM:BOOL=ON} \
  -DAUTOREMOVE:BOOL=OFF \
  -DBUILD_PLASMOID=%{?updater:ON}%{?!updater:OFF}
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# hack around gnome-packagekit conflict
mv %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service \
   %{buildroot}%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.apper.desktop ||:


%files
%doc TODO
%license COPYING
%{_kf5_bindir}/apper
%{_kf5_datadir}/apper/
%{_kf5_datadir}/applications/org.kde.apper.desktop
%{_kf5_datadir}/applications/org.kde.apper_installer.desktop
%{_kf5_datadir}/applications/org.kde.apper_settings.desktop
%{_kf5_datadir}/applications/org.kde.apper_updates.desktop
%{_kf5_libdir}/apper/
%{_libexecdir}/apper-pk-session
%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service
%{_kf5_qtplugindir}/kded_apperd.so
%{_kf5_datadir}/kservices5/kded/apperd.desktop
%{_kf5_datadir}/apperd/
%{_mandir}/man1/apper.1*
%{_kf5_metainfodir}/org.kde.apper.appdata.xml

%if 0%{?updater}
%files updater
%{_kf5_datadir}/kservices5/plasma-applet-org.packagekit.updater.desktop
%{_kf5_datadir}/plasma/plasmoids/org.packagekit.updater/
%endif


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-3
- pull in upstream fixes
- drop deprecated scriptlets
- drop rpath hacks (no longer needed)
- qt511.patch

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- 1.0.0 (v1.0.0 tag)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-0.3.20180119
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.20180119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.1.20180119
- apper-1.0.0 snapshot, PackageKit-Qt-1.0 support

* Thu Dec 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.11.20171102
- refresh snapshot (20171102)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-0.10.20170226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-0.9.20170226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.8.20170226
- apper: K4AboutData::appName crasher (#1383747)

* Wed Mar 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.7.20170226
- fresh snapshot, includes theming fix
- omit broken -updater subpkg (for now at least)
- update URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-0.6.20161109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.5.20161109
- apper crashes on startup (#1400011, kde#372292)

* Thu Nov 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.4.20161109
- 20161109 snapshot, namespaced appdata/.desktop
- Recommends: qt5-style-oxygen, support APPER_NO_STYLE_OVERRIDE env

* Tue Sep 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.3.20160329
- restore rpath hack

* Tue Jul 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.2.20160329
- %%check: verify rpath

* Thu Jun 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-0.1.20160329
- master/ branch snapshot, kf5-based

* Thu May 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.2-6
- hard-code style (plastique/oxygen) to workaround UI glitches (#1209017)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-4
- (unversioned) Requires: kde-runtime

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-3
- rebuild (PackageKit-Qt)

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-2
- .spec cosmetics, use %%license, (explicitly) Requires: PackageKit

* Wed Oct 28 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-1
- 0.9.2, upstream patches

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-11
- omit kded/apperd on plasma5/f22+

* Tue Apr 28 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-10
- use cache_age for updater applet too (#1188207)

* Mon Apr 27 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-9
- Apper won't check for updates (#1188207)

* Wed Apr 22 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-8
- Requires: plasma-pk-updates (#1214397)
- use %%{?kde_runtime_requires} macro

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-7
- omit plasma4-based updater applet (f22+)

* Tue Jan 13 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-6
- disable appstream support (#1180819)

* Mon Dec 15 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-5
- Your current backend does not support installing files (#1167018)

* Mon Dec 15 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-4
- update URL: (use projects.kde.org)

* Sat Dec 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-3
- don't try !allow_deps, -yum,-hif backends do not support it apparently (#877038,kde#315063)

* Tue Oct 28 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-2
- pull in some upstream fixes

* Tue Aug 26 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-1
- apper-0.9.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-3
- rebuild (appstream)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- apper-0.9.0

* Sat Apr 26 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.3-0.3.20140426
- respin with translations

* Sat Apr 26 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.3-0.2.20140426
- 0.8.3 20140426 snapshot, fixed appstream support, sans translations (kde svn down)

* Tue Apr 22 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.3-0.1.20140422
- 0.8.3 20140422 snapshot compatible with PK-0.9 (#1089630)

* Sat Apr 19 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-5
- rebuild (PackageKit-Qt)

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-4
- enable appstream support (#1026118)

* Sun Nov 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.8.1-3
- pull in some upstream fixes
- get ready to enable appstream support (#1026118)

* Mon Aug 26 2013 Lukáš Tinkl <ltinkl@redhat.com> 0.8.1-2
- fix translations in the updater applet

* Tue Jul 30 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-1
- 0.8.1 (final)

* Mon Jun 24 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-0.4.20130624
- 0.8.1 20130624 snapshot

* Mon May 20 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-0.3.20130511
- test kded crasher fix (kde#319967)

* Mon May 13 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-0.2.20130511
- don't run apper applet on live image (#948099)

* Sat May 11 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-0.1.20130511
- 0.8.1 201305011 snapshot

* Mon Apr 29 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-5
- respin previous patch to use kDebug instead

* Mon Apr 29 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-4
- Apper ignores "never check for updates" option (#948099)

* Wed Feb 13 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-3
- a few more upstream fixes

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-2
- pull in a few upstream fixes, including followup for kde#302786

* Tue Jan 08 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

* Sat Jan 05 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.13.20121231git
- Problems with the display of software origins (#891294)

* Tue Jan 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.8.0-0.12.20121231git
- 20121231 snapshot
- enable apper updater systray applet

* Mon Nov 26 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.11.20121126git
- 20121126git snapshot
- use PackageKit-Qt

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.10.20121102git
- 20121102git snapshot

* Tue Oct 30 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.9.20121024git
- 20121024git snapshot (for pk-0.8.5)

* Mon Oct 15 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.8.0-0.8.20121002git
- drop systemd_inhibit (here at least, PK or elsewhere is better)
- Apper: cannot perform system update (#866486)

* Tue Oct 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.7.20121002git
- 20121002git snapshot
- initial systemd_inhibit support (#830181)
- displays wrong warning when no updates are available (#851864)

* Fri Sep 07 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.6.20120724git
- add scriptlet to register mimetypes (#836559)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-0.4.20120724git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.3.20120724git
- 20120724git snapshot

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.2.20120628git
- rebuild

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-0.1.20120628git
- apper-0.8.0 snapshot

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-2
- rebuild (PackageKit)

* Mon May 21 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-1
- apper-0.7.2

* Mon May 7 2012 Lukáš Tinkl <ltinkl@redhat.com> 0.7.1-5
- respect the settings and don't check for updates when on battery

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-4
- rebuild (PackageKit-qt)

* Sat Apr 21 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-3
- more work on wakeups, kudos to Martin Kho (#752564)

* Mon Apr 16 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-2
- "Unsigned packages" popup constantly reappears (#806508)
- Apper wakes up yumBackend.py every 5 to 10 minutes (#752564)

* Tue Feb 21 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-1
- 0.7.1 (final)

* Sat Feb 18 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-0.7.20120218
- 20120218 snapshot (#749240, #753146, #781726)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.6.20111102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-0.5.20111102 
- 20111102 snapshot

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.4.20111021
- Rebuilt for glibc bug#747377

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-0.3.20111021
- 20111021 snapshot, checkbox fixes, translations.

* Thu Oct 20 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-0.2.20111020
- fresher snapshot, more fixes upstream.  mmm, mmm, good.

* Thu Oct 20 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-0.1.20111020
- 0.7.1 20111020 snapshot (with better fix for hack in 0.7.0-5)

* Wed Oct 19 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-5
- hack around crash on installing standalone rpms

* Wed Oct 19 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-4
- systray_actions patch/hack

* Mon Oct 17 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-3
- apper.desktop: Exec=apper %%F (not %%U, it only handles files, not urls)

* Mon Oct 17 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-2
- -DAUTOREMOVE:BOOL=OFF (#727788)

* Tue Oct 11 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-1
- kpackagekit -> apper

* Mon Aug 01 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.6.3.3-3
- support the InstallResources interface, in particular for Plasma services
- bump minimum PackageKit version to 0.6.16 to support the above

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> 0.6.3.3-1
- 0.6.3.3 release

* Thu Dec 23 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3.2-2
- show version information by default (#665372)
- show arch information by default (on multilib-capable archs)
- upstream patch for issues found by valgrind

* Thu Dec 23 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3.2-1
- 0.6.3.2 release

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3-3
- fix for software_sources category
- fix reported version

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3-2
- fix/improve browsing pk categories

* Tue Dec 21 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3-1
- kpk-0.6.3

* Wed Dec 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.6.3-0.2.20101214
- fetch translations from SVN

* Tue Dec 14 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3-0.1.20101214
- 0.6.3 snapshot (sans translations)

* Tue Oct 12 2010 Steven M. Parrish <smparrish@gmail.com> 0.6.2-1
- New upstream release

* Tue Sep 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 0.6.1-2
- fix wrong i18n() usage in a patch resulting in broken translations

* Tue Sep 07 2010 Steven M. Parrish <smparrish@gmail.com> - 0.6.1-1
- New upstream release

* Fri Mar 26 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.0-2
- rebase InstallPrinterDrivers patch
- readd disttag

* Fri Mar 26 2010 Steven M. Parrish <smparrish@gmail.com> - 0.6.0-1
- Official 0.6.0 release

* Wed Mar 24 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.0-0.9.20100301svn
- add support for automatic printer driver installation (Tim Waugh, #576615)

* Sat Mar 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-0.8.20100301svn
- add minimal kdelibs4 runtime dependency

* Tue Mar 02 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.0-0.7.20100301svn
- update to 20100301 SVN snapshot

* Fri Feb 26 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.0-0.6.20100223svn
- update to 20100223 SVN snapshot
- include translations again

* Wed Feb 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-0.5.r1095080
- r1095080

* Wed Feb 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-0.4.20100224
- fresh 20100224 svn snapshot

* Fri Feb 05 2010 Richard Hughes  <rhughes@redhat.com> - 0.6.0-0.3.20100111
- Add Provides: PackageKit-session-service
- Resolves #561437

* Thu Jan 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-0.2.20100111
- File conflict between kpackagekit and gnome-packagekit (#555139)

* Mon Jan 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-0.1.20100111
- kpk-0.6.0 2001-01-11 snapshot

* Mon Jan 11 2010 Richard Hughes  <rhughes@redhat.com> - 0.5.2-3
- Rebuild for PackageKit-qt soname bump

* Thu Dec 10 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.2-2
- Clean up spec file 

* Mon Dec 07 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.2-1
- New upstream release

* Thu Nov 19 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.1.1-2
- Remove no longer need patches

* Tue Nov 17 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.1.1-1
- New upstream release fixes #531447, #533755, #536930

* Sat Oct 31 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0.3-1
- Official 0.5.0.3 release

* Sun Oct 25 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0.2-1
- Official 0.5.0.2 release

* Tue Oct 20 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0.1-1
- Official 0.5.0.1 release
- Includes patch to fix (#469375) default/none issue

* Tue Sep 15 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-0.1.20090915svn
- New git snapshot

* Tue Sep 08 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-0.1.20090908svn
- New git snapshot, disable history

* Wed Sep 02 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-0.1.20090902svn
- New git snapshot

* Mon Aug 24 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-0.1.20090824svn
- New git snapshot

* Wed Aug 19 2009 Steven M. Parrish <smparrish@gmail.com> - 0.5.0-0.1.20090819svn
- New upstream release with PolicyKit 1 integration

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Steven M. Parrish <smparrish@gmail.com> 0.4.1.1-3
- Now includes Sloval(sk) translations

* Tue Jul 7 2009 Steven M. Parrish <smparrish@gmail.com> 0.4.1.1-2
- rebuild for new packagekit

* Thu Jun 11 2009 Steven M. Parrish <smparrish@gmail.com> 0.4.1.1-1
- Fixed all krazy issues (2 or 3 not much important changed in backend details)
- With KDE >= 4.2.3 persistent notifications are working again so the code to use it was commented out
- Getting duplicated updates was trully fixed
- Added "details" button on error notifications

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-3
- apply awol InitialPreference patch

* Fri Jun 05 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.4.1-2
- Added missing translations

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-1
- min pk_version 0.4.7
- touchup %%files
- highlight missing translations during build (but make it non-fatal)
- drop upstreamed patches

* Fri Jun 05 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 0.4.1-0
- New upstream release.  Fixes compatibility with Packagekit 0.4.8 (#503989)

* Tue Apr 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 0.4.0-7
- upstream patch to fix catalog loading (#493061)

* Thu Apr 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-6
- make update notification persistent (#485796)

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 0.4.0-5
- another respun tarball to fix using those translations (#493061)

* Tue Mar 17 2009 Lukáš Tinkl <ltinkl@redhat.com> - 0.4.0-4
- respun (fixed) tarball with translations included

* Mon Mar 09 2009 Richard Hughes  <rhughes@redhat.com> - 0.4.0-3
- Rebuild for PackageKit-qt soname bump

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 0.4.0-1
- Official 0.4.0 release

* Fri Feb 06 2009 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-0.2.20090128svn
- workaround: mime-type/extension binding for .rpm is wrong (#457783)

* Wed Jan 28 2009 Steven M. Parrish <smparrish@shallowcreek.net> 0.4.2-0.1.20090128svn
- Corrected release tag

* Wed Jan 28 2009 Steven M. Parrish <smparrish@shallowcreek.net> 0-0.1.20090128svn
- Corrected release tag

* Wed Jan 28 2009 Steven M. Parrish <smparrish@shallowcreek.net> 0.4.2-svn.1
- SVN build to solve compatibility issues with packagekit 0.4.2

* Wed Nov 26 2008 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-6
- respin (PackageKit)
- spec cleanup

* Sat Nov 01 2008 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-5
- use PackageKit's FindQPackageKit.cmake

* Tue Oct 21 2008 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-4
- build against PackageKit-qt

* Mon Oct 20 2008 Rex Dieter <rdieter@fedoraproject.rog> 0.3.1-3
- patch kpackagekit.desktop (guessed correct X-DBUS-ServiceName value), 
- fixes: KDEInit could not launch "/usr/bin/kpackagekit"
- cleanup %%files

* Thu Oct 16 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.1-2
- Fix build error

* Thu Oct 16 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.1-1
- New upstream release

* Mon Sep 29 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-1
- Official 0.1 release

* Sun Aug 24 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.3.b4
- Excluded underdevelopment binaries and associated files 

* Fri Aug 22 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.2.b4
- Adding missing files

* Tue Aug 19 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.1.b4
- New upstream release

* Fri Aug 01 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.5.b3
- Corrected SPEC file regression

* Thu Jul 31 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.4.b3
- Changed wording on serveral windows to make them better understood

* Thu Jul 24 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.3.b3
- Removed additional uneeded BRs

* Tue Jul 22 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.2.b3
- Removed uneeded BRs
- Made use of predefined macros

* Wed Jul 16 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.1-0.1.b3
- Initial SPEC file
