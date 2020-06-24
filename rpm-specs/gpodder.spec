Name:           gpodder
Version:        3.10.16
Release:        1%{?dist}
Summary:        Podcast receiver/catcher written in Python

License:        GPLv3+ and LGPLv2+
URL:            http://gpodder.org
Source0:        https://github.com/gpodder/gpodder/archive/%{version}/gpodder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel, python3-feedparser
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  help2man
#Requires:       python-gpod, python-eyed3 #re-enable once Python 3 support exists.
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-podcastparser
Requires:       python3-imaging
Requires:       python3-mygpoclient
Requires:       hicolor-icon-theme
Requires:       youtube-dl
%description
gPodder is a Podcast receiver/catcher written in Python, using GTK. 
It manages podcast feeds for you and automatically downloads all 
podcasts from as many feeds as you like.
It also optionally supports syncing with ipods.

%prep
%setup -qn %{name}-%{version}

#drop examples for now
rm -rf share/gpodder/examples

%build
make messages


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                 \
  --remove-key Miniicon --add-category Application              \
  --remove-category FileTransfer --remove-category News         \
  --remove-category Network                                     \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://bugs.gpodder.org/show_bug.cgi?id=1846
SentUpstream: 2013-10-07
-->
<application>
  <id type="desktop">gpodder.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>gPodder</name>
  <summary>Manage and download podcasts</summary>
  <description>
    <p>
      gPodder lets you manage your Podcast subscriptions, discover new content
      and download episodes to your devices.
    </p>
    <p>
      You can also take advantage of the service gpodder.net, which lets
      you sync subscriptions, playback progress and starred episodes.
    </p>
  </description>
  <url type="homepage">http://gpodder.org/</url>
  <screenshots>
    <screenshot type="default">http://gpodder.org/images/full_desktop.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
  <project_group>GNOME</project_group>
</application>
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README.md
%{_bindir}/%{name}
%{_bindir}/gpo
%{_bindir}/%{name}-migrate2tres
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/metainfo/org.gpodder.gpodder.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gpodder.service
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.16-1
- 3.10.16

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.10.15-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.15-1
- 3.10.15

* Tue Apr 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.14-1
- 3.10.14

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.13-1
- 3.10.13

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.12-1
- 3.10.12

* Mon Sep 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.11-1
- 3.10.11

* Fri Sep 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.10-1
- 3.10.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.10.9-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.9-1
- 3.10.9

* Wed Jun 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.8-1
- 3.10.8

* Sat Feb 02 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.10.7-1
- 3.10.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.10.6-1
- 3.10.6.

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.5-1
- 3.10.5.

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.4-1
- 3.10.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Todd Zullinger <tmz@pobox.com> - 3.10.2-3
- Avoid python 3.7 "async" keyword

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.10.2-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.2-1
- 3.10.2

* Mon May 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.1-2
- Bump EVR for f28 release issue.

* Tue Feb 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.1-1
- 3.10.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.0-2.1
- Patch for opml error.

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.0-2
- Remove obsolete scriptlets

* Tue Jan 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.0-1
- 3.10.0, move to Python 3.

* Mon Dec 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.9.5-1
- 3.9.5 prerelease.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.3-1
- 3.9.3

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.2-1
- 3.9.2
- Requires python2-podcastparser

* Thu Sep 01 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.1-1
- 3.9.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-3
- Fix directory ownership.

* Tue Jun 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-2
- Drop pywebkitgtk.

* Thu Feb 04 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-1
- 3.9.0, BZ 1304554.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Jon Ciesla <limburgher@gmail.com> - 3.8.5-1
- 3.8.5.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Jon Ciesla <limburgher@gmail.com> - 3.8.4-1
- 3.8.4.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.8.3-2
- Add an AppData file for the software center

* Fri Nov 21 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.3-1
- 3.8.3.

* Wed Oct 29 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.2-1
- 3.8.2.

* Wed Jul 30 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.0-1
- 3.8.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Jon Ciesla <limburgher@gmail.com> - 3.7.0-1
- 3.7.0.

* Mon Mar 17 2014 Jon Ciesla <limburgher@gmail.com> - 3.6.1-1
- 3.6.1.

* Mon Mar 03 2014 Jon Ciesla <limburgher@gmail.com> - 3.6.0-1
- 3.6.0.

* Wed Jan 29 2014 Jon Ciesla <limburgher@gmail.com> - 3.5.2-1
- 3.5.2.
- Date fixups.
- License tag fixup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.20.3-1
- 2.20.3.
- Drop desktop vendor tag.
- Youtube patch upstreamed.

* Mon Feb  4 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.20.2-2
- Patch for compatibility with pyhton-pillow as well as python-imaging

* Tue Oct 09 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20.2-1
- New upstream release
- Add patch from git master to fix Youtube feeds

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20.1-1
- New upstream release
- Update project and source URLs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20-1
- New upstream release
- Remove the INSTALL file from the docs

* Fri Sep 16 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.19-1
- New upstream release

* Sun Aug 14 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.18-1
- New upstream release

* Sat Aug 06 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.17-1
- New upstream release

* Sat Jul 23 2011 Matěj Cepl <mcepl@redhat.com> - 2.16-1
- New upstream release

* Wed May 18 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.15-1
- New upstream release
- Remove dependency on gstreamer-python. Upstream removed gstreamer track
  length detection because it was too crashy.

* Sat Apr 23 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.14-1
- New upstream release, remove upstreamed patches

* Wed Mar 02 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.13-2
- Add patch to fix problems if there is no active podcast (rhbz #681383,
  gPodder #1291)
- Add patch to fix invalid UTF-8 text in podcast descriptions (gPodder #1277)

* Wed Feb 23 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.13-1
- New upstream release, remove upstreamed patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.12-2
- Add patch to fix encoding issues in minidb (rhbz #674758, gPodder #1088)

* Sat Jan 15 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.12-1
- New upstream release
- Add patch to fix exception handling in the 'gpo' command line utility
  (rhbz #668284, gPodder #1264)
- Add patch to fix youtube search (Maemo #11756)
- Require python-pymtp for MTP support

* Mon Dec 20 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.11-1
- New upstream release

* Sat Dec 18 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.10-1
- New upstream release

* Tue Oct 12 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.9-1
- New upstream release
- Remove unneeded patch
- Add patch to use systemwide pymtp and remove bundled pymtp

* Sun Oct 03 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.8-2
- Add a patch to fix the 'gpo update' command, rhbz #638107, Maemo #11217

* Sun Aug 29 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.8-1
- New upstream release
- Remove both patches, upstreamed
- Add dependency on gstreamer-python for ipod sync

* Mon Aug 23 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.7-3
- Add patches to fix two Fedora bugs, #620584 (problems with the episode list)
  and #619295 (database ProgrammingError)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 07 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.7-1
- New upstream release
- Drop all patches, upstreamed
- Upstream added the Network category to the .desktop file, remove it so that
  gPodder doesn't show up in both the Network and the Audio menu

* Fri Jun 04 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-7
- Add a patch to fix another TypeError, upstream bug #1041, rhbz #599232

* Sun May 30 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-6
- Require python-mygpoclient >= 1.4, rhbz #597740

* Fri May 28 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-5
- Replace All Episodes patch with better patch from upstream.  

* Fri May 28 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-4
- Upstream patch for TypeError in gui.py, upstream bug #934, rhbz #595980

* Sun May 23 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-3
- better patch 

* Sun May 23 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-2
- small patch to prevent crashes when selecting All episodes for subscription edit 

* Sun May 23 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-1
- New upstream release, mostly bug fixes

* Sun May 02 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.5-1
- Update to the latest upstream release
- Require pywebkitgtk instead of gnome-python2-gtkhtml2
- Remove both patches, they are upstreamed
- Remove desktop file categories News and FileTransfer,
  desktop-file-install would require the Network category to be used with
  them, but that would put gPodder into both the Network and the Audio menus

* Mon Mar 15 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-3
- Add a patch from upstream git to not raise an exception if PyMTP is
  missing, helps avoid ABRT reports which are not bugs, such as
  rhbz#570811. Upstream bug #924.

* Mon Mar 01 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-2
- Add a patch from upstream git to fix rhbz#569111, upstream bug #911
  (GError in desktopfile.py)

* Sat Feb 27 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-1
- New upstream release
- Remove both patches, they're in the release

* Thu Feb 25 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-3
- Add patch from upstream git to mention gnome-bluetooth instead of bluez in
  gPodder's own dependency manager
- Drop RPM dependency on gnome-bluetooth so that gPodder can be installed
  without having PulseAudio in the system, upstream bug #884

* Wed Feb 24 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-2
- Add patch from upstream git to fix rhbz#566566, upstream bug #874
  (crash in episode lock counting)

* Wed Feb 10 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-1
- New upstream release
- Add Requires python-mygpoclient and dbus-python
- Add Requires gnome-python2-gtkhtml2 for nicer shownotes
- Remove BuildRequires ImageMagick
- Remove Requires wget and pybluez, not needed anymore

* Mon Dec 14 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.1-1
- New upstream release

* Mon Aug 17 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.0-1
- New upstream release

* Mon Aug 17 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.17.0-3
- Fix for desktop file encoding packaging problem

* Mon Jul 27 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.17.0-2
- New upstream release, fixes multiple bugs since 0.16.1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 2 2009 - 0.16.1-2 jpaleta <jspaleta AT fedoraproject DOT org>
- feedparser buildrequires fix

* Sun Jun 14 2009 - 0.16.1-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream point release new features and bug fixes. See upstream website for details.

* Mon Apr 13 2009 - 0.15.2-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream point release with multiple bug fixes and updates translations.

* Fri Mar 20 2009 - 0.15.1-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream release and packaging fixes

* Thu Feb 05 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.1-1
- new upstream release

* Sat Jan 03 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.0-2
- pybluez dep fix

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.0-1
- New upstream release

* Mon Dec 01 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.13.1-2.1
- Source Fix

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.13.1-2
- Rebuild for Python 2.6

* Wed Nov 12 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.13.1-1
- Update to 0.13.1 

* Thu Oct 9 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.13.0-1
- 0.13 Series

* Sun Aug 10 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.12.2-1
- Bugfix release of the 0.12.x series

* Tue Jul 15 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.12.0-1
- First of the 0.12.x series

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.11.3-1
- latest stable release

* Wed Apr 2 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.11.1-2
- New Upstream version. 

* Wed Feb 27 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.11.1-1
- New Upstream version. 

* Wed Jan 23 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.10.4-1
- New Upstream version. Minor desktop file patch needed.

* Mon Dec 17 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.3-1
- New Upstream version

* Thu Nov 29 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.2-1
- New Upstream version
- A mixed bag of bugfixes and enhancements
- See upstream release notes for full details

* Tue Oct 30 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.1-1
- New Upstream version
- Channel list selection/update bugfixes
- Really load channel metadata
- See upstream website for full release notes

* Sun Oct 07 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.0-1
- New Upstream version

* Sun Aug 26 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.5-1
- New Upstream version

* Fri Aug 03 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.4-2
- Update license tag to GPLv2+ for new licensing guidance

* Sat Jul 28 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.4-1
- Update to 0.9.4 release and adjust specfile accordingly

* Mon Mar 26 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.0-1
- Update to 0.9.0 release and adjust specfile accordingly

* Sun Feb 11 2007 Jef Spaleta <jspaleta@gmail.com> 0.8.9-1
- Update to 0.8.9 release and adjust specfile accordingly

* Wed Dec 27 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-3
- Rmove X-Fedora-Extras Category and python dependancy as per review comments 

* Sun Dec 24 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-2
- added iconv call to force utf-8 encoding.

* Sun Dec 24 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-1
- Initial build for FE inclusion review
