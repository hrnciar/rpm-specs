
Name:           konversation
Version:        1.7.5
Release:        8%{?dist}
Summary:        A user friendly IRC client

License:        GPLv2+
URL:            http://konversation.kde.org/
%if 0%{?snap}
# use releaseme script
Source0:        %{name}-%{version}-%{snap}.tar.bz2
%else
Source0:        http://download.kde.org/%{?beta:un}stable/konversation/%{version}%{?beta:-%{beta}}/src/konversation-%{version}%{?beta:-%{beta}}.tar.xz
%endif

Source1:        konversationrc

## upstream patches
Patch7: 0007-Fix-regex-for-cap-ack.patch
Patch16: 0016-Fix-build-with-Qt-5.13.patch
Patch17: 0017-appdata-use-https-for-URLs.patch
Patch19: 0019-Remove-extra-Python-shebang.patch
Patch28: 0028-Fix-build-with-Qt-5.15-missing-header.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libappstream-glib
BuildRequires: perl-generators
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(qca2-qt5)
BuildRequires: pkgconfig(Qt5Widgets)
# python3
BuildRequires: python3
BuildRequires: python3-rpm-macros
%global __python %{_python3}
BuildRequires: sed

Requires: qca-qt5-ossl%{?_isa}

%description
A simple and easy to use IRC client with support for
strikeout; multi-channel joins; away / unaway messages;
ignore list functionality; support for foreign
language characters; auto-connect to server; optional timestamps
to chat windows; configurable background colors and much more


%prep
%autosetup -n %{name}-%{version}%{?beta:-%{beta}} -p1

# Add Comment key to .desktop file
grep '^Comment=' %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop || \
desktop-file-edit \
  --set-comment="A user friendly IRC client" \
  data/org.kde.%{name}.desktop

# Add StartupWMClass to .desktop
grep '^StartupWMClass=' %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop || \
desktop-file-edit \
  --set-key=StartupWMClass --set-value=konversation \
  data/org.kde.%{name}.desktop

# purge use of /usr/bin/env
sed -i \
  -e "s|^#!/usr/bin/env bash|#!/bin/bash|g" \
  -e "s|^#!/usr/bin/env perl|#!/usr/bin/perl|g" \
  -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" \
  data/scripts/* \
  data/scripting_support/python/konversation/*.py


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -p -m644 -D %{SOURCE1} %{buildroot}%{_kf5_sysconfdir}/xdg/konversationrc

%find_lang konversation --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.konversation.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.konversation.desktop


%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null ||:

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null ||:
  update-desktop-database -q &> /dev/null ||:
fi
%endif

%files  -f konversation.lang
%doc ChangeLog README
%license COPYING
%config(noreplace) %{_kf5_sysconfdir}/xdg/konversationrc
%{_kf5_bindir}/konversation
%{_kf5_metainfodir}/org.kde.konversation.appdata.xml
%{_kf5_datadir}/applications/org.kde.konversation.desktop
%{_kf5_datadir}/konversation/
%{_kf5_datadir}/kconf_update/konversation*
%{_kf5_datadir}/knotifications5/konversation.notifyrc
%{_kf5_datadir}/kxmlgui5/konversation/
%{_kf5_datadir}/icons/hicolor/*/*/*


%changelog
* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.7.5-8
- more upstream fixes (qt5.15 in particular)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Rex Dieter <rdieter@fedoraproject.org> 1.7.5-6
- pull in upstream fixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.7.5-2
- missing StartupWMClass=konversation in .desktop file (#1590462)
- move script/desktop modifiations to %%prep (ie, like patching)
- fix byte-compile warning (python2 vs python3)

* Sat Jun 30 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.7.5-1
- konversation-1.7.5

* Tue Jun 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.7.4-4
- backport upstream FTBFS fix
- use %%make_build, update %%scriptlets

* Mon Feb 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.7.4-3
- use %%_kf5_metainfodir

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7.4-1
- 1.7.4

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7.3-1
- 1.7.3

* Wed Aug 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7.2-3
- pull in upstream crash fix (#1476527,kde#378854)
- use %%find_lang --with-html

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.7.2-1
- Update to 1.7.2.

* Sat Apr 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7-1
- konversation-1.7

* Thu Apr 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7-0.2.rc1
- use python3 instead of python(2)

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.7-0.1.rc1
- konversation-1.7-rc1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-1
- 1.6.2

* Fri Jul 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-1
- 1.6.1

* Thu Mar 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.6-8
- fix icon scriptlets, set some pre-configured channels

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-6
- use %%license, %%lang'ify HTML docs

* Wed Oct 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-5
- purge /usr/bin/env runtime dep

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-3
- add Comment= key to .desktop file

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-1
- 1.6

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-0.1.beta1
- 1.6-beta1

* Tue Nov 04 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-1
- 1.5.1

* Mon Nov 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-8
- Connection to TLS-only server does not work (kde#340396)

* Wed Oct 29 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-7
- add update-desktop-database scriptlets 

* Mon Oct 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-6
- pull in 1.5 branch fixes, including... out-of-bounds read flaw (#1157342,1156418)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-4
- .spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-2
- Requires: kde-runtime

* Tue Jan 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-1
- 1.5(final)

* Wed Jan 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.7.rc2
- 1.5-rc2

* Sun Sep 29 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.6.20130929
- 20130929 snapshot

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.5-0.5.20130730
- Perl 5.18 rebuild

* Tue Jul 30 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.4.20130730
- 20130730 snapshot

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5-0.3.20130607
- Perl 5.18 rebuild

* Fri Jun 07 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.2.20130607
- 20130607 snapshot

* Sat Mar 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.1.rc1
- 1.5-rc1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-3
- rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-1
- 1.4 (final)

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-0.1.beta1
- 1.4-beta1
- pkgconfig-style deps

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for glibc bug#747377

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-5
- Crash in marker cleanup code (kde#210106)

* Sat Mar 12 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-4
- add Requires: qca-ossl

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.3.1-2
- added patch to fix scrolling background

* Thu Jul 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-1
- konversation-1.3.1

* Tue Jun 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3-1
- konversation-1.3

* Sat May 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3-0.1.beta1
- konversation-1.3-beta1

* Mon May 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.3-2.20100510
- 20100510 snapshot

* Fri Feb 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.3-1
- konversation-1.2.3

* Fri Feb 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.2-1
- konversation-1.2.2

* Wed Feb 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-3
- test out qt46/cpu/fonts patch (kde#215256)

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-2
- use %%{_kde4_version}

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-1
- konversation-1.2.1

* Fri Oct 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-1
- konversation-1.2 (final)

* Sat Oct 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.12.rc1
- konversation-1.2-rc1

* Mon Sep 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.11.beta1
- With auto-expand input box, ircview doesn't scroll (kdebug #208097)

* Mon Sep 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.10.beta1
- konversation-1.2-beta1

* Sat Sep 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.9.20090919svn
- localized snapshot

* Sat Sep 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.8.20090919svn1025849
- konversation-20090919svn1025849 snapshot, for marker line testing

* Mon Aug 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.6.alpha6
- BR: qca2-devel, libXScrnSaver-devel

* Tue Aug 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.5.alpha6
- add min kdelibs4 version

* Sat Aug 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.4.alpha6
- konversation-1.2-alpha6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.2.alpha4
- konversation-1.2-alpha4

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.1.alpha3
- konversation-1.2-alpha3
- optimize scriptlets

* Mon Mar 02 2009 Dennis gilmore <dennis@ausil.us> - 1.1-6
- make Patch and %%patch use the same number

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Dennis Gilmore <dennis@ausil.us> - 1.1-4
- rebuild

* Fri Feb 13 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1-3
- patch media script for amarok2 support

* Wed Feb 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1-2
- s/for KDE//

* Thu Aug 07 2008 Dennis Gilmore <dennis@ausil.us> - 1.1-1
- update to 1.1 final

* Tue Jul 15 2008 Dennis Gilmore <dennis@ausil.us> - 1.1-0.2.rc1
- fix stupidity

* Tue Jul 15 2008 Dennis Gilmore <dennis@ausil.us> - 1.1-0.1.rc1
- update to 1.1 rc1

* Wed Apr 09 2008 Dennis Gilmore <dennis@ausil.us> - 1.0.1-6
- apply patch from upstream handling CVE-2007-4400 correctly
- reenable media script

* Mon Mar 10 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-5
- drop Requires: kdebase3 (#435873)
- f9+: dfi vendor fedora -> kde
- %%doc ChangeLog COPYING README TODO

* Thu Feb 07 2008 Dennis Gilmore <dennis@ausil.us> - 1.0.1-4
- remove /usr/share/apps/konversation/scripts/media for CVE-2007-4400

* Tue Aug 28 2007 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- clarify license GPLv2+, and rebuild for F8

* Tue Oct 17 2006 Dennis Gilmore <dennis@ausil.us> - 1.0.1-2
- add gettext  as br  so translations get built correctly

* Fri Oct 06 2006 Dennis Gilmore <dennis@ausil.us> - 1.0.1-1
- Upgrade to 1.0.1

* Thu Sep 14 2006 Dennis Gilmore <dennis@ausil.us> - 1.0-1
- Upgrade to 1.0 :)

* Sat Sep 02 2006 Dennis Gilmore <dennis@ausil.us> - 0.19-3
- rebuild for fc6

* Tue Feb 14 2006 Dennis Gilmore <dennis@ausil.us> - 0.19-2
- rebuild for fc5

* Mon Jan 30 2006 Dennis Gilmore <dennis@ausil.us> - 0.19-1
- update to 0.19

* Thu Dec 22 2005 Dennis Gilmore <dennis@ausil.us> - 0.18-6
- Rebuild for gcc 4.1

* Sat Oct 22 2005 Dennis Gilmore <dennis@ausil.us> - 0.18-5
- add BuildRequires desktop-file-utils  http://fedoraproject.org/wiki/QAChecklist 
- add %%post and %%postun scriptlets  to notify of new icons per
- http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html#implementation_notes

* Sun Jul 03 2005 Dennis Gilmore <dennis@ausil.us> - 0.18-4
- Explicly export QT lib and include dirs  for x86_64 build issue

* Tue Jun 28 2005  Dennis Gilmore <dennis@ausil.us> - 0.18-3
- Destop-file-install,  change gcc4 patch  to configure  
  remove unneeded build deps.

* Mon Jun 27 2005  Dennis Gilmore <dennis@ausil.us> - 0.18-2
- Fix build requires,set QT, %%lang'ify LOCALE bits and HTML docs
  move automake to prep

* Sat Jun 25 2005  Dennis Gilmore <dennis@ausil.us> - 0.18-1
- Initial build
