# Until upstream starts tagging releases properly again, commits are used...
# Picking this commit for https://github.com/enGits/engrid/issues/59
%global commit 0563bcc093884687a087b25f2813d420979dc5b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snap .20170615git%{shortcommit}

Name:           engrid
Version:        2.0.0
Release:        0.35%{?snap}%{?dist}
Summary:        Mesh generation tool

License:        GPLv3+
URL:            http://engits.eu/en/engrid
# wget https://github.com/enGits/engrid/tarball/$commit
Source0:        https://github.com/enGits/engrid/archive/%{commit}/%{name}-%{commit}.tar.gz
# Taken from src/libengrid/resources/icons/G.png and resized to 64x64
Source1:        engrid.png
# - Unbundle netgen
# - Link against netcdf_cxx
# - Link against vtk libraries
# - Don't link against QtNetwork
Patch0:         engrid_build.patch
# Port to Qt5
Patch1:         engrid_qt5.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libXext-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  vtk-devel >= 8.1
BuildRequires:  CGAL-devel
BuildRequires:  tetgen-devel
BuildRequires:  netcdf-cxx-devel
BuildRequires:  libSM-devel
BuildRequires:  tex(latex)
BuildRequires:  texlive-helvetic texlive-ec
BuildRequires:  tex(amsfonts.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(babel.sty)
BuildRequires:  tex(boxedminipage.sty)
BuildRequires:  tex(calc.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(ifthen.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(layouts.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(setspace.sty)
BuildRequires:  tex(titlesec.sty)
BuildRequires:  tex(ucs.sty)
BuildRequires:  tex(xspace.sty)
BuildRequires:  tex(german.ldf)

Requires:       hicolor-icon-theme

%description
enGrid is an open-source mesh generation software with CFD applications in mind.
enGrid uses the Netgen library for tetrahedral grid generation and an in-house
development for prismatic boundary layer grids. Internally, enGrid uses the VTK
data structures as well as the *.vtu file format.


%package devel
Summary:        Development files for enGrid
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use enGrid.


%package doc
Summary:        Documentation and Tutorials for enGrid
BuildArch:      noarch
Obsoletes:      %{name}-blender < 1.4.0-6
Provides:       %{name}-blender = %{version}-%{release}

%description doc
This package contains the documentation and tutorials for enGrid.


%prep
%autosetup -p1 -n engrid-%{commit}

# Unbundle tetgen
rm -rf src/tetgen

# Fix bad permissions
chmod -x src/libengrid/egvtkinteractorstyle.h
chmod -x src/libengrid/egvtkinteractorstyle.cpp
chmod -x src/libengrid/createvolumemesh.cpp


%build
# Build application
pushd src
%cmake -DGIT_SHA1=%{commit} .
%cmake_build
popd

# Build documentation
pushd manual
pdflatex main.tex
mv main.pdf manual.pdf
popd


%install
pushd src
%cmake_install
popd

# Remove useless script
rm %{buildroot}%{_bindir}/%{name}.bash

# Desktop file, icon
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --set-icon=engrid \
  --add-category=Science \
  --remove-category=Education \
  engrid.desktop
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/engrid.png

# Manpage
install -Dpm 0644 debian/engrid.1 %{buildroot}%{_mandir}/man1/engrid.1


%ldconfig_scriptlets

%files
%license licence.txt gpl.txt
%{_bindir}/engrid
%{_datadir}/applications/engrid.desktop
%{_datadir}/icons/hicolor/64x64/apps/engrid.png
%{_libdir}/liblibengrid.so.*
%{_mandir}/man1/engrid.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/liblibengrid.so


%files doc
%doc tutorials manual/manual.pdf src/blender_scripts
%license fdl-1.3.txt


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.35.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.34.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.33.20170615git0563bcc
- Rebuild (CGAL)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.32.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.0.0-0.31.20170615git0563bcc
- Rebuild for vtk 8.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.30.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.29.20170615git0563bcc
- Rebuild against vtk-8.1
- Port to Qt5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.28.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.27.20170615git0563bcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-0.26.20170615git0563bcc
- Remove obsolete scriptlets

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 2.0.0-0.25.20170615git0563bcc
- Rebuilt for jsoncpp.so.20

* Thu Sep 07 2017 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.24.20170615git0563bcc
- Update to latest git

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 2.0.0-0.23.20151218gitd81ae48
- Rebuilt for jsoncpp-1.8.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.22.20151218gitd81ae48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.21.20151218gitd81ae48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-0.20.20151218gitd81ae48
- Rebuilt for new CGAL

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.19.20151218gitd81ae48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.18.20151218gitd81ae48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-0.17.20151218gitd81ae48
- Update to new snapshot

* Mon Oct 17 2016 Björn Esser <fedora@besser82.io> - 2.0.0-0.16.gitbaef0ce
- Re-rebuilt for libjsoncpp.so.11

* Thu Oct 06 2016 Björn Esser <fedora@besser82.io> - 2.0.0-0.15.gitbaef0ce
- Re-rebuilt for libCGAL.so.12

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 2.0.0-0.14.gitbaef0ce
- Rebuilt for libjsoncpp.so.11

* Wed Sep 21 2016 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.13.gitbaef0ce
- Rebuild (CGAL)

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 2.0.0-0.12.gitbaef0ce
- Rebuilt for libjsoncpp.so.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.11.gitbaef0ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-0.10.gitbaef0ce
- Rebuild for hdf5 1.8.16

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-0.9.gitbaef0ce
- Rebuilt for Boost 1.60

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-0.8.gitbaef0ce
- Add patch for VTK 6.3 support

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-0.7.gitbaef0ce
- Rebuilt for Boost 1.59

* Fri Jul 31 2015 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.6.gitbaef0ce
- Rebuild (boost)

* Fri Jul 24 2015 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.5.gitbaef0ce
- Rebuild (boost)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.4.gitbaef0ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.3.gitbaef0ce
- Rebuild (hdf5)

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.0-0.2.gitbaef0ce
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.1.gitbaef0ce
- Update to latest git
- Remove blender subpackage and ship them in -doc, they are out of date anyway

* Tue Oct 07 2014 Sandro Mani <manisandro@gmail.com> - 1.4.0-5.gite6d55f5
- Rebuild (netgen-mesher)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4.gite6d55f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Sandro Mani <manisandro@gmail.com> - 1.4.0-3.gite6d55f5
- Install manpage
- Fix spurious executable permissions

* Wed Jul 30 2014 Sandro Mani <manisandro@gmail.com> - 1.4.0-2.gite6d55f5
- Don't rename license file
- Use desktop-file-install to set icon and fix category
- Add doc subpackage
- Add blender subpackage
- Update build patch to also link against vtk libraries, and not QtNetwork

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 1.4.0-1.gite6d55f5
- Initial package
