# Colorize terminal output. Helps to find problems during build process.
%global optflags %{optflags} -fdiagnostics-color=always

%global commit  ddd39f209f4ce6f03ed3198d7d58c2e36565baa9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200806

%global corename pcsx-rearmed
%global filename pcsx_rearmed

Name:           libretro-%{corename}
Version:        15
Release:        9.%{date}git%{shortcommit}%{?dist}
Summary:        ARM optimized PCSX fork

# Public domain
# ----------------------------
# deps/flac-1.3.2/
# deps/lzma-16.04/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# deps/flac-1.3.2/
# deps/libchdr/
#
# Expat License
# -------------
# frontend/vita/
# libretro-common/
# plugins/dfsound/
#
# GNU General Public License
# --------------------------
# deps/flac-1.3.2/
#
# GNU General Public License (v2 or later)
# ----------------------------------------
# frontend/cspace_arm.S
# libpcsxcore/gte_arm.S
# plugins/dfxvideo/draw_pl.c
#
# GNU Lesser General Public License (v2 or later)
# -----------------------------------------------
# deps/flac-1.3.2/include/share/getopt.h
#
# GNU Lesser General Public License (v2.1 or later)
# -------------------------------------------------
# deps/flac-1.3.2/include/share/grabbag.h
#
# GPL (v2 or later)
# -----------------
# deps/flac-1.3.2/include/share/grabbag/picture.h
# libpcsxcore/cdriso.c
# plugins/gpu_neon/psx_gpu/vector_ops.h
#
License:        GPLv2 and Public Domain and BSD and MIT

URL:            https://github.com/libretro/pcsx_rearmed
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{filename}.libretro
ExcludeArch:    armv7hl

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

Supplements:    gnome-games%{?_isa}
Supplements:    retroarch%{?_isa}

# All hardcoded
# * https://github.com/libretro/pcsx_rearmed/blob/master/Makefile#L167
Provides:       bundled(crypto)
Provides:       bundled(flac) = 1.3.2
Provides:       bundled(libchdr)
Provides:       bundled(lzma) = 16.04

%description
PCSX ReARMed is yet another PCSX fork based on the PCSX-Reloaded project, which
itself contains code from PCSX, PCSX-df and PCSX-Revolution. This version is ARM
architecture oriented and features MIPS->ARM recompiler by Ari64, NEON GTE code
and more performance improvements. It was created for Pandora handheld, but
should be usable on other devices after some code adjustments (N900, GPH
Wiz/Caanoo, PlayBook versions are also available).

PCSX ReARMed features ARM NEON GPU by Exophase, that in many cases produces
pixel perfect graphics at very high performance. There is also Una-i's GPU
plugin from PCSX4ALL project, and traditional P.E.Op.S. one.


%prep
%autosetup -n %{filename}-%{commit} -p1
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' ChangeLog

# Unbundling zlib
rm -r deps/zlib/


%build
%set_build_flags
%make_build -f Makefile.libretro    \
    GIT_VERSION=%{shortcommit}      \
    HAVE_CHD=1                      \
    WANT_ZLIB=0                     \


%install
install -m0755 -Dp %{filename}_libretro.so %{buildroot}%{_libdir}/libretro/%{filename}_libretro.so
install -m0644 -Dp %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{filename}.libretro


%files
%license COPYING
%doc README.md AUTHORS NEWS ChangeLog
%{_libdir}/libretro/


%changelog
* Sun Aug 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 15-9.20200806gitddd39f2
- Update to latest git snapshot

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-9.20200521gitf4c902e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 15-8.20200521gitf4c902e
- Update to latest git snapshot

* Tue Feb 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 15-7.20200211git74ec4f3
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-6.20191024git4b353f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 15-5.20191024git4b353f8
- Packaging fixes

* Wed Nov 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 15-1.20191024git4b353f8
- Update to latest git snapshot
- Packaging fixes

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 15-1.20191007gitcb4aa3e
- Initial package
