# Tarfile created using git
# git clone git://git.gnome.org/evolution-rss
# git archive --format=tar --prefix=evolution-rss-0.2.9/ %{git_version} | xz > evolution-rss-0.2.9-%{gitdate}.tar.xz

Name:		evolution-rss
Summary:	Evolution RSS Reader
Epoch:		1
Version:	0.3.96
Release:	4%{?dist}
License:	GPLv2 and GPLv2+
URL:		http://gnome.eu.org/evo/index.php/Evolution_RSS_Reader_Plugin
Source:		https://download.gnome.org/sources/evolution-rss/0.3/%{name}-%{version}.tar.xz
Requires:	evolution

Patch01: drop-gconf.patch
Patch02: evo-3.37.2.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	evolution-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	gnome-common

%description
This is an evolution plugin which enables evolution to read rss feeds.

%prep
%setup -q -n evolution-rss-%{version}
%patch01 -p1 -b .drop-gconf
%patch02 -p1 -b .evo-3.37.2

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make ChangeLog
make install DESTDIR="%{buildroot}" INSTALL="install -p"
find %{buildroot} -name \*\.la -print | xargs rm -f
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
#remove changelog until I figure a way how to generate this from git archive
%doc AUTHORS COPYING FAQ NEWS README TODO
# GSettings schemas:
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-rss.gschema.xml
# Only the following binary is under GPLv2. Other
# parts are under GPLv2+.
%{_bindir}/evolution-import-rss
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/evolution-rss.metainfo.xml
%{_datadir}/evolution/errors/org-gnome-evolution-rss.error
%{_datadir}/evolution/ui/*.ui
%{_datadir}/evolution/images/*.png
%{_libdir}/evolution-data-server/registry-modules/module-eds-rss.so
%{_libdir}/evolution/plugins/org-gnome-evolution-rss.eplug
%{_libdir}/evolution/plugins/org-gnome-evolution-rss.xml
%{_libdir}/evolution/plugins/liborg-gnome-evolution-rss.so
%{_libdir}/evolution/modules/evolution-module-rss.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 1:0.3.96-3
- Rebuilt for evolution-data-server soname version bump

* Fri Jun 05 2020 Milan Crha <mcrha@redhat.com> - 1:0.3.96-2
- Add patch to build against Evolution 3.37.2

* Fri Jan 31 2020 Milan Crha <mcrha@redhat.com> - 1:0.3.96-1
- Update to 0.3.96

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 1:0.3.95-22
- Rebuild for newer evolution-data-server

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Milan Crha <mcrha@redhat.com> - 1:0.3.95-20
- Add patch for Red Hat bug #1624609 (Crash under strlen(), emfe_evolution_rss_format())

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Milan Crha <mcrha@redhat.com> - 1:0.3.95-18
- Rebuild for newer evolution-data-server

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 1:0.3.95-17
- Rebuilt for evolution-data-server soname bump

* Wed Nov 29 2017 Milan Crha <mcrha@redhat.com> - 1:0.3.95-16
- Add patch for Red Hat bug #1517021 (Crash when importing OPML file with feeds without 'title' attribute)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-12
- Add a patch to build against evolution-data-server 3.23.2

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-11
- Rebuild for newer evolution-data-server

* Wed Aug 17 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-10
- Adapt to changes in evolution 3.21.90 (notably do not require webkitgtk3)

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-9
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-8
- Rebuild for newer evolution-data-server

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-7
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Milan Crha <mcrha@redhat.com> - 1:0.3.95-5
- Rebuild for newer evolution-data-server

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 1:0.3.95-4
- Rebuild for newer evolution-data-server

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 1:0.3.95-2
- Rebuild for newer evolution-data-server

* Wed Apr 01 2015 Lucian Langa <lucilanga@gnome.eu.org> - 1:0.3.95-1
- drop all patches - fixed upstream
- update to latest upstream

* Mon Feb 16 2015 Milan Crha <mcrha@redhat.com> - 1:0.3.94-11
- Rebuild against newer evolution-data-server

* Mon Sep 22 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-10
- Rebuild against newer evolution (changed folder structure)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.94-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-8
- Rebuild against newer evolution-data-server and evolution
- Add patch for GNOME bug #731553 (Add metainfo file)
- Add patch for GNOME bug #733139 (Crash on message send + some more upstream fixes)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.94-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-6
- Add a patch to adapt to evolution 3.11.91 changes
- Add a patch for runtime errors (GNOME bug #720459)

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-5
- Rebuild against newer evolution-data-server

* Fri Jan 17 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-4
- Rebuild against newer evolution-data-server
- Add an upstream patch for a build break due to evolution changes

* Thu Jan 09 2014 Milan Crha <mcrha@redhat.com> - 1:0.3.94-3
- Add an upstream patch for a build break due to eds/evo changes

* Fri Nov 08 2013 Milan Crha <mcrha@redhat.com> - 1:0.3.94-2
- Rebuild against newer evolution-data-server
- Add an upstream patch to adapt to Camel API changes

* Sun Sep 22 2013 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.94-1
- fix bogus dates in changelog
- drop all patches - fixed upstream
- new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> - 1:0.3.93-4
- Rebuild against newer evolution-data-server
- Add upstream patches to work with latest evolution

* Thu May 02 2013 Milan Crha <mcrha@redhat.com> - 1:0.3.93-3
- Add patch for Red Hat bug #886881 (global variable clash with evolution-rspam)
- Add patch for Red Hat bug #887246 (.convert file touches evolution schema)
- Add patch to be able to build against evolution-3.9.1 (removed e-shell-settings.h)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.93-1
- use name/version vars in source field
- new upstream release

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 1:0.3.92-3
- Rebuild against newer evolution-data-server

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 1:0.3.92-2
- Rebuild against newer evolution-data-server

* Thu Sep 06 2012 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.92-1
- add gsettings files
- add new evolution rss module
- new upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Milan Crha <mcrha@redhat.com> - 1:0.3.91-1
- Update to 0.3.91 release

* Tue Feb 21 2012 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.90-7.20120221git
- new upstream snapshot

* Wed Feb 08 2012 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.90-6.20120208git
- new upstream git snapshot

* Wed Feb 08 2012 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.90-5.20111219git
- rebuild against newer eds

* Fri Feb 03 2012 Lucian Langa <cooly@gnome.eu.org> - 1:0.3.90-4.20111219git
- added mistakenly dropped epoch number - RH #768699

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-3.20111219git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Lucian Langa <cooly@gnome.eu.org> - 0.3.90-2.20111219git
- new upstream snapshot

* Mon Dec 19 2011 Lucian Langa <cooly@gnome.eu.org> - 0.3.90-1.20111219git
- new upstream snapshot

* Tue Nov 22 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-32.20111108git
- rebuilt against newer eds

* Tue Nov 08 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-31.20111108git
- drop patches - fixed upstream
- new git snapshot

* Fri Nov 04 2011 Milan Crha <mcrha@redhat.com> - 0.2.90-30.20110818git
- Replace dropped e_shell_get_watched_windows() function

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> - 0.2.90-30.20110818git
- Rebuild against newer evolution-data-server

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 0.2.90-29.20110818git
- Rebuild against newer evolution-data-server

* Thu Aug 18 2011 cooly@gnome.eu.org - 0.2.90-28.20110818git
- drop patch - fixed upstream
- new upstream release

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> - 0.2.90-27.20110726git
- Rebuild against newer evolution-data-server

* Tue Jul 26 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-26.20110726git
- new git snapshot, possibly fix (#659630)

* Sun Jul 24 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-25.20110716git
- rebuild against newer evolution

* Sat Jul 16 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-24.20110516git
- add patch to remove G_DISABLE_DEPRECATED flag as it breaks webkit build
- new git snapshot

* Tue Jun 21 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-23.20110621git
- new git snapshot

* Wed Jun 15 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-22.20110615git
- add desktop file
- new upstream git snapshot

* Mon May 23 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-21.20110523git
- update to latest git snapshot

* Wed Mar 23 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-20.20110323git
- new upstream git snapshot

* Mon Mar 07 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.90-19.20110306git
- new upstream git snapshot

* Sun Mar 06 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.9-18.20110306git
- drop all patches - fixed upstream
- require webkit gtk3 build
- new upstream git snapshot

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.9-17.20101225git
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-16.20101225git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Milan Crha <mcrha@redhat.com> - 0.2.9-15.20101225git
- Add patch for build with gtk3 and evolution 2.91.6 (Gnome bug #631899)

* Mon Jan 17 2011 Lucian Langa <cooly@gnome.eu.org> - 0.2.9-14.20101225git
- support builds with newer webkit

* Wed Jan 12 2011 Milan Crha <mcrha@redhat.com> - 0.2.9-13.20101225git
- Rebuild against newer evolution-data-server

* Sat Dec 25 2010 Lucian Langa <cooly@gnome.eu.org> - 0.2.9-12.20101225git
- update to latest git snapshot

* Sat Dec 18 2010 Lucian Langa <cooly@gnome.eu.org> - 0.2.9-11.20101218git
- update to latest git snapshot

* Wed Jul 21 2010 Lucian Langa <cooly@gnome.eu.org> - 0.2.1-10.20100721git
- update to latest git snapshot

* Mon Jul 05 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-9.20100611git
- rebuilt with newer webkit

* Fri Jun 11 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-8.20100611git
- update to latest snapshot

* Tue May 25 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-7.20100525git
- latest upstream snapshot (fixes possible image problems)

* Wed May 19 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-6.20100428git
- update to latest snapshot

* Wed May 19 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-5.20100428git
- bump rel to fix NVR upgrade path

* Wed Apr 28 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-4.20100428git
- drop xulrunner-devel as no longer supported upstream
- update to latest git snapshot

* Fri Jan 22 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-0.20100109git
- update to latest git snapshot

* Sat Jan 09 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-1.20100109git
- update to latest git snapshot

* Mon Nov 23 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.9-1.20091123git
- drop undeeded files
- drop all patches - fixed upstream
- new source from latest git master

* Mon Nov 23 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.4-6.1
- upstream patch to fix a crash in displaying folder icons (#539649)

* Thu Nov 05 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.4-5
- add new upstream fix for feeds fetching for evolution > 2.28.1
- add patch2 to fix loading of icons (gtk refuses to load icons with size 0)

* Wed Sep 16 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.4-4
- added patch to fix folder properties in evolution (#523552)
- added upstream patch to fix folder rename (#594704)

* Wed Aug 26 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.4-2
- fix source0

* Tue Aug 25 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.4-1
- force main render gecko
- new upstream release

* Wed Jul 29 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.3-1.20090729git
- drop patch0 - fixed upstream
- update to git snapshot

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 0.1.2-9
- Rebuild against newer gecko

* Sun Apr 12 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.2-8
- EVR bump

* Sat Apr 11 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.2-5
- temporary fix for bug #489217: set interval longer than 100 minutes

* Sun Mar 08 2009 Lucian Langa <cooly@gnome.eu.org> - 0.1.2-4
- rebuild against newer webkit

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 19 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.2-2
- add intltool as buildrequires

* Wed Nov 19 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.2-1
- new upstream 0.1.2

* Sat Sep 27 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.1-3
- new upstream snapshot for 0.1.1

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.1-2
- fix for #458818

* Tue Jul 29 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.1-1
- remove patches for RH #452322 (fixed upstream)
- Update to devel version 0.1.1

* Thu Jul 24 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.0-2
- Fix firefox import RH bug #452322

* Wed Jul  2 2008 Lucian Langa <cooly@gnome.eu.org> - 0.1.0-1
- New upstream

* Mon Mar 24 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-5
- Fixed wrong function def in previous patch

* Sun Mar 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-4
- Fix for No rss feeds configured

* Sat Mar 22 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-3
- Upstream fix for empty description

* Tue Mar  4 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-2
- Rebuild against libxul

* Mon Mar  3 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-1
- Update to 0.0.8 release

* Thu Feb 28 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.7-9
- Build against xulrunner

* Tue Feb 19 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.7-8
- Misc cleanups

* Sun Feb 17 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.7-7
- Misc cleanup

* Sat Feb 16 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.7-6
- Drop gecko requirements till xulrunner is fixed

* Tue Feb 12 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.7-5
- buildroot fixes

* Wed Feb 06 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.7-4
- Modified firefox-devel requirement for build

* Wed Jan 30 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.7-1
- Updates and sanitize

* Thu Jan 24 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.7-1
- Fixed rpmlint warnings
- Updated to Fedora Packaging Guidelines

* Thu Nov 22 2007 Lucian Langa <lucilanga@gnome.org> - 0.0.6-1
- Added gconf schemas
- Added evolution-import-rss

* Tue Sep 04 2007 Lucian Langa <lucilanga@gnome.org> - 0.0.5
- Updated installed files

* Mon Apr 23 2007 root <root@mayday> - 0.0.1
- Initial spec file created by autospec ver. 0.8 with rpm 3 compatibility
