%global revision 164

Name: virtualplanet
Version: 2.5
Release: 9.%{revision}svn%{?dist}
Summary: An atlas for planets surface formations
# Some component of glscene used by virtualplanet are licensed MPLv1.1 only
License: GPLv3+ and MPLv1.1
URL: http://www.ap-i.net/avp/
# Virtual Planetary Atlas source contains Mac and Windows stuff
# so we use a script to remove that before importing in Fedora.
# Use this script to download svn version and clean it up:
# ./generate-tarball.sh 2.0 164
Source0: %{name}-%{version}-src-%{revision}-nopatents.tar.xz
Source1: generate-tarball.sh
# Base data
Source2: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_JPLeph.tgz
Source3: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Overlay.tgz
# Base textures
Source4: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Callisto.tgz
Source5: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Europa.tgz
Source6: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Ganymede.tgz
Source7: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Io.tgz
Source8: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Jupiter.tgz
Source9: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Mars.tgz
Source10: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Mercury.tgz
Source11: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Venus.tgz
# Historical textures
Source12: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Callisto_Historical.tgz
Source13: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Europa_Historical.tgz
Source14: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Ganymede_Historical.tgz
Source15: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Io_Historical.tgz
Source16: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Jupiter_Historical.tgz
Source17: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Mars_Historical.tgz
Source18: http://sourceforge.net/projects/%{name}/files/9-Source_Data/VPA_Base_Texture_Mercury_Historical.tgz


# Virtualplanet doesn't support set FPC options from command line
# This patch changes options in Makefiles to avoid stripping
# executables and to enable debug info
# Fedora specific, not reported upstream
Patch1:         vpa-2.5-fix_debuginfo.patch

# Virtualplanet use wget to download source data
# We disable that and use source files
# Fedora specific, not reported upstream
Patch2:         virtualplanet-wgetdata.patch

# Appdata files are present in sources but not installed
Patch99:        vpa-2.5-appdata.patch


ExclusiveArch: %{fpc_arches}
# virtualplanet cannot be built on these arches due to incompatibile GLScene component
ExcludeArch:    ppc64le %{arm} aarch64


BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gtk2-devel
BuildRequires:  fpc
BuildRequires:  lazarus >= 1.6.4
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xxf86vm)

Requires:       %{name}-data-base = %{version}-%{release}
# Virtualplanet requires libpasastro to function properly
# but rpm doesn't find this autorequire
Requires:       libpasastro%{?_isa}


%description
Virtual Planets Atlas displays surface information for planets
Jupiter, Mars, Venus and Mercury and for the major moons
of Jupiter.

It is based on the interface of well known Virtual Moon Atlas

%package doc
Summary:        Documentation files for Virtual Planets Atlas
License:        GFDL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for Virtual Planets Atlas

%package data-base
Summary:        Base data for Virtual Planets Atlas
License:        Public Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-base
Base data for Virtual Planets Atlas. It includes base textures, 
database and overlays

%package data-historical
Summary:        Historical textures for Virtual Planets Atlas
License:        Public Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-historical
Historical addon textures for Virtual Planets Atlas

%prep
%autosetup -p1 -n %{name}-%{version}-src


%build
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Virtualplanet doesn't like parallel building so we don't use macro.
# Some components support passing options to fpc compiler 
# to generate debug info.
make fpcopts="-O1 -gw3 -fPIC"

# Put additional catalogs files where required for installation
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
%{__cp} -p %SOURCE13 ./BaseData
%{__cp} -p %SOURCE14 ./BaseData
%{__cp} -p %SOURCE15 ./BaseData
%{__cp} -p %SOURCE16 ./BaseData
%{__cp} -p %SOURCE17 ./BaseData
%{__cp} -p %SOURCE18 ./BaseData


%install
# Install main program
make install PREFIX=%{buildroot}%{_prefix}

# Install data files
make install install_data PREFIX=%{buildroot}%{_prefix}
make install install_data2 PREFIX=%{buildroot}%{_prefix}

# For now we don't provide extra textures
# because they're over 1GB of data
#make install install_data3 PREFIX=%%{buildroot}%%{_prefix}


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/virtualplanet.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license gpl-3.0.txt LICENSE
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/*/*/*/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/language/

%files doc
%license doc/fdl-1.3.txt doc/LICENSE
%doc %{_datadir}/%{name}/doc/

%files data-base
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/Database/
%{_datadir}/%{name}/Overlay/
%{_datadir}/%{name}/Textures/
%exclude %{_datadir}/%{name}/Textures/*/Historical/

%files data-historical
%{_datadir}/%{name}/Textures/*/Historical/
%{_datadir}/metainfo/%{name}-data-historical.metainfo.xml


%changelog
* Sat Feb 01 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.5-9.164svn
- Add libxxf86vm to BR
- Disable arm, aarch64 and ppc64le

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8.164svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7.164svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6.164svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5.164svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 Mattia Verga <mattia.verga@email.it> - 2.5-4.164svn
- Rebuild for fpc 3.0.4 and lazarus 1.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3.164svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-2.164svn
- Remove obsolete scriptlets

* Fri Dec 08 2017 Mattia Verga <mattia.verga@email.it> - 2.5-1.164svn
- Update to development version rev164
- Exclude arm architectures due to component not compatible with arm

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Mattia Verga <mattia.verga@tiscali.it> - 2.0-5
- Change FPC compiler options to fix debuginfo package build
- Change metainfo.xml files location

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Mattia Verga <mattia.verga@tiscali.it> - 2.0-3
- Set ExcludeArch ppc64 due to lazarus limitations

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Mattia Verga <mattia.verga@tiscali.it> - 2.0-1
- Upgrade to stable 2.0
- Add appdata files

* Sat Mar 12 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-7.20160119svn99
- Fix directories ownership
- Add update-desktop-database scripts
- Use ExclusiveArch instead of ExcludeArch
- Correct license to reflect some components only MPLv1.1

* Fri Jan 22 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-6.20160119svn99
- Update svn revision to fix ARM build
- Moved tests into %%check
- Added architecture to libpasastro dependency

* Sun Dec 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-5.20151220svn
- Properly set ExcludeArch

* Sun Dec 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-4.20151220svn
- Libraries are now in separate package libpasastro

* Sat Dec 19 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-3.20151217svn
- Add mesa-libGLU-devel to buildrequire

* Thu Dec 17 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-2.20151217svn
- Update svn version
- Add license to main package and to documentation
- Fix building library with optflags scriptlets

* Fri Dec 04 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-1
- Initial release
