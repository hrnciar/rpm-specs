%global svnversion 4108

Name:       skychart
Version:    4.3
Release:    2.%{svnversion}svn%{?dist}
Summary:    Planetarium software for the advanced amateur astronomer
License:    GPLv2+
URL:        http://www.ap-i.net/skychart/
# Upstream sources are modified to:
# - Remove pre-built software (iridflare.exe, quicksat.exe, dll files)
# - Remove unneeded Windows and MacOS stuff
# - Remove libraries provided by libpasastro package
#   (they still are in sources only for compiling the Windows version)
# To do this we use the generate-tarball.sh script
# Download upstream tarball in the same directory of the script
# and run:
# ./generate-tarball.sh 4.3-4108
Source0:    %{name}-%{version}-%{svnversion}-src-nopatents.tar.xz
Source1:    generate-tarball.sh
# Source data for skychart-data-stars
Source2:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcvs.tgz
Source3:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_tycho2.tgz
Source4:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_wds.tgz
Source5:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_idx.tgz
# Source data for skychart-data-dso
Source6:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_leda.tgz
Source7:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_barnard.tgz
Source8:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcm.tgz
Source9:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gpn.tgz
Source10:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_lbn.tgz
Source11:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_ocl.tgz
Source12:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_sh2.tgz


# Avoid stripping debuginfo from executables
# This is Fedora specific and not reported upstream
Patch1:     skychart-4.1-nostrip.patch

# Disable wget in install script
# This is Fedora specific and not reported upstream
Patch2:     skychart-4.1-wgetdata.patch

# Notify the user that artificial satellites calculation
# has been disabled in Fedora RPMs due to Fedora policies
# This is Fedora specific and not reported upstream
Patch3:     skychart-4.3-satmessage.patch

# Disable software update menu item
# This feature was asked upstream specifically for Fedora
Patch4:     skychart-4.2-noupdatemenu.patch


ExclusiveArch: %{fpc_arches}
ExcludeArch: ppc64le


BuildRequires: fpc
BuildRequires: lazarus
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: gtk2-devel
BuildRequires: ImageMagick
BuildRequires: libappstream-glib

Requires: libpasastro
Requires: tzdata
Requires: xdg-utils
Requires: xplanet

Recommends: openssl-libs

%description
This program enables you to draw sky charts, making use of the data in 16
catalogs of stars and nebulae. In addition the position of planets,
asteroids and comets are shown.

The purpose of this program is to prepare different sky maps for a
particular observation. A large number of parameters help you to choose
specifically or automatically which catalogs to use, the colour and the
dimension of stars and nebulae, the representation of planets, the display
of labels and coordinate grids, the superposition of pictures, the
condition of visibility and more. All these features make this celestial
atlas more complete than a conventional planetarium.

%package doc
Summary:        Documentation files for Skychart
License:        CC-BY-SA or GFDL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files from the official Skychart wiki provided
within the program as an offline copy.

%package data-stars
Summary:        Additional star catalogs for Skychart
License:        Public Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-stars
Additional star catalogs for Skychart. This package install all the standard
stars catalog down to magnitude 12, variable and double stars:
Tycho 2; General Catalogue of Variable Stars; Washington Double Stars.

%package data-dso
Summary:        Additional Deep Sky Object catalogs for Skychart
License:        Public Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-dso
Additional DSO catalogs for Skychart. This package install all the standard
nebulae catalogs: LEDA Catalogue; Lynds Bright Nebulae; Open Cluster Data;
Globular Clusters in the Milky Way; Galactic Planetary Nebulae;
Barnard Catalogue of Dark Nebulae; Sharpless Catalog.

%prep
%setup0 -q -n %{name}-%{version}-%{svnversion}-src

%patch1 -p1

%patch2 -p1

%patch3 -p1

%patch4 -p1

# Fix executable bit set on sources
find skychart -type f -print0 | xargs -0 chmod -x

# Put additional catalogs files where where required for installation
%{__cp} -p %SOURCE2 ./BaseData
%{__cp} -p %SOURCE3 ./BaseData
%{__cp} -p %SOURCE4 ./BaseData
%{__cp} -p %SOURCE5 ./BaseData
%{__cp} -p %SOURCE6 ./BaseData
%{__cp} -p %SOURCE7 ./BaseData
%{__cp} -p %SOURCE8 ./BaseData
%{__cp} -p %SOURCE9 ./BaseData
%{__cp} -p %SOURCE10 ./BaseData
%{__cp} -p %SOURCE11 ./BaseData
%{__cp} -p %SOURCE12 ./BaseData

# Add directories to fix builds on arm and ppc architectures
declare -a arches=("arm-linux-gtk2" "powerpc-linux-gtk2" "powerpc64-linux-gtk2")
for arch in "${arches[@]}"
do
    %{__mkdir_p} ./skychart/component/lib/$arch
    %{__mkdir_p} ./skychart/units/$arch
    %{__mkdir_p} ./varobs/units/$arch
done



%build
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Skychart doesn't like parallel building so we don't use macro.
# We pass options to fpc compiler for generate debug info.
make fpcopts="-O1 -gw3 -fPIC"

%install
# Install main program
make install PREFIX=%{buildroot}%{_prefix}

# Install catalogs, translations and data files
make install install_data PREFIX=%{buildroot}%{_prefix}

# Install wiki documentation
make install install_doc PREFIX=%{buildroot}%{_prefix}

# Install additional catalogs
make install install_cat1 PREFIX=%{buildroot}%{_prefix}
make install install_cat2 PREFIX=%{buildroot}%{_prefix}


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/skychart.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license skychart/gpl.txt
%doc %{_datadir}/doc/skychart/changelog
%doc %{_datadir}/doc/skychart/copyright
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/*/*/*/%{name}.png
%{_datadir}/icons/*/*/*/%{name}.svg
%dir %{_datadir}/skychart
%{_datadir}/skychart/data
%dir %{_datadir}/skychart/cat
%{_datadir}/skychart/cat/DSoutlines
%{_datadir}/skychart/cat/milkyway
%{_datadir}/skychart/cat/openngc
%{_datadir}/skychart/cat/RealSky
%{_datadir}/skychart/cat/sac
%{_datadir}/skychart/cat/xhip
%dir %{_datadir}/skychart/doc
%{_datadir}/skychart/doc/html_doc
%{_datadir}/skychart/doc/releasenotes*.txt
%{_datadir}/skychart/doc/varobs


%files doc
%doc %{_datadir}/skychart/doc/wiki_doc

%files data-stars
%{_datadir}/skychart/cat/gcvs
%{_datadir}/skychart/cat/tycho2
%{_datadir}/skychart/cat/wds
%{_datadir}/skychart/cat/bsc5
%{_datadir}/metainfo/%{name}-data-stars.metainfo.xml

%files data-dso
%{_datadir}/skychart/cat/leda
%{_datadir}/skychart/cat/lbn
%{_datadir}/skychart/cat/ocl
%{_datadir}/skychart/cat/gcm
%{_datadir}/skychart/cat/gpn
%{_datadir}/skychart/cat/barnard
%{_datadir}/skychart/cat/sh2
%{_datadir}/metainfo/%{name}-data-dso.metainfo.xml

%changelog
* Sat Feb 08 2020 Mattia Verga <mattia.verga@protonmail.com> - 4.3-2.4108svn
- ExcludeArch ppc64le due to compilation errors

* Sat Feb 01 2020 Mattia Verga <mattia.verga@protonmail.com> - 4.3-1.4108svn
- Update to 4.3 svn

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2.4073svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Mattia Verga <mattia.verga@protonmail.com> - 4.2.1-1.4073svn
- Update to stable 4.2.1

* Fri Oct 18 2019 Mattia Verga <mattia.verga@protonmail.com> - 4.2-1.4046svn
- Release stable 4.2

* Thu Aug 29 2019 Mattia Verga <mattia.verga@protonmail.com> - 4.1.1-5.4000svn
- Update svn version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4.3925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Mattia Verga <mattia.verga@protonmail.com> - 4.1.1-3.3925svn
- Update svn version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2.3792svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Mattia Verga <mattia.verga@protonmail.com> - 4.1.1-1.3792svn
- Update svn version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2.3730svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 Mattia Verga <mattia.verga@email.it> - 4.1-1.3730svn
- Upgrade to development version to fix build failures

* Sun Feb 25 2018 Mattia Verga <mattia.verga@email.it> - 4.0-8
- Rebuild for fpc 3.0.4 and lazarus 1.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Mattia Verga <mattia.verga@email.it> - 4.0-4
- Change FPC compiler options to fix debuginfo package build

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Mattia Verga <mattia.verga@tiscali.it> - 4.0-2
- Fix for OpenSSL 1.1

* Sun Mar 19 2017 Mattia Verga <mattia.verga@tiscali.it> - 4.0-1
- Release ver 4.0

* Sun Mar 05 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.11-17.3549svn
- Patch to fix libssl and libcrypto links

* Mon Feb 27 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.11-16.3549svn
- Update svn version

* Sun Feb 12 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.11-15.3287svn
- Set ExcludeArch ppc64 due to lazarus limitations

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-14.3287svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 17 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-13.3287svn
- Update svn version

* Sun Apr 17 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-12.3238svn
- Use new fpc_arches macro as ExclusiveArch

* Sun Apr 17 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-11.3238svn
- Remove additional NGC catalog due to incompatible license

* Mon Feb 15 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-10.3238svn
- Update svn version
- Remove remnants of pre built .dll files in sources
- Remove libraries from sources that are now provided externally
- Patch to inform user about artificial satellites calculation removal
- Patch to set option to disable software update menu item

* Fri Feb 12 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-9.3229svn
- Update svn version
- FSF address in sources is now fixed upstream
- Appdata file is now fixed upstream
- Updated catalog_wds source file from upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-8.3157svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Richard Hughes <richard@hughsie.com> - 3.11-7.3157svn
- Fix the metainfo files by removing zero-width space chars

* Mon Jan 11 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-6.3157svn
- Add .metainfo.xml files to subpackages

* Sun Jan 10 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.11-5.3157svn
- Update svn version
- Libraries are now in separate package libpasastro
- Fix wrong FSF address in source headers
- Fix appdata file validation

* Sun Dec 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.11-4.3141svn
- Properly set ExcludeArch

* Fri Dec 11 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.11-3.3141svn
- Revert back to ExcludeArch

* Fri Nov 27 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.11-2.3141svn
- Set ExclusiveArch to prevent build on arm and s390x

* Sat Nov 14 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.11-1.3141svn
- Update to 3.11svn to fix incompatibility with lazarus 1.4.2

* Sun Jun 21 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.10-7
- Validate appdata file
- Change license file location

* Sat Jun 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 3.10-6
- Added patch to fix build with lazarus 1.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Mattia Verga <mattia.verga@tiscali.it> - 3.10-2
- Fix patch1

* Thu Apr 03 2014 Mattia Verga <mattia.verga@tiscali.it> - 3.10-1
- Update to 3.10
