%undefine __cmake_in_source_build

%bcond_with doxy

%global gitdate 20191104
%global commit0 36b05871b00f282f5d5695e036d1efe0765cd1d2
%global srcurl  https://github.com/KDE/%{name}
#%%global srcurl  https://github.com/jktjkt/%{name}

Name:           trojita
%if 0%{?gitdate}
Version:        0.7.0.1
Release:        0.7.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
Source0:        %{srcurl}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Version:        0.7
Release:        6%{?dist}
Source0:        %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# manually generated manpage with help2man
# help2man -o trojita.1 --no-info --no-discard-stderr -h --version-string=0.6 /usr/bin/trojita
#Source1:        trojita.1

# cd $SRCDIR ; python3 ./l10n-fetch-po-files.py ; tar czf ../%%{name}_common-po-20190729.tar.gz po/
# calls svn to get latest po files
Source10:       %{name}_common-po-20190729.tar.gz

### upstream patches
# Fix GPG test, otherwise b0rken with gnupg2 v2.1.16
Patch0:         %{srcurl}/commit/be8fd5831afa0a04f14cd6206e6576f03ee59558.patch
# tests: Skip QtWebKit tests when building with ASAN
Patch1:         %{srcurl}/commit/73a7b085454ca5b9d8f28529da26c54c5109678a.patch

## downstream patches
# rhbz#1401716, increase timeout for CryptographyPGPTest::testDecryption
#Patch10:         delay-test_Cryptography_PGP.patch

# disable the GPG tests because they fail due to a GPG limitation:
# gpg: can't connect to the agent: File name too long
# https://bugs.kde.org/show_bug.cgi?id=410414
Patch11:        trojita-0.7.0.1-disable-gpg-tests.patch

# Almost everything: dual-licensed under the GPLv2 or GPLv3
# (with KDE e.V. provision for relicensing)
# src/XtConnect: BSD
# src/Imap/Parser/3rdparty/kcodecs.*: LGPLv2
# Nokia imports: LGPLv2.1 or GPLv3
# src/Imap/Parser/3rdparty/rfccodecs.cpp: LGPLv2+
# src/qwwsmtpclient/: GPLv2
## note that LGPL 2.1 short name is LGPLv2 according to
## https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
#License:        GPLv2+ and LGPLv2+ and BSD
License:        GPLv2+

Summary:        IMAP e-mail client
URL:            http://%{name}.flaska.net

# rhbz#1402577 ppc64* FIXME: src/Imap/Parser/Rfc5322HeaderParser.cpp:2238:3:
# error: narrowing conversion of '-1' from 'int' to 'char' inside { } [-Wnarrowing]
# also rhbz#1402580 aarch64 and rhbz#1450505 s390x
ExcludeArch:    ppc64 ppc64le s390x
# rhbz#1402582 FIXME: ragel core dumps
#ExcludeArch:    armv7hl
# both issues above for aarch64
#ExcludeArch:    aarch64

BuildRequires:  kf5-rpm-macros
%global ctest ctest%{?rhel:3} %{?_smp_mflags} --output-on-failure -VV

# pre-build: generation of additional sources
#BuildRequires:  python2 subversion
#BuildRequires:  help2man

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qttools-devel

# explicitly install Qt5Svg for runtime, rpmbuild's magic fails
Requires:       qt5-qtsvg

# (optional) features
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtkeychain-qt5-devel
%if 0%{?fedora}
#BuildRequires:  ragel
%endif

# (optional) support for GPG and S/MIME
BuildRequires:  gnupg2-smime
BuildRequires:  kf5-gpgmepp-devel
BuildRequires:  gpgme-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  boost-devel
BuildRequires:  mimetic-devel
# fix for inside mockbuild, gpg: deleting secret key failed: No pinentry
BuildRequires:  pinentry
BuildRequires:  qgpgme-devel

BuildRequires:  kf5-akonadi-contacts-devel
BuildRequires:  kf5-sonnet-devel


%if %{with doxy}
BuildRequires:  doxygen graphviz
%endif

# needs for %%check
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  xorg-x11-server-Xvfb

# provide some icons
Requires:       hicolor-icon-theme

%description
Trojitá is a IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity of an e-mail
    user, we better do.
  * Respects open standards and facilitates modern technologies. We value
    the vendor-neutrality that IMAP provides and are committed to be as
    inter-operable as possible.
  * Is efficient — be it at conserving the network bandwidth, keeping memory
    use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone, but our
    IMAP core works fine on anything from desktop computers to cell phones
    and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing wheels,
    but when the existing wheels quite don't fit the tracks, we're not afraid
    of making them work.

This application is heavily based on Qt and uses WebKit.


%prep
%if 0%{?gitdate}
%setup -qn%{name}-%{commit0} -a10
%patch11 -p1 -b .disable-gpg-tests
%else
%autosetup -p1 -a10
%endif

%build
%if %{without testsqtwebkit}
export CXXFLAGS="%{optflags} -DSKIP_WEBKIT_TESTS"
%endif
# change path for the library, https://bugs.kde.org/show_bug.cgi?id=332579
%cmake_kf5 \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=%{_libdir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DWITH_AKONADIADDRESSBOOK_PLUGIN:BOOL=ON \
    -DWITH_GPGMEPP:BOOL=ON \
    -DWITH_SONNET_PLUGIN:BOOL=ON \
    -DWITH_RAGEL:BOOL=OFF
%cmake_build

%if %{with doxy}
doxygen src/Doxyfile
%endif

%install
%cmake_install
%find_lang %{name}_common --with-qt
# work around find_lang not supporting nds
echo '%lang(nds) %{_datadir}/%{name}/locale/%{name}_common_nds.qm' \
    >>%{name}_common.lang
#install -m644 -p -D %%{SOURCE1} %%{buildroot}%%{_mandir}/man1/%%{name}.1


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop
# appstream is not available in EPEL
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*%{name}.appdata.xml
%endif
# do tests in some fake X
#xvfb-run -a find %%{_target_platform} -name test_\* -print -exec '{}' \;
xvfb-run -a %ctest


%files -f %{name}_common.lang
%license LICENSE
%doc README src/Doxyfile
#%%{_mandir}/man1/%%{name}.1*
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/be.contacts
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale

%if %{with doxy}
# optional developer documentation
%package doc
BuildArch: noarch
Summary:   Documentation files for %{name}

%description doc
%{summary}.

%files doc
%license LICENSE
%doc _doxygen/*
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.7.20191104git36b0587
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.6.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.5.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.4.20190618git90b417b
- new git snapshot, enable builds for armv7hl and aarch64

* Thu Oct 10 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.3.20190618git90b417b
- rebuilt

* Mon Jul 29 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0.1-0.2.20190618gitIcf4fda
- work around GPG test failure (kde#410414, GPG/kernel limitation) by disabling
  the offending tests for now (pending a better fix from upstream)
- add missing BuildRequires: qgpgme-devel
- fix unpackaged file (work around find_lang not supporting nds (Low Saxon))
- fix unowned locale parent directories

* Sun Jul 28 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.1.20190618gitIcf4fda
- use latest git snapshot with a bunch of fixes
- enable build testing, again
- enable akonadi addressbook plugin
- enable sonnet plugin
- enable gpgmepp plugin, again
- disable ragel,  rhbz#1734036

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-9
- add patch to skip instable tests for qtwebkit
- merge unpacking of po files into setup command

* Fri May 12 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-8
- add s390x to exluded architectures

* Mon Feb 27 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-8
- rebuilt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7-6
- Rebuild for gpgme 1.18

* Wed Dec 07 2016 Builder <projects.rg@smart.ms> - 0.7-5
- add ExcludeArch
- fix gpg test
- add BR: gnupg2-smime

* Sat Jul 02 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-4
- [epel7] rebuild for qtkeychain-0.7.0

* Sat Jun 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-3
- explicitly R: qt5-qtsvg

* Sat Jun 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-2
- [epel7] enable gpg and mimetic
- [epel7] fix cmake for kf5
- improve some comments
- [epel7] appstream is not available
- [epel7] fix ctest

* Sun Jun 12 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-1
- official upstream version

* Sun Jun 12 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-0.1.20160610git8901a5c
- switch to git snapshot
- add support for GPG and MIME
- drop manpage
- use target build folder

* Mon May 23 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6-6
- Rebuild for qtkeychain new release

* Fri May 20 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-5
- rebuild due to qtkeychain ABI change

* Tue Apr 05 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-4
- reenable tests on all arches, icu/gcc6 bug is fixed, rhbz#1307633, rhbz#1309731

* Tue Mar 08 2016 Rex Dieter <rdieter@fedoraproject.org> 0.6-3
- drop DBUS_FATAL_WARNINGS=0 hack, rhbz#1309731 fixed
- use pregenerated trojita manpage (built-time one is bad)

* Sun Feb 21 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-2
- use xvfb-run -a
- workaround for FTBFS cause of dbus, rhbz#1309731
- disable fatal warnings

* Tue Feb 02 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-1
- new version
- use xvfb-run

* Wed Dec 16 2015 Raphael Groner <projects.rg@smart.ms> - 0.5a-2.20151216gitefa30f3
- add QtKeyChain
- drop qt4

* Wed Dec 16 2015 Raphael Groner <projects.rg@smart.ms> - 0.5a-1.20151216gitefa30f3
- use latest upstream snapshot as post-release
- finally well Qt5.6 support!

* Sat Dec 12 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-9
- add upstream patches for Qt5.x

* Mon Oct 05 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-8
- add missing headers inclusion, rhbz#1266712

* Fri Jun 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-7
- fix build conditional for optional doxygen

* Fri Jun 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-6
- optional BR: at EPEL

* Wed Jun 24 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-5
- add files validation
- use license GPLv2+ aggregated
- use build conditionals
- insert some comments
- insert BR: zlib-devel (optional imap compression)

* Wed Apr 01 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-4
- reenable html formatting testcase
- optional doxygen

* Wed Apr 01 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-3
- ease switching build with qt4 or qt5
- disable doxygen
- remove toolkit from summary
- use build subfolder
- improve tests execution

* Tue Mar 31 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-2
- build for qt5

* Sat Feb 28 2015 Raphael Groner <projects.rg (AT) smart.ms> - 0.5-1
- clean files section and R: hicolor-icon-theme
- introduce license macro
- use name macro generally
- new upstream version 0.5
- distribute doxygen files

* Mon Oct 27 2014 Karel Volný <kvolny@redhat.com> 0.4.1-3
- Added ragel build requirement

* Mon Apr 14 2014 Karel Volný <kvolny@redhat.com> 0.4.1-2
- Fixed icon handling and added comments as per the package review
- https://bugzilla.redhat.com/show_bug.cgi?id=1080411#c2

* Tue Mar 25 2014 Karel Volný <kvolny@redhat.com> 0.4.1-1
- Initial Fedora version based on upstream OBS package
