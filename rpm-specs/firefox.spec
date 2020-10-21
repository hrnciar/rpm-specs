# Set to true if it's going to be submitted as update.
%global release_build     1
%global debug_build       0
%global build_with_clang  0
%global build_with_asan   0

# Disabled due to https://bugzilla.redhat.com/show_bug.cgi?id=1886672
ExcludeArch: s390x

%global enable_mozilla_crashreporter 0
%ifarch x86_64 %{ix86}
%global enable_mozilla_crashreporter 1
%endif
%if %{build_with_asan}
%global enable_mozilla_crashreporter 0
%endif
%if 0%{?flatpak}
%global enable_mozilla_crashreporter 0
%endif

%global system_nss        1
%global system_ffi        1
%ifarch armv7hl
%global system_libvpx     1
%else
%global system_libvpx     0
%endif
%global hardened_build    1
%global system_jpeg       1
%global run_tests         0
%global disable_elfhack   1
%global use_bundled_cbindgen  1
# Build PGO+LTO on x86_64 and aarch64 only due to build issues
# on other arches.
%global build_with_pgo    0
%ifarch x86_64
%if %{release_build}
%global build_with_pgo    1
%endif
# Build PGO builds on Wayland backend
%global pgo_wayland       0
%endif
%global wayland_backend_default 1
%if 0%{?flatpak}
%global build_with_pgo    0
%endif
# Big endian platforms
%ifarch ppc64 s390x
%global big_endian        1
%endif

%ifarch armv7hl
%define _unpackaged_files_terminate_build 0
%global debug_package %{nil}
%endif

%if 0%{?build_with_pgo}
%global use_xvfb          1
%global build_tests       1
%endif

%if 0%{?run_tests}
%global use_xvfb          1
%global build_tests       1
%endif

%global default_bookmarks_file  %{_datadir}/bookmarks/default-bookmarks.html
%global firefox_app_id  \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
# Minimal required versions
%global cairo_version 1.13.1
%global freetype_version 2.1.9
%global libnotify_version 0.7.0
%if %{?system_libvpx}
%global libvpx_version 1.8.2
%endif

%if %{?system_nss}
%global nspr_version 4.21
%global nspr_build_version %{nspr_version}
%global nss_version 3.56
%global nss_build_version %{nss_version}
%endif

%global mozappdir     %{_libdir}/%{name}
%global mozappdirdev  %{_libdir}/%{name}-devel-%{version}
%global langpackdir   %{mozappdir}/langpacks
%global tarballdir    firefox-%{version}

%global official_branding       1

%bcond_without langpacks

%if !%{release_build}
%global pre_tag .npgo
%endif
%if %{build_with_clang}
%global pre_tag .clang
%endif
%if %{build_with_asan}
%global pre_tag .asan
%global build_with_pgo    0
%endif
%if !%{system_nss}
%global nss_tag .nss
%endif

Summary:        Mozilla Firefox Web browser
Name:           firefox
Version:        82.0
Release:        5%{?dist}
URL:            https://www.mozilla.org/firefox/
License:        MPLv1.1 or GPLv2+ or LGPLv2+
Source0:        https://archive.mozilla.org/pub/firefox/releases/%{version}%{?pre_version}/source/firefox-%{version}%{?pre_version}.source.tar.xz
%if %{with langpacks}
Source1:        firefox-langpacks-%{version}%{?pre_version}-20201015.tar.xz
%endif
Source2:        cbindgen-vendor.tar.xz
Source10:       firefox-mozconfig
Source12:       firefox-redhat-default-prefs.js
Source20:       firefox.desktop
Source21:       firefox.sh.in
Source23:       firefox.1
Source24:       mozilla-api-key
Source25:       firefox-symbolic.svg
Source26:       distribution.ini
Source27:       google-api-key
Source28:       firefox-wayland.sh.in
Source29:       firefox-wayland.desktop
Source30:       firefox-x11.sh.in
Source31:       firefox-x11.desktop
Source32:       node-stdout-nonblocking-wrapper
Source33:       firefox.appdata.xml.in
Source34:       firefox-search-provider.ini
Source35:       google-loc-api-key

# Build patches
Patch3:         mozilla-build-arm.patch
Patch25:        rhbz-1219542-s390-build.patch
Patch32:        build-rust-ppc64le.patch
Patch35:        build-ppc-jit.patch
# Fixing missing cacheFlush when JS_CODEGEN_NONE is used (s390x)
Patch38:        build-cacheFlush-missing.patch
Patch40:        build-aarch64-skia.patch
Patch41:        build-disable-elfhack.patch
Patch44:        build-arm-libopus.patch
Patch46:        firefox-nss-version.patch
Patch47:        fedora-shebang-build.patch
Patch48:        build-arm-wasm.patch
Patch49:        build-arm-libaom.patch
Patch53:        firefox-gcc-build.patch
# This should be fixed in Firefox 83
Patch54:        mozilla-1669639.patch
Patch55:        mozilla-1669442.patch

# Fedora specific patches
Patch215:        firefox-enable-addons.patch
Patch219:        rhbz-1173156.patch
Patch221:        firefox-fedora-ua.patch
Patch224:        mozilla-1170092.patch
#ARM run-time patch
Patch226:        rhbz-1354671.patch
Patch227:        firefox-locale-debug.patch
Patch228:        disable-openh264-download.patch

# Upstream patches
Patch402:        mozilla-1196777.patch
Patch406:        mozilla-1665329.patch
Patch407:        mozilla-1667096.patch
Patch408:        mozilla-1663844.patch
Patch409:        mozilla-1640567.patch
Patch410:        mozilla-1661192.patch
Patch411:        mozilla-1668771.patch
Patch412:        mozilla-1634404.patch
Patch413:        mozilla-1669495.patch
Patch414:        mozilla-1656727.patch
Patch415:        mozilla-1670333.patch

# Wayland specific upstream patches
Patch574:        firefox-pipewire-0-2.patch
Patch575:        firefox-pipewire-0-3.patch

#VA-API patches
Patch584:        firefox-disable-ffvpx-with-vapi.patch
Patch585:        firefox-vaapi-extra-frames.patch

# PGO/LTO patches
Patch600:        pgo.patch
Patch602:        mozilla-1516803.patch

%if %{?system_nss}
BuildRequires:  pkgconfig(nspr) >= %{nspr_version}
BuildRequires:  pkgconfig(nss) >= %{nss_version}
BuildRequires:  nss-static >= %{nss_version}
%endif
BuildRequires:  pkgconfig(libpng)
%if %{?system_jpeg}
BuildRequires:  libjpeg-devel
%endif
BuildRequires:  zip
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(freetype2) >= %{freetype_version}
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libnotify) >= %{libnotify_version}
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  dbus-glib-devel
%if %{?system_libvpx}
BuildRequires:  libvpx-devel >= %{libvpx_version}
%endif
BuildRequires:  autoconf213
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  yasm
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  clang
BuildRequires:  clang-libs
%if %{build_with_clang}
BuildRequires:  lld
%endif

BuildRequires:  pipewire-devel

%if !0%{?use_bundled_cbindgen}
BuildRequires:  cbindgen
%endif
BuildRequires:  nodejs
BuildRequires:  nasm >= 1.13
BuildRequires:  libappstream-glib

%if 0%{?big_endian}
BuildRequires:  icu
%endif

Requires:       mozilla-filesystem
Requires:       p11-kit-trust
%if %{?system_nss}
Requires:       nspr >= %{nspr_build_version}
Requires:       nss >= %{nss_build_version}
%endif
BuildRequires:  python3-devel
%if !0%{?flatpak}
Requires:       u2f-hidraw-policy
%endif
BuildRequires:  nss-devel >= 3.29.1-2.1
Requires:       nss >= 3.48.0

BuildRequires:  desktop-file-utils
%if !0%{?flatpak}
BuildRequires:  system-bookmarks
%endif
%if %{?system_ffi}
BuildRequires:  pkgconfig(libffi)
%endif

%if 0%{?use_xvfb}
BuildRequires:  xorg-x11-server-Xvfb
%endif
%if 0%{?pgo_wayland}
BuildRequires:  mutter
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gnome-settings-daemon
BuildRequires:  mesa-dri-drivers
%endif
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  clang-devel
%if %{build_with_asan}
BuildRequires:  libasan
BuildRequires:  libasan-static
%endif
BuildRequires:  perl-interpreter
BuildRequires:  fdk-aac-free-devel

Obsoletes:      mozilla <= 37:1.7.13
Provides:       webclient

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%if %{enable_mozilla_crashreporter}
%global moz_debug_prefix %{_prefix}/lib/debug
%global moz_debug_dir %{moz_debug_prefix}%{mozappdir}
%global uname_m %(uname -m)
%global symbols_file_name %{name}-%{version}.en-US.%{_os}-%{uname_m}.crashreporter-symbols.zip
%global symbols_file_path %{moz_debug_dir}/%{symbols_file_name}
%global _find_debuginfo_opts -p %{symbols_file_path} -o debugcrashreporter.list
%global crashreporter_pkg_name mozilla-crashreporter-%{name}-debuginfo
%package -n %{crashreporter_pkg_name}
Summary: Debugging symbols used by Mozilla's crash reporter servers
%description -n %{crashreporter_pkg_name}
This package provides debug information for Firefox, for use by
Mozilla's crash reporter servers.  If you are trying to locally
debug %{name}, you want to install %{name}-debuginfo instead.
%files -n %{crashreporter_pkg_name} -f debugcrashreporter.list
%endif

%if 0%{?wayland_backend_default}
%package x11
Summary: Firefox X11 launcher.
Requires: %{name}
%description x11
The firefox-x11 package contains launcher and desktop file
to run Firefox explicitly on X11.
%files x11
%{_bindir}/firefox-x11
%{_datadir}/applications/firefox-x11.desktop
%endif

%package wayland
Summary: Firefox Wayland launcher.
Requires: %{name}
%description wayland
The firefox-wayland package contains launcher and desktop file
to run Firefox explicitly on Wayland.
%files wayland
%{_bindir}/firefox-wayland
%{_datadir}/applications/firefox-wayland.desktop

%if %{run_tests}
%global testsuite_pkg_name mozilla-%{name}-testresults
%package -n %{testsuite_pkg_name}
Summary: Results of testsuite
%description -n %{testsuite_pkg_name}
This package contains results of tests executed during build.
%files -n %{testsuite_pkg_name}
/test_results
%endif

#---------------------------------------------------------------------

%prep
%setup -q -n %{tarballdir}

# Build patches, can't change backup suffix from default because during build
# there is a compare of config and js/config directories and .orig suffix is
# ignored during this compare.

%ifarch s390
%patch25 -p1 -b .rhbz-1219542-s390
%endif
%patch40 -p1 -b .aarch64-skia
%if 0%{?disable_elfhack}
%patch41 -p1 -b .disable-elfhack
%endif
%patch3  -p1 -b .arm
%patch44 -p1 -b .build-arm-libopus
#%patch46 -p1 -b .nss-version
%patch47 -p1 -b .fedora-shebang
%patch48 -p1 -b .build-arm-wasm
%patch49 -p1 -b .build-arm-libaom
%patch53 -p1 -b .firefox-gcc-build
%patch54 -p1 -b .1669639
%patch55 -p1 -b .1669442

# Fedora patches
%patch215 -p1 -b .addons
%patch219 -p1 -b .rhbz-1173156
%patch221 -p1 -b .fedora-ua
%patch224 -p1 -b .1170092
#ARM run-time patch
%ifarch aarch64
%patch226 -p1 -b .1354671
%endif
%patch227 -p1 -b .locale-debug
%patch228 -p1 -b .disable-openh264-download

%patch402 -p1 -b .1196777
%patch406 -p1 -b .1665329
%patch407 -p1 -b .1667096
%patch408 -p1 -b .1663844
%patch409 -p1 -b .1640567
%patch410 -p1 -b .1661192
%patch411 -p1 -b .1668771
%patch412 -p1 -b .1634404
%patch413 -p1 -b .1669495
%patch414 -p1 -b .1656727
%patch415 -p1 -b .1670333

# Wayland specific upstream patches
%if 0%{?fedora} > 31 || 0%{?eln}
%patch575 -p1 -b .firefox-pipewire-0-3
%else
%patch574 -p1 -b .firefox-pipewire-0-2
%endif

# VA-API fixes
%patch584 -p1 -b .firefox-disable-ffvpx-with-vapi
%patch585 -p1 -b .firefox-vaapi-extra-frames

# PGO patches
%if %{build_with_pgo}
%if !%{build_with_clang}
%patch600 -p1 -b .pgo
%patch602 -p1 -b .1516803
%endif
%endif

%{__rm} -f .mozconfig
%{__cp} %{SOURCE10} .mozconfig
echo "ac_add_options --enable-default-toolkit=cairo-gtk3-wayland" >> .mozconfig
%if %{official_branding}
echo "ac_add_options --enable-official-branding" >> .mozconfig
%endif
%{__cp} %{SOURCE24} mozilla-api-key
%{__cp} %{SOURCE27} google-api-key
%{__cp} %{SOURCE35} google-loc-api-key

echo "ac_add_options --prefix=\"%{_prefix}\"" >> .mozconfig
echo "ac_add_options --libdir=\"%{_libdir}\"" >> .mozconfig

%if %{?system_nss}
echo "ac_add_options --with-system-nspr" >> .mozconfig
echo "ac_add_options --with-system-nss" >> .mozconfig
%else
echo "ac_add_options --without-system-nspr" >> .mozconfig
echo "ac_add_options --without-system-nss" >> .mozconfig
%endif

%if %{?system_ffi}
echo "ac_add_options --enable-system-ffi" >> .mozconfig
%endif

%ifarch %{arm}
echo "ac_add_options --disable-elf-hack" >> .mozconfig
%endif

%if %{?debug_build}
echo "ac_add_options --enable-debug" >> .mozconfig
echo "ac_add_options --disable-optimize" >> .mozconfig
%else
%global optimize_flags "none"
%ifarch ppc64le aarch64
%global optimize_flags "-g -O2"
%endif
%if %{optimize_flags} != "none"
echo 'ac_add_options --enable-optimize=%{?optimize_flags}' >> .mozconfig
%else
echo 'ac_add_options --enable-optimize' >> .mozconfig
%endif
echo "ac_add_options --disable-debug" >> .mozconfig
%endif

# Second arches fail to start with jemalloc enabled
%ifnarch %{ix86} x86_64
echo "ac_add_options --disable-jemalloc" >> .mozconfig
%endif

%if !%{enable_mozilla_crashreporter}
echo "ac_add_options --disable-crashreporter" >> .mozconfig
%endif

%if 0%{?build_tests}
echo "ac_add_options --enable-tests" >> .mozconfig
%else
echo "ac_add_options --disable-tests" >> .mozconfig
%endif

%if !%{?system_jpeg}
echo "ac_add_options --without-system-jpeg" >> .mozconfig
%else
echo "ac_add_options --with-system-jpeg" >> .mozconfig
%endif

%if %{?system_libvpx}
echo "ac_add_options --with-system-libvpx" >> .mozconfig
%else
echo "ac_add_options --without-system-libvpx" >> .mozconfig
%endif

%ifarch s390 s390x
echo "ac_add_options --disable-jit" >> .mozconfig
%endif

%if %{build_with_asan}
echo "ac_add_options --enable-address-sanitizer" >> .mozconfig
echo "ac_add_options --disable-jemalloc" >> .mozconfig
%endif

# api keys full path
echo "ac_add_options --with-mozilla-api-keyfile=`pwd`/mozilla-api-key" >> .mozconfig
# It seems that the api key we have is for the safe browsing only
echo "ac_add_options --with-google-location-service-api-keyfile=`pwd`/google-loc-api-key" >> .mozconfig
echo "ac_add_options --with-google-safebrowsing-api-keyfile=`pwd`/google-api-key" >> .mozconfig

echo 'export NODEJS="%{_buildrootdir}/bin/node-stdout-nonblocking-wrapper"' >> .mozconfig

# Remove executable bit to make brp-mangle-shebangs happy.
chmod -x third_party/rust/itertools/src/lib.rs
chmod a-x third_party/rust/gfx-backend-vulkan/src/*.rs
chmod a-x third_party/rust/gfx-hal/src/*.rs
chmod a-x third_party/rust/ash/src/extensions/ext/*.rs
chmod a-x third_party/rust/ash/src/extensions/khr/*.rs

#---------------------------------------------------------------------

%build
# Disable LTO to work around rhbz#1883904
%define _lto_cflags %{nil}

%if 0%{?use_bundled_cbindgen}

mkdir -p my_rust_vendor
cd my_rust_vendor
%{__tar} xf %{SOURCE2}
mkdir -p .cargo
cat > .cargo/config <<EOL
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "`pwd`"
EOL

env CARGO_HOME=.cargo cargo install cbindgen
export PATH=`pwd`/.cargo/bin:$PATH
%endif
cd -

#echo "Generate big endian version of config/external/icu/data/icudt67l.dat"
#%if 0%{?big_endian}
#  icupkg -tb config/external/icu/data/icudt67l.dat config/external/icu/data/icudt67b.dat
#  ls -l config/external/icu/data
#  rm -f config/external/icu/data/icudt*l.dat
#%endif

mkdir %{_buildrootdir}/bin || :
cp %{SOURCE32} %{_buildrootdir}/bin || :

# Update the various config.guess to upstream release for aarch64 support
# Do not update config.guess in the ./third_party/rust because that would break checksums
find ./ -path ./third_party/rust -prune -o -name config.guess -exec cp /usr/lib/rpm/config.guess {} ';'

MOZ_OPT_FLAGS=$(echo "%{optflags}" | %{__sed} -e 's/-Wall//')
#rhbz#1037063
# -Werror=format-security causes build failures when -Wno-format is explicitly given
# for some sources
# Explicitly force the hardening flags for Firefox so it passes the checksec test;
# See also https://fedoraproject.org/wiki/Changes/Harden_All_Packages
%if 0%{?fedora} < 30
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wformat-security -Wformat -Werror=format-security"
%else
# Workaround for mozbz#1531309
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-Werror=format-security//')
%endif
%if 0%{?fedora} > 30
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fpermissive"
%endif
%if %{?hardened_build}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fPIC -Wl,-z,relro -Wl,-z,now"
%endif
%if %{?debug_build}
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-O2//')
%endif
%ifarch s390
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-g/-g1/')
# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g1 from line above and breaks building on s390/arm
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "
%endif
%ifarch %{arm} %{ix86}
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-g/-g0/')
export MOZ_DEBUG_FLAGS=" "
%endif
%if !%{build_with_clang}
%ifarch s390 ppc aarch64 %{ix86}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%ifarch %{arm}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--strip-debug"
echo "ac_add_options --enable-linker=gold" >> .mozconfig
%endif
%endif
%if 0%{?flatpak}
# Make sure the linker can find libraries in /app/lib64 as we don't use
# __global_ldflags that normally sets this.
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -L%{_libdir}"
%endif
%ifarch %{arm} %{ix86}
export RUSTFLAGS="-Cdebuginfo=0"
%endif
%if %{build_with_asan}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fsanitize=address -Dxmalloc=myxmalloc"
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -fsanitize=address -ldl"
%endif

# We don't wantfirefox to use CK_GCM_PARAMS_V3 in nss
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DNSS_PKCS11_3_0_STRICT"

echo "export CFLAGS=\"$MOZ_OPT_FLAGS\"" >> .mozconfig
echo "export CXXFLAGS=\"$MOZ_OPT_FLAGS\"" >> .mozconfig
echo "export LDFLAGS=\"$MOZ_LINK_FLAGS\"" >> .mozconfig

%if %{build_with_clang}
echo "export LLVM_PROFDATA=\"llvm-profdata\"" >> .mozconfig
echo "export AR=\"llvm-ar\"" >> .mozconfig
echo "export NM=\"llvm-nm\"" >> .mozconfig
echo "export RANLIB=\"llvm-ranlib\"" >> .mozconfig
echo "ac_add_options --enable-linker=lld" >> .mozconfig
%else
echo "export CC=gcc" >> .mozconfig
echo "export CXX=g++" >> .mozconfig
echo "export AR=\"gcc-ar\"" >> .mozconfig
echo "export NM=\"gcc-nm\"" >> .mozconfig
echo "export RANLIB=\"gcc-ranlib\"" >> .mozconfig
%endif
%if 0%{?build_with_pgo}
echo "ac_add_options MOZ_PGO=1" >> .mozconfig

# Temporary disabled due to GCC bug
# Fixed by https://bugzilla.mozilla.org/show_bug.cgi?id=1671345
# Should be in Firefox 83
%if 0%{?fedora} > 33
echo "ac_add_options --enable-lto" >> .mozconfig
%endif

# PGO build doesn't work with ccache
export CCACHE_DISABLE=1
%endif

MOZ_SMP_FLAGS=-j1
# On x86_64 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %{ix86}
[ -z "$RPM_BUILD_NCPUS" ] && \
     RPM_BUILD_NCPUS="`/usr/bin/getconf _NPROCESSORS_ONLN`"
[ "$RPM_BUILD_NCPUS" -ge 2 ] && MOZ_SMP_FLAGS=-j2
%endif
%ifarch x86_64 ppc ppc64 ppc64le %{arm} aarch64
[ -z "$RPM_BUILD_NCPUS" ] && \
     RPM_BUILD_NCPUS="`/usr/bin/getconf _NPROCESSORS_ONLN`"
[ "$RPM_BUILD_NCPUS" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "$RPM_BUILD_NCPUS" -ge 4 ] && MOZ_SMP_FLAGS=-j4
[ "$RPM_BUILD_NCPUS" -ge 8 ] && MOZ_SMP_FLAGS=-j8
[ "$RPM_BUILD_NCPUS" -ge 16 ] && MOZ_SMP_FLAGS=-j16
[ "$RPM_BUILD_NCPUS" -ge 24 ] && MOZ_SMP_FLAGS=-j24
%endif

echo "mk_add_options MOZ_MAKE_FLAGS=\"$MOZ_SMP_FLAGS\"" >> .mozconfig
echo "mk_add_options MOZ_SERVICES_SYNC=1" >> .mozconfig
echo "export STRIP=/bin/true" >> .mozconfig
export MACH_USE_SYSTEM_PYTHON=1
%if %{build_with_pgo}
%if %{pgo_wayland}
if [ -z "$XDG_RUNTIME_DIR" ]; then
  export XDG_RUNTIME_DIR=$HOME
fi
xvfb-run mutter --wayland --nested &
if [ -z "$WAYLAND_DISPLAY" ]; then
  export WAYLAND_DISPLAY=wayland-0
else
  export WAYLAND_DISPLAY=wayland-1
fi
MOZ_ENABLE_WAYLAND=1 ./mach build  2>&1 | cat -
%else
GDK_BACKEND=x11 xvfb-run ./mach build  2>&1 | cat -
%endif
%else
./mach build -v 2>&1 | cat -
%endif

# create debuginfo for crash-stats.mozilla.com
%if %{enable_mozilla_crashreporter}
make -C objdir buildsymbols
%endif

%if %{?run_tests}
%if %{?system_nss}
ln -s %{_prefix}/bin/certutil objdir/dist/bin/certutil
ln -s %{_prefix}/bin/pk12util objdir/dist/bin/pk12util

%endif
mkdir test_results
./mach --log-no-times check-spidermonkey &> test_results/check-spidermonkey || true
./mach --log-no-times check-spidermonkey &> test_results/check-spidermonkey-2nd-run || true
./mach --log-no-times cppunittest &> test_results/cppunittest || true
xvfb-run ./mach --log-no-times crashtest &> test_results/crashtest || true
./mach --log-no-times gtest &> test_results/gtest || true
xvfb-run ./mach --log-no-times jetpack-test &> test_results/jetpack-test || true
# not working right now ./mach marionette-test &> test_results/marionette-test || true
xvfb-run ./mach --log-no-times mochitest-a11y &> test_results/mochitest-a11y || true
xvfb-run ./mach --log-no-times mochitest-browser &> test_results/mochitest-browser || true
xvfb-run ./mach --log-no-times mochitest-chrome &> test_results/mochitest-chrome || true
xvfb-run ./mach --log-no-times mochitest-devtools &> test_results/mochitest-devtools || true
xvfb-run ./mach --log-no-times mochitest-plain &> test_results/mochitest-plain || true
xvfb-run ./mach --log-no-times reftest &> test_results/reftest || true
xvfb-run ./mach --log-no-times webapprt-test-chrome &> test_results/webapprt-test-chrome || true
xvfb-run ./mach --log-no-times webapprt-test-content &> test_results/webapprt-test-content || true
./mach --log-no-times webidl-parser-test &> test_results/webidl-parser-test || true
xvfb-run ./mach --log-no-times xpcshell-test &> test_results/xpcshell-test || true
%if %{?system_nss}
rm -f  objdir/dist/bin/certutil
rm -f  objdir/dist/bin/pk12util
%endif

%endif
#---------------------------------------------------------------------

%install

# set up our default bookmarks
%if !0%{?flatpak}
%{__cp} -p %{default_bookmarks_file} objdir/dist/bin/browser/chrome/en-US/locale/browser/bookmarks.html
%endif

# Make sure locale works for langpacks
%{__cat} > objdir/dist/bin/browser/defaults/preferences/firefox-l10n.js << EOF
pref("general.useragent.locale", "chrome://global/locale/intl.properties");
EOF

DESTDIR=%{buildroot} make -C objdir install

%{__mkdir_p} %{buildroot}{%{_libdir},%{_bindir},%{_datadir}/applications}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE20}
%if 0%{?wayland_backend_default}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE31}
%endif
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE29}

# set up the firefox start script
%if 0%{?wayland_backend_default}
%global wayland_default true
%else
%global wayland_default false
%endif
%{__rm} -rf %{buildroot}%{_bindir}/firefox
%{__sed} -e 's/__DEFAULT_WAYLAND__/%{wayland_default}/' \
         -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE21} > %{buildroot}%{_bindir}/firefox
%{__chmod} 755 %{buildroot}%{_bindir}/firefox


%if 0%{?flatpak}
sed -i -e 's|%FLATPAK_ENV_VARS%|export TMPDIR="$XDG_CACHE_HOME/tmp"|' %{buildroot}%{_bindir}/firefox
%else
sed -i -e 's|%FLATPAK_ENV_VARS%||' %{buildroot}%{_bindir}/firefox
%endif

%if 0%{?wayland_backend_default}
%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE30} > %{buildroot}%{_bindir}/firefox-x11
%{__chmod} 755 %{buildroot}%{_bindir}/firefox-x11
%endif
%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE28} > %{buildroot}%{_bindir}/firefox-wayland
%{__chmod} 755 %{buildroot}%{_bindir}/firefox-wayland

%{__install} -p -D -m 644 %{SOURCE23} %{buildroot}%{_mandir}/man1/firefox.1

%{__rm} -f %{buildroot}/%{mozappdir}/firefox-config
%{__rm} -f %{buildroot}/%{mozappdir}/update-settings.ini

for s in 16 22 24 32 48 256; do
    %{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    %{__cp} -p browser/branding/official/default${s}.png \
               %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done

# Install hight contrast icon
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
%{__cp} -p %{SOURCE25} \
           %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps

echo > %{name}.lang
%if %{with langpacks}
# Extract langpacks, make any mods needed, repack the langpack, and install it.
%{__mkdir_p} %{buildroot}%{langpackdir}
%{__tar} xf %{SOURCE1}
for langpack in `ls firefox-langpacks/*.xpi`; do
  language=`basename $langpack .xpi`
  extensionID=langpack-$language@firefox.mozilla.org
  %{__mkdir_p} $extensionID
  unzip -qq $langpack -d $extensionID
  find $extensionID -type f | xargs chmod 644

  cd $extensionID
  zip -qq -r9mX ../${extensionID}.xpi *
  cd -

  %{__install} -m 644 ${extensionID}.xpi %{buildroot}%{langpackdir}
  language=`echo $language | sed -e 's/-/_/g'`
%if 0%{?flatpak}
  echo "%{langpackdir}/${extensionID}.xpi" >> %{name}.lang
%else
  echo "%%lang($language) %{langpackdir}/${extensionID}.xpi" >> %{name}.lang
%endif
done
%{__rm} -rf firefox-langpacks

# Install langpack workaround (see #707100, #821169)
function create_default_langpack() {
language_long=$1
language_short=$2
cd %{buildroot}%{langpackdir}
ln -s langpack-$language_long@firefox.mozilla.org.xpi langpack-$language_short@firefox.mozilla.org.xpi
cd -
echo "%%lang($language_short) %{langpackdir}/langpack-$language_short@firefox.mozilla.org.xpi" >> %{name}.lang
}

# Table of fallbacks for each language
# please file a bug at bugzilla.redhat.com if the assignment is incorrect
#create_default_langpack "bn-IN" "bn"
create_default_langpack "es-AR" "es"
create_default_langpack "fy-NL" "fy"
create_default_langpack "ga-IE" "ga"
create_default_langpack "gu-IN" "gu"
create_default_langpack "hi-IN" "hi"
create_default_langpack "hy-AM" "hy"
create_default_langpack "nb-NO" "nb"
create_default_langpack "nn-NO" "nn"
create_default_langpack "pa-IN" "pa"
create_default_langpack "pt-PT" "pt"
create_default_langpack "sv-SE" "sv"
create_default_langpack "zh-TW" "zh"
%endif

%{__mkdir_p} %{buildroot}/%{mozappdir}/browser/defaults/preferences

# System config dir
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/%{name}/pref

# System extensions
%{__mkdir_p} %{buildroot}%{_datadir}/mozilla/extensions/%{firefox_app_id}
%{__mkdir_p} %{buildroot}%{_libdir}/mozilla/extensions/%{firefox_app_id}

# Copy over the LICENSE
%{__install} -p -c -m 644 LICENSE %{buildroot}/%{mozappdir}

# Use the system hunspell dictionaries
%{__rm} -rf %{buildroot}%{mozappdir}/dictionaries
ln -s %{_datadir}/myspell %{buildroot}%{mozappdir}/dictionaries

# Enable crash reporter for Firefox application
%if %{enable_mozilla_crashreporter}
sed -i -e "s/\[Crash Reporter\]/[Crash Reporter]\nEnabled=1/" %{buildroot}/%{mozappdir}/application.ini
# Add debuginfo for crash-stats.mozilla.com
%{__mkdir_p} %{buildroot}/%{moz_debug_dir}
%{__cp} objdir/dist/%{symbols_file_name} %{buildroot}/%{moz_debug_dir}
%endif

%if %{run_tests}
# Add debuginfo for crash-stats.mozilla.com
%{__mkdir_p} %{buildroot}/test_results
%{__cp} test_results/* %{buildroot}/test_results
%endif

# Default
%{__cp} %{SOURCE12} %{buildroot}%{mozappdir}/browser/defaults/preferences

# Copy over run-mozilla.sh
%{__cp} build/unix/run-mozilla.sh %{buildroot}%{mozappdir}

# Add distribution.ini
%{__mkdir_p} %{buildroot}%{mozappdir}/distribution
%{__cp} %{SOURCE26} %{buildroot}%{mozappdir}/distribution

# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
%{__sed} -e 's/__VERSION__/%{version}/' %{SOURCE33} > %{buildroot}%{_datadir}/metainfo/firefox.appdata.xml

# Install Gnome search provider files
mkdir -p %{buildroot}%{_datadir}/gnome-shell/search-providers
%{__cp} %{SOURCE34} %{buildroot}%{_datadir}/gnome-shell/search-providers

# Remove copied libraries to speed up build
rm -f %{buildroot}%{mozappdirdev}/sdk/lib/libmozjs.so
rm -f %{buildroot}%{mozappdirdev}/sdk/lib/libmozalloc.so
rm -f %{buildroot}%{mozappdirdev}/sdk/lib/libxul.so
#---------------------------------------------------------------------

# Moves defaults/preferences to browser/defaults/preferences
%pretrans -p <lua>
require 'posix'
require 'os'
if (posix.stat("%{mozappdir}/browser/defaults/preferences", "type") == "link") then
  posix.unlink("%{mozappdir}/browser/defaults/preferences")
  posix.mkdir("%{mozappdir}/browser/defaults/preferences")
  if (posix.stat("%{mozappdir}/defaults/preferences", "type") == "directory") then
    for i,filename in pairs(posix.dir("%{mozappdir}/defaults/preferences")) do
      os.rename("%{mozappdir}/defaults/preferences/"..filename, "%{mozappdir}/browser/defaults/preferences/"..filename)
    end
    f = io.open("%{mozappdir}/defaults/preferences/README","w")
    if f then
      f:write("Content of this directory has been moved to %{mozappdir}/browser/defaults/preferences.")
      f:close()
    end
  end
end

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%preun
# is it a final removal?
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{mozappdir}/components
  %{__rm} -rf %{mozappdir}/extensions
  %{__rm} -rf %{mozappdir}/plugins
  %{__rm} -rf %{langpackdir}
fi

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%{_bindir}/firefox
%{mozappdir}/firefox
%{mozappdir}/firefox-bin
%doc %{_mandir}/man1/*
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/*
%dir %{_datadir}/mozilla/extensions/*
%dir %{_libdir}/mozilla/extensions/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/gnome-shell/search-providers/*.ini
%dir %{mozappdir}
%license %{mozappdir}/LICENSE
%{mozappdir}/browser/chrome
%{mozappdir}/browser/defaults/preferences/firefox-redhat-default-prefs.js
%{mozappdir}/browser/features/*.xpi
%{mozappdir}/distribution/distribution.ini
# That's Windows only
%ghost %{mozappdir}/browser/features/aushelper@mozilla.org.xpi
%if %{with langpacks}
%dir %{langpackdir}
%endif
%{mozappdir}/browser/omni.ja
%{mozappdir}/run-mozilla.sh
%{mozappdir}/application.ini
%{mozappdir}/pingsender
%exclude %{mozappdir}/removed-files
%{_datadir}/icons/hicolor/16x16/apps/firefox.png
%{_datadir}/icons/hicolor/22x22/apps/firefox.png
%{_datadir}/icons/hicolor/24x24/apps/firefox.png
%{_datadir}/icons/hicolor/256x256/apps/firefox.png
%{_datadir}/icons/hicolor/32x32/apps/firefox.png
%{_datadir}/icons/hicolor/48x48/apps/firefox.png
%{_datadir}/icons/hicolor/symbolic/apps/firefox-symbolic.svg
%if %{enable_mozilla_crashreporter}
%{mozappdir}/crashreporter
%{mozappdir}/crashreporter.ini
%{mozappdir}/minidump-analyzer
%{mozappdir}/Throbber-small.gif
%{mozappdir}/browser/crashreporter-override.ini
%endif
%{mozappdir}/*.so
%{mozappdir}/gtk2/*.so
%{mozappdir}/defaults/pref/channel-prefs.js
%{mozappdir}/dependentlibs.list
%{mozappdir}/dictionaries
%{mozappdir}/omni.ja
%{mozappdir}/platform.ini
%{mozappdir}/plugin-container
%{mozappdir}/gmp-clearkey
%{mozappdir}/fonts/TwemojiMozilla.ttf
%if !%{?system_nss}
%exclude %{mozappdir}/libnssckbi.so
%endif
%if %{build_with_asan}
%{mozappdir}/llvm-symbolizer
%endif

#---------------------------------------------------------------------

%changelog
* Tue Oct 20 2020 Martin Stransky <stransky@redhat.com> - 82.0-5
- Added fix for rhbz#1889742 - Typo in /usr/bin/firefox

* Mon Oct 19 2020 Martin Stransky <stransky@redhat.com> - 82.0-4
- Updated openh264 patch to use keyframes from contained
  for openh264 only.

* Mon Oct 19 2020 Martin Stransky <stransky@redhat.com> - 82.0-3
- Added ELN build fixes

* Thu Oct 15 2020 Martin Stransky <stransky@redhat.com> - 82.0-2
- Updated SELinux relabel setup (rhbz#1731371)

* Thu Oct 15 2020 Martin Stransky <stransky@redhat.com> - 82.0-1
- Updated to 82.0 Build 2

* Thu Oct 15 2020 Martin Stransky <stransky@redhat.com> - 81.0.2-3
- Added experimental openh264 seek patch (mzbz#1670333)

* Mon Oct 12 2020 Martin Stransky <stransky@redhat.com> - 81.0.2-2
- Added a partial fox for rhbz#1886722

* Mon Oct 12 2020 Martin Stransky <stransky@redhat.com> - 81.0.2-1
- Updated to latest upstream - 81.0.2

* Thu Oct 8 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-9
- Added an updated fix for mozbz#1656727

* Thu Oct 8 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-8
- Added fixes for mozbz#1634404, mozbz#1669495

* Thu Oct 8 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-7
- Removed mozbz#1656727 as it causes a regression rhbz#1886243

* Wed Oct 7 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-6
- PGO patch update
- Added fix for mzbz#1669442 (LTO builds)

* Mon Oct 5 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-5
- Added fix for mozbz#1656727

* Fri Oct 2 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-4
- Added fix for mozbz#1668771

* Thu Oct 1 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-3
- Added fix for mozbz#1661192

* Thu Oct 1 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-2
- Added fix for mozbz#1640567
- Enable PGO

* Wed Sep 30 2020 Martin Stransky <stransky@redhat.com> - 81.0.1-1
- Updated to 81.0.1

* Wed Sep 30 2020 Martin Stransky <stransky@redhat.com> - 81.0-9
- Disabled openh264 download
- Removed fdk-aac-free dependency (rhbz#1883672)
- Enabled LTO

* Sat Sep 26 2020 Dan Horák <dan[at]danny.cz> - 81.0-8
- Re-enable builds for ppc64le

* Fri Sep 25 2020 Martin Stransky <stransky@redhat.com> - 81.0-7
- Added openh264 fixes

* Wed Sep 23 2020 Martin Stransky <stransky@redhat.com> - 81.0-6
- Added fix for rhbz#1731371

* Tue Sep 22 2020 Kalev Lember <klember@redhat.com> - 81.0-5
- Re-enable builds for armv7hl and aarch64 architectures

* Tue Sep 22 2020 Kalev Lember <klember@redhat.com> - 81.0-4
- Disable LTO to work around firefox build failing in F33+

* Mon Sep 21 2020 Martin Stransky <stransky@redhat.com> - 81.0-3
- Updated to 81.0 Build 2
- Updated firefox-disable-ffvpx-with-vapi patch
- Deleted old changelog entries

* Thu Sep 17 2020 Martin Stransky <stransky@redhat.com> - 81.0-2
- Added upstream patches mzbz#1665324 mozbz#1665329
- Updated requested nss version to 3.56

* Tue Sep 15 2020 Martin Stransky <stransky@redhat.com> - 81.0-1
- Updated to 81.0

* Thu Sep 10 2020 Martin Stransky <stransky@redhat.com> - 80.0.1-3
- Test build for all arches.

* Fri Sep 4 2020 Martin Stransky <stransky@redhat.com> - 80.0.1-2
- Added patch for mozbz#1875469

* Tue Sep 1 2020 Martin Stransky <stransky@redhat.com> - 80.0.1-1
- Updated to 80.0.1

* Tue Aug 18 2020 Martin Stransky <stransky@redhat.com> - 80.0-1
- Updated to 80.0 Build 2
- Go back to gcc
- Disabled WebGL dmabuf backend due to reported errors
  (mzbz#1655323, mozbz#1656505).

* Tue Aug 18 2020 Martin Stransky <stransky@redhat.com> - 79.0-6
- Enabled pgo
- Build with clang

* Tue Aug 4 2020 Martin Stransky <stransky@redhat.com> - 79.0-5
- Added upstream fix for mozbz#1656436.

* Mon Aug 3 2020 Martin Stransky <stransky@redhat.com> - 79.0-4
- Updated fix for mozbz#1645671

* Thu Jul 30 2020 Martin Stransky <stransky@redhat.com> - 79.0-3
- Added VA-API fix for mozbz#1645671

* Wed Jul 29 2020 Martin Stransky <stransky@redhat.com> - 79.0-2
- Try to enable armv7hl again.
- Disabled ppc64le due to cargo crash (rhbz#1862012).

* Mon Jul 27 2020 Martin Stransky <stransky@redhat.com> - 79.0-1
- Update to 79.0
- Disabled PGO due to rhbz#1849165 (gcc internal error).

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 78.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.0-4
- Use python3 instead of python2 for build

* Tue Jul 21 2020 Martin Stransky <stransky@redhat.com> - 78.0-3
- Added fix for mozbz#1651701/rhbz#1855730

* Fri Jul 10 2020 Jan Horak <jhorak@redhat.com> - 78.0.2-2
- Fixing clang build - linker setup

* Thu Jul 09 2020 Jan Horak <jhorak@redhat.com> - 78.0.2-1
- Update to 78.0.2 build2

* Wed Jul 01 2020 Jan Horak <jhorak@redhat.com> - 78.0.1-1
- Update to 78.0.1 build1

* Wed Jul 1 2020 Martin Stransky <stransky@redhat.com> - 78.0-2
- Add 'Open the Profile Manager' desktop file entry

* Mon Jun 29 2020 Jan Horak <jhorak@redhat.com> - 78.0-1
- Update to 78.0 build2

* Tue Jun 23 2020 Martin Stransky <stransky@redhat.com> - 77.0.1-3
- Build with PGO/LTO again.

* Wed Jun 03 2020 Jan Horak <jhorak@redhat.com> - 77.0.1-2
- Update to 77.0.1 build1

* Wed Jun 03 2020 Jan Horak <jhorak@redhat.com> - 77.0.1-1
- Fixing pipewire patch
- New upstream version (77.0.1)

* Tue Jun 2 2020 Martin Stransky <stransky@redhat.com> - 77.0-2
- Rebuild with updated langpacks (rhbz#1843028).

* Fri May 29 2020 Martin Stransky <stransky@redhat.com> - 77.0-1
- Updated to Firefox 77.0

* Mon May 25 2020 Martin Stransky <stransky@redhat.com> - 76.0.1-7
- Added fix for mozbz#1632456

* Mon May 25 2020 Martin Stransky <stransky@redhat.com> - 76.0.1-6
- Added fix for mozbz#1634213

* Mon May 25 2020 Martin Stransky <stransky@redhat.com> - 76.0.1-5
- Added fix for mozbz#1619882 - video flickering when va-api is used.

* Thu May 21 2020 Jan Grulich <jgrulich@redhat.com> - 76.0.1-4
- Add support for PipeWire 0.3

* Wed May 20 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 76.0.1-3
- Build aarch64 again so aarch64 users get updates

* Wed May 13 2020 Martin Stransky <stransky@redhat.com> - 76.0.1-2
- Added extra va-api frames to vp8/9 decoder.

* Fri May 8 2020 Martin Stransky <stransky@redhat.com> - 76.0.1-1
- Updated to 76.0.1

* Thu May 7 2020 Martin Stransky <stransky@redhat.com> - 76.0-3
- Disable ffvpx when va-api is enabled.

* Tue May 05 2020 Jan Horak <jhorak@redhat.com> - 76.0-2
- Don't use google safe browsing api key for the geolocation

* Sun May 3 2020 Martin Stransky <stransky@redhat.com> - 76.0-1
- Updated to 76.0

* Thu Apr 23 2020 Martin Stransky <stransky@redhat.com> - 75.0-3
- Added fix for mozilla bug #1527976 (browser D&D)

* Tue Apr 14 2020 Jan Horak <jhorak@redhat.com> - 75.0-2
- Removed gconf-2.0 build requirement

* Mon Apr 06 2020 Martin Stransky <stransky@redhat.com> - 75.0-1
- Updated to 75.0

* Mon Apr 06 2020 Martin Stransky <stransky@redhat.com> - 74.0.1-3
- Added fix for mozbz#1627469

* Mon Apr 06 2020 Jan Horak <jhorak@redhat.com> - 74.0.1-2
- Fixing pipewire patch

* Sat Apr 4 2020 Martin Stransky <stransky@redhat.com> - 74.0.1-1
- Updated to latest upstream
- Added fix for mozbz#1624745

* Wed Apr 1 2020 Martin Stransky <stransky@redhat.com> - 74.0-14
- Added fixes to gnome shell search provider

* Tue Mar 31 2020 Jan Horak <jhorak@redhat.com> - 74.0-13
- Allow addons sideload to fix missing langpacks issues

* Thu Mar 19 2020 Martin Stransky <stransky@redhat.com> - 74.0-12
- Added fix for rhbz#1814850 by Daniel Rusek

* Tue Mar 17 2020 Martin Stransky <stransky@redhat.com> - 74.0-11
- Added fix for mozbz#1623106

* Tue Mar 17 2020 Martin Stransky <stransky@redhat.com> - 74.0-9
- Added fix for mozbz#1623060

* Tue Mar 17 2020 Jan Grulich <jgrulich@redhat.com> - 74-0-8
- Add support for window sharing

* Mon Mar 16 2020 Martin Stransky <stransky@redhat.com> - 74.0-7
- Use D-Bus remote exclusively for both X11 and Wayland backends
  when WAYLAND_DISPLAY is present.

* Fri Mar 13 2020 Martin Stransky <stransky@redhat.com> - 74.0-6
- Added fix for mozbz#1615098

* Thu Mar 12 2020 Martin Stransky <stransky@redhat.com> - 74.0-5
- Added fix for mozbz#1196777

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 74.0-4
- Remove unused libIDL build dep
- Disabled arm due to build failures

* Tue Mar 10 2020 Martin Stransky <stransky@redhat.com> - 74.0-3
- Update to 74.0 Build 3

* Mon Mar 09 2020 Martin Stransky <stransky@redhat.com> - 74.0-2
- Update to 74.0 Build 2

* Tue Mar 03 2020 Martin Stransky <stransky@redhat.com> - 74.0-1
- Update to 74.0 Build 1
- Added mozbz#1609538

* Mon Feb 24 2020 Martin Stransky <stransky@redhat.com> - 73.0.1-4
- Using pipewire-0.2 as buildrequire
- Added armv7hl fixes by Gabriel Hojda

* Mon Feb 24 2020 Martin Stransky <stransky@redhat.com> - 73.0.1-2
- Fixed Bug 1804787 - Some .desktop menu entries unlocalized

* Thu Feb 20 2020 Martin Stransky <stransky@redhat.com> - 73.0.1-1
- Update to 73.0.1

* Tue Feb 11 2020 Jan Horak <jhorak@redhat.com> - 73.0-1
- Update to 73.0 build3

* Tue Feb 04 2020 Kalev Lember <klember@redhat.com> - 72.0.2-3
- Fix various issues with appdata, making the validation pass again
- Validate appdata during the build
- Make sure the release tag in appdata is in sync with the package version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 72.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Jan Horak <jhorak@redhat.com> - 72.0.2-1
- Update to 72.0.2 build1

* Wed Jan 15 2020 Jan Horak <jhorak@redhat.com> - 72.0.1-2
- Added fix for wrong cursor offset of popup windows and bumped required nss
  version

* Wed Jan 08 2020 Jan Horak <jhorak@redhat.com> - 72.0.1-1
- Update to 72.0.1 build1

* Mon Jan 06 2020 Jan Horak <jhorak@redhat.com> - 72.0-2
- Update to 72.0 build4

* Fri Jan 03 2020 Jan Horak <jhorak@redhat.com> - 72.0-1
- Update to 72.0 build3

* Wed Dec 18 2019 Jan Horak <jhorak@redhat.com> - 71.0-17
- Fix for wrong intl.accept_lang when using non en-us langpack

* Mon Dec 9 2019 Martin Stransky <stransky@redhat.com> - 71.0-16
- Build with asan

* Mon Dec 9 2019 Martin Stransky <stransky@redhat.com> - 71.0-15
- Enabled Mozilla crash reporter
- Enabled PGO builds

* Mon Dec 9 2019 Martin Stransky <stransky@redhat.com> - 71.0-14
- Updated workaround for mzbz#1601707

* Sat Dec 7 2019 Martin Stransky <stransky@redhat.com> - 71.0-13
- Built with -fno-lifetime-dse

* Fri Dec 6 2019 Martin Stransky <stransky@redhat.com> - 71.0-12
- Clang test build, should fix extension breakage

* Fri Dec 6 2019 Martin Stransky <stransky@redhat.com> - 71.0-11
- Added workaround for:
  https://bugzilla.mozilla.org/show_bug.cgi?id=1601707
  http://gcc.gnu.org/PR92831

* Fri Dec 6 2019 Martin Stransky <stransky@redhat.com> - 71.0-10
- Remove appdata and ship metainfo only

* Wed Dec 4 2019 Martin Stransky <stransky@redhat.com> - 71.0-9
- Included kiosk mode workaround (mozbz#1594738)

* Tue Dec 3 2019 Martin Stransky <stransky@redhat.com> - 71.0-8
- Disabled PGO due to startup crash

* Mon Dec 2 2019 Martin Stransky <stransky@redhat.com> - 71.0-7
- Updated to 71.0 Build 5
- Updated Gnome search provider

* Wed Nov 27 2019 Martin Stransky <stransky@redhat.com> - 71.0-6
- Enable Gnome search provider

* Wed Nov 27 2019 Martin Stransky <stransky@redhat.com> - 71.0-5
- Added fix for mozbz#1593408
- Temporary disable Gnome search provider

* Tue Nov 26 2019 Martin Stransky <stransky@redhat.com> - 71.0-2
- Enable Gnome search provider

* Tue Nov 26 2019 Martin Stransky <stransky@redhat.com> - 71.0-1
- Updated to 71.0 Build 2

* Tue Nov 19 2019 Jan Horak <jhorak@redhat.com> - 70.0.1-5
- Added fixes for missing popup and overflow widget glitches

* Mon Nov 04 2019 Jan Horak <jhorak@redhat.com> - 70.0.1-4
- Added fix for non-scrollable popups

* Fri Nov 1 2019 Martin Stransky <stransky@redhat.com> - 70.0.1-1
- Updated to 70.0.1
- Built with system-nss (reverted 70.0-2 change).

* Thu Oct 31 2019 Martin Stransky <stransky@redhat.com> - 70.0-2
- Switched to in-tree nss due to rhbz#1752303

* Tue Oct 15 2019 Martin Stransky <stransky@redhat.com> - 70.0-1
- Updated to 70.0
