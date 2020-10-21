Name:		ekiga
Version:	4.0.1
Release:	50%{?dist}
Summary:	A Gnome based SIP/H323 teleconferencing application
License:	GPLv2+
URL:		https://www.ekiga.org/
Source0:	https://download.gnome.org/sources/ekiga/4.0/%{name}-%{version}.tar.xz

Patch01: ekiga-4.0.1-libresolv.patch
Patch02: ekiga-4.0.1-boost-signals2.patch
Patch03: ekiga-4.0.1-gcc10.patch

BuildRequires:	ptlib-devel = 2.10.11
BuildRequires:	opal-devel = 3.10.11
BuildRequires:	alsa-lib-devel
BuildRequires:	avahi-devel
BuildRequires:	avahi-glib-devel
BuildRequires:	boost-devel >= 1.53.0
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	expat-devel
BuildRequires:	gnome-icon-theme-devel
BuildRequires:	gtk2-devel
BuildRequires:	GConf2-devel
BuildRequires:	libnotify-devel
BuildRequires:	libxml2-devel
BuildRequires:	libXv-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	SDL-devel
BuildRequires:	speex-devel

BuildRequires:	autoconf
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper

Requires:	evolution-data-server
Requires:	dbus
Requires:	GConf2
Requires(pre):	GConf2
Requires(post):	GConf2
Requires(preun):GConf2
Requires(post):	scrollkeeper
Requires(postun):scrollkeeper


%description
Ekiga is a tool to communicate with video and audio over the internet.
It uses the standard SIP and H323 protocols.

%prep
%setup -q
%patch01 -p1 -b .libresolv
%patch02 -p1 -b .boost-signals2
%patch03 -p1 -b .gcc10

# force regeneration to drop translations
rm ekiga.schemas

%build
# The supported version is hardcoded
sed -i 's#.10.10#.10.11#' configure*
autoreconf -vif

CXXFLAGS="$RPM_OPT_FLAGS -DLDAP_DEPRECATED=1 -fPIC"
%configure --disable-scrollkeeper --with-boost-libdir=%{_libdir}
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -rf %{buildroot}/var/scrollkeeper

# Replace identical images in the help by links.
# This reduces the RPM size by several megabytes.
helpdir=%{buildroot}%{_datadir}/gnome/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done

desktop-file-install --vendor gnome \
  --dir=%{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/ekiga.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gnome-ekiga.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736831
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">gnome-ekiga.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Ekiga is a softphone, video conferencing and instant messenger application
      over the Internet.
      It supports HD sound quality and video up to DVD size and quality.
    </p>
    <p>
      It is interoperable with many other standard compliant softwares,
      hardwares and service providers as it supports both the major telephony
      standards (SIP and H.323).
    </p>
  </description>
  <url type="homepage">http://www.ekiga.org/</url>
  <screenshots>
    <screenshot type="default">http://www.ekiga.org/sites/all/themes/ekiga_net/images/ekiga_s3.png</screenshot>
    <screenshot>http://www.ekiga.org/sites/all/themes/ekiga_net/images/Roster3.png</screenshot>
  </screenshots>
  <updatecontact>ekiga-list@gnome.org</updatecontact>
  <project_group>GNOME</project_group>
</application>
EOF

%find_lang ekiga --with-gnome

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%pre
if [ "$1" -gt 1 ] ; then
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
%{_sysconfdir}/gconf/schemas/ekiga.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
%{_sysconfdir}/gconf/schemas/ekiga.schemas > /dev/null || :

scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :


%preun
if [ "$1" -eq 0 ] ; then
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
%{_sysconfdir}/gconf/schemas/ekiga.schemas > /dev/null || :
fi

%postun
scrollkeeper-update -q || :

%files -f ekiga.lang
%license COPYING
%doc AUTHORS FAQ NEWS
%{_bindir}/ekiga
%{_bindir}/ekiga-helper
%{_bindir}/ekiga-config-tool
%{_libdir}/ekiga
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/gnome-ekiga.desktop
%{_datadir}/pixmaps/ekiga
%{_datadir}/man/*/*
%{_datadir}/sounds/ekiga
%{_datadir}/dbus-1/services/org.ekiga.*
%{_datadir}/icons/hicolor/*/apps/ekiga.png
%{_sysconfdir}/gconf/schemas/ekiga.schemas

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 4.0.1-49
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 4.0.1-47
- Add missing #include for gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 4.0.1-45
- Rebuild for newer evolution-data-server

* Thu May 16 2019 Robert Scheck <robert@fedoraproject.org> - 4.0.1-44
- Backported upstream changes for Boost.Signals2 support (#1674843)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-42
- Build agaisnt new ptlib/opal, minor spec cleanups

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 4.0.1-40
- Rebuilt for evolution-data-server soname bump

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-39
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.1-38
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-35
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-34
- Rebuilt for Boost 1.64

* Thu Feb 23 2017 Milan Crha <mcrha@redhat.com> - 4.0.1-33
- Add a patch to avoid libresolv check for res_gethostbyaddr()

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-32
- Rebuild for newer evolution-data-server

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-31
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-30
- Rebuild for newer evolution-data-server

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-29
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-27
- Rebuilt for Boost

* Tue Jan 19 2016 Milan Crha <mcrha@redhat.com> - 4.0.1-26
- Rebuild for newer evolution-data-server

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-25
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-24
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.0.1-22
- rebuild for Boost 1.58

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 4.0.1-21
- Rebuild for newer evolution-data-server

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 4.0.1-19
- Rebuild for newer evolution-data-server

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 4.0.1-18
- Add an AppData file for the software center

* Tue Feb 17 2015 Milan Crha <mcrha@redhat.com> - 4.0.1-17
- Rebuild against newer evolution-data-server

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.0.1-16
- Rebuild for boost 1.57.0

* Wed Sep 24 2014 Milan Crha <mcrha@redhat.com> - 4.0.1-15
- Rebuild against newer evolution-data-server

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Milan Crha <mcrha@redhat.com> - 4.0.1-13
- Rebuild against newer evolution-data-server

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.0.1-11
- Rebuild for boost 1.55.0

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 4.0.1-10
- Rebuild against newer evolution-data-server

* Tue Jan 14 2014 Milan Crha <mcrha@redhat.com> - 4.0.1-9
- Rebuild against newer evolution-data-server

* Tue Nov 19 2013 Milan Crha <mcrha@redhat.com> - 4.0.1-8
- Rebuild against newer evolution-data-server

* Fri Nov 08 2013 Milan Crha <mcrha@redhat.com> - 4.0.1-7
- Rebuild against newer evolution-data-server

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> - 4.0.1-6
- Rebuild against newer evolution-data-server

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 4.0.1-4
- Rebuild for boost 1.54.0

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> - 4.0.1-3
- Rebuild against newer evolution-data-server
- Add BuildRequires: gnome-icon-theme-devel

* Thu Jun 27 2013 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-2
- Rebuild (evolution)

* Wed Feb 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-1
- Ekiga 4.0.1 stable release - Changelog
  http://ftp.gnome.org/pub/gnome/sources/ekiga/4.0/ekiga-4.0.1.news

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.0.0-3
- Rebuild for Boost-1.53.0

* Tue Dec 25 2012 Bruno Wolff III <bruno@wolff.to> 4.0.0-2
- Rebuild for libcamel soname bump

* Mon Nov 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.0-1
- Ekiga 4.0.0 stable release - Changelog
  http://ftp.gnome.org/pub/gnome/sources/ekiga/4.0/ekiga-4.0.0.news

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 3.9.90-3
- Rebuild against newer evolution-data-server

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 3.9.90-2
- Rebuild against newer evolution-data-server

* Sat Aug 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.9.90-1
- Ekiga 3.9.90 devel - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.9/ekiga-3.9.90.news

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.2-7
- Fix build with gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.2-4
- Rebuild for boost 1.48

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> - 3.3.2-3
- Rebuild against newer evolution-data-server

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 3.3.2-2
- Rebuild against newer evolution-data-server

* Tue Aug 23 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.2-1
- Ekiga 3.3.2 devel - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.3/ekiga-3.3.2.news

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> - 3.3.1-3
- Rebuild against newer evolution-data-server

* Sun Jul 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.1-2
- Rebuild for new boost and evolution-data-server

* Sat Jul 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.1-1
- Ekiga 3.3.1 devel - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.3/ekiga-3.3.1.news

* Fri Jun 17 2011 Milan Crha <mcrha@redhat.com> - 3.3.0-10
- Rebuild against newer evolution-data-server

* Fri May 20 2011 Kalev Lember <kalev@smartlink.ee> - 3.3.0-9
- Rebuilt for libcamel soname bump

* Tue Apr 12 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.0-8
- rebuild again for new boost

* Tue Mar 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.0-7
- rebuild for new boost

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.3.0-5
- rebuild for new boost

* Tue Feb 01 2011 Milan Crha <mcrha@redhat.com> - 3.3.0-4
- Rebuild against newer evolution-data-server

* Wed Jan 12 2011 Milan Crha <mcrha@redhat.com> - 3.3.0-3
- Rebuild against newer evolution-data-server

* Fri Dec 24 2010 Dan Horák <dan[at]danny.cz> - 3.3.0-2
- fix build on non-x86 64-bit architectures (ax_boost_base.m4 is wrong)

* Thu Dec 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.0-1
- Ekiga 3.3.0 devel - Changelog
  http://mail.gnome.org/archives/ekiga-devel-list/2010-December/msg00036.html

* Fri Nov  5 2010 Matthias Clasen <mclasen@redhat.com> - 3.2.7-5
- Rebuild against libnotify 0.7.0

* Mon Jul 26 2010 Caolán McNamara <caolanm@redhat.com> - 3.2.7-4
- add gtk flags to notify plugin to rebuild

* Tue Jul 20 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.7-3
- rebuild against new evolution-data-server

* Thu Jul 15 2010 Matthias Clasen <mclasen@redhat.com> - 3.2.7-2
- rebuild against new evolution-data-server

* Mon May 31 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.7-1
- Ekiga 3.2.7 stable - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.2/ekiga-3.2.7.news

* Wed May 26 2010 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.6-4
- Bump build for new evolution

* Tue May  4 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.6-3
- Rebuild for new evolution

* Wed Mar  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.6-2
- Add patch to fix DSO linking. Bug 564828

* Tue Sep 22 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.6-1
- Ekiga 3.2.6 stable - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.2/ekiga-3.2.6.news

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.2.5-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Matthias Clasen <mclasen@redhat.com> - 3.2.5-2
- Shrink GConf schemas
 
* Mon Jul  6 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.5-1
- Ekiga 3.2.5 stable - Changelog
  ftp://ftp.gnome.org/pub/gnome/sources/ekiga/3.2/ekiga-3.2.5.news

* Wed May 20 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.4-1
- Ekiga 3.2.4 stable - Changelog
  http://mail.gnome.org/archives/ekiga-devel-list/2009-May/msg00062.html
  http://mail.gnome.org/archives/ekiga-devel-list/2009-May/msg00064.html

* Tue May 19 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.1-1
- Ekiga 3.2.1 stable - Changelog
  http://mail.gnome.org/archives/ekiga-devel-list/2009-May/msg00054.html

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> - 3.2.0-3
- Rebuild against newer GConf/intltool

* Mon Apr 20 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.0-2
- Add a couple of upstream patches from 3.2.1

* Tue Mar 17 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.0-1
- Ekiga 3.2.0 stable

* Fri Mar  6 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.2-4
- Remove CELT until the bitstream is stable and can hence intercommunicate between versions

* Tue Mar  3 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.2-3
- Remove autoconf bits

* Tue Mar  3 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.2-2
- Disable xcap for the moment so ekiga builds

* Tue Mar  3 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.2-1
- Upgrade to the 3.1.2 beta release, enable celt codec, reinstate 
  proper desktop file now its fixed

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 3.1.0-10
- rebuild with new openssl
- add libtoolize call to replace libtool with current version

* Thu Jan 15 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-9
- Add other buildreq for Makefile regen

* Thu Jan 15 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-8
- Regen Makefile.in using autoreconf due to patch

* Wed Jan 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-7
- Another fix

* Tue Jan 13 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-6
- And SDL too

* Tue Jan 13 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-5
- Add expat-devel, why not everything else wants it

* Tue Jan 13 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-4
- Disable gstreamer support until there's a new gst-plugins-base

* Tue Jan 13 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-3
- Proper fix from upstream for desktop file

* Wed Jan  7 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-2
- Fix issues with the desktop file

* Mon Jan  5 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-1
- Upgrade to the 3.1.0 devel release, enable gstreamer and xcap, remove libgnome

* Fri Nov 14 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.1-4
- Fix spec file error

* Fri Nov 14 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.1-3
- Patch to fix libnotify's breakage of its api

* Mon Oct 20 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.1-2
- Fix dependency issue

* Mon Oct 20 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Thu Oct 9 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.0-5
- Remove gnomemeeting obsolete, package review updates

* Thu Oct 9 2008 Matthias Clasen  <mclasen@redhat.com> - 3.0.0-4
- Save some space

* Thu Oct 2 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.0-3
- require dbus

* Tue Sep 23 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.0-2
- add libnotify-devel as a build dep

* Tue Sep 23 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.0-1
- Ekiga 3 final release

* Sun Sep 14 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 2.9.90-3
- more rawhide build fixes

* Sun Sep 14 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 2.9.90-2
- rawhide build fixes

* Thu Sep 11 2008 Peter Robinson <pbrobinson@fedoraproject.org> - 2.9.90-1
- First beta of ekiga 3

* Mon May 12 2008 Paul W. Frields <stickster@gmail.com> - 2.0.12-2
- Rebuild against new opal (#441202)

* Thu Mar 13 2008 Daniel Veillard <veillard@redhat.com> - 2.0.12-1.fc9
- Upgrade to ekiga-2.0.12

* Thu Feb 28 2008 Daniel Veillard <veillard@redhat.com> - 2.0.11-4
- rebuild after applying some fo the cleanups of #160727

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.11-3
- Autorebuild for GCC 4.3

* Thu Dec 13 2007 Matěj Cepl <mcepl@redhat.com> 2.0.11-2
- compile with the D-Bus support
- Making rpmlint silent.

* Tue Sep 18 2007 Daniel Veillard <veillard@redhat.com> - 2.0.11-1
- Upgrade to ekiga-2.0.11

* Sun Apr 15 2007 Daniel Veillard <veillard@redhat.com> - 2.0.9-1
- Upgrade to ekiga-2.0.9

* Mon Mar 12 2007 Daniel Veillard <veillard@redhat.com> - 2.0.7-1
- Upgrade to ekiga-2.0.7

* Mon Feb 19 2007 Jeremy Katz <katzj@redhat.com> - 2.0.5-2
- rebuild 

* Wed Feb 14 2007 Daniel Veillard <veillard@redhat.com> - 2.0.5-1
- Upgrade to ekiga-2.0.5

* Mon Jan 22 2007 Daniel Veillard <veillard@redhat.com> - 2.0.4-1
- Upgrade to ekiga-2.0.4

* Thu Nov  2 2006 Daniel Veillard <veillard@redhat.com> - 2.0.3-3
- Resolves: rhbz#201535
- fixes build-requires for opal-devel and pwlib-devel

* Sat Oct 28 2006 Matthias Clasen <mclasen@redhat.com> - 2.0.3-2
- Rebuild against evolution-data-server 1.9

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.0.3-1
- Update to 2.0.3

* Sat Sep 30 2006 Matthias Clasen <mclasen@redhat.com> - 2.0.2-7
- Make the status icon work in transparent panels

* Thu Aug 31 2006 Matthias Clasen <mclasen@redhat.com> - 2.0.2-6
- Fix translator credits (197871)

* Mon Aug  7 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.2-5
- Rebuild against evolution-data-server-1.7.91

* Sat Aug  5 2006 Caolán McNamara <caolanm@redhat.com> - 2.0.2-4
- rebuild against new e-d-s

* Tue Aug  1 2006 Daniel Veillard <veillard@redhat.com> - 2.0.2-3
- rebuilt for #200960

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.2-1.1
- rebuild

* Wed May 31 2006 Daniel Veillard <veillard@redhat.com> - 2.0.2-1
- new release of ekiga 2.0.2
- activating Zeroconf support though avahi

* Mon May 22 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-3
- Fix BuildRequires and Requires(post), Requires(postun)

* Wed Mar 15 2006 Daniel Veillard <veillard@redhat.com> - 2.0.1-2
- run 'ekiga-config-tool --install-schemas' in %%post, c.f. #178929

* Tue Mar 14 2006 Daniel Veillard <veillard@redhat.com> - 2.0.1-1
- last minute bug rerelease 2.0.1

* Mon Mar 13 2006 Daniel Veillard <veillard@redhat.com> - 2.0.0-1
- final release of 2.0.0

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 1.99.1-2
- Buildrequires: gnome-doc-utils

* Mon Feb 13 2006 Daniel Veillard <veillard@redhat.com> - 1.99.1-1
- new beta release issued

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.99.0-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.99.0-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sat Jan 28 2006 Daniel Veillard <veillard@redhat.com> - 1.99.0-3
- Rebuilt following a libedataserver revision

* Fri Jan 27 2006 Matthias Clasen <mclasen@redhat.com> - 1.99.0-2
- Use the upstream .desktop file

* Tue Jan 24 2006 Daniel Veillard <veillard@redhat.com> - 1.99.0-1
- initial version based on the 1.99.0 beta and gnomemeeting spec file.
