Name:           gmpc
Summary:        GNOME frontend for the MPD
Version:        11.8.16
Release:        24%{?dist}

License:        GPLv2+
URL:            http://gmpclient.org/

Source0:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-11.8.16.tar.gz
Source1:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-alarm-11.8.16.tar.gz
Source2:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-albumview-11.8.16.tar.gz
Source3:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-avahi-11.8.16.tar.gz
Source4:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-awn-11.8.16.tar.gz
Source5:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-jamendo-11.8.16.tar.gz
Source6:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-libnotify-11.8.16.tar.gz
Source7:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-lyrics-11.8.16.tar.gz
Source8:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-lyricwiki-11.8.16.tar.gz
Source9:        http://download.sarine.nl/Programs/gmpc/11.8/gmpc-magnatune-11.8.16.tar.gz
Source10:       http://download.sarine.nl/Programs/gmpc/11.8/gmpc-mmkeys-11.8.16.tar.gz
Source11:       http://download.sarine.nl/Programs/gmpc/11.8/gmpc-tagedit-11.8.16.tar.gz

Source12:       gmpc.appdata.xml

Patch0:         gmpc-dso.patch
Patch1:         gmpc-awn-11.8.16-plugin.patch
Patch2:         http://repo.or.cz/gmpc-albumview.git/patch/aff7338cd6808020f51c69a988c629f7c5704561
Patch3:         bugzilla-1417462-load_list_itterate.patch
Patch4:         http://repo.or.cz/gmpc.git/patch/f4a011831887392d4b7d3c621501c0a431b90331

BuildRequires:  scrollkeeper, gtk2-devel, libglade2-devel
BuildRequires:  gettext, gnome-vfs2-devel, desktop-file-utils
BuildRequires:  perl-XML-Parser, findutils
BuildRequires:  curl-devel, xosd-devel, libSM-devel
BuildRequires:  pkgconfig(avahi-client) pkgconfig(avahi-glib)
BuildRequires:  libnotify-devel
BuildRequires:  gob2, libsexy-devel, libsoup-devel
BuildRequires:  json-glib-devel, lirc-devel
BuildRequires:  libmpd-devel >= 0.20.0
BuildRequires:  taglib-devel, libmicrohttpd-devel
BuildRequires:  intltool, sqlite-devel, vala
BuildRequires:  unique-devel

Requires:       yelp

%description
Gmpc is a GNOME client for the Music Player Daemon
Features :
 * Support for loading/saving playlists.
 * File Browser
 * Browser based on ID3 information. (on artist and albums)
 * Search
 * Current playlist viewer with search.
 * ID3 information
 * Lots more

%package devel
Summary:  Development files for gmpc
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package includes header files necessary for developing gmpc plugins.

%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11
%patch0 -p0
%patch1 -p0
cd gmpc-albumview-11.8.16
%patch2 -p1
cd ..
%patch3 -p1
%patch4 -p1

%build
%configure --disable-dependency-tracking
make %{?_smp_mflags} LDFLAGS=-Wl,--export-dynamic
export PKG_CONFIG_PATH="$PWD/data"
CFLAGS="-I$PWD -I$PWD/src/vala -I$PWD/src -I$PWD/src/MetaData -I$PWD/src/Tools -DGMPC_BUILD=1"
# Subdir configury needs ${RPM_OPT_FLAGS}
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
# Add -DHAVE_STRNDUP=1 to work around bug in
# /usr/include/libmpd-1.0/libmpd/libmpd-internal.h
CFLAGS="${CFLAGS} -DHAVE_STRNDUP=1"
export CFLAGS

ln -s src gmpc
ln -s MetaData/metadata.h src
ln -s Widgets/playlist3-messages.h src
ln -s Tools/misc.h src
ln -s Tools/gmpc_easy_download.h src
for i in \
	gmpc-alarm-11.8.16 \
	gmpc-albumview-11.8.16 \
	gmpc-avahi-11.8.16 \
	gmpc-awn-11.8.16 \
	gmpc-jamendo-11.8.16 \
	gmpc-libnotify-11.8.16 \
	gmpc-lyrics-11.8.16 \
	gmpc-lyricwiki-11.8.16 \
	gmpc-magnatune-11.8.16 \
	gmpc-mmkeys-11.8.16 \
	gmpc-tagedit-11.8.16; do
	pushd $i
	%configure
	make %{?_smp_mflags}
	popd
done

%install
make install DESTDIR=$RPM_BUILD_ROOT
# this is the default search path
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
# rpmlint complains if arch-dependent files are in %{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

for i in \
	gmpc-alarm-11.8.16 \
	gmpc-albumview-11.8.16 \
	gmpc-avahi-11.8.16 \
	gmpc-awn-11.8.16 \
	gmpc-jamendo-11.8.16 \
	gmpc-libnotify-11.8.16 \
	gmpc-lyrics-11.8.16 \
	gmpc-lyricwiki-11.8.16 \
	gmpc-magnatune-11.8.16 \
	gmpc-mmkeys-11.8.16 \
	gmpc-tagedit-11.8.16; do
	pushd $i
	make install DESTDIR=$RPM_BUILD_ROOT
	popd
done

%find_lang %{name}

for i in \
	gmpc-alarm \
	gmpc-lyricwiki \
	gmpc-tagedit; do
	%find_lang $i
	cat $i.lang >> %{name}.lang
done

desktop-file-install \
        --delete-original \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT%{_datadir}/applications/gmpc.desktop

install -D -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_bindir}/%name-remote
%{_bindir}/%name-remote-stream
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/*/*/*/*
%{_datadir}/gmpc-albumview/icons/*/*/*/*
%{_mandir}/man1/*
%{_datadir}/gnome/help/%{name}
%{_datadir}/appdata/%{name}.appdata.xml

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.8.16-17
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Adrian Reber <adrian@lisas.de> - 11.8.16-13
- fixed "gmpc: load_list_itterate(): gmpc killed by SIGSEGV" (#1417462)

* Wed Sep 14 2016 Adrian Reber <adrian@lisas.de> - 11.8.16-12
- fixed "gmpc must not depend on webkitgtk" (#1375811)

* Tue Feb 09 2016 Adrian Reber <adrian@lisas.de> - 11.8.16-11
- fix for crash on exit (#1290929)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.16-9
- Fix F23FTBFS (RHBZ#1239534):
  - Append -DHAVE_STRNDUP=1 to CFLAGS to work-around bug in libmpd.
  - Append RPM_OPT_FLAGS to subdir CFLAGS.
- Add gmpc-awn-11.8.16-plugin.patch.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 Adrian Reber <adrian@lisas.de> - 11.8.16-5
- added appdata file (#1034007)

* Thu Sep 26 2013 Rex Dieter <rdieter@fedoraproject.org> 11.8.16-4
- add explicit avahi build deps

* Wed Aug 07 2013 Adrian Reber <adrian@lisas.de> - 11.8.16-3
- fix #992396 (gmpc: FTBFS in rawhide)
- update URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Adrian Reber <adrian@lisas.de> - 11.8.16-1
- updated to 11.8.16

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.20.0-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Adrian Reber <adrian@lisas.de> - 0.20.0-3
- rebuilt for new libmicrohttpd

* Sun Nov 07 2010 Adrian Reber <adrian@lisas.de> - 0.20.0-2
- rebuilt for new libnotify
- added patches for new libnotify

* Sat Jul 31 2010 Adrian Reber <adrian@lisas.de> - 0.20.0-1
- updated to 0.20.0

* Fri Jul 09 2010 Mike McGrath <mmcgrath@redhat.com> - 0.19.1-3.1
- Rebuilt to fix libwebkit-1.0.so.2 broken dep

* Fri May 07 2010 Adrian Reber <adrian@lisas.de> - 0.19.1-3
- added patch for " FTBFS gmpc-0.19.1-2.fc13: ImplicitDSOLinking" (#564660)

* Wed Nov 25 2009 Adrian Reber <adrian@lisas.de> - 0.19.1-2
- updated to 0.19.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Adrian Reber <adrian@lisas.de> - 0.18.0-1
- updated to 0.18.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Adrian Reber <adrian@lisas.de> - 0.16.1-1
- updated to 0.16.1

* Wed Oct 01 2008 Adrian Reber <adrian@lisas.de> - 0.15.5.0-4
- re-created patch to apply cleanly (fixes #465008)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.15.5.0-3
- Autorebuild for GCC 4.3

* Fri Feb 15 2008 Adrian Reber <adrian@lisas.de> - 0.15.5.0-2
- rebuilt for gcc43

* Sun Dec 23 2007 Adrian Reber <adrian@lisas.de> - 0.15.5.0-1
- updated to 0.15.5.0
- this should fix #242226
- added six more plugins (wikipedia, random-playlist,
  mserver, libnotify, favorites, extraplaylist)
- added BR libnotify-devel for libnotify plugin

* Sun Nov 11 2007 Adrian Reber <adrian@lisas.de> - 0.15.1-1
- update to 0.15.1
- dropped gmpc-fix-album-play-order.diff patch
- two more plugins (avahi, shout)

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 0.14.0-3
- rebuilt

* Wed Jun 20 2007 Adrian Reber <adrian@lisas.de> - 0.14.0-2
- applied patch to fix album play order from David Woodhouse

* Sun Mar 25 2007 Adrian Reber <adrian@lisas.de> - 0.14.0-1
- updated to 0.14.0
- added more plugins
- fixed #233837 (gmpc-devel: unowned directory)

* Sat Dec 09 2006 Adrian Reber <adrian@lisas.de> - 0.13.0-1
- updated to 0.13.0
- created devel package for header files
- removed X-Fedora from desktop-file-install
- added some plugins and moved the plugins to %%{_libdir}/%%{name}/plugins

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.11.2-6
- BR: perl-XML-Parser

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.11.2-5
- rebuild

* Thu Mar 23 2006 Jonathan Dieter <jdieter99[AT]gmx.net> 0.11.2-4
- fix dynamic linking bug

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 0.11.2-3
- rebuild for FC5

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Nov 05 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.11.2-0.fdr.1
- initial Fedora release (from Mandrake)
