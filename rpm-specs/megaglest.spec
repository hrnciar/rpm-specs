Name:		megaglest
Version:	3.13.0
Release:	6%{?dist}
Summary:	Open Source 3d real time strategy game
License:	GPLv3+ and GPL+
Url:		http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}-source/releases/download/%{version}/%{name}-source-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	mesa-libGL-devel
BuildRequires:	ftgl-devel
BuildRequires:	glew-devel
BuildRequires:	gnutls-devel
BuildRequires:	help2man
BuildRequires:	openjpeg-devel
BuildRequires:	libcurl-devel
BuildRequires:	libicu-devel
BuildRequires:	libircclient-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lua-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	openal-soft-devel
BuildRequires:	openssl-devel
BuildRequires:	libpng-devel
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_net-devel
BuildRequires:	subversion
BuildRequires:	xerces-c27-devel
BuildRequires:	wxGTK3-devel
BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	zlib-devel
Requires:	glx-utils
Requires:	megaglest-data = %{version}
Requires:	p7zip
Obsoletes:	glest <= 3.2.2

# Correct use of XERCESC_INCLUDE and XERCESC_INCLUDE_DIR that
# should have the same value if xerces is found.
Patch0:		%{name}-xerces.patch
# Correct usage of xvfb-run when generating manpages
Patch1:		%{name}-help2man.patch
# Do not fail with cryptic message if there are missing translations
# just use english text
Patch2:		%{name}-translation-missing.patch
# Build with lua5.2
Patch3:		%{name}-lua.patch
# Add extra libraries to link command line to satisfy unresolved symbols
Patch4:		%{name}-underlink.patch
# Prevent multiple definitions of symbols
Patch5:		%{name}-feathery_ftp.patch

%description
MegaGlest is an entertaining free (freeware and free software) and
open source cross-platform 3D real-time strategy (RTS) game, where
you control the armies of one of seven different factions: Tech,
Magic, Egypt, Indians, Norsemen, Persian or Romans. The game is
setup in one of 17 naturally looking settings, which -like the
unit models- are crafted with great appreciation for detail.
A lot of additional game data can be downloaded from within the
game at no cost.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
mkdir -p build
pushd build
    export XERCESC_INCLUDE_DIR=%{_includedir}/xercesc-2.7.0
    export XERCESC_LIBRARY_DIR=%{_libdir}/xerces-c-2.7.0
    %cmake								\
	-DMEGAGLEST_BIN_INSTALL_PATH=%{_bindir}				\
	-DWANT_GIT_STAMP=OFF						\
	..
    make %{?_smp_mflags}
popd

%install
make install DESTDIR=${RPM_BUILD_ROOT} -C build
install -d $RPM_BUILD_ROOT%{_datadir}/megaglest

%files
%doc docs/AUTHORS.source_code.txt
%doc docs/CHANGELOG.txt
%doc docs/COPYRIGHT.source_code.txt
%doc docs/gnu_gpl_3.0.txt
%doc docs/README.txt
%{_bindir}/*
%{_mandir}/man6/*.6*
%{_datadir}/megaglest/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.13.0-4
- Correct Fedora 32 FTBFS (#1799642)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Scott Talbert <swt@techie.net> - 3.13.0-2
- Rebuild with wxWidgets GTK3 build

* Tue Sep 24 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.13.0-1
- Update to latest upstream release
- Drop no longer needed patches

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 3.12.0-11
- Rebuilt for miniupnpc soname bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.12.0-9
- Rebuilt for glew 2.1.0

* Wed Aug 15 2018 Scott Talbert <swt@techie.net> - 3.12.0-8
- Rebuild with wxWidgets 3.0 (GTK+ 2 build)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-2
- Rebuild for glew 2.0.0

* Fri Jun 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.12.0-1
- Update to latest upstream release
- Add patch to build with gcc6
- Add patch to build with miniupnpc2
- Move icons to -data package
- Remove appdata and use upstream ones from -data package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 3.11.1-5
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.11.1-3
- Rebuild for new libircclient.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.11.1-2
- Add an AppData file for the software center

* Tue Mar 24 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.11.1-1
- Update to latest upstream release.
- Remove upstreamed icon-path patch.
- Update to become megaglest.bmp file owner.
- Update description from upstream webpage.
- Add patch to build with lua 5.2 fedora package.
- Add underlink patch to correct missing symbols during link.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.1-2
- Rebuild with minupnpc 1.9.

* Thu Jan 23 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.1-1
- Update to latest upstream release.

* Tue Nov 19 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.0-1
- Update to latest upstream release.

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 3.7.1-10
- rebuilt for GLEW 1.10

* Fri Aug 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-9
- Rebuild with minupnpc 1.8.

* Wed Aug 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-8
- Add support for minupnpc >= 1.7 (#996357)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-4
- Correct crash with NULL unit in selection (#924874)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.7.1-4
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-3
- Add patch suggested by upstream for better color picking selection mode.

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 3.7.1-2
- Rebuild for glew 1.9.0

* Fri Nov 23 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-1
- Update to latest upstream release.
- Remove no longer required gcc 4.7 patch.
- Add versioned requires to megaglest-data.

* Thu Jul 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-5
- Do not use %%{_iconsdir} macro (#817315).
- Correct libjpeg-turbo-devel build requires (#817315).
- Add missing desktop-file-utils build requires (#817315).
- Update license tag to match source files (#817315).

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-4
- Add turbojpeg-devel to build requires.
- Install documentation (#817315).
- Correct sourceforge source url (#817315).

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-3
- Removed %%defattr.
- Update to build with gcc 4.7.
- Do not own %%{_datadir}/megaglest as megaglest-data is required.
- Remove comments about pending review requests of build requires.

* Wed May  2 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-2
- Remove no longer required patch to link to openssl and static libircclient.
- Update build requires for miniupnpc rename.

* Sat Apr 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-1
- Initial megaglest spec.
