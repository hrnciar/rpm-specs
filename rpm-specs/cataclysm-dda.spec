# Optimize for build time or performance
%bcond_without release_build

%if %{with release_build}
%else
%global optflags %{optflags} -O0
%endif

Name:           cataclysm-dda
Version:        0.E.2
Release:        7%{?dist}
Summary:        Turn-based survival game set in a post-apocalyptic world

License:        CC-BY-SA
URL:            http://cataclysmdda.org
Source0:        https://github.com/CleverRaven/Cataclysm-DDA/archive/0.E-2/%{name}-0.E-2.tar.gz
Patch0:         cataclysm-dda-gcc11.patch

# Due virtual memory exhausted and build fail
ExcludeArch:    i686

BuildRequires:  astyle
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 7
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)

Requires:       %{name}-data = %{version}-%{release}

Recommends:     %{name}-tiles%{?_isa} = %{version}-%{release}

%description
Cataclysm - Dark Days Ahead. A turn-based survival game set in a
post-apocalyptic world.

Roguelike set in a post-apocalyptic world. While some have described it as a
"zombie game", there is far more to Cataclysm than that. Struggle to survive in
a harsh, persistent, procedurally generated world. Scavenge the remnants of a
dead civilization for food, equipment, or, if you are lucky, a vehicle with a
full tank of gas to get you the hell out of Dodge. Fight to defeat or escape
from a wide variety of powerful monstrosities, from zombies to giant insects to
killer robots and things far stranger and deadlier, and against the others like
yourself, who want what you have...


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%package        tiles
Summary:        %{name} version with gfx and sound

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-tiles-data = %{version}-%{release}

%description    tiles
%{name} version with gfx and sound.


%package        tiles-data
Summary:        Data files for %{name}-tiles
BuildArch:      noarch

Requires:       %{name}-tiles = %{version}-%{release}
Requires:       hicolor-icon-theme
#Recommends:     unifont-fonts

# Bundled, hardcoded fonts. Tiles version doesn't work if delete.
Provides:       bundled(fixedsys)
Provides:       bundled(square)
Provides:       bundled(Square-Smallcaps)
Provides:       bundled(unifont-fonts) = 12.0.01

%description    tiles-data
Data files for %{name}-tiles.


%prep
%autosetup -n Cataclysm-DDA-0.E-2 -p1


%build
%ifarch armv7hl
# This package is triggering a compiler error on armv7hl when
# LTO is enabled.  Disable on armv7hl for now
%define _lto_cflags %{nil}
%endif

%set_build_flags

# Note: Don't use LTO for builds in COPR due to limited resources. COPR build
# will fail because of LTO.
%make_build             \
    PREFIX=%{_prefix}   \
    USE_HOME_DIR=1      \
    %if %{with release_build}
    RELEASE=1           \
    #LTO=1               \
    %endif

# Version with gfx and sound
%make_build             \
    PREFIX=%{_prefix}   \
    SOUND=1             \
    TILES=1             \
    USE_HOME_DIR=1      \
    %if %{with release_build}
    RELEASE=1           \
    #LTO=1               \
    %endif


%install
%make_install           \
    PREFIX=%{_prefix}   \
    USE_HOME_DIR=1      \
    %if %{with release_build}
    RELEASE=1           \
    #LTO=1               \
    %endif

# Version with gfx and sound
%make_install           \
    PREFIX=%{_prefix}   \
    SOUND=1             \
    TILES=1             \
    USE_HOME_DIR=1      \
    %if %{with release_build}
    RELEASE=1           \
    #LTO=1               \
    %endif

# Install desktop file, icon and appdata manifest
install -m 0644 -Dp data/xdg/%{name}.desktop        %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m 0644 -Dp data/xdg/%{name}.svg            %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -m 0644 -Dp data/xdg/%{name}.appdata.xml    %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# FIXME: Remove bundled fonts
# * This for next builds and requires some testing
#rm -r   %{buildroot}%{_datadir}/%{name}/font

rm -r   %{buildroot}%{_datadir}/%{name}/font/terminus.fon \
        %{buildroot}%{_datadir}/%{name}/LICENSE-OFL-Terminus-Font.txt

# Remove duplicate license file
rm      %{buildroot}%{_datadir}/%{name}/LICENSE.txt

# Move changelog info in proper location
rm      %{buildroot}%{_datadir}/%{name}/changelog.txt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE.txt
%doc doc/* README.md CODE_OF_CONDUCT.md data/changelog.txt
%{_bindir}/cataclysm

%files data
%{_datadir}/%{name}/cataicon.ico
%{_datadir}/%{name}/core/
%{_datadir}/%{name}/credits/
%{_datadir}/%{name}/json/
%{_datadir}/%{name}/mods/
%{_datadir}/%{name}/motd/
%{_datadir}/%{name}/names/
%{_datadir}/%{name}/raw/
%{_datadir}/%{name}/title/
%dir %{_datadir}/%{name}/

%files tiles
%{_bindir}/cataclysm-tiles

%files tiles-data
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/%{name}/font/
%{_datadir}/%{name}/fontdata.json
%{_datadir}/%{name}/gfx/
%{_datadir}/%{name}/help/
%{_datadir}/%{name}/sound/
%{_metainfodir}/*.xml


%changelog
* Mon Oct 19 2020 Jeff Law <law@redhat.com> - 0.E.2-7
- Fix range-loop-construct diagnostic from gcc-11

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 0.E.2-6
- Fix uninitialized variable caught by gcc-11.  Fix dynamic casts
  to avoid gcc-11 diagnostic

* Sat Aug 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.E.2-5
- Fix Fedora build flags invocation

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.E.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.E.2-3
- Disable LTO on armv7hl

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.E.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.E.2-1
- Update to 0.E-2
- Disable LTO

* Tue Apr 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.E-1
- Update to 0.E

* Sun Apr 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10491-1.20200405git0f1e6aa
- Update to 10491

* Tue Mar 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10444-1.20200324git5cee241
- Update to 10444

* Fri Mar 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10399-1.20200306git3eee117
- Update to 10399

* Tue Feb 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10337-1.20200218git9aa8765
- Update to 10337

* Fri Feb 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10304-1.20200207gite7271b0
- Update to 10304

* Thu Jan 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10280-1.20200131gitbab7781
- Update to 10280

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.D.10232-2.20200122gitff0f233
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10232-1.20200122gitff0f233
- Update to 10232

* Tue Jan 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10229-1.20200121git0696252
- Update to 10229

* Sun Jan 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10174-1.20200112git00699b2
- Update to 10174

* Sun Dec 22 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10053-1.20191222git8761541
- Update to 10053
- Exclude i686 arch

* Sat Dec 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10047-1.20191221git1e8f27e
- Update to 10047

* Sat Dec 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.10045-1.20191128git8d27979
- Update to 10045

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.D.9984-1.20191128git8d27979
- Update to 9984

* Thu Nov 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9940-1.20191128git8d27979
- Update to 9940

* Sun Nov 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9926-1.20191124git1a06c34
- Update to 9926

* Wed Nov 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9893-1.20191031git15bd2e1
- Update to 9893

* Sat Nov 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9853-1.20191031git15bd2e1
- Update to 9853

* Thu Oct 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9842-1.20191031git15bd2e1
- Update to 9842
- Spec file fixes

* Tue Oct 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9822-2.20191029git5c100d7
- Update to 9822

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9799-1.20191024git923c311
- Initial package
