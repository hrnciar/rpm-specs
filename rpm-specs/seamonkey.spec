%bcond_without	system_nspr
%bcond_without	system_nss
%bcond_without	system_libvpx
%bcond_without	system_icu
%bcond_without	system_sqlite
%bcond_without	system_ffi
%bcond_with	system_hunspell
%bcond_with	system_cairo

%bcond_without	langpacks
%bcond_without	clang
%bcond_with	lto
%bcond_with	stylo

%bcond_without	calendar
%bcond_without	dominspector
%bcond_without	irc
%bcond_with	debugqa

%global nspr_version	4.21.0
%global nss_version	3.44.0
%global libvpx_version	1.5.0
%global icu_version	59.1
%global sqlite_version	3.31.1
%global ffi_version	3.0.9
%global	hunspell_version 1.6.1
%global cairo_version	1.10

%define homepage http://start.fedoraproject.org/

%define sources_subdir %{name}-%{version}

%define seamonkey_app_id	\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}


Name:           seamonkey
Summary:        Web browser, e-mail, news, IRC client, HTML editor
Version:        2.53.2
Release:        2%{?dist}
URL:            http://www.seamonkey-project.org
License:        MPLv2.0


Source0:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
%if %{with langpacks}
Source1:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
%endif

Source3:        seamonkey.sh.in
Source4:        seamonkey.desktop
Source12:       seamonkey-mail.desktop
Source13:       seamonkey-mail.svg
Source100:      seamonkey-find-requires.sh

Patch3:		firefox-60-mozilla-1516803.patch
Patch5:		firefox-35-rhbz-1173156.patch
Patch6:		firefox-56-build-prbool.patch
Patch7:		firefox-51-mozilla-1005640.patch
Patch8:		firefox-48-mozilla-256180.patch
Patch10:	firefox-56-mozilla-440908.patch
Patch11:	firefox-60-mozilla-1436242.patch
Patch13:	seamonkey-2.53.1-mozilla-revert-1332139.patch
Patch14:	seamonkey-2.53.2-sysctl.patch
Patch16:	firefox-52-rhbz-1451055.patch
Patch20:	seamonkey-2.53.2-system_nss_nspr.patch
Patch30:	seamonkey-2.53.1-rhbz-1503632.patch
Patch31:	seamonkey-2.53.1-mozilla-526293.patch
Patch32:	seamonkey-2.53.2-useragent.patch
Patch34:	seamonkey-2.53.1-startupcache.patch

%{?with_system_nspr:BuildRequires:      nspr-devel >= %{nspr_version}}
%{?with_system_nss:BuildRequires:       nss-devel >= %{nss_version}}
%{?with_system_nss:BuildRequires:       nss-static >= %{nss_version}}
%{?with_system_libvpx:BuildRequires:    libvpx-devel >= %{libvpx_version}}
%{?with_system_icu:BuildRequires:       libicu-devel >= %{icu_version}}
%{?with_system_sqlite:BuildRequires:    sqlite-devel >= %{sqlite_version}}
%{?with_system_ffi:BuildRequires:       libffi-devel >= %{ffi_version}}
%{?with_system_hunspell:BuildRequires:  hunspell-devel >= %{hunspell_version}}
%{?with_system_cairo:BuildRequires:     cairo-devel >= %{cairo_version}}

BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  zlib-devel
BuildRequires:  zip
BuildRequires:  libIDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  krb5-devel
BuildRequires:  pango-devel
BuildRequires:  freetype-devel >= 2.1.9
BuildRequires:  glib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  coreutils
BuildRequires:  alsa-lib-devel
BuildRequires:  libnotify-devel
BuildRequires:  yasm >= 1.1
BuildRequires:  mesa-libGL-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  startup-notification-devel

BuildRequires:  autoconf213
BuildRequires:  python27

%if %{with clang} || %{with stylo}
BuildRequires:	clang, llvm-devel
%endif
%if %{without clang}
BuildRequires:	gcc-c++ >= 6.1
%endif

BuildRequires:	rust >= 1.35
BuildRequires:	cargo

Requires:       mozilla-filesystem
Requires:       hicolor-icon-theme
Requires:       p11-kit-trust
%if %{with system_nspr}
Requires:       nspr >= %(pkg-config --silence-errors --modversion nspr 2>/dev/null || echo %{nspr_version})
%endif
%if %{with system_nss}
Requires:       nss >= %(pkg-config --silence-errors --modversion nss 2>/dev/null || echo %{nss_version})
%endif
%if %{with system_sqlite}
Requires:       sqlite >= %(pkg-config --silence-errors --modversion sqlite 2>/dev/null || echo %{sqlite_version})
%endif

# ppc64:   http://bugzilla.redhat.com/bugzilla/866589
# armv7hl: http://bugzilla.redhat.com/bugzilla/1035485
# %{ix86}: no more supported upstream
ExclusiveArch:  x86_64

%define _use_internal_dependency_generator 0
%define __find_requires %{SOURCE100}
#  prepare .desktop files only...
%define __find_provides /usr/lib/rpm/desktop-file.prov

Provides: webclient


%description
SeaMonkey is an all-in-one Internet application suite. It includes 
a browser, mail/news client, IRC client, JavaScript debugger, and 
a tool to inspect the DOM for web pages. It is derived from the 
application formerly known as Mozilla Application Suite.
 

%prep

%setup -q -c

%if %{with langpacks}
%setup -q -T -D -c -n %{name}-%{version}/%{sources_subdir}/l10n -a 1
#  come back...
%setup -q -T -D
%endif

cd %{sources_subdir}

pushd mozilla
%patch3 -p1 -b .1516803
%patch5 -p2 -b .1173156
%patch6 -p1 -b .prbool
%patch7 -p1 -b .1005640
%patch8 -p1 -b .256180
%patch10 -p1 -b .440908
%patch11 -p1 -b .1436242
%{?with_system_libvpx:%patch13 -p1 -b .1332139}
%patch14 -p1 -b .sysctl
%patch16 -p1 -b .1451055
popd

%patch20 -p2 -b .system_nss_nspr
%patch30 -p2 -b .1503632
%patch31 -p2 -b .526293
%patch32 -p1 -b .useragent
%patch34 -p1 -b .startupcache

%if %{without calendar}
sed -i 's/MOZ_CALENDAR/UNDEF_MOZ_CALENDAR/' suite/installer/package-manifest.in
%endif


#
#   generate .mozconfig
#

cat >.mozconfig <<EOF
ac_add_options --enable-application=suite

export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1

ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}

#  to know where to remove extra things...
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}

ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --with-pthreads
ac_add_options --disable-tests
ac_add_options --disable-install-strip
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --enable-chrome-format=omni
ac_add_options --disable-necko-wifi
ac_add_options --enable-startup-notification
ac_add_options --enable-optimize=-O2

ac_add_options --enable-startupcache

%define with_sys()	ac_add_options --with%%{!?with_system_%1:out}-system-%1
%define endis_sys()	ac_add_options --%%{?with_system_%1:enable}%%{!?with_system_%1:disable}-system-%1
%define endis()		ac_add_options --%%{?with_%1:enable}%%{!?with_%1:disable}-%1

%{expand:%with_sys   nspr}
%{expand:%with_sys   nss}
%{expand:%with_sys   libvpx}
%{expand:%with_sys   icu}

%{expand:%endis_sys  sqlite}
%{expand:%endis_sys  ffi}
%{expand:%endis_sys  hunspell}
%{expand:%endis_sys  cairo}

#  always enable calendar to build needed internal components required for both bundled and external addons
ac_add_options --enable-calendar

%{expand:%endis dominspector}
%{expand:%endis irc}
%{expand:%endis debugqa}


ac_add_options --disable-webrender
ac_add_options %{?with_stylo:--enable-stylo=build}%{!?with_stylo:--disable-stylo}


%if %{with langpacks}
ac_add_options --with-l10n-base=../l10n
%endif

EOF
#  .mozconfig


#
#   generate default prefs
#
cat >all-fedora.js <<EOF

pref("app.update.auto", false);
pref("app.update.enabled", false);
pref("app.updatecheck.override", true);
pref("browser.display.use_system_colors", true);
pref("browser.helperApps.deleteTempFileOnExit", true);
pref("general.smoothScroll", true);
pref("intl.locale.matchOS",   true);
pref("extensions.shownSelectionUI", true);
pref("extensions.autoDisableScopes", 0);
pref("shell.checkDefaultApps",   0);
pref("media.gmp-gmpopenh264.provider.enabled", false);
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.enabled", false);
pref("gfx.xrender.enabled", true);
pref("devtools.webide.enabled", false);

/*  use system dictionaries (hunspell)   */
pref("spellchecker.dictionary_path", "%{_datadir}/myspell");

/* Allow sending credetials to all https:// sites */
pref("network.negotiate-auth.trusted-uris", "https://");

/* To avoid UA string garbling by the old instances of Lightning  */
lockPref("calendar.useragent.extra", "");

pref("general.useragent.compatMode.strict-firefox", true);

EOF
# all-fedora.js

#  default homepage can be actually changed in localized properties only
sed -i -e "s|browser.startup.homepage.*$|browser.startup.homepage = %{homepage}|g" \
	suite/locales/en-US/chrome/browser/region.properties


%build

cd %{sources_subdir}

%if %{with clang}
export CC=clang
export CXX=clang++
%endif

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-Wall//')
MOZ_LINK_FLAGS=

#  Still not handled by clang < 11
%if %{with clang}
MOZ_OPT_FLAGS=$(echo $MOZ_OPT_FLAGS | sed -e 's/-fstack-clash-protection//')
%endif

#  needed for -Werror=format-security
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wformat"
#  just temporary for gcc9 ...
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wno-format-overflow"

%if %{with lto}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto"
%if %{with clang}
export AS=llvm-as
export AR=llvm-ar
export RANLIB=llvm-ranlib
export STRIP=llvm-strip
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -fuse-ld=gold"
%else
export AR=gcc-ar
export RANLIB=gcc-ranlib
%endif
%endif

%if %(awk '/^MemTotal:/ { print $2 }' /proc/meminfo) <= 4200000
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--no-keep-memory"
%if %{without clang} || %{without lto}
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--reduce-memory-overheads"
%endif
%endif
  
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS
export LDFLAGS=$MOZ_LINK_FLAGS


MOZ_SMP_FLAGS=%{?_smp_mflags}
[ ${MOZ_SMP_FLAGS#-j} -gt 8 ] && MOZ_SMP_FLAGS=-j8

make -f client.mk build MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"


%if %{with langpacks}

languages=`ls l10n | while read lang
       do
           case "$lang" in
               en-US)  continue ;;
               [a-z][a-z])  ;;
               [a-z][a-z]-[A-Z][A-Z])  ;;
               *)  continue ;;     #  drops ja-JP-mac as well...
           esac
           echo $lang
       done`

pushd obj-*/suite/locales

for lang in $languages
do
    make langpack-$lang
done

popd
%endif #  langpacks


%install

cd %{sources_subdir}

DESTDIR=$RPM_BUILD_ROOT make -f client.mk install

#  not needed in non-sdk install
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/seamonkey-devel
rm -rf $RPM_BUILD_ROOT%{_datadir}/idl/seamonkey

install -p -m 644 -D obj-*/dist/man/man1/seamonkey.1	$RPM_BUILD_ROOT/%{_mandir}/man1/seamonkey.1

rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/removed-files
rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/libnssckbi.so

#   default prefs
install -p -m 644 all-fedora.js \
	$RPM_BUILD_ROOT/%{_libdir}/seamonkey/defaults/pref/all-fedora.js

install -d -m 755 $RPM_BUILD_ROOT/%{_libdir}/seamonkey/plugins || :


echo >../seamonkey.lang

%if %{with langpacks}

for langpack in `ls obj-*/dist/linux-*/xpi/*.langpack.xpi`; do
    language=${langpack%.langpack.xpi}
    language=${language##*.}

    dir=$RPM_BUILD_ROOT/%{_libdir}/seamonkey/extensions/langpack-$language@seamonkey.mozilla.org
    mkdir -p $dir

    unzip $langpack -d $dir
    find $dir -type f | xargs chmod 644
    find $dir -name ".mkdir.done" | xargs rm -f

    sed -i -e "s|browser.startup.homepage.*$|browser.startup.homepage = %{homepage}|g" \
           $dir/chrome/$language/locale/$language/navigator-region/region.properties

    jarfile=$dir/chrome/$language.jar
    pushd $dir/chrome/$language
    zip -r -D $jarfile locale
    popd
    rm -rf $dir/chrome/$language  #  now in jarfile

    mv -f $dir/chrome/$language.manifest $dir/chrome.manifest
    #  fix manifest to point to jar
    sed -i -e "s,$language/locale,jar:chrome/$language.jar!/locale," $dir/chrome.manifest 

    language=${language/-/_}
    dir=${dir#$RPM_BUILD_ROOT}
    echo "%%lang($language) $dir" >>../seamonkey.lang
done


%if %{with calendar}

ext=\{e2fda1a4-762b-4020-b5ad-a41df1933103\}
extfile=$RPM_BUILD_ROOT/%{_libdir}/seamonkey/distribution/extensions/$ext.xpi

mkdir tmp
unzip $extfile -d tmp

for dir in `ls -d obj-*/dist/xpi-stage/locale-*/distribution/extensions/$ext`
do
    cp -aL $dir/chrome/calendar-* $dir/chrome/lightning-* tmp/chrome/
    cat $dir/chrome.manifest >>tmp/chrome.manifest
done

pushd tmp
sort chrome.manifest >chrome.manifest.new && mv -f chrome.manifest.new chrome.manifest

rm -f $extfile
zip -r -D $extfile .
popd
rm -rf tmp

%endif


%if %{with irc}

ext=\{59c81df5-4b7a-477b-912d-4e0fdf64e5f2\}
extfile=$RPM_BUILD_ROOT/%{_libdir}/seamonkey/distribution/extensions/$ext.xpi

mkdir tmp
unzip $extfile -d tmp

for dir in `ls -d obj-*/dist/xpi-stage/chatzilla-*/chrome`
do
    cp -aL $dir/chatzilla/locale/* tmp/chrome/chatzilla/locale/
    cat $dir/chatzilla.manifest >>tmp/chrome/chatzilla.manifest
done

pushd tmp
sort chrome/chatzilla.manifest >chrome/chatzilla.manifest.new && \
       mv -f chrome/chatzilla.manifest.new chrome/chatzilla.manifest

rm -f $extfile
zip -r -D $extfile .
popd
rm -rf tmp

%endif

%endif #  langpacks


# install desktop files in correct directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE12}

# install icons
pushd $RPM_BUILD_ROOT%{_libdir}/seamonkey/chrome/icons/default
icons=$RPM_BUILD_ROOT%{_datadir}/icons/hicolor
# seamonkey icons
install -p -m 644 -D default16.png	$icons/16x16/apps/seamonkey.png
install -p -m 644 -D default.png	$icons/32x32/apps/seamonkey.png
install -p -m 644 -D default48.png	$icons/48x48/apps/seamonkey.png
install -p -m 644 -D default64.png	$icons/64x64/apps/seamonkey.png
install -p -m 644 -D default128.png	$icons/128x128/apps/seamonkey.png
# seamonkey mail icons
install -p -m 644 -D messengerWindow16.png	$icons/16x16/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow.png	$icons/32x32/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow48.png	$icons/48x48/apps/seamonkey-mail.png
install -p -m 644 -D %{SOURCE13}		$icons/scalable/apps/seamonkey-mail.svg
popd


# System extensions
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/extensions/%{seamonkey_app_id}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/%{seamonkey_app_id}


%files -f seamonkey.lang

%license %{_libdir}/seamonkey/license.txt

%{_libdir}/seamonkey

%{_bindir}/seamonkey
%{_mandir}/*/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop

%dir %{_datadir}/mozilla/extensions/%{seamonkey_app_id}
%dir %{_libdir}/mozilla/extensions/%{seamonkey_app_id}


%changelog
* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 2.53.2-2
- Rebuild for ICU 67

* Mon May  4 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.2-1
- update to 2.53.2
- drop startup shell script (no more needed)

* Thu Apr  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-5
- rebuild with rust-1.42

* Wed Mar 25 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-4
- drop system-bookmarks dependencies

* Sat Mar 21 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-3
- fix localization for bundled calendar and chatzilla (#1815109)
- clear obsolete stuff from desktop-file-install

* Tue Mar  3 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-2
- add patch for classic theme (#1808197)

* Fri Feb 28 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-1
- Upgrade to 2.53.1
- use clang to build

* Mon Sep  9 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-2
- rebuid to properly handle external lightning extension (#1750450)

* Sat Aug 24 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-1
- update to 2.49.5
- add support for conditional build of inspector and irc

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-5
- add patch for new gettid() in glibc >= 2.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.49.4-4
- rebuilt (libvpx)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.49.4-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.4-1
- update to 2.49.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-3
- Rebuild for ICU 62

* Wed May 16 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-2
- Rebuild for ICU 61.1

* Fri May  4 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.3-1
- update to 2.49.3

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.2-3
- Rebuild for ICU 61.1

* Sun Feb 18 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-2
- revert some upstream gtk3-related changes to avoid regressions
  since we still build with gtk2 (mozbz#1269145, mozbz#1398973)
- spec file cleanup from old deprecated stuff

* Sat Feb 17 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-1
- update to 2.49.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-4
- rebuild for libvpx 1.7.0

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> 2.49.1-3
- rebuild for new libvpx

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> 2.49.1-2
- rebuild for hunspell 1.6.2

* Sat Oct 21 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-1
- update to 2.49.1
- apply some patches from firefox-52.4.0 package
- disable webide by default to avoid autoload of broken addons

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.48-1
- update to 2.48
- apply some patches from firefox-51 package
- use standard optimize level -O2 for compiling
- new langpacks obtaining stuff for more easier maintaining
- revert broken mozbz#1148544 changes for site-specific overrides

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-2
- fix for new system nss (#1414982, mozbz#1290037)
- fix build with system icu (mozbz#1329272)

* Fri Dec 23 2016 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-1
- update to 2.46
- apply some patches from firefox-49 package
- avoid runtime linking with too old ffmpeg libraries (#1330898)
- still enable XRender extension by default

