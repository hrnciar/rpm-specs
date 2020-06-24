%bcond_with debug

Name:          crawl
Summary:       Roguelike dungeon exploration game
Version:       0.25.0
Release:       1%{?dist}
# Main license : GPLv2+
# 2-clause BSD: all contributions by Steve Noonan and Jesse Luehrs
# Public Domain|CC0: most of tiles, perlin.cc, perlin.h
# The majority of Crawl's tiles and artwork are released under the CC0 license
# MIT: json.cc and worley.cc
# ASL 2.0: pcg.cc 
## According to the 'license.txt' file,
## This program can be redistribute under GPLv2+ license; MIT and BSD are GPL compatible.
License:       GPLv2+ and ASL 2.0
URL:           https://crawl.develz.org/
Source0:       https://github.com/%{name}/%{name}/archive/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}-tiles.desktop
Source2:       %{name}-tiles.png
Source3:       %{name}-tiles.appdata.xml

## These patches fix installation paths
Patch0:        %{name}_bin.patch
Patch1:        %{name}_tiles.patch

Patch2:        %{name}-rltiles_cflags.patch

# See https://github.com/crawl/crawl/issues/1372
Patch3:        %{name}-add_iswalnum_reference.patch

Patch4:        %{name}-use_lua53.patch

BuildRequires: advancecomp
BuildRequires: bison
BuildRequires: gcc-c++, git
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(lua-5.1)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: pngcrush

Requires: %{name}-common-data = %{version}-%{release}
Requires(pre): shadow-utils

%description
This is the Console (ncurses) version of %{name}.

Dungeon Crawl Stone Soup is a free roguelike game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup has diverse species and many different character
backgrounds to choose from, deep tactical game-play, sophisticated magic,
religion and skill systems, and a grand variety of monsters to fight and
run from, making each game unique and challenging.

####################
%package common-data
Summary: Common data files of %{name}
BuildArch: noarch
Requires:  hicolor-icon-theme

%description common-data
Data files for tiles and console versions of %{name}.

####################
%package tiles
Summary:  Roguelike dungeon exploration game with tiles
Requires: %{name}-tiles-data = %{version}-%{release}

%description tiles
This is the tiles (graphical) version of %{name}.

Dungeon Crawl Stone Soup is a free roguelike game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup has diverse species and many different character
backgrounds to choose from, deep tactical game-play, sophisticated magic,
religion and skill systems, and a grand variety of monsters to fight and
run from, making each game unique and challenging.

####################
%global fonts font(bitstreamverasans)
%global fonts %{fonts} font(bitstreamverasansmono)
%package tiles-data
Summary: Data files of %{name}-tiles
BuildArch: noarch
BuildRequires: fontconfig %{fonts}
Requires: %{name}-common-data = %{version}-%{release}
Requires: %{fonts}

%description tiles-data
Data files of %{name}-tiles.

%prep
%autosetup -n %{name}-%{version} -N

cat > crawl-ref/source/util/release_ver <<EOF
%{version}
EOF

## Remove unused/bundled files
rm -rf MSVC
rm -rf webserver

find crawl-ref/source -name '*.py' | xargs pathfix.py -i %{__python3} -pn

#%%patch4 -p1 -b .use_lua53
%patch3 -p1 -b .add_iswalnum_reference

cp -a crawl-ref/source crawl-ref/crawl-tiles

%patch0 -p1 -b .crawl_bin
%patch1 -p1 -b .crawl_tiles
%patch2 -p1 -b .rltiles_cflags

%build
%if %{with debug}
%make_build V=1 debug -C crawl-ref/source \
%else
%make_build -C crawl-ref/source \
%endif
 CXX=g++ CFOPTIMIZE_L="%{build_cxxflags} -fPIC" \
%ifnarch x86_64 i386
 CFOTHERS="" \
%endif
 SOUND=y V=y MONOSPACED_FONT=y \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" NO_TRY_GOLD=y \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%if %{with debug}
%make_build V=1 debug -C crawl-ref/crawl-tiles \
%else
%make_build -C crawl-ref/crawl-tiles \
%endif
 CXX=g++ CFOPTIMIZE_L="%{build_cxxflags} -fPIC" \
%ifnarch x86_64 i386
 CFOTHERS="" \
%endif
 TILES=y SOUND=y V=y MONOSPACED_FONT=y \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" NO_TRY_GOLD=y \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%install
%if %{with debug}
%make_install debug -C crawl-ref/crawl-tiles \
%else
%make_install -C crawl-ref/crawl-tiles \
%endif
 CXX=g++ CFOPTIMIZE_L="%{build_cxxflags} -fPIC" \
%ifnarch x86_64 i386
 CFOTHERS="" \
%endif
 TILES=y SOUND=y V=y MONOSPACED_FONT=y \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" NO_TRY_GOLD=y \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%if %{with debug}
%make_install debug -C crawl-ref/source \
%else
%make_install -C crawl-ref/source \
%endif
 CXX=g++ CFOPTIMIZE_L="%{build_cxxflags} -fPIC" \
%ifnarch x86_64 i386
 CFOTHERS="" \
%endif
 SOUND=y V=y MONOSPACED_FONT=y \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" NO_TRY_GOLD=y \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

# Move doc files into /usr/share/crawl/docs (bz#1498448)
mkdir -p %{buildroot}%{_datadir}/%{name}/docs
mv %{buildroot}%{_pkgdocdir}/*.txt %{buildroot}%{_datadir}/%{name}/docs/
mv %{buildroot}%{_pkgdocdir}/develop %{buildroot}%{_datadir}/%{name}/docs/
install -pm 644 crawl-ref/CREDITS.txt %{buildroot}%{_pkgdocdir}/
install -pm 644 README* %{buildroot}%{_pkgdocdir}/

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man6
install -pm 644 crawl-ref/docs/crawl.6 %{buildroot}%{_mandir}/man6/

## Instal icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -Dpm 644 crawl-ref/crawl-tiles/dat/tiles/stone_soup_icon-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -Dpm 644 crawl-ref/crawl-tiles/dat/tiles/stone_soup_icon-512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps

mkdir -p %{buildroot}%{_datadir}/icons/%{name}
install -pm 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/%{name}

## Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install %{SOURCE1} --dir=%{buildroot}%{_datadir}/applications

## Links to system's fonts
ln -sf $(fc-match -f "%{file}" "bitstreamverasansmono") %{buildroot}%{_datadir}/%{name}/dat/tiles/VeraMono.ttf
ln -sf $(fc-match -f "%{file}" "bitstreamverasans") %{buildroot}%{_datadir}/%{name}/dat/tiles/Vera.ttf

## Install appdata file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE3} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%{_bindir}/crawl
%{_mandir}/man6/crawl*

%files common-data
%{_datadir}/%{name}/
%{_pkgdocdir}/
%license LICENSE
%{_datadir}/icons/%{name}/
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/512x512/apps/*.png
%exclude %{_datadir}/%{name}/dat/tiles

%files tiles
%{_bindir}/crawl-tiles
%{_datadir}/applications/%{name}-tiles.desktop
%{_metainfodir}/%{name}-tiles.appdata.xml

%files tiles-data
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/dat
%{_datadir}/%{name}/dat/tiles/

%changelog
* Fri Jun 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.25.0-1
- Release 0.25.0

* Thu May 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.24.1-3
- Conform fonts symlinks to the new paths

* Thu Apr 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.24.1-2
- Tested with lua-5.3 (incompatible)

* Wed Apr 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.24.1-1
- Release 0.24.1

* Sun Apr 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.24.0-3
- Fix rhbz#1825629

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.24.0-1
- Release 0.24.0 (rhbz#1765342)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.23.2-1
- Upstream bugfix release 0.23.2

* Fri Mar 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.23.1-1
- Upstream bugfix release 0.23.1 (bz#1684362)
- Override -mfpmath=sse -msse2 except on x86_64 and i386 architectures

* Fri Feb 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.23.0-1
- Upstream release 0.23.0 (bz#1673723)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.22.1-1
- Upstream release 0.22.1

* Sat Aug 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0 (bz#1614779)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.21.1-4
- Remove '-Wp,-D_GLIBCXX_ASSERTIONS' flag (bz#1575324) (upstream bug 11467)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.21.1-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.21.1-1
- Update to 0.21.1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.0-2
- Remove obsolete scriptlets

* Sat Jan 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0 (bz#1531816)

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.20.1-6
- Appdata file moved into metainfo data directory

* Wed Oct 04 2017 Antonio Trande <sagitterATfedoraproject.org>  0.20.1-5
- Move doc files into /usr/share/crawl/docs (bz#1498448)
- Install manpage

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Antonio Trande <sagitterATfedoraproject.org>  0.20.1-2
- Do not  create a crawl group

* Sun Jul 02 2017 Antonio Trande <sagitterATfedoraproject.org>  0.20.1-1
- Update to 0.20.1

* Mon Jun 26 2017 Antonio Trande <sagitterATfedoraproject.org>  0.20.0-2
- Set datadir permissions

* Wed Jun 07 2017 Antonio Trande <sagitterATfedoraproject.org>  0.20.0-1
- Update to 0.20.0
- Set permissions with %%defattr (bz#1458489)

* Sat Jun 03 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.5-3
- Set directory permissions (bz#1458489)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Mar 01 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.5-1
- Update to 0.19.5

* Sun Feb 05 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.4-2.20170205git5e19f3
- Patched for gcc7

* Wed Feb 01 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.4-1
- Update to 0.19.4 (bz#14179114)

* Sun Jan 22 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.3-2
- Use pkg-config on Fedora > 25

* Sun Jan 22 2017 Antonio Trande <sagitterATfedoraproject.org>  0.19.3-1
- Update to 0.19.3 (bz#1415476)

* Thu Nov 24 2016 Antonio Trande <sagitterATfedoraproject.org>  0.19.1-1
- Update to 0.19.1 (bz#1398298)

* Tue Nov 01 2016 Antonio Trande <sagitterATfedoraproject.org>  0.19.0-1
- Update to 0.19.0 (bz#1390562)
- Drop old patch
- Use -std=gnu++11 instead of -std=c++11 (build issue on PPC64le)

* Wed Sep 07 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-9
- Rebuild without NOWIZARD option (bz#1372480)

* Fri Sep 02 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-8
- Rebuild in nowizard mode (bz#1372480)

* Fri Jul 15 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-7
- Fix Crawl Tiles name (bz#1357087)

* Fri Jul 15 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-6
- Fix crawl-tiles's dependencies (bz#1357067)

* Sun Jun 12 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-5
- Remove unused/bundled files
- License clarification
- Compile debugging files and make Crawl tests

* Sat Jun 11 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-4
- Include MIT license
- Fix scriptlets for icons

* Mon Jun 06 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-3
- Add an appdata file

* Sat Jun 04 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-2
- Patched to fix the installation paths

* Sat Jun 04 2016 Antonio Trande <sagitterATfedoraproject.org>  0.18.1-1
- First package

