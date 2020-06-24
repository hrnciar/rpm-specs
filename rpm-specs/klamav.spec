Summary: Clam Anti-Virus on the KDE Desktop
Name: klamav
Version: 0.46
Release: 29%{?dist}
Source0: http://downloads.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
Patch0: klamav-0.46-suse-clamav-path.patch
# Upstream notified via mailing list:
# http://sourceforge.net/mailarchive/message.php?msg_name=20080123100636.GC1177%40serv.smile.org.ua
Patch1: klamav-0.41.1-pwd-echo.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=483518
Patch2: klamav-0.44-no-kde3-mediamanager.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=553811
Patch3: klamav-0.46-fix-docpath.patch
# fix pointless gzip API abuse causing FTBFS
Patch4: klamav-0.46-gzip-api.patch
# fix FTBFS against clamav 0.101 (#1604507)
Patch5: klamav-0.46-clamav-0.101.patch
URL: http://klamav.sourceforge.net
License: GPLv2+
Requires: clamav >= 0.93
Requires: clamav-update >= 0.93
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kdelibs3-devel >= 3.5.2
BuildRequires: clamav-devel >= 0.93
BuildRequires: curl-devel
BuildRequires: gmp-devel
BuildRequires: desktop-file-utils
BuildRequires: sqlite-devel >= 3.0
BuildRequires: gettext

%description
ClamAV Anti-Virus protection for the KDE desktop.

%prep
%setup -q
%patch0 -p1 -b .suse-clamav-path
%patch1 -p1 -b .pwd-echo
%patch2 -p1 -b .no-kde3-mediamanager
%patch3 -p1 -b .fix-docpath
%patch4 -p1 -b .gzip-api
%patch5 -p1 -b .clamav-0.101

# Remove staled files (#553807)
%{__rm} -f po/*.gmo

# Fix documentation module name (#553811)
find doc \
    -name 'Makefile.*' -o -name 'index.docbook' \
    -type f | xargs %{__sed} -i -e 's,klamav02,klamav,g'

%build
%configure --disable-rpath --without-included-sqlite --with-disableupdates
make %{?_smp_mflags}

%install
%{__rm} -rf "${RPM_BUILD_ROOT}"
make DESTDIR="${RPM_BUILD_ROOT}" install

# Fix Terminal value in desktop-file
%{__sed} -i.orig -e '/^Terminal/s|^.*$|Terminal=false|' \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop
%{__rm} -f ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop.orig

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor fedora \
%endif
    --delete-original \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications/ \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop

%find_lang %{name}

# satisfy rpmlint claim on debuginfo subpackage
chmod 644 src/klammail/*.{c,h}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_datadir}/doc/HTML/en/klamav
%{_bindir}/klamav
%{_bindir}/klammail
%{_bindir}/klamarkollon
%attr(755,root,root) %{_bindir}/ScanWithKlamAV
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/apps/klamav
%{_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{_datadir}/config.kcfg/klamavconfig.kcfg
%{_datadir}/icons/*/*x*/apps/klamav.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.46-26
- add missing BuildRequires: gcc-c++
- fix FTBFS against clamav 0.101 (#1604507)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.46-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 0.46-18
- Rebuilt for libclamav soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.46-16
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.46-12
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.46-10
- fix pointless gzip API abuse causing FTBFS
- drop ancient conditional for Fedora < 7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-8.1
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.46-6.1
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 30 2010 Andy Shevchenko <andy@smile.org.ua> - 0.46-4.1
- add gettext to build requirements

* Sat Jan 30 2010 Andy Shevchenko <andy@smile.org.ua> - 0.46-4
- remove staled files to build translations properly (#553807)
- rename module in documentation and fix *.desktop file (#553811)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Andy Shevchenko <andy@smile.org.ua> - 0.46-2
- disable update from GUI (#490451)

* Tue Mar 10 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.46-1
- upgrade to 0.46 (compatible with clamav 0.95rc1)
- drop klamav-clamav094.patch (fixed upstream)
- disable device mounting which requires KDE 3 (#483518)
- rediff suse-clamav-path patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.44-3
- rebuild for clamav 0.94
- add klamav-clamav094.patch from Gentoo

* Sun Jul 20 2008 Andy Shevchenko <andy@smile.org.ua> 0.44-2
- update to 0.44
- bump clamav requirements to have their at least for 0.93
- remove upstreamed patches

* Fri Mar 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.42-3
- patch for clamav 0.93 (#438627)

* Thu Mar 06 2008 Andy Shevchenko <andy@smile.org.ua> 0.42-2
- rebuild against newer clamav

* Wed Feb 13 2008 Andy Shevchenko <andy@smile.org.ua> 0.42-1
- update to 0.42
- remove upstreamed and useless patches

* Thu Jan 10 2008 Andy Shevchenko <andy@smile.org.ua> 0.41.1-14
- inherit archive limit defaults and pass their to the clamav
  even if they are equal to zero (#428066)

* Sat Jan 05 2008 Andy Shevchenko <andy@smile.org.ua> 0.41.1-10
- fix compilation with gcc 4.3

* Sat Dec 22 2007 Andy Shevchenko <andy@smile.org.ua> 0.41.1-9
- rebuild against new clamav

* Sun Dec 02 2007 Andy Shevchenko <andy@smile.org.ua> 0.41.1-7
- build with kdelibs3-devel
  (http://www.redhat.com/archives/fedora-devel-announce/2007-November/msg00005.html)

* Wed Nov 07 2007 Andy Shevchenko <andy@smile.org.ua> 0.41.1-6
- do not build internal sqlite
- set special echo mode for password field (#362061)

* Sun Aug 19 2007 Andy Shevchenko <andy@smile.org.ua> 0.41.1-5
- fix desktop Categories
- use system sqlite

* Thu Aug 16 2007 Andy Shevchenko <andy@smile.org.ua> 0.41.1-3
- update to 0.41.1
- fix License tag according to new guidelines
- do not use __make macro
- fix __open_missing_mode error

* Tue Mar 06 2007 Andy Shevchenko <andy@smile.org.ua> 0.41-2
- rebuild against new clamav

* Mon Feb 26 2007 Andy Shevchenko <andy@smile.org.ua> 0.41-1
- update to 0.41

* Wed Sep 27 2006 Andy Shevchenko <andy@smile.org.ua> 0.38-4
- drop zlib-devel and bzip2-devel
- require clamav-update
- remove condition check from post scriptlets
- satisfy rpmlint claim on debuginfo subpackage
- fix Terminal value in desktop-file
- do not ship NEWS file due to is empty

* Sat Sep 02 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.38-2
- require freshclam for correct DB update
- fix rpmlint claim:
  - pack ScanWithKlamAV as executable
  - do not use absolute link
- use $RPM_BUILD_ROOT and $RPM_OPT_FLAGS in all places

* Tue Aug 08 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.38-1
- update to 0.38

* Wed Jul 12 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.37-4
- do not set CFLAGS explicitly

* Tue Jul 11 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.37-3
- fix Source0 URL
- change patch1 to patch0
- use smp if possible when make

* Tue Jul 11 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.37-2
- adjust spec according to Fedora Extras review:
  - remove --with-qt-dir, add --disable-rpath
  - BRs: desktop-file-utils
  - place desktop file properly
  - update gtk icon cache

* Wed May 03 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.37-1
- update to 0.37

* Thu Apr 06 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- update to 0.35.1

* Tue Jan 10 2006 Andy Shevchenko <andy@asplinux.com.ua>
- update to 0.32.1

* Tue Nov 15 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.30.3

* Mon Sep 19 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.30.1
- separate klamav from whole source tarball
- drop unneeded patch (in mainstream)

* Mon Jul 25 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.22

* Fri Jul 08 2005 Andy Shevchenko <andriy@asplinux.ru>
- fix translations names

* Fri Jul 08 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.20.1

* Tue Jun 21 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.20

* Wed May 04 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.17.3

* Thu Apr 14 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 0.17

* Wed Mar 30 2005 Andy Shevchenko <andriy@asplinux.ru>
- rebuild for ASPLinux
- update to 0.15.2

* Wed Mar 16 2005 Pascal Bleser <guru@unixtech.be> 0.15-1
- version 0.15

* Mon Feb 14 2005 Pascal Bleser <guru@unixtech.be> 0.12.1-1
- version 0.12.1

* Sun Jan 16 2005 Pascal Bleser <guru@unixtech.be> 0.09.3-1
- version 0.09.3-1

* Wed Jan 12 2005 Pascal Bleser <guru@unixtech.be> 0.09.1-2
- added patch to use correct clamav locations

* Sun Jan  2 2005 Pascal Bleser <guru@unixtech.be> 0.09.1-1
- new package

