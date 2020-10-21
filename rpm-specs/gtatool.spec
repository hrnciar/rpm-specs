%global completion_path %(pkg-config --variable=completionsdir bash-completion)

Name:      gtatool
Version:   2.4.0
Release:   3%{?dist}
Summary:   Commandline tool to manipulate GTAs
License:   GPLv3+
URL:       https://marlam.de/gta/
Source0:   https://marlam.de/gta/releases/%{name}-%{version}.tar.xz
#Patch0:    gtatool-2.4.0-pcl-1.11.patch
Patch1:    gtatool-gcc11.patch

BuildRequires: gettext-devel
BuildRequires: bash-completion
BuildRequires: dcmtk-devel
BuildRequires: desktop-file-utils
BuildRequires: gdal-devel
BuildRequires: glew-devel
BuildRequires: ImageMagick-c++-devel
BuildRequires: libgta-devel
BuildRequires: libsndfile-devel
BuildRequires: matio-devel
BuildRequires: muParser-devel
BuildRequires: netcdf-devel
BuildRequires: netpbm-devel
BuildRequires: OpenEXR-devel
BuildRequires: openjpeg-devel
BuildRequires: pcl-devel
BuildRequires: pkgconfig
BuildRequires: pfstools-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libtool automake autoconf
# For gdal tests
BuildRequires: uriparser

# Optional new BRs, when available in Fedora: libgls, libequalizer, libteem
# http://teem.sourceforge.net/
# http://libgls.sourceforge.net/
# https://github.com/Eyescale/Equalizer
# https://bugzilla.redhat.com/show_bug.cgi?id=758472

Requires(post): info
Requires(preun): info

%description
Gtatool is a command line tool to manipulate GTAs.

It provides a set of commands that manipulate GTAs on various levels:
array element components, array dimensions, whole arrays, and streams of arrays.
For example, you can add components to array elements, merge separate arrays
into combined arrays in different ways, apply global transformations to array
data, reorder the array data, and much more.

Additionally, gtatool can import from and export to many other file formats, see
the sub-packages!


%package gui
Summary:        Graphical interface of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gui
This sub-package contains the graphical interface of %{name}.


%package dcmtk
Summary:        Module to import/export via dcmtk
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dcmtk
This sub-package contains the necessary module to import and export
medical image data in DICOM format via dcmtk.


%package gdal
Summary:        Module to import/export via gdal
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gdal
This sub-package contains the necessary module to import and export
remote sensing data via the gdal library.


%package hdr
Summary:        Module to import/export high dynamic range data
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description hdr
This sub-package contains the necessary module to import and export
high dynamic range images or data via OpenEXR and pfstools.


%package imagemagick
Summary:        Module to import/export traditional image formats
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description imagemagick
This sub-package contains the necessary module to import and export
traditional image formats via imagemagick.


%package matlab
Summary:        Module to import/export matlab files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description matlab
This sub-package contains the necessary module to import and export
matlab files via matio.


%package netcdf
Summary:        Module to import/export traditional netcdf files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description netcdf
This sub-package contains the necessary module to import and export
netcdf files, including HDF4 and 5.


%package pcd
Summary:        Module to import/export point cloud data
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description pcd
This sub-package contains the necessary module to import and export
point cloud data via pcl.


%package sndfile
Summary:        Module to import/export sound data
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sndfile
This sub-package contains the necessary module to import and export
sound data via libsndfile.


%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
# Stupid way to avoid overwriting the original LDFLAGS.
# __global_ldflags might do instead
export CFLAGS="%{optflags} -I%{_includedir}/netpbm"
export CXXFLAGS="%{optflags} -I%{_includedir}/netpbm"
export BASHCOMPLETIONDIR="%{completion_path}"

autoreconf -fi

# 1994 ply files are bundled; rply could take over, but the API is different
# pvm uses files from vvv; No package is currently available in Fedora
#TODO: Consider to switch to GraphicsMagick, as that's the default or even supply both
export MOC=%{_libdir}/qt5/bin/moc
%configure LDFLAGS="$LDFLAGS" \
    --with-magick-flavor=ImageMagick \
    --without-ffmpeg \
    --without-ply \
    --without-pvm

make V=1 LDFLAGS="$LDFLAGS $LDFLAGS_ADD" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/gta_gui.desktop

# Remove info directory, created by make install
rm -rf %{buildroot}%{_infodir}/dir

# Completion scripts are loaded on demand from bash-completion 1.99 on


%check
make check

%files 
%doc COPYING AUTHORS README
%{_bindir}/gta
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/component-compute.so
%{_libdir}/%{name}/conv-csv.so
%{_libdir}/%{name}/conv-datraw.so
%{_libdir}/%{name}/conv-jpeg.so
%{_libdir}/%{name}/conv-netpbm.so
%{_libdir}/%{name}/conv-png.so
%{_libdir}/%{name}/conv-rat.so
%{_libdir}/%{name}/conv-raw.so
%{_infodir}/gta.info*
%{_mandir}/man1/gta.1*

%dir %{completion_path}
%{completion_path}/gta

%files gui
%{_libdir}/%{name}/gui.so
%{_datadir}/applications/gta_gui.desktop
%{_datadir}/icons/hicolor/*/*

%files dcmtk
%{_libdir}/%{name}/conv-dcmtk.so

%files gdal
%{_libdir}/%{name}/conv-gdal.so

%files hdr
%{_libdir}/%{name}/conv-pfs.so
%{_libdir}/%{name}/conv-exr.so

%files imagemagick
%{_libdir}/%{name}/conv-magick.so

%files matlab
%{_libdir}/%{name}/conv-mat.so

%files netcdf
%{_libdir}/%{name}/conv-netcdf.so

%files pcd
#%{_libdir}/%{name}/conv-pcd.so

%files sndfile
%{_libdir}/%{name}/conv-sndfile.so


%changelog
* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-3
- Matio rebuild.

* Fri Sep 18 2020 Jeff Law <law@redhat.com> - 2.4.0-2
- Add missing #include for gcc-11

* Sat Aug 15 2020 Volker Froehlich <volker27@gmx.at> - 2.4.0-1
- New upstream release
- Temporarily disable pcl sub-package

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-6
- Rebuild for hdf5 1.10.6

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 2.2.3-5
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 2.2.3-4
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Volker Froehlich <volker27@gmx.at> - 2.2.3-1
- New upstream release
- Patch to allow for pcl 1.9

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-4
- Rebuild for OpenEXR 2.3.0.

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.2.1-3
- Rebuild for netcdf 4.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Volker Froehlich <volker27@gmx.at> - 2.2.1-1
- New upstream release
- Provide moc path in environment, as the discovery is broken
  and failure is not handled gracefully
- New URL

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 2.2.0-15
- Rebuild for new ImageMagick 6.9.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-12
- Remove obsolete scriptlets

* Wed Jan 03 2018 Volker Froehlich <volker27@gmx.at> - 2.2.0-11
- Rebuild for dcmtk

* Mon Oct 02 2017 Volker Froehlich <volker27@gmx.at> - 2.2.0-10
- Apply upstream patches to resolve BZ#1485423
- Add uriparser BR for tests

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 2.2.0-9
- Rebuild for ImageMagick 6 reversion, drop ImageMagick 7 patch

* Fri Aug 25 2017 Michael Cronenworth <mike@cchtml.com> - 2.2.0-8
- Rebuild for new ImageMagick

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Volker Froehlich <volker27@gmx.at> - 2.2.0-6
- Rebuild for imagemagick

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 06 2016 Volker Froehlich <volker27@gmx.at> - 2.2.0-2
- Rebuild for libmatio

* Tue Feb 09 2016 Volker Froehlich <volker27@gmx.at> - 2.2.0-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Volker Froehlich <volker27@gmx.at> - 2.1.0-11
- Rebuild for netcdf

* Sun Jan 17 2016 Volker Froehlich <volker27@gmx.at> - 2.1.0-10
- Rebuild for libGLEWmx

* Sun Aug 30 2015 Volker Froehlich <volker27@gmx.at> - 2.1.0-9
- Version bump required for F23

* Fri Jul 24 2015 Volker Froehlich <volker27@gmx.at> - 2.1.0-8
- Modified to build with pfstools 2.0
- Apply an upstream patch that applies to 64 bit builds

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-6
- Rebuild for hdf5 1.8.15

* Sun Apr 19 2015 Volker Fröhlich <volker27@gmx.at> - 2.1.0-5
- Re-enable the dcmtk sub-package

* Sat Mar 07 2015 Volker Fröhlich <volker27@gmx.at> - 2.1.0-4
- Rebuild for imagemagick 6.9

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- Rebuild for hdf5 1.8.14

* Sun Jan 04 2015 Volker Fröhlich <volker27@gmx.at> - 2.1.0-2
- Re-enable the pcd sub-package

* Thu Dec 18 2014 Volker Fröhlich <volker27@gmx.at> - 2.1.0-1
- New upstream release
- Remove F17 conditionals
- Don't require bash-completion
- Let the build system install the BASH completion file
- Temporarily disable the dcmtk sub-package, due to BZ #922937
- Temporarily disable the pcd sub-package, due to BZ #1177244

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.2-14
- rebuild (openexr)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 01 2014 Volker Fröhlich <volker27@gmx.at> - 1.5.2-11
- Rebuild for imagemagick ABI 16

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.5.2-10
- rebuild (openexr)

* Thu Oct 10 2013 Volker Fröhlich <volker27@gmx.at> - 1.5.2-9
- Rebuild for new Imagemagick++ ABI

* Wed Sep 11 2013 Volker Fröhlich <volker27@gmx.at> - 1.5.2-8
- Patch to allow for pcl 1.7

* Wed Sep 11 2013 Volker Fröhlich <volker27@gmx.at> - 1.5.2-7
- Re-enable pcd sub-package

* Tue Sep 10 2013 Volker Fröhlich <volker27@gmx.at> - 1.5.2-6
- Rebuild for ilmbase 2.0.1

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.5.2-5
- Rebuild for gdal 1.10.0

* Fri Aug 16 2013 Volker Fröhlich <volker27@gmx.at> - 1.5.2-4
- Temporarily disable pcd sub-package, due to broken pcl in Rawhide

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.5.2-2
- Rebuild for hdf5 1.8.11

* Tue Apr 30 2013 Volker Fröhlich <volker27@gmx.at> 1.5.2-1
- New upstream release

* Sat Mar 30 2013 Volker Fröhlich <volker27@gmx.at> 1.5.1-3
- Remove gcc-c++ as BR
- Disable pvm and ply, due to bundle issues
- Put the bash completion script in the proper place for dynamical loading

* Wed Feb 13 2013 Volker Fröhlich <volker27@gmx.at> 1.5.1-2
- pcd sub-package conditional for F17, due to version constraint in pcl

* Sun Feb 10 2013 Volker Fröhlich <volker27@gmx.at> 1.5.1-1
- New upstream release
- Remove now included tex info patch
- Remove now included changes of pcl_config and desktop file
- Own bash_completion.d for the newly introduced completion file

* Fri Feb  1 2013 Volker Fröhlich <volker27@gmx.at> 1.5.0-1
- Initial package for Fedora
