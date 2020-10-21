###
# cmake flag -DRAWSPEED_ENABLE_LTO needs GCC >= 9 and EL8 has GCC 8
%global _use_rawspeed_lto "ON"
%if 0%{?el8}
%global _use_rawspeed_lto "OFF"
%endif
###

###
# To build darktable from Github master branch add cmake flag -DPROJECT_VERSION="%{version}"
# darktable stable releases have src/version_gen.c file that makes
# -DPROJECT_VERSION="%{version}" no longer needed
# src/version_gen.c file is not available in darktable master Github branch instead
###

Name: darktable
Version: 3.2.1
Release: 8%{?dist}

Summary: Utility to organize and develop raw images
License: GPLv3+
URL: http://www.darktable.org/

Source0: https://github.com/darktable-org/darktable/releases/download/release-%{version}/%{name}-%{version}.tar.xz

# https://github.com/darktable-org/darktable/pull/4445
Patch0: appdata-file.patch
# https://github.com/darktable-org/darktable/pull/6380
Patch1: 0001.patch

BuildRequires: cairo-devel
BuildRequires: clang >= 3.9
%if 0%{?el7}
BuildRequires: cmake3 >= 3.10
%else
BuildRequires: cmake >= 3.10
%endif
BuildRequires: colord-gtk-devel
BuildRequires: colord-devel
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
# EPEL7 does not have a recent GCC
%if 0%{?el7}
BuildRequires: devtoolset-7-toolchain
BuildRequires: devtoolset-7-libatomic-devel
%endif
BuildRequires: exiv2-devel >= 0.24
%if (0%{?el7} || 0%{?fedora})
BuildRequires: flickcurl-devel
%endif
BuildRequires: gcc >= 5.0
BuildRequires: GraphicsMagick-devel
BuildRequires: gtk3-devel >= 3.22
BuildRequires: intltool
# iso-codes dependency not mandatory, just optional / recommended
# in future please check if EL7 iso-codes version is >= 3.66
%if 0%{?fedora}
BuildRequires: iso-codes >= 3.66
%endif
BuildRequires: gettext
BuildRequires: json-glib-devel
BuildRequires: lcms2-devel
BuildRequires: lensfun-devel
BuildRequires: libappstream-glib
# libavif is not available in EPEL 8
%if ((0%{?el} > 8) || (0%{?fedora} >= 33))
BuildRequires: cmake(libavif)
%endif
BuildRequires: libcurl-devel >= 7.18.0
BuildRequires: libgphoto2-devel >= 2.4.5
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: librsvg2-devel >= 2.26
BuildRequires: libsecret-devel
BuildRequires: libsoup-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: opencl-headers
BuildRequires: OpenEXR-devel >= 1.6
BuildRequires: openjpeg2-devel
%if (0%{?el7} || 0%{?fedora})
BuildRequires: osm-gps-map-devel >= 1.0
%endif
BuildRequires: perl-interpreter
BuildRequires: perl(FindBin)
# perl-lib contains lib.pm, that was used to be included in perl-interpreter
# but on Fedora >= 33 it has been splitted to perl-lib
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
BuildRequires: perl-lib
%endif
BuildRequires: pkgconfig >= 0.22
BuildRequires: po4a
BuildRequires: /usr/bin/pod2man
BuildRequires: pugixml-devel >= 1.8
BuildRequires: sqlite-devel
BuildRequires: zlib-devel >= 1.2.11

# iso-codes dependency not mandatory, just optional / recommended
# in future please check if EL7 iso-codes version is >= 3.66
%if 0%{?fedora}
Requires: iso-codes >= 3.66
%endif

# Concerning rawspeed bundled library, see
# https://fedorahosted.org/fpc/ticket/550#comment:9
Provides: bundled(rawspeed)
Provides: bundled(lua)

# uses xmmintrin.h
%if (0%{?fedora} || 0%{?el7})
ExclusiveArch: x86_64 aarch64 ppc64le
%endif

# dependency colord-gtk-devel is not availble on EL8 aarch64
%if 0%{?el8}
ExclusiveArch: x86_64 ppc64le
%endif

%description
Darktable is a virtual light-table and darkroom for photographers:
it manages your digital negatives in a database and lets you view them
through a zoom-able light-table.
It also enables you to develop raw images and enhance them.

%package tools-noise
Summary:        The noise profiling tools to support new cameras
Requires:       ImageMagick
Requires:       gnuplot

%description tools-noise
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

%package tools-basecurve
Summary:        The basecurve tool from tools/basecurve/
Requires:       ImageMagick
Requires:       dcraw
Requires:       exiftool

%description tools-basecurve
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

This package provides the basecurve tool from tools/basecurve/.
Another option to solve the same problem might be the darktable-chart module
from the darktable package.

%prep
%autosetup -p1

# Remove bundled OpenCL headers.
rm -rf src/external/CL
sed -i -e 's, \"external/CL/\*\.h\" , ,' src/CMakeLists.txt


%build
%if 0%{?el7}
. /opt/rh/devtoolset-7/enable
mkdir %{_target_platform} 
pushd %{_target_platform}
%cmake3 \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DDONT_USE_INTERNAL_LUA=OFF \
        -DBUILD_NOISE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=ON \
        %ifarch ppc64le
        -DUSE_OPENCL=OFF \
        %endif
        ..
%endif
#
# Germano Massullo: I wanted to use %%elseif but it is not yet active in
# Fedora, etc., despite is supported upstream. I did not compare the Fedora RPM version
# but I empirically verified that %%elseif and %%elif do not work here, even if you don't get
# errors during builds
# https://github.com/rpm-software-management/rpm/issues/311
# https://github.com/debbuild/debbuild/issues/182
# 
#
%if (0%{?el8} || (0%{?fedora} < 33))
mkdir %{_target_platform} 
pushd %{_target_platform}
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DDONT_USE_INTERNAL_LUA=OFF \
        -DBUILD_NOISE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=%{_use_rawspeed_lto} \
        ..
%else
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DDONT_USE_INTERNAL_LUA=OFF \
        -DBUILD_NOISE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=%{_use_rawspeed_lto}
%endif

%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_build
%else
%make_build
popd
%endif


%install
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_install
%else
pushd %{_target_platform}
%make_install
popd
%endif

%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/doc/darktable
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/darktable.appdata.xml

%files -f %{name}.lang 
%license LICENSE
%doc doc/README.md
%{_bindir}/darktable
%{_bindir}/darktable-chart
%{_bindir}/darktable-cli

%{_bindir}/darktable-cltest
%{_bindir}/darktable-cmstest
%{_bindir}/darktable-generate-cache
%{_bindir}/darktable-rs-identify
%{_libdir}/darktable
%{_datadir}/darktable
%{_datadir}/applications/darktable.desktop
%{_datadir}/appdata/darktable.appdata.xml
%{_datadir}/icons/hicolor/*/apps/darktable*
%{_mandir}/man1/darktable*.1*
%{_mandir}/*/man1/darktable*.1*
%{_libexecdir}/darktable/

%files tools-noise
%dir %{_libexecdir}/darktable
%dir %{_libexecdir}/darktable/tools
%{_libexecdir}/darktable/tools/darktable-gen-noiseprofile
%{_libexecdir}/darktable/tools/darktable-noiseprofile
%{_libexecdir}/darktable/tools/profiling-shot.xmp
%{_libexecdir}/darktable/tools/subr.sh

%changelog
* Mon Oct 19 2020 Andreas Schneider <asn@redhat.com> - 3.2.1-8
- Rebuild for libavif 0.8.2

* Sat Oct 03 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-7
- enabled bundled Lua, because darktable does not support Lua 5.4 that is shipped in Fedora and EPEL 8

* Sat Oct 03 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-6
- Added BuildRequires: perl-lib for Fedora > 32 and EL > 8

* Fri Oct 02 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-5
- Fixed Lua macros
- Fixed errors of new cmake macros

* Sat Sep 26 2020 Andreas Schneider <asn@redhat.com> - 3.2.1-4
- Fix build with new cmake macros

* Fri Sep 25 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-3
- resumed OpenMP on ppc64le aarch64
- resumed OpenCL on ppc64le
- added 0001.patch
- removed %%ifnarch ppc64le %%{_bindir}/darktable-cltest

* Fri Sep 25 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-2
- Introduced new cmake macros for Fedora >= 33 and EL >= 9 https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
- Added BuildRequires: perl(FindBin)
- Added BuildRequires: cmake(libavif) for Fedora >= 33 and EL >= 9

* Mon Aug 10 2020 Germano Massullo <germano.massullo@gmail.com> - 3.2.1-1
- 3.2.1 release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Germano Massullo <germano.massullo@gmail.com> - 3.0.2-1
- 3.0.2 release
- Removed 4447-legacy_params.patch

* Sat Apr 04 2020 Germano Massullo <germano.massullo@gmail.com>
- Enabled flickrcurl-devel and osm-gps-map-devel BuildRequires only for EL7 and Fedora
- Removed aarch64 EL8 due missing colord-gtk-devel

* Thu Mar 12 2020 Germano Massullo <germano.massullo@gmail.com> - 3.0.1-2
- removed -DPROJECT_VERSION:STRING="%%{name}-%%{version}-%%{release}" because version is already provided by src/version_gen.c Source: Andreas Schneider
- added %%global _use_rawspeed_lto to enable Rawspeed LTO only for distros that have GCC >= 9
- added 4447-legacy_params.patch

* Mon Mar 09 2020 Germano Massullo <germano.massullo@gmail.com> - 3.0.1-1
- 3.0.1 release
- removed 0001-Add-last-two-releases-to-appdata-file.patch
- added appdata-file.patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Kalev Lember <klember@redhat.com> - 3.0.0-2
- Add last two releases to appdata file

* Tue Dec 24 2019 Germano Massullo <germano.massullo@gmail.com> - 3.0.0-1
- 3.0.0 release

* Mon Dec 02 2019 Germano Massullo <germano.massullo@gmail.com> - 3.0.0~rc2-0.1
- 3.0.0 RC 2
- cmake and cmake3 >= 3.10
- pugixml-devel >= 1.8
- zlib-devel >= 1.2.11

* Thu Nov 14 2019 Germano Massullo <germano.massullo@gmail.com> - 3.0.0~rc1-1
- 3.0.0 RC 1

* Tue Nov 05 2019 Germano Massullo <germano.massullo@gmail.com> - 3.0.0~rc0-1
- 3.0.0 RC 0
- BuildRequires: gtk3-devel >= 3.22

* Wed Oct 23 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.3-2
- Enabled again ppc64le and aarch64 architectures, disabling OpenMP. See https://gcc.gnu.org/bugzilla/show_bug.cgi?id=91920

* Sun Oct 20 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.3-1
- 2.6.3 release
- Enabled again OpenMP

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.2-1
- 2.6.2 release
- Renamed imagemagick to ImageMagick

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 2.6.1-2
- Rebuild for OpenEXR 2.3.0.

* Sun Mar 10 2019 Germano Massullo <germano.massullo@gmail.com> - 2.6.1-1
- 2.6.1 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-3
- rebuild (exiv2)

* Fri Dec 28 2018 Germano Massullo <germano@germanomassullo.org> - 2.6.0-2
- changed cmake and clang minimum version requirement

* Fri Dec 28 2018 Pete Walter <pwalter@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- Enable ppc64le build (#1660807)

* Wed Jul 18 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.4-3
- added noise tools and basecurve tools subpackages

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.4-1
- 2.4.4 release

* Sat Jun 02 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-3
- rebuilt due osm-gps-map update

* Thu May 31 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-2
- rebuilt due osm-gps-map update

* Wed Apr 25 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-1
- 2.4.3 release
- removed noise tools MakeFile because it is now included in regular CMake system

* Thu Apr 19 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.2-2
- forced Requires: iso-codes for Fedora only

* Thu Mar 22 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-7
- 2.4.2 release

* Tue Mar 13 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-6
- added devtoolset for EPEL7 needs

* Thu Mar 08 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-5
- on Fedora: replaced bundled lua with Fedora lua

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.1-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-2
- increased gcc minimum required version

* Mon Jan 22 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-1
- 2.4.1 release
- added iso-codes library requirement
- added .md extension to README file

* Sun Dec 24 2017 Germano Massullo <germano.massullo@gmail.com> - 2.4.0-2
- rebuilt as precaution to have a Fedora release number higher than the 2.4.0.rc0-1, that was entered by mistake

* Sun Dec 24 2017 Germano Massullo <germano.massullo@gmail.com> - 2.4.0-1
- 2.4.0 release

* Mon Dec 11 2017 Germano Massullo <germano.massullo@gmail.com> - 2.4.0.rc1-0.1
- 2.4.0.rc1 release

* Sun Dec 10 2017 Germano Massullo <germano.massullo@gmail.com> - 2.4.0.rc0-0.2
- replaced make %%{?_smp_mflags} with %%make_build
- replaced make install DESTDIR=%%{buildroot} with %%make_install
- fixed previous wrong Fedora release tag (it was 1 instead of 0.1)

* Mon Dec 04 2017 Germano Massullo <germano.massullo@gmail.com> - 2.4.0.rc0-0.1
- 2.4 release candidate 1
- added BuildRequires gcc and clang minimum version requirements
- added BuildRequires: zlib-devel
- enabled osm-gps-map-devel for EPEL7, because version 1.x reached that repository too

* Thu Nov 09 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.5-5
- added cmake3 EPEL7 macro

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.5-2
- de-commented %%{_bindir}/darktable-cltest line

* Mon May 29 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.5-1
- 2.2.5 release

* Wed May 10 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.4-4
- Resumed OpenCL support

* Fri May 05 2017 Jared Smith <jsmith@fedoraproject.org> - 2.2.4-3
- Turn off OpenCL support, as it is causing a segfault on start

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.2.4-2
- rebuild (exiv2)

* Mon Apr 10 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.4-1
- 2.2.4 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- 2.2.3 release

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.2.2-2
- Rebuild (libwebp)

* Sat Jan 28 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.2-1
- 2.2.2 release 

* Mon Jan 02 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-1
- 2.2.1 release

* Fri Dec 23 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.0-1
- 2.2.0 release

* Mon Dec 05 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.0.rc2-0.1
- 2.2.0 RC2

* Fri Nov 25 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.0.rc1-0.1
- 2.2.0 RC1
- Enabled bundled Lua, while discussing the creation of a compat-lua-52 package with Fedora Lua Special Interest Group

* Sun Nov 06 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.0.rc0-0.1
- 2.2.0 release candidate
- Enforced dependencies versions according to 2.2.0 requirements

* Wed Oct 26 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.7-2
- Added rawspeed bundled library details

* Tue Oct 25 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.7-1
- Minor update

* Wed Sep 07 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.6-1
- Minor update

* Tue Jul 05 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.5-1
- Minor update

* Tue May 03 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.4-1
- Minor update

* Mon Apr 25 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.3-3
- Added app-data-validate usage. See https://fedoraproject.org/wiki/Packaging:AppData#app-data-validate_usage

* Sat Apr 02 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.3-2
- Changed %%if 0%%{with_osm_gps_map_devel} to %%if 0%%{?with_osm_gps_map_devel}

* Fri Apr 01 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.3-1
- Minor update

* Mon Mar 07 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.2-1
- Minor update

* Sun Feb 07 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.1-2
- Fixed Openstreetmap support

* Wed Feb 03 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.1-1
- Minor update with a lot of fixes. Further infos at https://github.com/darktable-org/darktable/releases/tag/release-2.0.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Germano Massullo <germano.massullo@gmail.com> - 2.0.0-1
- dartable-generate-nopatents-tarball.sh no longer requires since squid is no longer present in Darktable
- Added %%{_libexecdir}/darktable/ to fix bugreport #1278142
- Added %%{_bindir}/darktable-generate-cache
- Adjusted dependencies to reflect Darktable 2.0 dependencies
- Replaced %%{_datadir}/man/man1/darktable.1.gz and %%{_datadir}/man/man1/darktable-cli.1.gz with %%{_mandir}/man1/darktable*.1.gz and %%{_mandir}/*/man1/darktable*.1.gz
- Sorted BuildRequire list in alphabetical order

* Sat Nov 07 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.9-5
- Removed -DCUSTOM_CFLAGS=ON Please read https://bugzilla.redhat.com/show_bug.cgi?id=1278064#c18

* Sat Nov 07 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.9-4
- Added -DCUSTOM_CFLAGS=ON

* Fri Nov 06 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.9-3
- Removed x86 32 bit CPU support

* Wed Nov 04 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.9-2
- Rework bundled opencl-headers handling in %%prep (RHBZ#1264933).

* Wed Oct 21 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.9-1
- Update to 1.6.9

* Thu Sep 10 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.8-3
- spec file: removed BuildRequires: lua-devel because Darktable supports only LUA 5.2 version

* Tue Sep 08 2015 Kalev Lember <klember@redhat.com> - 1.6.8-2
- Build with system lua
- Remove bundled lua in prep to make sure it's not used

* Tue Sep 08 2015 Kalev Lember <klember@redhat.com> - 1.6.8-1
- Update to 1.6.8
- Modernize spec file for current rpmbuild
- Drop GConf handling now that darktable no longer uses it
- Drop unused build deps
- Build with libsecret support, instead of libgnome-keyring
- Use license macro

* Tue Jul  7 2015 Tom Callaway <spot@fedoraproject.org> - 1.6.7-4
- unbundle opencl headers (and use system opencl headers)

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.6.7-3
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 9 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.7-1
- Corrected Darktable website in spec file
- Minor update

* Thu May 14 2015 Nils Philippsen <nils@redhat.com> - 1.6.6-2
- rebuild for lensfun-0.3.1

* Sun Apr 26 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.6-1
- Minor update. Full changelog at https://github.com/darktable-org/darktable/releases/tag/release-1.6.6

* Sat Apr 4 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.4-1
- Minor update. Full changelog at https://github.com/darktable-org/darktable/releases/tag/release-1.6.4
- Removed patch for Canon EOS Rebel, because the fixed code is in the upstream stable release.

* Wed Mar 18 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.3-2
- Backport of fix for bugreport #1202105

* Mon Mar 02 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.3-1
- Darktable 1.6.3
- Fixed date of Feb 22 2015 changelog.

* Sun Feb 22 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.2-5
- Removed LUA support due missing LUA 5.3 support by Darktable. This will avoid breaking build tree.

* Wed Feb 04 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.2-4
- Removed "Requires: lua-devel"

* Wed Feb 04 2015 Germano Massullo <germano.massullo@gmail.com> - 1.6.2-3
- Added LUA support

* Wed Feb 04 2015 Edouard Bourguignon <madko@linuxed.net> - 1.6.2-2
- Aesthetic changes (useless spaces)
- Use mkdir %%{_target_platform} instead of buildFedora
- Consistence use of %%var instead of $VAR
 
* Mon Feb 02 2015 Edouard Bourguignon <madko@linuxed.net> - 1.6.2-1
- Darktable 1.6.2

* Sun Feb 01 2015 Edouard Bourguignon <madko@linuxed.net> - 1.6.1-1
- Darktable 1.6.1

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.0-2
- Rebuild (libgpohoto2) 

* Tue Dec 09 2014 Edouard Bourguignon <madko@linuxed.net> - 1.6.0-1
- Darktable 1.6.0 stable 

* Sat Dec 06 2014 Edouard Bourguignon <madko@linuxed.net> - 1.5.1-0.2
- Add missing darktable-cmstest

* Sat Dec 06 2014 Edouard Bourguignon <madko@linuxed.net> - 1.5.1-0.1
- Darktable 1.6 rc1

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.2-4
- rebuild (openexr)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4.2-1
- Upgrade to 1.4.2

* Mon Mar  3 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4.1-3
- Remove wrong library path

* Mon Mar  3 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4.1-2
- Restore rpath for internal lib

* Wed Feb 12 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4.1-1
- Upgrade to 1.4.1
- Remove tools source files

* Tue Jan 14 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4-2
- Add OpenJPEG and WebP support
- Add missing buildrequires on pod2man

* Wed Jan  1 2014 Edouard Bourguignon <madko@linuxed.net> - 1.4-1
- Upgrade to 1.4

* Mon Dec  2 2013 Edouard Bourguignon <madko@linuxed.net> - 1.4-0.1.rc1
- Upgrade to 1.4~rc1

* Sun Nov 24 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.3-2
- Add colord-devel support

* Sun Sep 15 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.3-1
- Upgrade to 1.2.3

* Tue Jun 25 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.2-1
- Upgrade to 1.2.2

* Tue Jun 11 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.1-4
- Remove patented code (DXT/squish)

* Mon Jun 10 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.1-3
- Patch to make squish optional

* Mon Jun 10 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.1-2
- fix for CVE-2013-2126 (Thanks to Alex Tutubalin's patch)
- Do not use squish (bug #972604)

* Sun May 26 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2.1-1
- Upgrade to 1.2.1

* Thu May  2 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2-2
- Add profiling sensor and photon noise tools

* Sat Apr  6 2013 Edouard Bourguignon <madko@linuxed.net> - 1.2-1
- Upgrade to 1.2

* Sun Mar 10 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.4-2
- Rebuild

* Sun Mar 10 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.4-1
- Upgrade to 1.1.4

* Fri Feb 22 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.3-2
- Add some missing dependancies

* Mon Feb 11 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.3-1
- Upgrade to 1.1.3

* Fri Feb  1 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.2+26~ge1f2980
- Pre 1.1.3

* Mon Jan 21 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.2-2
- Add missing gtk2-engine dependancy (bug #902288)

* Sat Jan 12 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.2-1
- Upgrade to 1.1.2

* Sun Jan  6 2013 Edouard Bourguignon <madko@linuxed.net> - 1.1.1-2
- Add map mode

* Wed Nov 28 2012 Edouard Bourguignon <madko@linuxed.net> - 1.1.1-1
- Upgrade to 1.1.1 

* Sat Nov 24 2012 Edouard Bourguignon <madko@linuxed.net> - 1.1-1
- Upgrade to 1.1

* Wed Nov 14 2012 Edouard Bourguignon <madko@linuxed.net> - 1.1-0.1.rc2
- Upgrade to 1.1~rc2

* Wed Oct 31 2012 Edouard Bourguignon <madko@linuxed.net> - 1.1-0.1.rc1
- Upgrade to 1.1~rc1

* Thu Jul 26 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0.5-1
- Upgrade to 1.0.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Jindrich Novy <jnovy@redhat.com> - 1.0.4-2
- rebuild because of new libgphoto2

* Sat Jun 30 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0.4-1
- Upgrade to 1.0.4

* Sun Apr 29 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0.3-1
- Upgrade to 1.0.3

* Sat Apr 28 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0.1-1
- Upgrade to 1.0.1

* Thu Mar 15 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-1
- Upgrade to stable 1.0

* Sun Mar 11 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.4.rc2
- Remove pre script

* Sat Mar 10 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.3.rc2
- Patch for uninitialised variables

* Sat Mar 10 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.2.rc2
- Remove useless darktable gconf schemas

* Sat Mar 10 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.1.rc2
- Upgrade to rc2

* Wed Mar  7 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.2.rc1
- Correct invalid type in darktable gconf schemas

* Sun Mar  4 2012 Edouard Bourguignon <madko@linuxed.net> - 1.0-0.1.rc1
- Darktable 1.0 RC1

* Mon Dec  5 2011 Edouard Bourguignon <madko@linuxed.net> - 0.9.3-2
- Add SDL-devel for darktable-viewer

* Mon Nov  7 2011 Edouard Bourguignon <madko@linuxed.net> - 0.9.3-1
- Upgrade to 0.9.3

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.9.2-2
- rebuild (exiv2)

* Fri Aug 26 2011 Edouard Bourguignon <madko@linuxed.net> - 0.9.2-1
- Upgrade to 0.9.2

* Thu Jul 28 2011 Edouard Bourguignon <madko@linuxed.net> - 0.9.1-1
- Upgrade to 0.9.1
- Remove some old patches

* Sat Jul  2 2011 Edouard Bourguignon <madko@linuxed.net> - 0.9-1
- Upgrade to 0.9

* Mon May 23 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-11
- Add a patch for BINARY_PACKAGE_BUILD (preventing march=native)

* Fri Apr 22 2011 Dan Horák <dan[at]danny.cz> - 0.8-10
- make it x86-only

* Fri Apr 22 2011 Dan Horák <dan[at]danny.cz> - 0.8-9
- don't use x86-only compiler flags on non-x86 arches

* Tue Apr 19 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-8
- Change build option

* Mon Apr 11 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.8-7.1
- rebuild (exiv2)

* Wed Mar 30 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-7
- Change cmake options

* Tue Mar 22 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-6
- Keep rpath for internal libs 

* Wed Feb 23 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-5
- Change build options
- Change permission on gconf darktable.schemas
- Add patch and cmake option to remove relative path (thanks to Karl Mikaelsson)

* Sat Feb 19 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-4
- Add missing doc files

* Sat Feb 19 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-3
- Clean up set but unused variables patch for GCC 4.6 (Karl Mikaelsson)

* Thu Feb 17 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-2
- Add flickcurl support
- Add patch to fix unused but set variables

* Tue Feb 15 2011 Edouard Bourguignon <madko@linuxed.net> - 0.8-1
- Upgrade to version 0.8
- Rebuilt using cmake

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Edouard Bourguignon <madko@linuxed.net> - 0.7.1-3
- Change exiv2 headers to use the new umbrella header (#666887)

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.7.1-2
- rebuild (exiv2)

* Tue Dec 14 2010 Edouard Bourguignon <madko@linuxed.net> - 0.7.1-1
- Upgrade to version 0.7.1

* Mon Nov 29 2010 Edouard Bourguignon <madko@linuxed.net> - 0.7-1
- Upgrade to darktable 0.7

* Mon Sep 20 2010 Edouard Bourguignon <madko@linuxed.net> - 0.6-9
- Only use RPM_BUILD_ROOT
- Remove duplicated doc

* Mon Sep 20 2010 Edouard Bourguignon <madko@linuxed.net> - 0.6-8
- Change gegl-devel buildrequires
- Correct with_gegl option
- Correct typo in changelog
- Remove useless configure option (--disable-schemas)
- Add buildrequires on pkgconfig

* Fri Sep 10 2010 Edouard Bourguignon <madko@linuxed.net> - 0.6-7
- Remove useless removal of *.a files
- Change name of desktop patch (no version)

* Tue Aug 31 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.6-6
- disable static lib and schemas
- update desktop database and icon cache
- disable gegl support 

* Mon Aug 30 2010 Edouard Bourguignon <madko@linuxed.net> - 0.6-5
- Upgrade to Darktable 0.6
- Change to tar.gz for source0
- Remove rpath patch
- Add BuildRequires on missing devel packages
- Change path to libdarktable.so
- Add icons
- Make a clean desktop file
- Add desktop file validation

* Mon Aug 23 2010 Edouard Bourguignon <madko@linuxed.net> - 0.5-4
- Use Gconf scriplets to hangle gconf schema
- Add a patch to remove rpath from Dmitrij S. Kryzhevich

* Wed Jul  7 2010 Edouard Bourguignon <madko@linuxed.net> - 0.5-3
- Removing rpath

* Fri Apr 23 2010 Edouard Bourguignon <madko@linuxed.net> - 0.5-2
- Update to 0.5
- Shorten file list
- Use devel packages for building
- Correct URL for Source0

* Tue Feb 02 2010 İbrahim Eser <ibrahimeser@gmx.com.tr> - 0.4-1
- Initial package.
