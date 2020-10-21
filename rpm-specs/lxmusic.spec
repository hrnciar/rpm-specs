Name:           lxmusic
Version:        0.4.7
Release:        10%{?dist}
Summary:        Lightweight XMMS2 client with simple user interface

License:        GPLv2+
URL:            http://lxde.org
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# As long as there are no plugins, disable the Tools menu
Patch0:         lxmusic-0.3.0-no-tools-menu.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1250738
# https://sourceforge.net/p/lxde/bugs/774/
Patch10:		lxmusic-0.4.6-saver_quit_from_taskber_on_play.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(xmms2-client)
BuildRequires:  pkgconfig(xmms2-client-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       xmms2 >= 0.7

%description
LXMusic is a very simple gtk+ XMMS2 client written in pure C. It has very few 
functionality, and can do nothing more than play the music. The UI is very 
clean and simple. This is currently aimed to be used as the default music 
player of LXDE (Lightweight X11 Desktop Environment) project.

%prep
%setup -q
%patch0 -p1 -b .no-tools
%patch10 -p1 -b .saverquit

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install                                       \
  --delete-original                                        \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

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
<application>
<id type="desktop">lxmusic.desktop</id>
<metadata_license>CC0-1.0</metadata_license>
<name>LXMusic</name>
<summary>A minimalist music player for LXDE</summary>
</application>
EOF

%files -f %{name}.lang
%doc AUTHORS
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/lxmusic.desktop
%{_datadir}/lxmusic
%{_datadir}/pixmaps/lxmusic.png


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.7-1
- 0.4.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug  9 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.6-2
- Prevent segv when quitting from taskbar while playing
  (bug 1250738)

* Thu Jul 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.6-1
- 0.4.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4.4-13
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.4-6
- Rebuild for new libpng

* Mon Dec 05 2011 Tom Callaway <spot@fedoraproject.org> - 0.4.4-5
- rebuild for xmms2 0.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-3
- Fix segfault in xmmsv_get_int (#634698)

* Wed Nov 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-2
- Fix for libnotify 0.7.0

* Thu Jun 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4 with xmms2 0.7.0

* Tue Dec 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sun Dec 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- New upstream release to fix #539729, so we drop the patches

* Wed Dec 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Fix crash when emptying large playlists (#539729)

* Sat Sep 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-1
- update to 0.3.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-3
- Disable empty tools menu

* Sun Mar 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-2
- Build Require gtk2-devel

* Sat Dec 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Initial Fedora Package
