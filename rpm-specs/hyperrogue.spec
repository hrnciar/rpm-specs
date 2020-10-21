%global version_tag 11.3a

Name:           hyperrogue
Version:        11.3
Release:        1.a%{?dist}
Summary:        An SDL roguelike in a non-euclidean world

# The game is under the GPLv2 (src/mtrand.h is under BSD, src/savepng.* is under zlib) and the music under CC-BY (v3)
License:        GPLv2 and BSD and zlib
URL:            http://www.roguetemple.com/z/hyper/
Source0:        https://github.com/zenorogue/hyperrogue/archive/v%{version_tag}/%{name}-%{version_tag}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Source3:        http://roguetemple.com/z/hyper/bigicon-osx.png
# Add the right location of the font file (DejaVuSans-Bold.ttf)
Patch0:         %{name}.fixfontlocation.patch

BuildRequires:  gcc, gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel, SDL_ttf-devel, SDL_gfx-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  glew-devel

Requires: dejavu-sans-fonts

Provides: bundled(mtrand)
Provides: bundled(savepng)

Recommends: %{name}-music

# Hmm.. it seems that hyperrogue does not build on 32-bit arm anymore?
# "as: out of memory allocating 32 bytes after a total of 3020046336 bytes"
# https://kojipkgs.fedoraproject.org//work/tasks/8579/50098579/build.log
ExcludeArch: armv7hl

%description
You are a lone outsider in a strange, non-Euclidean world.
Fight to find treasures and get the fabulous Orbs of Yendor!

%package music
Requires: %{name}
Summary: Music for hyperrogue
BuildArch: noarch
License: CC-BY

%description music
Set of 11 music for hypperrogue.

%prep
%autosetup -n %{name}-%{version_tag}
rm -f src/glew.c
autoreconf -fvi

%build
%configure

# Hmm... this seems like a bug somewhere.
%make_build CXXFLAGS="%{optflags} -I%{_includedir}/SDL"

%install
# Upstream not provides "install" target. I have to install files "by hands".
#mkdir -p %{buildroot}%{_bindir}
#install -pDm755 -p src/hyper %{buildroot}%{_bindir}/%{name}

# Install music files.
#mkdir -p %{buildroot}%{_datadir}/%{name}
#install -pDm644 *ogg %{buildroot}%{_datadir}/%{name}/
#install -pDm644 hyperrogue-music.txt %{buildroot}%{_datadir}/%{name}/

%make_install

# Install the desktop file.
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pDm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install the appdata file.
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/

rm -rf %{buildroot}%{_datadir}/%{name}/DejaVuSans-Bold.ttf

%check
#Test the appdata file.
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

# Under GPLv2
%files
#%%license COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_defaultdocdir}/%{name}/README.md

# Under CC-BY
%files music
%{_datadir}/%{name}


%changelog
* Mon Aug 24 2020 Ben Rosser <rosser.bjr@gmail.com> - 11.3-1.a
- Update to newer upstream release, fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-11.d
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-10.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-9.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-8.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-7.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 10.0-6.d
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-5.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-4.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-2.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 <nobrakal@cthugha.org> 10.0-1.d
- Update to new upstream

* Wed Jun 21 2017 <nobrakal@cthugha.org> 9.4-1.n
- Update to new upstream on github

* Mon Feb 06 2017 <nobrakal@gmail.com> 8.3-3.j
- Update destkop file to match current icon name

* Sat Nov 19 2016 <nobrakal@gmail.com> 8.3-2.j
- Add mtrand as a bundled lib, and add BSD licence
- Add savepng as a bundled lib, and add zlib license
- Update appdata.xml file with new licence and open age rating

* Sat Mar 12 2016 Alexandre Moine <nobrakal@gmail.com> 8.3-1.j
- Update to new upstream
- Make music subpackage a noarch subpackage
- Add lipng-devel as a new BuildRequires
- Update appdata file
- Update desktop file (thanks Rémi Verschelde)

* Sat Mar 12 2016 Alexandre Moine <nobrakal@gmail.com> 7.4-1.h
- Update to new upstream
- Force code relocation with -fPIC
- Remove license: COPYING, since the file was removed by upstream (I contact them about it)

* Thu Aug 06 2015 Alexandre Moine <nobrakal@gmail.com> 6.6-1
- Update to new upstream.
- Create a subpackage for music.
- Set the correct path for the music-info file.
- Fix typo.

* Sat May 09 2015 Alexandre Moine <nobrakal@gmail.com> 5.5-0.3.a
- Use right versioning rules.

* Tue Mar 24 2015 Alexandre Moine <nobrakal@gmail.com> 5.5a-2
- Use install instead of cp.
- Add a correct test of the .appadata.xml file

* Tue Mar 17 2015 Alexandre Moine <nobrakal@gmail.com> 5.5a-1
- Update to the new 5.5a
- Remove the manual install of VeraBD.ttf, not used anymore, replaced by DejaVuSans-Bold.ttf.
- Patch the code to use the fedora DejaVuSans-Bold.ttf file.
- The problem with the executable is solved, put it back in %%{_bindir}

* Sat Nov 15 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-4
- Remove the explicit Requires: SDL_mixer SDL_ttf SDL_gf

* Mon Oct 27 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-3
- Chmod the executable to 755
- Change the icon for a wider
- Add an appdata file

* Sat Oct 25 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-2
- Change %%{_datadir} to %%{_libdir} for the arch-dependent binairie

* Wed Oct 22 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-1
- Original spec
