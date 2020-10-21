# Headless is editor binary to run without X11, e.g. for exporting games from CLI
%bcond_without  headless
# Server is template (optimized, no tools) binary to run multiplayer servers
%bcond_without  server

# Undefine for stable
#define prerel  1
%define status  stable
%define uversion %{version}-%{status}

%define rdnsname org.godotengine.Godot

Name:           godot
Version:        3.2.1
Release:        %{?prerel:0.%{status}.}1%{?dist}.1
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor
%if 0%{?mageia}
Group:          Development/Tools
%endif
# Godot itself is MIT-licensed, the rest is from vendored thirdparty libraries
License:        MIT and CC-BY and ASL 2.0 and BSD and zlib and OFL and Bitstream Vera and ISC and MPLv2.0
URL:            https://godotengine.org
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{?prerel:%{status}/}%{name}-%{uversion}.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{?prerel:%{status}/}%{name}-%{uversion}.tar.xz.sha256

# Upstream does not support those arches (for now)
ExcludeArch:    ppc64 ppc64le s390x

BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
%if ! 0%{?rhel}
BuildRequires:  miniupnpc-devel
%endif
BuildRequires:  pkgconfig(alsa)
%if 0%{?mageia}
# Fedora doesn't provide bullet 2.89
BuildRequires:  pkgconfig(bullet)
%endif
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
%if 0%{?mageia}
# Fedora doesn't provide wslay yet
BuildRequires:  pkgconfig(libwslay)
%endif
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
%if 0%{?mageia}
BuildRequires:  scons
%else
BuildRequires:  python3-scons
%endif

# For desktop and appdata files validation
BuildRequires:  desktop-file-utils
%if 0%{?mageia}
BuildRequires:  appstream-util
%else
BuildRequires:  libappstream-glib
%endif

# Ensure the hicolor icon theme dirs exist
Requires:       hicolor-icon-theme

# Bundled libraries: many of the libraries code in `thirdparty` can be
# unbundled when the libraries are provided by the system. Keep in mind
# though that the `thirdparty` folder also contains code which is typically
# not packaged in distros, and is probably best left bundled.

# Upstream commit newer than the latest upstream release needed for features
# and fixes developed for Godot 3.2.
# Upstream commit 308db73d0b3c2d1870cd3e465eaa283692a4cf23.
# Could be unbundled if a recent enough version is packaged, but care is needed
# as Godot currently used experimental features which may change upstream.
Provides:       bundled(assimp)
%if ! 0%{?mageia}
# Can be unbundled once bullet 2.89+ is packaged.
Provides:       bundled(bullet) = 2.89
%endif
# Has some modifications for IPv6 support, upstream enet is unresponsive.
# Should not be unbundled.
# Cf: https://github.com/godotengine/godot/issues/6992
Provides:       bundled(enet) = 1.3.14
# Upstream commit from 2016 (32d5ac49414a8914ec1e1f285f3f927c6e8ec29d),
# newer than 1.0.0.27 which is the last tag.
# Could be unbundled if packaged.
Provides:       bundled(libwebm)
%if ! 0%{?mageia}
# Could be unbundled if packaged.
Provides:       bundled(libwslay) = 1.1.0
%endif
%if 0%{?rhel}
# Not provided in RHEL8.
# Upstream commit 0ab1d6725b800f007f9bb9919150546476616f1b.
Provides:       bundled(miniupnpc)
%endif
# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.2.11
# Upstream commit 25241c5a8f8451d41ab1b02ab2d865b01600d949, no releases.
# Could be unbundled if packaged.
Provides:       bundled(nanosvg)
# Could be unbundled if packaged.
Provides:       bundled(squish) = 1.15
# Upstream commit 656bb611afd517394dc1a202359b9ccaa3c03a53.
# Could be unbundled if packaged.
Provides:       bundled(tinyexr)

%description
Godot is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

%files
%doc CHANGELOG.md DONORS.md README.md
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt LOGO_LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%{_datadir}/mime/application/x-%{name}-project.xml
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%if %{with headless}
%package        headless
Summary:        Godot headless editor binary for CLI usage
%if 0%{?mageia}
Group:          Development/Tools
%endif

%description    headless
This package contains the headless binary for the Godot game engine,
particularly suited for CLI usage, e.g. to export projects from a server
or build system.

To run game servers, see the godot-server package which contains an
optimized template build.

%files          headless
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-headless
%endif

#----------------------------------------------------------------------

%if %{with server}
%package        server
Summary:        Godot headless runtime binary for hosting game servers
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    server
This package contains the headless binary for the Godot game engine's
runtime, useful to host standalone game servers.

To use editor tools from the command line, see the godot-headless
package.

%files          server
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-server
%endif

#----------------------------------------------------------------------

%package        runner
Summary:        Shared binary to play games developed with the Godot engine
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

%files          runner
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-runner

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{uversion}

%build
# Needs to be in %%build so that system_libs stays in scope
# We don't unbundle enet and minizip as they have necessary custom changes
to_unbundle="freetype libogg libpng libtheora libvorbis libvpx libwebp mbedtls opus pcre2 zlib zstd"
# Godot requires bullet 2.89+, which Fedora doesn't package yet
# TODO: Fedora doesn't provide wslay yet, package it
%if 0%{?mageia}
to_unbundle+=" bullet wslay"
%endif
# RHEL8 doesn't provide miniupnpc
%if ! 0%{?rhel}
to_unbundle+=" miniupnpc"
%endif

system_libs=""
for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done

%define _scons scons-3 %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" $system_libs use_lto=yes udev=yes progress=no

%if 0%{?fedora}
export BUILD_NAME="fedora"
%endif
%if 0%{?rhel}
export BUILD_NAME="rhel"
%endif
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif

# Build graphical editor (tools)
%_scons p=x11 tools=yes target=release_debug

# Build game runner (without tools)
%_scons p=x11 tools=no target=release

%if %{with headless}
# Build headless version of the editor
%_scons p=server tools=yes target=release_debug
%endif

%if %{with server}
# Build headless version of the runtime for servers
%_scons p=server tools=no target=release
%endif

%install
install -d %{buildroot}%{_bindir}
install -m755 bin/%{name}.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}
install -m755 bin/%{name}.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-runner
%if %{with headless}
install -m755 bin/%{name}_server.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-headless
%endif
%if %{with server}
install -m755 bin/%{name}_server.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-server
%endif

install -D -m644 icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m644 misc/dist/linux/%{rdnsname}.desktop \
    %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
install -D -m644 misc/dist/linux/%{rdnsname}.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
install -D -m644 misc/dist/linux/x-%{name}-project.xml \
    %{buildroot}%{_datadir}/mime/application/x-%{name}-project.xml
install -D -m644 misc/dist/linux/%{name}.6 \
    %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m644 misc/dist/shell/%{name}.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m644 misc/dist/shell/_%{name}.zsh-completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
# Validate desktop and appdata files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Rémi Verschelde <akien@fedoraproject.org> - 3.2.1-1
- Version 3.2.1-stable
- Bundles assimp, requires development version not packaged anywhere
- Bundles libwslay, not packaged on Fedora (replaces libwebsockets)
- Adds bash and zsh completion files

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Rémi Verschelde <akien@fedoraproject.org> - 3.1.2-1
- Version 3.1.2-stable
- Bundled libwebsockets was downgraded to 3.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Rémi Verschelde <akien@fedoraproject.org> - 3.1.1-1
- Version 3.1.1-stable
- Adds dependency on system mbedtls and miniupnpc
- Removes dependency on openssl
- Bundles libwebsockets, can't build against system one for now
- Bundles tinyexr, not packaged (and likely not relevant to package)
- Rename -server build to -headless, add an actual server runtime package
- Build with LTO, improves performance a lot (but slow linking)
- Adds MIME type for .godot project files

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.6-3
- rebuilt (libvpx)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.6-1
- Version 3.0.6-stable (fixes CVE-2018-1000224)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.4-1
- Version 3.0.4-stable

* Wed Jun 20 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.3-1
- Version 3.0.3-stable
- Enable aarch64 support

* Mon Mar 26 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.2-2
- Fix inclusion of armv7hl-specific patch in SRPM

* Tue Mar 20 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.2-1
- Initial Godot package for Fedora, based on my own Mageia package.
- Exclude unsupported arches: aarch64 ppc64 ppc64le s390x
- Workaround GCC < 8.1 ICE on armv7hl

* Wed Mar 14 2018 Rémi Verschelde <akien@mageia.org> 3.0.2-2.mga7
+ Revision: 1209402
- Fix launch argument of desktop file

* Sun Mar 04 2018 Rémi Verschelde <akien@mageia.org> 3.0.2-1.mga7
+ Revision: 1206473
- Add upstream patch to fix server platform build
- Version 3.0.2-stable

* Fri Feb 02 2018 Rémi Verschelde <akien@mageia.org> 3.0-3.mga7
+ Revision: 1198620
- Update tarball to final 3.0-stable

* Fri Feb 02 2018 David GEIGER <daviddavid@mageia.org> 3.0-2.mga7
+ Revision: 1198552
- rebuild for new libvpx 1.7.0

* Fri Jan 26 2018 Rémi Verschelde <akien@mageia.org> 3.0-1.mga7
+ Revision: 1197290
- Disable LTO, seems to break debuginfo
- New upstream tarball with fixed debuginfo stripping
- Prevent stripping binaries
- Don't unbundle zstd yet as Godot uses experimental APIs exposed only in the static library
- Keep bundled bullet, needs >= 2.88 which is not released yet
- Version 3.0-stable
- No longer provide demos, they can be downloaded from the editor
- Disable server binary, not available in 3.0
- Compile with GCC and LTO
- Document bundled() provides thoroughly
- Document bundled() provides

* Sun Dec 03 2017 David GEIGER <daviddavid@mageia.org> 2.1.4-4.mga7
+ Revision: 1180794
- rebuild for new glew 2.1.0

* Sun Sep 24 2017 Rémi Verschelde <akien@mageia.org> 2.1.4-3.mga7
+ Revision: 1158526
- Add upstream patches to improve packaging:
  * P0: OpenSSL 1.1.0 support, adjust BRs accordingly
  * P1: Upstream desktop and AppStream files
  * P2: Help output improvements
  * P3: Upstream man page
- Add license files to server package
- Remove ExclusiveArch, should be possible to build on ARMv7
- Clarify why clang and openssl-compat10 are used
- Package doc for demos

* Sat Sep 23 2017 Rémi Verschelde <akien@mageia.org> 2.1.4-2.mga7
+ Revision: 1157793
- Add debug_release symbols
- Enable udev support for joypads
- Package COPYRIGHT.txt and AUTHORS.md in docs

* Mon Sep 11 2017 Guillaume Rousse <guillomovitch@mageia.org> 2.1.4-1.mga7
+ Revision: 1152942
- new version 2.1.4
- use llvm, as gcc 7 is not supported upstream

* Tue Apr 11 2017 Rémi Verschelde <akien@mageia.org> 2.1.3-1.mga6
+ Revision: 1096424
- Version 2.1.3

* Sat Jan 21 2017 Rémi Verschelde <akien@mageia.org> 2.1.2-1.mga6
+ Revision: 1082732
- Version 2.1.2-stable

* Wed Nov 16 2016 Rémi Verschelde <akien@mageia.org> 2.1.1-1.mga6
+ Revision: 1067563
- Version 2.1.1
- Unbundle libraries thanks to upstream work to facilitate this:
  freetype, glew, libogg, libpng, libtheora, libvorbis, libwebp, openssl, opus, zlib
- Drop packaged templates for x11 32-bit and 64-bit
  o It was too much work for building templates just for Linux, and 32-bit systems
    would not have had access to the 64-bit templates anyway.
  o Godot 3.0 (next major) will let users download official templates directly,
    which is much better for the many supported platforms the Linux editor can
    export to.

* Tue Aug 09 2016 Rémi Verschelde <akien@mageia.org> 2.1-1.mga6
+ Revision: 1045186
- Enable conditional server build, for testing purposes
- Sync new 2.1 tarball
- Add tarball for demos, provided separately upstream
- Version 2.1
  o BRs xrandr for dpi detection
  o No longer links statically against stdc++-static

* Sun Jul 10 2016 Rémi Verschelde <akien@mageia.org> 2.0.4.1-1.mga6
+ Revision: 1040624
- Version 2.0.4.1, hotfix for a regression
- Version 2.0.4

* Thu Jun 16 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-4.mga6
+ Revision: 1021639
- Fix Comment in desktop file
- Force starting the project manager in the desktop file

* Tue May 17 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-3.mga6
+ Revision: 1016575
- Resync tarball with upstream, makes Patch0 obsolete

* Fri May 13 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-2.mga6
+ Revision: 1014571
- Patch upstream regression in ItemList

* Thu May 12 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-1.mga6
+ Revision: 1014421
- Version 2.0.3
- No longer compress templates with upx

* Tue Mar 08 2016 Rémi Verschelde <akien@mageia.org> 2.0.1-1.mga6
+ Revision: 987284
- Version 2.0.1

* Wed Mar 02 2016 Sysadmin Bot <umeabot@mageia.org> 2.0-3.mga6
+ Revision: 983443
- Rebuild for openssl

* Sat Feb 27 2016 Rémi Verschelde <akien@mageia.org> 2.0-2.mga6
+ Revision: 979993
- Install demos (in a separate package)
- Set build revision to mageia instead of custom_build
- Use Mageia optflags and linkflags for builds (apart from debug template, no optflags)

* Tue Feb 23 2016 Rémi Verschelde <akien@mageia.org> 2.0-1.mga6
+ Revision: 977125
- Version 2.0-stable

* Sun Feb 21 2016 Rémi Verschelde <akien@mageia.org> 2.0-0.dev.1.mga6
+ Revision: 975107
- imported package godot
