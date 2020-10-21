%global alias ValyriaTear
Name:       valyriatear
Version:    1.0.0
Release:    22%{?dist}
Summary:    Valyria Tear is a free 2D J-RPG based on the Hero of Allacrost engine
License:    GPLv2
URL:        http://valyriatear.blogspot.de/
Source0:    https://github.com/Bertram25/%{alias}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:   %{name}-data = %{version}-%{release}
BuildRequires:  gcc-c++
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libvorbis-devel
BuildRequires: luabind-devel
BuildRequires: lua-devel
BuildRequires: openal-soft-devel
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: zlib-devel

# Fix build failures https://bugzilla.redhat.com/show_bug.cgi?id=1308215
Patch1:     valyriatear-1.0.0-fstream-check.patch
Patch2:     valyriatear-1.0.0-nullptr-check.patch

%description
Valyria Tear is a free (as meant in the GNU Public License) 2D J-RPG game
based on the Hero of Allacrost engine.

You can play it very much like a typical console role-playing game.
You can explore maps and talk to non-playable characters (NPCs),
fight active-time battles against multiple enemies,
and manage your characters and equipment through a series of menus.
Valyria Tear runs in a series of "game modes" which represent
different states of operation in the game.

This package contains the binary.

%package data
Summary:    A single player, 2D-isometric, action Role-Playing Game, data files
# See LICENSE file
License:    CC-BY-SA and CC-BY and CC0 and GPLv2 and GPLv2+ and GPLv3
Requires:   %{name} = %{version}-%{release}
Requires:   linux-libertine-biolinum-fonts
Requires:   linux-libertine-fonts
BuildArch:  noarch

%description data
Valyria Tear is a free (as meant in the GNU Public License) 2D J-RPG game
based on the Hero of Allacrost engine.

You can play it very much like a typical console role-playing game.
You can explore maps and talk to non-playable characters (NPCs),
fight active-time battles against multiple enemies,
and manage your characters and equipment through a series of menus.
Valyria Tear runs in a series of "game modes" which represent
different states of operation in the game.

This package contains the game data.

%prep
%setup -q -n %{alias}-%{version}
%patch1 -p1 -b .fstream-check
%patch2 -p1 -b .nullptr-check
# Ensure that it builds against system libaries
rm -r src/luabind
# Use system fonts
rm -r img/fonts/*
sed -i dat/config/fonts.lua \
    -e 's/img\/fonts\/LinLibertine_aBS\.ttf/\/usr\/share\/fonts\/linux-libertine\/LinLibertine_RB.otf/' \
    -e 's/img\/fonts\/LinBiolinum_RBah\.ttf/\/usr\/share\/fonts\/linux-libertine\/LinBiolinum_RB.otf/' \
    -e 's/img\/fonts\/Berenika-Oblique\.ttf/\/usr\/share\/fonts\/linux-libertine\/LinBiolinum_RB.otf/'


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DUSE_SYSTEM_LUABIND=ON
%cmake_build


%install
%cmake_install
install -D -p -m644 doc/%{name}.6 %{buildroot}/%{_mandir}/man6/%{name}.6

desktop-file-validate  %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS MANUAL README.md LICENSES COPYING.CC0 COPYING.CC-BY-3 COPYING.CC-BY-SA-3 COPYING.GPL-2 COPYING.GPL-3
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/valyriatear.png
%{_mandir}/man6/%{name}.6*

%files data
%{_datadir}/%{name}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1.0.0-21
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-10
- Rebuilt for Boost 1.63 and patch for C++11 (#1308215)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-8
- Rebuilt for Boost 1.60

* Fri Aug 28 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.0-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.0-2
- Rebuild for boost 1.57.0

* Fri Sep 05 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.0.0-1
- New release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 03 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.0.0-0.1rc1
- New release candidate

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.6.0-2
- Rebuild for boost 1.55.0

* Sat Mar 01 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.6.0-1
- New release

* Wed Sep 4 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.6-0.1rc1
- New rc release

* Tue Jul 30 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-6
- Fixed building with newer boost version

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.5.0-5
- Rebuild for boost 1.54.0

* Thu Mar 28 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-4
- Fixed serious crash in the inventory (redhat bug: #928608)

* Fri Feb 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-3
- Fixed download link to github directly

* Fri Feb 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-2
- Fixed Gnu -> GNU
- Added comment to Source0

* Fri Feb 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-1
- New upstream release 0.5.0

* Tue Jan 8 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-0.2rc2
- Added patch for lua 5.2

* Tue Jan 8 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.5.0-0.1rc2
- Initial packaging
