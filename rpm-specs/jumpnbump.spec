# From GitLab tag: https://gitlab.com/LibreGames/jumpnbump/tags
%global uploadhash 95acdae2a232513f068e260977371dcf

Name:           jumpnbump
Version:        1.61
Release:        3%{?dist}
Summary:        Cute multiplayer platform game with bunnies
License:        GPLv2+
URL:            https://gitlab.com/LibreGames/jumpnbump
Source0:        https://gitlab.com/LibreGames/jumpnbump/uploads/%{uploadhash}/%{name}-%{version}.tar.xz
Patch0:         0001-Makefile-Set-fcommon-to-workaround-GCC-10-change.patch

BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(zlib)

# For desktop file validation
BuildRequires:  desktop-file-utils
# For AppStream metainfo validation
BuildRequires:  libappstream-glib

# For music support, dlopen()'ed by SDL2_music
Requires:       libmodplug

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-menu
%else
Requires:       %{name}-menu
%endif

%description
Jump 'n Bump is a cute multiplayer platform game in which you, as a bunny,
have to jump on your opponents to make them explode. It is a true multiplayer
game with network support and shouldn't be played alone, although computer
bunnies with limited AI are available. The game is a UNIX port of the old DOS
game by Brainchild Design.

%package menu
Summary:        Level selection and config menu for the Jump 'n Bump game
BuildArch:      noarch

BuildRequires:  gettext
# For potential auto dep generation
%if 0%{?rhel} == 7
BuildRequires:  python36-devel
%else
BuildRequires:  python3-devel
%endif

Requires:       %{name} = %{version}-%{release}
Requires:       %{_bindir}/convert
%if 0%{?rhel} == 7
Requires:       python36-gobject
%else
Requires:       python3-gobject
%endif

%description menu
Python 3/GTK+3 based level selection and configuration interface for the Jump 'n
Bump game.

%prep
%autosetup -p1

%build
export CFLAGS="%{?__global_cflags}"
export LDFLAGS="%{?__global_ldflags}"

%make_build PREFIX=%{_prefix}
%make_build PREFIX=%{_prefix} -C menu

%install
%make_install PREFIX=%{_prefix}
%make_install PREFIX=%{_prefix} -C menu

%find_lang %{name}-menu

%check
# Validate desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}{,-menu}.desktop

# Validate AppStream metainfo data
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%post
/bin/touch --no-create %{_datadir}/icons &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :

%files
%doc AUTHORS ChangeLog docs/* README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gobpack
%{_bindir}/jnb*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jumpbump.dat
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6*

%files menu -f %{name}-menu.lang
%doc menu/README.md
%license COPYING
%{_bindir}/%{name}-menu
%{_datadir}/%{name}/%{name}_menu.glade
%{_datadir}/applications/%{name}-menu.desktop

%changelog
* Fri Feb 28 2020 Rémi Verschelde <rverschelde@gmail.com> - 1.61-3
- Workaround FTBFS with GCC 10 defaulting to -fno-common (rhbz#1799558)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Rémi Verschelde <rverschelde@gmail.com> - 1.61-1
- Version 1.61
- jumpnbump-menu now uses Python 3/GTK+3 (rhbz#1738040)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.60-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Rémi Verschelde <rverschelde@gmail.com> 1.60-2
- Add missing dependency: libmodplug for music support
- Add missing dependency: pygtk2-libglade

* Mon May 29 2017 Rémi Verschelde <rverschelde@gmail.com> 1.60-1
- Import in Fedora (#1456203)
- Adapt to Fedora with help from Neal Gompa
- Backport upstream patches for appdata file and python shebang
- Add scriptlets to update the icon cache in the absence of filetriggers
  https://fedoraproject.org/wiki/Packaging:Scriptlets#Icon_Cache

* Sat May 27 2017 Rémi Verschelde <akien@mageia.org> 1.60-2.mga6
+ Revision: 1105173
- Package more docs and license terms

* Wed May 24 2017 Rémi Verschelde <akien@mageia.org> 1.60-1.mga6
+ Revision: 1104457
- Version 1.60

* Fri May 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170519.3.mga6
+ Revision: 1103391
- Fix bogus requires in jumpnbump-menu, and make it noarch

* Fri May 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170519.2.mga6
+ Revision: 1103253
- Disable parallel build completely
- Sync with upstream 20170519, adds jumpnbump-menu subpackage

* Wed May 17 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170516.1.mga6
+ Revision: 1102304
- Snapshot 20170516

* Wed Apr 19 2017 Rémi Verschelde <akien@mageia.org> 1.60-0.20170411.4.mga6
+ Revision: 1096845
- Limit number of jobs for parallel build
- Another attempt to fix parallel building
- Attempt at fixing dependency ordering
- imported package jumpnbump
