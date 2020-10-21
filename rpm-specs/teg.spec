Name:           teg
Version:        0.11.2
Release:        48%{?dist}
Summary:        Turn based strategy game
License:        GPLv2
URL:            http://teg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        teg.desktop
Patch0:         teg_libxml.patch
#Patch1:         teg_themes.patch
#Patch2:         teg-disable-help.patch
Patch3:         teg_fixwording.patch
Source2:        teg-fix-help.patch

Patch20:        multiple_definitions.patch

BuildRequires:  gcc
BuildRequires:  tidy pkgconfig glib2-devel libxml2-devel libgnomeui-devel
BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Tenes Empanadas Graciela is a clone of Plan Táctico y Estratégico de la 
Guerra, a turn based strategy game. Some rules are different.

%prep
%setup -q 
%patch0 -p1
#%patch2 -p1
%patch3 -p1
for file in AUTHORS COPYING README TODO PEOPLE ChangeLog; do
    iconv -f iso8859-1 -t utf-8 < $file > $file.$$
    mv -f $file.$$  $file
done

%patch20 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/gconf/gconf.xml.defaults
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mv -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg_icono.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gnome/apps/Games/teg.desktop
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor="fedora"               \
%endif
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}
patch -p1 < %{SOURCE2}
mv -f $RPM_BUILD_DIR/%{?buildsubdir}/docs/gnome-help/C/teg.sgml $RPM_BUILD_ROOT/%{_datadir}/gnome/help/teg/C/teg.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README TODO PEOPLE ChangeLog
%{_bindir}/tegrobot
%{_bindir}/tegclient
%{_bindir}/tegserver
%{_datadir}/pixmaps/teg_pix/
%{_datadir}/pixmaps/teg.png
%{_datadir}/gnome/help/teg/
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-teg.desktop
%else
%{_datadir}/applications/teg.desktop
%endif
%{_sysconfdir}/gconf/schemas/teg.schemas

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/teg.schemas >/dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/teg.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/teg.schemas > /dev/null || :

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-48
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 josef radinger <cheese@nosuchhost.net> - 0.11.2-46
- add patch multiple_definitions.patch to fix FTBFS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-40
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 josef radinger <cheese@nosuchhost.net> - 0.11.2-32
- rebuild for fc21

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.11.2-30
- Remove the vendor from .desktop file. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.11.2-26
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 9 2010 josef radinger <cheese@nosuchhost.net>
- 0.11.2-24
- fix even more wording

* Thu Dec 9 2010 josef radinger <cheese@nosuchhost.net>
- 0.11.2-23
- fix more wording

* Thu Dec 9 2010 josef radinger <cheese@nosuchhost.net>
- 0.11.2-22
- fix wording

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- 0.11.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 17 2009 josef radinger <cheese@nosuchhost.net>
- 0.11.2-20
- fix and reenable help

* Sat Jul 11 2009 josef radinger <cheese@nosuchhost.net>
- 0.11.2-19
- fix and reenable help

* Sat Jun 27 2009 josef radinger <cheese@nosuchhost.net>
- 0.11.2-18
- disable help

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 22 2008 josef radinger <cheese@nosuchhost.net>
- 0.11.2-16
- move icons file to /usr/share/pixmaps/

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 
- 0.11.2-15
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-14
- actually execute cosmetic fix in spec-description

* Fri Jan 18 2008 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-13
- cosmetic fix in spec-description

* Tue Jan 15 2008 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-12
- fresh rebuild

* Tue Jan 15 2008 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-11
- fresh rebuild

* Sat Nov 24 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-10
- disable additional themes

* Sat Nov 24 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-9
- move desktop-icon to /usr/share/icons/hicolor/48x48/apps/teg.png
- added scripts for updateing icon-cache

* Wed Nov 21 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-8
- enable more themes

* Tue Nov 20 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-7
- "install -p" as option at installing
- "cleaner" files-section
- correct sourceforge-link

* Sat Nov 17 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-6
- reenable schemas
- buildrequires for desktop-file-utils
- use desktopfile-install
- own directories
- more files in doc

* Sat Oct 14 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-5
- better Summary, added TODO to docs
- add full path to sources
- correct perl-dependency
- new desktop.file
- no more use of makeinstall-macro
- todo:
- desktop.file gets installed correct now

* Sat Sep 14 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-4
- removed "macro" from changelog
- Correct License-Tag to GPLv2
- better spec-file

* Sat Aug 25 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-3
- desktop-file
- addded post postun macros
- added some deps

* Mon Aug 06 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-2
- encode description in utf-8 
- remove /etc/gconf-files (as life-files dont seem to get incorporated by rpms)

* Mon Aug 06 2007 josef radinger <cheese@nosuchhost.net> 
- 0.11.2-1
- initial version 

