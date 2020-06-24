
%global kbanking 1

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Summary: Personal finance 
Name:    kmymoney
Version: 5.0.8
Release: 5%{?dist}

# kmm itself is GPLv2+ 
# bundled kdchart is GPLv2 or GPLv3, but currently not using it
License: GPLv2+
Url:     http://kmymoney.org/
Source0: http://download.kde.org/stable/kmymoney/%{version}/src/kmymoney-%{version}.tar.xz

## upstreamable patches

## upstream patches
Patch100: 0100-Fix-transaction-filter-due-to-compiler-issue-with-g-.patch

BuildRequires: boost-devel
BuildRequires: cppunit-devel
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gettext

BuildRequires: libappstream-glib
BuildRequires: perl-generators
%if 0%{?kbanking}
BuildRequires: pkgconfig(aqbanking) >= 5.99
BuildRequires: cmake(gwengui-qt5) >= 4.99
%endif

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)

# TODO: test optional WebEngine support
BuildRequires: cmake(KF5WebKit)

BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Activities)

BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(KChart)

BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5PrintSupport)

BuildRequires: pkgconfig(ktoblzcheck)
BuildRequires: pkgconfig(libalkimia5) >= 8.0
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(libofx)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxml++-2.6)
BuildRequires: pkgconfig(glibmm-2.4)
## NEEDSWORK?
%global sqlcipher 1
BuildRequires: qt5-qtbase-private-devel
BuildRequires: pkgconfig(sqlcipher)
BuildRequires: pkgconfig(sqlite3)

## FIXME/TODO:
# kmymoney/payeeidentifier/ibanandbic/ibanbic.cpp includes gmpxx.h
BuildRequires: gmp-devel

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes: kmymoney2 < 2
Provides:  kmymoney2 = %{version}-%{release}

Obsoletes: kmymoney2-aqbanking < 2
Provides:  kmymoney2-aqbanking = %{version}-%{release} 


%description
KMyMoney strives to be the best personal finance manager.
The ultimate objectives of KMyMoney are...
* Accuracy.  Using time tested double entry accounting principles 
  helps ensure that your finances are kept in correct order.
* Ease of use.  Strives to be the easiest open source personal
  finance manager to use, especially for the non-technical user.
* Familiar Features.  Intends to provide all important features
  found in the commercially-available, personal finance managers.

%package libs
Summary: Run-time libraries for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: kmymoney2-libs < 2
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: kmymoney2-devel < 2
%description devel
%{summary}.

%package doc
Summary: Application handbook, documentation, translations
# for upgrade path
Obsoletes: kmymoney < 4.6.3
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kmymoney --with-html --without-mo && mv kmymoney.lang kmymoney-doc.lang
%find_lang kmymoney --with-man


%check 
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kmymoney.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kmymoney.desktop
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif


%files -f kmymoney.lang
%doc AUTHORS ChangeLog TODO
%doc README.Fileformats README.ofx
%license COPYING
%{_kf5_bindir}/kmymoney
%{_kf5_metainfodir}/org.kde.kmymoney.appdata.xml
%{_kf5_datadir}/applications/org.kde.kmymoney.desktop
%{_kf5_datadir}/checkprinting/
%{_kf5_datadir}/config.kcfg/k*.kcfg
%{_kf5_datadir}/kconf_update/kmymoney.upd
%{_kf5_datadir}/kmymoney/
%{_kf5_datadir}/kservices5/k*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kxmlgui5/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/mime/packages/x-kmymoney.xml
%{_mandir}/man1/kmymoney.1*
%if 0%{?kbanking}
%{_kf5_datadir}/kbanking/
%endif

%ldconfig_scriptlets libs

%files libs
%{_kf5_qtplugindir}/kmymoney/
%if 0%{?sqlcipher}
# adds dep on qt5 private api
%{_kf5_qtplugindir}/sqldrivers/qsqlcipher.so
%endif
%{_kf5_libdir}/libkmm_csvimportercore.so.5*
%{_kf5_libdir}/libkmm_icons.so.5*
%{_kf5_libdir}/libkmm_menus.so.5*
%{_kf5_libdir}/libkmm_models.so.5*
%{_kf5_libdir}/libkmm_mymoney.so.5*
%{_kf5_libdir}/libkmm_payeeidentifier.so.5*
%{_kf5_libdir}/libkmm_plugin.so.5*
%{_kf5_libdir}/libkmm_printer.so.5*
%{_kf5_libdir}/libkmm_settings.so.5*
%{_kf5_libdir}/libkmm_widgets.so.5*

%files devel
%{_includedir}/kmymoney/
%{_kf5_libdir}/lib*.so

%files doc -f kmymoney-doc.lang


%changelog
* Thu May 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-5
- pull in upstream gcc10 fix (kde#420761)

* Thu Apr 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-4
- enable autotests

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-3
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.8-1
- 5.0.8
- enable kbanking

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.7-2
- rebuild (qt5)

* Fri Sep 27 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.7-1
- 5.0.7
- disable kbanking support until updated aqbanking/gwenhywfar packaged

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.6-2
- rebuild (qt5)

* Tue Aug 20 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.6-1
- 5.0.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.5-1
- 5.0.5

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.4-3
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.4-2
- rebuild (qt5)

* Tue Apr 23 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.4-1
- 5.0.4

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.3-2
- rebuild (qt5)

* Thu Jan 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.3-1
- 5.0.3 (#1670007)

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-2
- rebuild (qt5)

* Mon Nov 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-1
- 5.0.2
- (re)enable sqlcipher support

* Wed Jul 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-5
- backport upstream Q5.11 fix

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Bill Nottingham <notting@splat.cc> - 5.0.1-3
- rebuild for libofx/gwen/aqbanking soname changes

* Mon Mar 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-1
- kmymoney-5.0.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-8
- backport gpgme-related patch (allow use of gpgmepp)

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-7
- backport fix for missing headers

* Thu Aug 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-6
- fix FTBFS related to newer cmake

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-3
- use bundled kdchart (calligra3 no longer provides it)
- include upstream fix for duplicated symbols

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- kmymoney-4.8.0

* Thu Jul 07 2016 Bill Nottingham <notting@splat.cc> - 4.7.2-5
- rebuild for aqbanking-5.6.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-3
- rebuild(libalkimia), update URL, .spec cosmetics

* Sat Jan 23 2016 Robert Scheck <robert@fedoraproject.org> - 4.7.2-2
- Rebuild for libical 2.0.0

* Sun Sep 13 2015 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2 (#1243475)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.7.1-10
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.7.1-8
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.7.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-5
- rebuild (kdchart)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.7.1-4
- Rebuild for boost 1.57.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.7.1-3
- Rebuild for boost 1.57.0

* Sat Jan 24 2015 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-2
- kde-apps fixes

* Mon Nov 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-1
- 4.7.1 (#1159491)

* Fri Oct 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-1
- 4.7.0

* Fri Oct 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.6-4
- backport upstream appstreaam data from 4.7.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.6-2
- optimize mimeinfo scriptlet

* Mon Jun 23 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.6-1
- kmymoney-4.6.6

* Fri Jun 20 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.5-1
- kmymoney-4.6.5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.6.4-5
- Rebuild for boost 1.55.0

* Fri Mar 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.4-4
- rebuild (kdchart)

* Thu Jan 16 2014 Bill Nottingham <notting@redhat.com> - 4.6.4-3
- rebuild (aqbanking)

* Mon Dec 16 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.4-2
- rebuild (kdchart)

* Sat Oct 05 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.4-1
- kmymoney-4.6.4

* Mon Sep 23 2013 Bill Nottingham <notting@redhat.com> - 4.6.3-13
- rebuild against new libofx

* Thu Aug 29 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-12
- Requires: kde-runtime (#1002429)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 4.6.3-10
- Rebuild for boost 1.54.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.6.3-9
- Perl 5.18 rebuild

* Sat Jun 29 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-8
- rebuild (calligra-kdchart)

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-7
- rebuild (libical)

* Wed Apr 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-6
- pull in a bunch of 4.6 branch fixes, in particular...
- 0020-Fix-build-with-GMP-5.1.0.patch

* Wed Apr 24 2013 Bill Nottingham <notting@redhat.com> 4.6.3-5
- rebuild (aqbanking)

* Mon Mar 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-4.2
- rebuild (calligra-kdchart)

* Mon Feb 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-4
- Only american english language available (#902501)

* Wed Nov 07 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-3
- rebuild (calligra-kdchart)

* Fri Sep 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-2
- file conflicts between kmymoney and kmymoney-doc (#859495)

* Tue Sep 11 2012 Rex Dieter <rdieter@fedoraproject.org>
- 4.6.3-1
- kmymoney-4.6.3 
- -libs: Requires: kdelibs4 ...
- -doc subpkg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.2-3
- rebuild (libofx)

* Sun Jun 17 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.2-2
- rebuild (kdchart)

* Sat Mar 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.2-1.1
- rebuild (calligra/kdchart)

* Sun Feb 19 2012 Rex Dieter <rdieter@fedoraproject.org> 4.6.2-1
- 4.6.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Wed Nov 02 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-2
- rebuild (gmp)

* Sun Aug 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-1
- 4.6.0
- use more pkgconfig-type build deps

* Thu Feb 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.5.3-1.1
- BR: aqbanking-devel >= 5.0

* Sun Feb 13 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.5.3-1
- kmymoney-4.5.3

* Fri Feb 11 2011 Bill Nottingham <notting@redhat.com> - 4.5.2-4
- rebuild against aqbanking5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.5.2-2
- rework/simplify rpath patch
- hicolor_icons patch

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- kmymoney-4.5.2

* Fri Nov 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- kmymoney-4.5.1

* Tue Nov 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5-2
- rebuild (kdchart)

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5-1
- kmymoney-4.5

* Sun May 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.98.0-1
- kmymoney-3.98.0

* Wed Apr 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.97.2-1
- kmymoney-3.97.2
- License: GPLv2 or GPLv3
- omit .directory files from packaging
- -debuginfo: fix world-writable perms in generated headers 

* Fri Apr 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.97.0-1
- kmymoney-3.97.0
- use external/shared kdchart

* Fri Mar 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.96.1-1
- kmymoney-3.96.1 (for kde4, beta)
- Obsoletes: kmymoney2 (and friends)

* Mon Feb 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.3-1
- kmymoney2-1.0.3

* Thu Jan 21 2010 Bill Nottingham <notting@redhat.com> - 1.0.2-2
- rebuild against latest aqbanking/qbanking

* Sun Oct 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.2-1
- kmymoney2-1.0.2

* Sun Sep 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- kmymoney2-1.0.1

* Wed Aug 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- kmymoney2-1.0.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-3
- validate .desktop file
- -libs unconditional
- use %%_isa where appropriate
- optimize scriptlets

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 24 2009 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-1
- kmymoney2-0.9.3

* Mon Sep 15 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-3
- respun tarball 

* Sun Sep 14 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-1
- kmymoney2-0.9.2

* Tue Sep  9 2008 Bill Nottingham <notting@redhat.com> 0.9-2
- rebuild for new libofx ABI

* Wed May 14 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- kmymoney2-0.9

* Wed Mar 26 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.9-1
- kmymoney2-0.8.9
- --disable-kbanking (requires aqbanking,kbanking fix/update)
- drop multilib upgrade hack

* Fri Feb 22 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.8-3
- gcc43 patch (#434398)
- multiarch conflicts, -libs subpkg (#341821)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.8-2
- Autorebuild for GCC 4.3

* Wed Dec 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.8-1
- kmymoney2-0.8.8
- --enable-kbanking

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.7-5
- BR: kdelibs3-devel

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.7-4
- respin (BuildID)

* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.7-3
- License: GPLv2+

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> 0.8.7-2
- Rebuild for RH #249435

* Mon Jul 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.7-1
- kmymoney2-0.8.7

* Sat Mar 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.6-1
- kmymoney2-0.8.6
- fix Obsoletes: kmymoney

* Thu Jan 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-3
- fix _enable_ofxbanking macro usage to re-enable ofx support

* Tue Nov 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.5-2
- drop desktop-file-utils bits
- Ob/Pr: kmymoney(-devel), upstream/rpmforge calls it kmymoney

* Thu Aug 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.5-1
- 0.8.5

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.4-2
- --disable-final (for now)
- BR: gettext

* Sun May 21 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.4-1
- 0.8.4

* Thu Apr 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-3
- desktop-file-install --vendor=""

* Wed Feb 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-1
- 0.8.3

* Fri Feb 10 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Sat Dec 31 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-1
- 0.8.2

* Fri Dec 23 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-7
- gcc41 patch

* Fri Dec 23 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-6
- cleanup ofx deps

* Fri Dec 23 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-5
- cleanup %%post
- fc5 respin for new(er) libofx

* Mon Nov 14 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-4
- relax BR: kdelibs-devel to 3.3 (for aurora/sparc, #173133)

* Thu Nov 10 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-3
- fix relative symlinks

* Wed Nov 09 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-2
- qt-3.3.5 patch
- 'make check' workaround (kde bug #115863)
- trim %%description

* Sat Nov 05 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-1
- 0.8.1

* Fri Nov 04 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8-5
- drop useless macros
- use %%fedora,%%rhel to conditionalize ofxbanking support

* Fri Oct 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8-4
- %%post,%%postun: gtk-update-icon-cache, update-desktop-database
- omit lib*.la
- x86_64: set QTDIR/QTLIB

* Thu Sep 01 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8-3
- BR: libofx-devel

* Tue Aug 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8-2
- simplify specfile
- fix build

* Fri Aug 12 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8-1
- 0.8

