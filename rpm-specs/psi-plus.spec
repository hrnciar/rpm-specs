%global version_l10n 1.4.636
%global genericplugins attentionplugin autoreplyplugin birthdayreminderplugin chessplugin cleanerplugin clientswitcherplugin conferenceloggerplugin contentdownloaderplugin enummessagesplugin extendedmenuplugin extendedoptionsplugin gnupgplugin gomokugameplugin historykeeperplugin httpuploadplugin icqdieplugin imageplugin imagepreviewplugin jabberdiskplugin juickplugin messagefilterplugin omemoplugin otrplugin pepchangenotifyplugin qipxstatusesplugin screenshotplugin skinsplugin stopspamplugin storagenotesplugin translateplugin videostatusplugin watcherplugin
# %%global unixplugins
%global devplugins pstoplugin ripperccplugin
%global desc_common Psi+ is a development branch of Psi XMPP client.

Summary:        Jabber client based on Qt
Name:           psi-plus
Version:        1.4.654
Release:        6%{?dist}
Epoch:          1

URL:            https://%{name}.com
# GPLv2+ - core of Psi+
# LGPLv2.1+ - iris library, Psi+ widgets, several Psi+ tools
# zlib/libpng - UnZip 0.15 additionnal library
License:        GPLv2+ and LGPLv2+ and zlib
Source0:        https://github.com/%{name}/%{name}-snapshots/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}-l10n/archive/%{version_l10n}.tar.gz#/%{name}-l10n-%{version_l10n}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(qjdns-qt5)
BuildRequires:  qt5-linguist

BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(openssl)
# FIXME drop compatibility to zlic when F29 becomes EOL
# https://src.fedoraproject.org/rpms/psi/blob/master/f/psi.spec#_38
%if 0%{?fedora} && 0%{?fedora} < 30
BuildRequires:  pkgconfig(minizip-compat)
%else
Provides:       bundled(minizip) = 1.2
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libotr)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libsignal-protocol-c)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libtidy-devel

Requires:       %{name}-common = %{epoch}:%{version}-%{release}
Requires:       sox%{?_isa}
Requires:       gnupg
Requires:       qca-qt5-ossl%{?_isa}

Requires:       qca-qt5-gnupg%{?_isa}

Requires:       hicolor-icon-theme

# New Fedora rules allow to use bundled libraries
# https://bugzilla.redhat.com/show_bug.cgi?id=737304#c15
Provides:       bundled(iris)

%description
%{desc_common}

%package        i18n
Summary:        Language packs for Psi
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description    i18n
%{desc_common}
This package adds internationalization to Psi+.

%package        common
Summary:        Noarch resources for Psi+
BuildArch:      noarch

%description    common
%{desc_common}
This package contains huge of base mandatory resources for Psi+.

%package        plugins
Summary:        Plugins pack for Psi+
# GPLv2 is used for the most plugins
# BSD - screenshot plugin
# Beerware - icqdie plugin
License:        GPLv2+ and BSD and Beerware
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
# Filter out plugins from provides
%global __provides_exclude_from ^%{_libdir}/%{name}


%description    plugins
%{desc_common}

 * Attention Plugin
This plugin is designed to send and receive special messages such as
Attentions.

 * Autoreply Plugin
This plugin acts as an auto-answering machine.

 * Birthday Reminder Plugin
This plugin is designed to show reminders of upcoming birthdays.

 * Chess Plugin
This plugin allows you to play chess with your friends.
The plugin is compatible with a similar plugin for Tkabber.

 * Cleaner Plugin
This plugin is designed to clear the avatar cache, saved local copies
of vCards and history logs.

 * Client Switcher Plugin
This plugin is intended to spoof version of the Jabber client, the
name and type of operating system. It is possible to manually specify
the version of the client and the operating system or choose from a
predefined list.

 * Conference Logger Plugin
This plugin is designed to save conference logs in which the Psi+
user sits.

 * Content Downloader Plugin
This plugin can currently be used to download and install roster
iconsets and emoticons.

 * Enum Messages Plugin
The plugin is designed to enumerate messages, adding the messages
numbers in chat logs and notification of missed messages. Supports
per contact on / off message enumeration via the buttons on the chats
toolbar.

 * Extended Menu Plugin
This plugin adds roster submenu 'Extended Actions' to contact's
context menu. At the moment we have the following items: 'Copy JID',
'Copy the nickname', 'Copy the status message' and 'Ping'.

 * Extended Options Plugin
This plugin is designed to allow easy configuration of some advanced
options in Psi+. This plugin gives you access to advanced application
options, which do not have a graphical user interface.

 * GnuPG Key Manager
GnuPG Key Manager can create, remove, export and import GnuPG keys.
It can do only the base operations but I hope it will be enough for
your needs.

 * History Keeper Plugin
This plugin is designed to remove the history of selected contacts
when the Psi+ is closed.

 * HTTP Upload Plugin
This plugin allows uploading images and other files via XEP-0363.

 * ICQ Must Die Plugin
This plugin is designed to help you transfer as many contacts as
possible from ICQ to Jabber.

 * Image Plugin
This plugin is designed to send images to roster contacts.

 * Image Preview Plugin
This plugin shows the preview image for an image URL.

 * Juick Plugin
This plugin is designed to work efficiently and comfortably with the
Juick microblogging service.

 * PEP Change Notify Plugin
The plugin is designed to display popup notifications on change of
moods, activities and tunes at the contacts of the roster. In the
settings you can choose which ones to include notification of events,
specify the time within which a notice will appear, as well as play a
sound specify.

 * Qip X-statuses Plugin
This plugin is designed to display X-statuses of contacts using the
QIP Infium jabber client.

 * Screenshot Plugin
This plugin allows you to make a snapshot (screenshot) of the screen,
edit the visible aria to make a screenshot and save the image to a
local drive or upload to HTTP/FTP server.

 * Stop Spam Plugin
This plugin is designed to block spam messages and other unwanted
information from Psi+ users.

 * Storage Notes Plugin
This plugin is an implementation of XEP-0049: Private XML Storage.
The plugin is fully compatible with notes saved using Miranda IM.
The plugin is designed to keep notes on the jabber server with the
ability to access them from anywhere using Psi+ or Miranda IM.

 * Translate Plugin
This plugin allows you to convert selected text into another language.

 * Video Status Changer Plugin
This plugin is designed to set the custom status when you see the
video in selected video player. Communication with players made by
D-Bus.

 * Skins Plugin
This plugin is designed to create, store and apply skins to Psi+.

 * Off-the-Record Messaging Plugin
a cryptographic protocol that provides strong encryption for instant
messaging conversations. OTR uses a combination of the AES
symmetric-key algorithm, the Diffie–Hellman key exchange, and the SHA-1
hash function. In addition to authentication and encryption, OTR
provides perfect forward secrecy and malleable encryption.

 * PSTO Plugin
Instant bloging service.

 * OMEMO Plugin
A plugin that adds support for OMEMO encryption.


%prep
%autosetup -n %{name}-snapshots-%{version}

# fix rpmlint spurious-executable-perm
find . -name '*.cpp' -or -name '*.h' | xargs chmod 644

# Remove bundled libraries
%if 0%{?fedora} && 0%{?fedora} < 30
rm -rf src/libpsi/tools/zip/minizip
%endif
rm -fr iris/src/jdns

# Psi+ always uses last iris version. So I need to provide bundled
# iris to guarantee efficiency of program.
# rm -fr iris

tar xf %{SOURCE1} -C .


%build
mkdir build
pushd build
%cmake .. \
 -DUSE_ENCHANT=ON \
 -DUSE_HUNSPELL=OFF \
 -DUSE_KEYCHAIN=ON \
 -DENABLE_PLUGINS=ON
popd
%make_build -C build

pushd %{name}-l10n-%{version_l10n}/translations
lrelease-qt5 *.ts
popd


%install
%make_install -C build
install -p -m0644 -D psi.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
for p in 16 32 48 64 128
do
 install -p -m0644 -D iconsets/system/default/psiplus/logo_${p}.png \
 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${p}x${p}/apps/%{name}.png
done

# Install languages
cp -p %{name}-l10n-%{version_l10n}/translations/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}
%find_lang psi --with-qt


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png

%files i18n -f psi.lang

%files plugins
%{_libdir}/%{name}/

%files common
%license COPYING
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/*.qm


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.654-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.654-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Raphael Groner <projects.rg@smart.ms> - 1:1.4.654-4
- drop gmailplugin from description as deprecated

* Sat Apr 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 1:1.4.654-3
- enable OMEMO plugin as we have libsignal-protocol-c now

* Sat Apr 13 2019 Raphael Groner <projects.rg@smart.ms> - 1:1.4.654-2
- apply patch from psi.spec for new minizip pkg in F30+, use bundled instead

* Sat Apr 13 2019 Raphael Groner <projects.rg@smart.ms> - 1:1.4.654-1
- use latest snapshot

* Wed Apr 10 2019 Raphael Groner <projects.rg@smart.ms> - 1:1.4.652-1
- use latest snapshot

* Tue Apr 09 2019 Raphael Groner <projects.rg@smart.ms> - 1:1.4.650-1
- new version
- notice and drop new-history patch merged into psi-im upstream
- mention new URL as wished by upstream
- revert useless cosmetic change to minizip dependency, see 1:1.3.408-2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Patrik Novotný <panovotn@redhat.com> - 1:1.3.408-2
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Wed Aug 22 2018 Raphael Groner <projects.rg@smart.ms> - 1:1.3.408-1
- new version
- modernize generally
- improve packages description
- use cmake
- drop patch for psimedia because it does not work with cmake
- omit omemoplugin due to unmet dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.7.20170612git9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.0-0.6.20170612git9
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.5.20170612git9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Ivan Romanov <drizt@land.ru> - 1:1.0-0.4.20170612git9
- Fix Fedora 27 building

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.3.20170612git9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.2.20170612git9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Ivan Romanov <drizt@land.ru> - 1:1.0-0.1.20170612git9
- Bump version to 1.0 and r9

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.16-0.27.20151216git476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 23 2016 Ivan Romanov <drizt@land.ru> - 1:0.16-0.26.20151216git476
- Just rebuild (#1314900)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.16-0.25.20151216git476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1:0.16-0.24.20151216git476
- use %%qmake_qt5/%%qmake_qt4 macros to ensure proper build flags

* Tue Dec 15 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.23.20151216git476
- Bump to r476
- Add Qt5 support
- Increase minimum qconf version

* Wed Nov 18 2015 Rex Dieter <rdieter@fedoraproject.org> 1:0.16-0.22
- rebuild (tidy)

* Thu Oct 22 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.21.20141205git440
- fixed qjdns BR for F22

* Tue Oct 20 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.20.20141205git440
- set correct plugins permissions
- Filter out plugins from provides

* Mon Oct 19 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.19.20141205git440
- Dropped .R suffix from changelog for Fedora review purposes
- Added license test to common subpackage

* Sat Oct 17 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.18.20141205git440.R
- no %%make_build in epel7
- no qjdns-qt4 in epel7

* Sat Oct 17 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.17.20141205git440.R
- dropped version for bundled iris
- added hicolor-icon-theme to Requires
- fixed post, postun and posttrans scriptlets
- moved noarch resources to common subpackage
- moved desktop-file-validate to %%check section
- use %%global instead of %%define
- preserve timestamp
- use modern %%make_build
- some fixes with licensies
- fixed %%{_libdir}/psi-plus is not owned any package
- fix duplicated /usr/share/psi-plus
- remove bundled jdns
- fix rpmlint spurious-executable-perm

* Wed Oct 14 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.16.20141205git440.R
- use %%license tag

* Tue Oct 13 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.15.20141205git440.R
- provide bundled iris

* Thu Aug 27 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.14.20141205git440.R
- qjdns renamed

* Thu Jun 11 2015 Ivan Romanov <drizt@land.ru> - 1:0.16-0.13.20141205git440.R
- no qca-gnupg in epel7
- use pkgpath(...) style in BR

* Fri Dec  5 2014 Ivan Romanov <drizt@land.ru> - 1:0.16-0.12.20141205git440.R
- updated to r440
- updated history patch
- updated generate-tarball.sh

* Wed Jun 11 2014 Ivan Romanov <drizt@land.ru> - 1:0.16-0.11.20140611git366.R
- updated to r366
- use system qjdns
- dropped obsoletes Group tag

* Tue Jan 28 2014 Ivan Romanov <drizt@land.ru> - 1:0.16-0.10.20140128git271.R
- updated to r271
- updated psi-new-history patch

* Thu Oct 24 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.9.20131024git242.R
- updated to r242
- added libidn to BR
- otr plugin now is stable
- dropped yandexnarod plugin

* Thu Apr 11 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.8.20130412git109.R
- updated to r109

* Mon Feb 11 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.7.20130212git90.R
- updated to r90

* Wed Jan 30 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.6.20130131git75.R
- updated to r75

* Wed Jan 30 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.5.20130131git72.R
- update to r72

* Wed Jan 30 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.4.20130130git71.R
- updated to r71
- changes in psi-plus-psimedia patch

* Thu Jan 24 2013 Ivan Romanov <drizt@land.ru> - 1:0.16-0.3.20130124git61.R
- updated to r61
- added devel plugins. psto and otr.
- uses url for l10n tarball instead of local one
- i18n has no arch
- added libtidy and libotr BR for otrplugin
- added patch to make working psimedia with psi-plus

* Mon Oct 29 2012 Ivan Romanov <drizt@land.ru> - 1:0.16-0.2.20121029git29.R
- updated to r29
- dropped %%defattr

* Sat Oct 27 2012 Ivan Romanov <drizt@land.ru> - 1:0.16-0.1.20121027git21.R
- updated to version 0.16 rev 21
- added many translations
- new i18n subpackage
- improved generate-tarball script
- bundled qca was dropped from upstream

* Mon Jun 25 2012 Ivan Romanov <drizt@land.ru> - 1:0.15-0.25.20120625git5339.R
- update to r5339
- new Gnome3 Support Plugin

* Sat Mar 17 2012 Ivan Romanov <drizt@land.ru> - 1:0.15-0.24.20120314git5253.R
- %%{?dist} allready has R suffix.

* Wed Mar 14 2012 Ivan Romanov <drizt@land.ru> - 1:0.15-0.23.20120314git5253.R
- updated to r5253
- corrected comment for Source0
- added %%{?_isa} to requires
- less rpmlint warnings
- clarified qt version in BuildRequires
- use system minizip
- explicity removed bundled qca
- psi-plus russian translation new home

* Fri Dec 23 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.22.20111220git5157.R
- reverted Webkit
- updated to r5157
- new Yandex Narod plugin
- Video Status plugin now is generic
- new place for tarball

* Fri Nov 18 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.21.20110919git5117.R
- special for RFRemix 16. workaround to fix the bug 804.

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.20.20110919git5117.R
- update to r5117
- dropped buildroot tag
- separated iconsets, skins, sounds and themes to standalone packages
- add generate-tarball scripts to make psi-plus source tarball
- skins plugin merged with plugins
- russian translated moved to github
- dropped README and COPYING from wrong site
- moved source tarball

* Tue Jun 21 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.19.20110621svn4080
- update to r4080
- explaining for licenses
- compile all language files instead of only psi_ru.ts
- dropped useless rm from install stage
- dropped packager
- added checking of desktop file

* Mon May 30 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.18.20110530svn3954
- update to r3954
- now will be used only .bz2 archives insted .gz
- moved psimedia to standalone package
- added skipped %%{?_smp_mflags} to plugins building
- removed unusual desktop-file-utils. Really .desktop file will be
  installed in make install stage
- removed clean stage
- added whiteboarding
- added themes subpackage
- new plugins: Client Switcher, Gomoku Game, Extended Menu,
  Jabber Disk, PEP Change Notify, Video Status
- dropped hint flags from Required

* Wed Jan 19 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.17.20110119svn3559
- all 'psi' dirs and files renamed to 'psi-plus'
- removed conflicts tag
- added psimedia sub-package
- update to r3559

* Sun Jan 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.16.20110110svn3465
- some a bit fixes
- update to r3465

* Sat Dec 18 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.15.20101218svn3411
- update to r3411

* Tue Nov 16 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.14.20101116svn3216
- update to r3216
- removed libproxy from reques

* Mon Nov 01 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.13.20101102svn3143
- update to r3143
- split main package to psi-plus-skins and psi-plus-icons

* Wed Oct 06 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.12.20101006svn3066
- update to r3066
- removed obsoletes tags
- psi-plus now conflicts with psi

* Fri Sep 10 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.11.20100919svn3026
- update to r3026
- added to obsoletes psi-i18n
- added Content Downloader Plugin
- added Captcha Plugin
- remove smiles.

* Thu Aug 12 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.10.20100812svn2812
- update to r2812

* Wed Aug 04 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.9.20100804svn2794
- update to r2794

* Mon Jul 26 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.8.20100726svn2752
- update to r2752

* Mon Jul 5 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.7.20100705svn2636
- fix for working with psimedia
- update to r2636

* Tue Jun 29 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.6.20100629svn2620
- update to r2620

* Fri Jun 04 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.6.20100603svn2507
- fix translations
- update to r2507

* Thu Jun 03 2010 Ivan Romanov <drizt@land.ru> - 0.15-0.5.20100603svn2500
- added skins
- update to r2500

* Thu May 20 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.15-0.4.20100520svn2439
- new Ivan Romanov <drizt@land.ru> build

* Tue Mar 02 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.15-0.3.20100122svn1671
- rebuilt with openssl

* Sat Jan 30 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.15-0.20100122svn1671
- initial Psi+ build
