%global appname CorsixTH
%global uuid    com.corsixth.CorsixTH

Name:           corsix-th
Version:        0.64
Release:        5%{?dist}
Summary:        Open source clone of Theme Hospital

# For a breakdown of the licensing, see LICENSE.txt
# The entire source code is MIT except:
# BSD:          CMake scripts
# GPLv3+:       SpriteEncoder
License:        MIT and BSD and GPLv3+
URL:            https://github.com/CorsixTH/CorsixTH
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  auto-destdir
BuildRequires:  cmake
BuildRequires:  compat-lua-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)

Requires:       %{name}-data
Requires:       hicolor-icon-theme
Requires:       lua-filesystem%{?_isa}

# For music support
Recommends:     fluid-soundfont-lite-patches%{?_isa}

# For extracting GOG version
Recommends:     innoextract%{?_isa}

%global _description \
CorsixTH aims to reimplement the game engine of Theme Hospital, and be able to\
load the original game data files. This means that you will need a purchased\
copy of Theme Hospital, or a copy of the demo, in order to use CorsixTH. After\
most of the original engine has been reimplemented in open source code, the\
project will serve as a base from which extensions and improvements to the\
original game can be made.\
\
- To play CorsixTH, you will need either the Demo:\
\
  https://th.corsix.org/Demo.zip\
\
- or the full game of Theme Hospital, available for example at:\
\
  https://www.gog.com/game/theme_hospital

%description %{_description}


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data %{_description}

Package contains data files for %{name}.


%prep
%autosetup -n %{appname}-%{version} -p1


%build
%cmake \
    -G Ninja \
    -DWITH_MOVIES=0
%ninja_build -C %{_vpath_builddir}


%install
%ninja_install -C %{_vpath_builddir}
rm %{buildroot}%{_datadir}/corsix-th/LICENSE.txt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.md README.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.*

%files data
%license LICENSE.txt
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_metainfodir}/*.xml


%changelog
* Wed Aug 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-5
- Build with 'compat-lua-devel' and fix FTBFS-33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-3
- Rebuild with out-of-source builds new CMake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-1
- Update to 0.64

* Mon Jun 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-0.3rc2
- Update to 0.64-rc2

* Thu Jun 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-0.2rc1
- Add patch: Fix #1627 by using static linking for libRnc | GH-1627

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.64-0.1rc1
- Update to 0.64-rc1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.63-1
- Update to 0.63
- Add *fluid-soundfont-lite-patches* package as Recommends for music support

* Tue May 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.63-0.6.rc1
- Update to 0.63rc1

* Mon Apr 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.63-0.4.beta1
- Initial package
