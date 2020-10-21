# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

# enable special maintainer debug build ?
%bcond_with	debug
%if %{with debug}
%global		config			debug
%global		dbg			_dbg
%else
%global		config			release
%global		dbg			%{nil}
%endif

%bcond_with	system_mozjs38

# Remember to rerun licensecheck after every update:
#	https://bugzilla.redhat.com/show_bug.cgi?id=818401#c46
#	http://trac.wildfiregames.com/ticket/1682

%bcond_without	system_nvtt
%bcond_without	nvtt

# Exclude private libraries from autogenerated provides and requires
%global __provides_exclude_from ^%{_libdir}/0ad/
%global __requires_exclude ^(libAtlasUI.*\.so|libCollada.*\.so|libmozjs38.*\.so)

Name:		0ad
Version:	0.0.23b
Release:	21%{?dist}
# BSD License:
#	build/premake/*
#	libraries/source/miniupnpc/*		(not built/used)
#	libraries/source/valgrind/*		(not built/used)
# MIT License:
#	libraries/source/fcollada/*
#	libraries/source/nvtt/*			(not built/used)
#	source/third_party/*
# LGPLv2+
#	libraries/source/cxxtest*/*		(not built/used)
# GPLv2+
#	source/*
# IBM
#	source/tools/fontbuilder2/Packer.py
# MPL-2.0
#	libraries/source/spidermonkey/*		(not built/used)
License:	GPLv2+ and BSD and MIT and IBM
Summary:	Cross-Platform RTS Game of Ancient Warfare
Url:		http://play0ad.com

%if ! %{with nvtt}
# wget http://releases.wildfiregames.com/%%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jxf %%{name}-%%{version}-alpha-unix-build.tar.xz
# rm -fr %%{name}-%%{version}-alpha/libraries/nvtt
# rm -f %%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jcf %%{name}-%%{version}-alpha-unix-build.tar.xz %%{name}-%%{version}-alpha
Source0:	%{name}-%{version}-alpha-unix-build.tar.xz
%else
Source0:	http://releases.wildfiregames.com/%{name}-%{version}-alpha-unix-build.tar.xz
%endif

# Simplify checking differences when updating the package
# (also to validate one did not forget to remake the tarball if
# %{without_nvtt} is enabled) Create it with:
# cd BUILD/%%{name}-%%{version}-alpha
# licensecheck -r . | sort > ../../SOURCES/%%{name}-licensecheck.txt
Source1:	%{name}-licensecheck.txt

# adapted from binaries/system/readme.txt
# It is advisable to review this file at on newer versions, to update the
# version field and check for extra options. Note that windows specific,
# and disabled options were not added to the manual page.
Source2:	%{name}.6

Requires:	%{name}-data = %{version}
Requires:	hicolor-icon-theme

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	enet-devel
BuildRequires:	gamin-devel
BuildRequires:	gcc-c++
BuildRequires:	gloox-devel
BuildRequires:	libcurl-devel
BuildRequires:	libdnet-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzip-devel
BuildRequires:	miniupnpc-devel
BuildRequires:  libsodium-devel
%if %{with system_nvtt}
BuildRequires:	nvidia-texture-tools-devel
%endif
BuildRequires:	openal-soft-devel
BuildRequires:	openjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	python2
BuildRequires:	SDL2-devel
BuildRequires:	subversion
BuildRequires:	valgrind-devel
BuildRequires:	wxGTK3-devel
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/python

%if %{without system_mozjs38}
# bundled mozjs
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	readline-devel
BuildRequires:	/usr/bin/zip
%endif

# bundled mozjs: For build time tests only
BuildRequires:	python-devel
BuildRequires:	perl-devel

ExclusiveArch:	%{ix86} x86_64 %{arm} aarch64 ppc64le

%if %{without system_mozjs38}
Provides: bundled(mozjs) = 38
%endif

# Only do fcollada debug build with enabling debug maintainer mode
# It also prevents assumption there that it is building in x86
Patch1:		%{name}-debug.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1141464
Patch3:		%{name}-valgrind.patch

# Fix build on ppc64le with patches from https://wiki.raptorcs.com/wiki/Porting/0ad
Patch5:     %{name}-ppc64.patch

# Due to significant reports matching:
# https://trac.wildfiregames.com/ticket/4053
# [[PATCH] Building spidermonkey on GCC 6 results in segfaults in the Garbage Collector]
# Basically reinstantiate:
# https://src.fedoraproject.org/rpms/mozjs38/c/761399aba092bcb1299bb4fccfd60f370ab4216e
Patch6:		%{name}-mozjs38.patch

# Possibly a gcc 10 or binutils 2.34 ld bug. Likely there is an explanation,
# but could not create a simple reproducer.
# Workaround was a single template declaration/definition by defining the
# template in the header file with the class declaration.
# https://bugzilla.redhat.com/show_bug.cgi?id=1799112
Patch7:		%{name}-fcollada.patch

# Workaround for Ryzen 3000 CPU support
# https://bugzilla.redhat.com/show_bug.cgi?id=1822835
# https://trac.wildfiregames.com/changeset/23262
Patch8:		0ad-ryzen-3000.patch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer,
hobbyist game developers, since 2001.

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-alpha
%if ! %{with debug}
# disable debug build, and "int 0x3" to trap to debugger (x86 only)
%patch1 -p0
%endif
%patch3 -p1
%patch5 -p1
%patch6 -p1
# Related to 0ad-mozjs38.patch
%ifarch %{ix86}
sed -i "s/\(-fno-delete-null-pointer-checks\)/\1 -O0/" \
    libraries/source/spidermonkey/build.sh
%endif
#end Related to 0ad-mozjs38.patch

%patch7 -p1
%patch8 -p1

%if %{with system_nvtt}
rm -fr libraries/source/nvtt
%endif

rm -fr libraries/source/valgrind

#-----------------------------------------------------------------------
%build
# This package appears to get a multiply defined symbol during the LTO
# link, but only on i686.  Disable LTO on that platform for now
%ifarch i686
%define _lto_cflags %{nil}
%endif

export CFLAGS="%{optflags}"
# avoid warnings with gcc 4.7 due to _FORTIFY_SOURCE in CPPFLAGS
export CPPFLAGS="`echo %{optflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//'`"
build/workspaces/update-workspaces.sh	\
    --bindir=%{_bindir}			\
    --datadir=%{_datadir}/%{name}	\
    --libdir=%{_libdir}/%{name}		\
%if %{with system_mozjs38}
    --with-system-mozjs38		\
%endif
%if %{with system_nvtt}
    --with-system-nvtt			\
%endif
%if ! %{with nvtt}
    --without-nvtt			\
%endif
    %{?_smp_mflags}

make %{?_smp_mflags} -C build/workspaces/gcc config=%{config} verbose=1

#-----------------------------------------------------------------------
%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 build/resources/0ad.sh %{buildroot}%{_bindir}/0ad
install -p -m 755 binaries/system/pyrogenesis%{dbg} %{buildroot}%{_bindir}/pyrogenesis%{dbg}

install -d -m 755 %{buildroot}%{_libdir}/%{name}
for name in AtlasUI%{dbg} Collada%{dbg}; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done

%if %{with nvtt} && ! %{with system_nvtt}
for name in nvcore nvimage nvmath nvtt; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done
%endif

%if %{without system_mozjs38}
%if %{with debug}
name=mozjs38-ps-debug
%else
name=mozjs38-ps-release
%endif
install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
%endif

install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 build/resources/0ad.appdata.xml %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/0ad.desktop

install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 build/resources/0ad.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/0ad.png

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a binaries/data/* %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man6/%{name}.6
ln -sf %{name}.6 %{buildroot}%{_mandir}/man6/pyrogenesis.6

%if %{with debug}
export STRIP=/bin/true
%endif

#-----------------------------------------------------------------------
%check
# Depends on availablity of nvtt
%ifnarch aarch64 ppc64le
%if %{with nvtt}
LD_LIBRARY_PATH=binaries/system binaries/system/test%{dbg} -libdir binaries/system
%endif
%endif

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/0ad.desktop

#-----------------------------------------------------------------------
%files
%doc README.txt
%license LICENSE.txt
%license license_gpl-2.0.txt license_lgpl-2.1.txt license_mit.txt
%{_bindir}/0ad
%{_bindir}/pyrogenesis%{dbg}
%{_libdir}/0ad/
%{_datadir}/0ad/
%{_datadir}/applications/0ad.desktop
%{_datadir}/icons/hicolor/128x128/apps/0ad.png
%{_datadir}/metainfo/0ad.appdata.xml
%{_mandir}/man6/*.6*

%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.0.23b-20
- Disable LTO on i686 for now

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Björn Esser <besser82@fedoraproject.org> - 0.0.23b-18
- Rebuilt for Boost 1.73 again

* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 0.0.23b-17
- Rebuild (gloox)

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.0.23b-16
- Rebuilt for Boost 1.73

* Sat May 23 2020 Kalev Lember <klember@redhat.com> - 0.0.23b-15
- Backport workaround for Ryzen 3000 CPU support (#1822835)

* Sun May 17 2020 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-14
- Rebuild for ICU 67

* Tue Mar 31 2020 <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.23b-13
- Fix Fedora 32 FTBFS (#1799112)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-11
- Rebuild for ICU 65

* Mon Sep 30 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.23b-10
- Add build conditional for system mozjs38

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-9
- Correctly install bundled mozjs38 (#1751250)
- Exclude private libraries from autogenerated provides and requires

* Tue Aug 13 2019 dftxbs3e <dftxbs3e@free.fr> - 0.0.23b-8
- Fix build on ppc64le

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-6
- Rebuilt for miniupnpc soname bump

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-5
- Correctly set RPATH for private libraries
- Install the icon to the hicolor icon theme
- Move the appdata file to metainfo directory
- Validate the appdata file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.0.23b-3
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-2
- Rebuild for ICU 63

* Thu Dec 27 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-1
- Update to 0.0.23b

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.23-2
- Rebuild for ICU 62

* Thu May 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.23-1
- Update to 0.0.23

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.22-8
- Rebuild for ICU 61.1

* Wed Mar 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.22-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.0.22-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 0.0.22-4
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.0.22-3
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.22-1
- Update to 0.0.22

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-5
- Patched for new GCC and rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-3
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-2
- Rebuilt for Boost 1.63

* Wed Nov 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.21-1
- Update to 0.0.21

* Fri Jun 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.20-4
- Rebuild for miniupnpc 2.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.0.20-3
- rebuild for ICU 57.1

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.20-2
- Upstream now supports aarch64 (tests currently fail)

* Sat Apr 02 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.0.20-1
- Update to 0.0.20

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.0.19-2
- Rebuilt for Boost 1.60

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19
- 0.0.19

* Sun Nov 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19-0.1.rc2
- 0.0.19-rc2

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.0.18-8
- rebuild for ICU 56.1

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.0.18-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.0.18-5
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.18-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.18-2
- Use bcond for rpm conditional macros
- Add rpm conditional to build with sdl2

* Sat Mar 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.18-1
- Update to latest upstream release
- Change to -p0 patches

* Thu Feb 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.17-3
- Rebuild for gloox 1.0.13

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.0.17-2
- Rebuild for boost 1.57.0

* Sun Oct 12 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.17-1
- Update to latest upstream release
- Remove no longer needed miniupnpc patch
- Remove backport changeset_15334 patch

* Sun Sep 14 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-11
- Remove unused valgrind sources and use system valgrind.h (#1141464)

* Thu Aug 28 2014 David Tardon <dtardon@redhat.com> - 0.0.16-10
- rebuild for ICU 53.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-7
- Rebuild for latest gloox

* Wed Jun 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-6
- Add proper patch for gcc 4.9 build

* Fri Jun  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.16-5
- Remove old Fedora release conditionals

* Fri Jun 06 2014 Dennis Gilmore <dennis@ausil.us> - 0.0.16-4
- add %%{arm} tp the ExclusiveArch list

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.0.16-2
- Rebuild for boost 1.55.0

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.16-1
- Update to latest upstream release

* Mon May  5 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-5
- Rebuild for newer enet

* Fri Apr 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-4
- Add workaround for %%check failure with gcc 4.9 on i686

* Fri Apr 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-3
- Rebuild with minupnpc 1.9

* Tue Jan 21 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-2
- Rebuild for latest gloox

* Fri Dec 27 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-1
- Update to latest upstream release
- Add new gloox and minupnpc build requires
- Use 0ad.appdata.xml from upstream tarball

* Sat Oct 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.14-2
- Install appdata file (#1018385)

* Thu Sep  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.14-1
- Update to latest upstream release

* Wed Aug  7 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-8
- Make package x86_64 and ix86 only as arm support is not finished.

* Wed Aug  7 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-7
- Correct build with boost 1.54.0 (#991906).

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.0.13-5
- Rebuild for boost 1.54.0

* Thu Jun 27 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-4
- Rebuild for enet soname change

* Sat Jun 15 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-3
- Rebuild for enet 1.3.8 soname bump

* Sat Apr 27 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-2
- Rebuild for enet 1.3.7 soname bump

* Wed Apr 3 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-1
- Update to latest upstream release
- Update the manual page for new and renamed options
- Regenerate the licensecheck text file and patches

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.0.12-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.0.12-4
- Rebuild for Boost-1.53.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.0.12-3
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-2
- Enable build with system nvtt as it is now approved in Fedora (#823096)
- Correct release date in manual page
- Minor consistency correction in manual page formatting
- Regenerate the licensecheck text file to match pristine tarball

* Tue Dec 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-1
- Update to latest upstream release
- Remove no longer required gamin patch
- Rediff rpath patch
- Remove libxml2 patch already applied upstream
- Update 0ad manpage for newer options and release information
- Add versioned requires to data files
- Add 0ad licensecheck text file to simplify checking changes

* Sat Nov 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-4
- Add %%with_debug maintainer mode build
- Disable fcollada debug build if %%with_debug is false
- Add patch to not crash and display helful messages in editor (#872801)

* Tue Sep 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-3
- Clarify source tree licenses information in spec (#818401)
- Preserve time stamp of installed files (#818401)

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Correct manpage group and symlink 0ad manual to pyrogenesis manual (#818401)
- Correct some typos and wrong information in 0ad.6

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release
- Switch to new versioning pattern
- Remove rpath patch already applied upstream
- Remove without-nvtt patch already applied upstream
- Remove boost patch already applied upstream
- Remake rpath patch to avoid package build special conditions

* Thu Sep 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-6
- Repackage tarball to not redistribute patented s3tc implementation (#818401)
- Add patch to rebuild with newer libxml2.
- Add upstream trac patch for build with newer boost.
- Rename patches to remove %%version and use %%name in source files.

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-5
- Clearly state nvtt is not mean't to be used (unless user build from sources).
- Update to use patch in wildfire trac instead of my patch to remove rpath.

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Actually remove %%defattr.
- Correct wrong fedora release check for enet-devel build requires.

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Make package build in Fedora 16 (rpmfusion #2342).
- Add conditionals to build with or without system nvtt or disable nvtt.

* Tue May 22 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-3
- Remove %%defattr from spec (#823096).
- Run desktop-file-validate (#823096).

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-2
- Disable dependency on nvidia-texture-tools (#823096).
- Disable %%check as it requires nvtt.
- Add manual page.

* Sat May 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-1
- Correct package license.
- Update to latest upstream release.
- Remove license_dbghelp.txt as dbghelp.dll is not in sources neither installed.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11339-1
- Initial 0ad spec.
