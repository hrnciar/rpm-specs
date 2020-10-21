%undefine __cmake_in_source_build

%global commit0 1c68b1e2b13bc113cbf41f142f2105f446a3cdce
%global cdate0  20180601

%global engine  dreamer

Name:           dreamchess
Version:        0.3.0
Release:        0.9.%{cdate0}git%{?dist}
Summary:        Portable chess game
# GPLv2+ generally for most of sources
# but BSD for dreamchess/src/include/gamegui/queue.h
License:        GPLv3+ and BSD
URL:            http://www.%{name}.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  bison flex

BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  pugixml-devel
BuildRequires:  glew-devel
BuildRequires:  help2man
BuildRequires:  desktop-file-utils

# icons get installed into hicolor folders
Requires:       hicolor-icon-theme

Requires:       chessprogram

%if 0%{?fedora}
Suggests:       %{name}-engine
Suggests:       gnuchess
%endif

Requires:       %{name}-data = %{version}-%{release}

%description
DreamChess is an open source chess game.

Features:
- 3D OpenGL graphics
- various chess board sets: from classic wooden to flat figurines
- music, sound effects
- on-screen move lists using SAN notation
- undo functionality
- save-games in PGN format

A moderately strong chess engine as a sub-package: Dreamer.


%package engine
Summary:        A moderately strong chess engine for the game DreamChess
License:        GPLv3+
Provides:       chessprogram

%if 0%{?fedora}
Supplements:    %{name}
%endif

%description engine
Should this chess engine be too weak for you, then you can use any other
XBoard-compatible chess engine, including the popular Crafty and GNU Chess.


%package data
Summary:        Data files for the game DreamChess
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description data
Data files for the game DreamChess:
Boards, Pieces, Sounds, Styles, Themes.


%prep
%autosetup -n %{name}-%{commit0}

%build
%cmake \
 -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
%cmake_build
# generate manpage
help2man -o %{name}.1 --no-discard-stderr \
 --version-string='%{version}' -v'%{release}' \
 %{_vpath_builddir}/%{name}/src/%{name}

%install
%cmake_install
install -D -t %{buildroot}%{_mandir}/man1 %{name}.1


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE.txt
%doc README.md NEWS.md AUTHORS.txt LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}.*

%files engine
%license LICENSE.txt
%doc AUTHORS.txt
%{_bindir}/%{engine}
%{_mandir}/man*/%{engine}.*

%files data
%license LICENSE.txt
%{_datadir}/%{name}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.9.20180601git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.8.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.7.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.6.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.5.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.3.0-0.4.20180601git
- Rebuilt for glew 2.1.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.3.0-0.3.20180601git
- Rebuild with fixed binutils

* Sun Jul 29 2018 Raphael Groner <projects.rg@smart.ms> - 0.3.0-0.2.20180601git
- drop accidently duplicated files

* Sat Jul 28 2018 Raphael Groner <projects.rg@smart.ms> - 0.3.0-0.1.20180601git
- new version, use latest snapshot
- switch to cmake
- add new build dependencies, e.g. SDL2
- cleanup generally

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-18.RC2
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.2.1-14.RC2
- Rebuild for glew 2.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.2.1-12.RC2
- Rebuild for glew 1.13

* Mon Aug 31 2015 Raphael Groner <projects.rg@smart.ms> - 0.2.1-11.RC2
- upstream moved to GitHub

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-9.RC2
- introduce license macro

* Sat Jan 03 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-8.RC2
- add manpage

* Sat Dec 27 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-7.RC2
- add glew as dependency
- add icon cache scriptlets

* Tue Dec 23 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-6.RC2
- v0.2.1 RC2
- use proper download url
- honor icons & desktop file from make install

* Tue Oct 07 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-5.1.RC1
- temporarily, disable weak dependencies due to unclear policy

* Mon Sep 29 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-5.RC1
- use desktop file from source tarball
- enable Suggests (rpm 4.12)

* Sun Sep 14 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-4.RC1
- fix folder owner

* Sun Sep 14 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-3.RC1
- fix Requires with right version
- rename dreamer sub-package to just engine
- licence of engine sub-package
- spelling for rpmlint

* Sat Sep 13 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-2.RC1
- dreamer engine provides chessprogram as a sub-package
- description mentions features
- manpages should not be in doc
- general cleanup for review
- proper licences
- tag for pre-release

* Wed Sep 10 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-1
- initial
