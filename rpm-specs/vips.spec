%global vips_version_base 8.10
%global vips_version %{vips_version_base}.2
%global vips_soname_major 42

Name:		vips
Version:	%{vips_version}
Release:	1%{?dist}
Summary:	C/C++ library for processing large images

License:	LGPLv2+
URL:		https://libvips.github.io/libvips/
Source0:	https://github.com/libvips/libvips/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(MagickWand)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(imagequant)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(matio)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(openslide)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(poppler-glib)

BuildRequires:	giflib-devel
BuildRequires:	nifticlib-devel

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig gettext
BuildRequires:	python3-devel
BuildRequires:	gtk-doc
BuildRequires:	/usr/bin/pathfix.py


%description
VIPS is an image processing library. It is good for very large images
(even larger than the amount of RAM in your machine), and for working
with color.

This package should be installed if you want to use a program compiled
against VIPS.


%package devel
Summary:	Development files for %{name}
Requires:	libjpeg-devel%{?_isa} libtiff-devel%{?_isa} zlib-devel%{?_isa}
Requires:	vips%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and
libraries necessary for developing programs using VIPS. It also
contains a C++ API and development documentation.


%package tools
Summary:	Command-line tools for %{name}
Requires:	vips%{?_isa} = %{version}-%{release}
Requires:	python3-cairo

%description tools
The %{name}-tools package contains command-line tools for working with VIPS.


%package doc
Summary:	Documentation for %{name}
Conflicts:	%{name} < %{version}-%{release}, %{name} > %{version}-%{release}

%description doc
The %{name}-doc package contains extensive documentation about VIPS in both
HTML and PDF formats.


%prep
%setup -q

# Avoid setting RPATH to /usr/lib64 on 64-bit builds
# The DIE_RPATH_DIE trick breaks the build wrt gobject-introspection
sed -i 's|sys_lib_dlsearch_path_spec="|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir} |' configure

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" tools/vipsprofile


%build
# Upstream recommends enabling auto-vectorization of inner loops:
# https://github.com/libvips/libvips/pull/212#issuecomment-68177930
export CFLAGS="%{optflags} -ftree-vectorize"
export CXXFLAGS="%{optflags} -ftree-vectorize"
# Disable orc on F31 for https://bugzilla.redhat.com/1780443
%configure --disable-static --enable-gtk-doc %{?fc31:--without-orc}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT \( -name '*.la' -o -name '*.a' \) -exec rm -f {} ';'

# delete doc (we will get it later with %%doc)
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/vips

# locale stuff
%find_lang vips%{vips_version_base}


%files -f vips%{vips_version_base}.lang
%doc AUTHORS NEWS THANKS README.md ChangeLog
%license COPYING
%{_libdir}/*.so.%{vips_soname_major}*
%{_libdir}/girepository-1.0


%files devel
%{_includedir}/vips
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0
%{_datadir}/gtk-doc


%files tools
%{_bindir}/vips-%{vips_version_base}
%{_bindir}/*
%{_mandir}/man1/*


%files doc
%doc doc/html
%license COPYING


%changelog
* Mon Oct 12 2020 Benjamin Gilbert <bgilbert@backtick.net> - 8.10.2-1
- New release

* Sun Oct 11 2020 Benjamin Gilbert <bgilbert@backtick.net> - 8.10.1-1
- New release

* Sun Oct 11 2020 Benjamin Gilbert <bgilbert@backtick.net> - 8.9.2-1
- New release
- Fix docs build with gobject-introspection 1.66

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 8.9.1-2
- Rebuild for hdf5 1.10.6

* Wed Apr  8 2020 Adam Goode <adam@spicenitz.org> - 8.9.1-1
- New release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 8.8.4-3
- Rebuild for poppler-0.84.0

* Sun Dec 08 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.8.4-2
- Disable orc on Fedora 31 for RHBZ 1780443

* Thu Dec 05 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.8.4-1
- New release

* Sat Sep 21 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.8.3-1
- New release

* Sun Sep 01 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.8.2-2
- Add python3-cairo dependency for vipsprofile

* Sun Sep 01 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.8.2-1
- New release
- Drop libvipsCC.so and python3-vips subpackage, both removed upstream
- Fix vipsprofile shebang to point to python3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.7.4-5
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 8.7.4-3
- Rebuild for OpenEXR 2.3.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.4-1
- New release

* Tue Jan 08 2019 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.3-1
- New release

* Sat Dec 08 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.2-1
- New release

* Sat Nov 17 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.1-1
- New release

* Thu Oct 04 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.7.0-1
- New release
- Add nifticlib and libimagequant dependencies

* Wed Oct 03 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.5-4
- Drop Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Mass_Pytho
n_2_Package_Removal
- Update package URLs

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 8.6.5-3
- Rebuild for ImageMagick 6.9.10

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 8.6.5-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.5-1
- New release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 8.6.4-4
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.4-3
- Don't assume /usr/bin/python is python2
- Switch libjpeg-turbo BuildRequires to pkgconfig()

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 8.6.4-2
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.4-1
- New release
- Drop ldconfig scriptlets per new policy

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 8.6.2-5
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 8.6.2-4
- rebuilt for cfitsio 3.420 (so version bump)

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 8.6.2-3
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.2-1
- New release

* Sun Jan 21 2018 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.1-1
- New release

* Sun Dec 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.6.0-1
- New release

* Thu Nov 23 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.9-2
- Rename python-gobject-base dependency to python2-gobject-base
- Don't version dependencies on python*-gobject-base

* Sun Nov 19 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.9-1
- New release

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 8.5.8-2
- Rebuild for ImageMagick 6 reversion

* Wed Aug 30 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.8-1
- New release

* Sun Aug 27 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.7-4
- Rebuild for ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 8.5.7-2
- Rebuild for new ImageMagick

* Sun Jul 30 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.7-1
- New release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.6-2
- Add expat build dependency
- Drop libxml2 build dependency

* Sat Jun 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 8.5.6-1
- New release
- Rename Python packages per policy
- Update project URLs
- Rename pygobject3-base dependency to python-gobject-base
- Switch python3-gobject dependency to python3-gobject-base
- Add missing arch-specific Python provide
- Drop Group tags

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 8.4.4-3
- Rebuild (libwebp)

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 8.4.4-2
- Rebuild for Python 3.6

* Sun Nov 13 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.4.4-1
- New release

* Thu Oct 13 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.4.2-1
- New release

* Sun Sep 25 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.4.1-1
- New release

* Sat Aug 06 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.3.3-1
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.3.1-2
- Rebuilt for matio 1.5.7

* Tue May 10 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.3.1-1
- New release
- Verify that wrapper script name matches base version

* Thu Apr 14 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.3.0-1
- New release
- Add giflib, librsvg2, poppler-glib dependencies

* Mon Mar 28 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2.3-1
- New release

* Sun Feb 21 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2.2-3
- BuildRequire gcc-c++ per new policy

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2.2-1
- New release

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 8.2.1-2
- Rebuild for hdf5 1.8.16

* Mon Jan 11 2016 Benjamin Gilbert <bgilbert@backtick.net> - 8.2.1-1
- New release

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 8.1.1-3
- Rebuilt for libwebp soname bump

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Oct 18 2015 Benjamin Gilbert <bgilbert@backtick.net> - 8.1.1-1
- New release
- Update to new Python guidelines

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 8.0.2-2
- Rebuild for hdf5 1.8.15

* Wed May 06 2015 Benjamin Gilbert <bgilbert@backtick.net> - 8.0.2-1
- New release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7.42.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 14 2015 Benjamin Gilbert <bgilbert@backtick.net> - 7.42.3-1
- New release

* Thu Feb 05 2015 Benjamin Gilbert <bgilbert@backtick.net> - 7.42.2-1
- New release
- Move license files to %%license

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 7.42.1-2
- Rebuild for hdf5 1.8.14

* Sun Dec 28 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.42.1-1
- New release
- Package new Python bindings
- Build with auto-vectorization

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 7.40.11-2
- rebuild (openexr)

* Wed Nov 05 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.11-1
- New release

* Thu Sep 25 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.9-1
- New release

* Fri Aug 22 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.6-1
- New release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.40.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.5-1
- New release

* Sat Jul 26 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.4-1
- New release

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 7.40.3-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 08 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.3-1
- New release

* Sun Jun 29 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.40.2-1
- New release
- Add libgsf dependency
- Fix version string consistency across architectures
- Use macros for package and soname versions

* Sun Jun 22 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.6-1
- New release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.38.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.5-2
- Rebuild for ImageMagick

* Wed Mar 26 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.5-1
- New release

* Tue Jan 21 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.38.1-1
- New release

* Thu Jan 09 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-3
- Rebuild for cfitsio

* Thu Jan 02 2014 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-2
- Rebuild for libwebp

* Mon Dec 23 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.5-1
- New release

* Thu Nov 28 2013 Rex Dieter <rdieter@fedoraproject.org> 7.36.3-2
- rebuild (openexr)

* Wed Nov 13 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.3-1
- New release
- BuildRequire libwebp

* Sat Oct 05 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.36.0-1
- New release

* Tue Sep 10 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.2-2
- Rebuild for ilmbase 2.0

* Tue Aug 06 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.2-1
- New release
- Update -devel description: there are no man pages anymore

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> - 7.34.0-2
- Rebuild for cfitsio 3.350

* Sat Jun 29 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.34.0-1
- New release

* Fri Jun 28 2013 Kalev Lember <kalevlember@gmail.com> - 7.32.4-2
- Rebuilt with libpng 1.6

* Thu Jun 13 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.4-1
- New release

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 7.32.3-2
- Rebuild for hdf5 1.8.11

* Fri Apr 26 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.3-1
- New release

* Thu Mar 21 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.1-1
- New release

* Thu Mar 21 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-4
- Rebuild for cfitsio

* Sun Mar 17 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-3
- Rebuild for ImageMagick

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> 7.32.0-2
- rebuild (OpenEXR)

* Thu Mar 07 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.32.0-1
- New release
- Stop setting rpath on 64-bit builds

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.30.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 7.30.7-2
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 17 2013 Benjamin Gilbert <bgilbert@backtick.net> - 7.30.7-1
- New release
- Modify %%files glob to catch accidental soname bumps
- Update BuildRequires

* Wed Nov 14 2012 Benjamin Gilbert <bgilbert@backtick.net> - 7.30.5-1
- New release

* Mon Oct 15 2012 Benjamin Gilbert <bgilbert@backtick.net> - 7.30.3-1
- New release
- Enable gobject introspection
- Add versioned dependency on base package
- Minor specfile cleanups

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Adam Jackson <ajax@redhat.com> 7.28.2-2
- Rebuild for new libmatio

* Fri Apr 13 2012 Adam Goode <adam@spicenitz.org> - 7.28.2-1
- New upstream release
   * libvips rewrite
   * OpenSlide support
   * better jpeg, png, tiff support
   * sequential mode read
   * operation cache

* Mon Jan 16 2012 Adam Goode <adam@spicenitz.org> - 7.26.7-1
- New upstream release
   * Minor fixes, mostly with reading and writing

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.26.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 7.26.3-2
- Rebuild for new libpng

* Sat Sep  3 2011 Adam Goode <adam@spicenitz.org> - 7.26.3-1
- New upstream release
   * More permissive operators
   * Better TIFF, JPEG, PNG, FITS support
   * VIPS rewrite!

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 7.24.7-2
- Clean up Requires and BuildRequires

* Wed Aug 10 2011 Adam Goode <adam@spicenitz.org> - 7.24.7-1
- New upstream release

* Mon Feb 14 2011 Adam Goode <adam@spicenitz.org> - 7.24.2-1
- New upstream release
   * Run-time code generation, for 4x speedup in some operations
   * Open via disc mode, saving memory
   * FITS supported
   * Improved TIFF and JPEG load

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 jkeating - 7.22.2-1.2
- Rebuilt for gcc bug 634757

* Wed Sep 29 2010 jkeating - 7.22.2-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.22.2-2
- rebuild against ImageMagick

* Fri Sep 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 7.22.2-1.1
- rebuild (ImageMagick)

* Fri Aug  6 2010 Adam Goode <adam@spicenitz.org> - 7.22.2-1
- New upstream release (a few minor fixes)

* Tue Jul 27 2010 Adam Goode <adam@spicenitz.org> - 7.22.1-2
- Add COPYING to doc subpackage

* Tue Jul 27 2010 Adam Goode <adam@spicenitz.org> - 7.22.1-1
- New upstream release
   + More revision of VIPS library
   + New threading system
   + New command-line program, vipsthumbnail
   + Improved interpolators
   + German translation
   + PFM (portable float map) image format read and write
   + Much lower VM use with many small images open
   + Rewritten flood-fill

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 7.20.7-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-3
- Don't require gtk-doc anymore (resolves #604421)

* Sun Mar  7 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-2
- Rebuild for imagemagick soname change
- Remove some old RPM stuff

* Tue Feb  2 2010 Adam Goode <adam@spicenitz.org> - 7.20.7-1
- New upstream release
   + C++ and Python bindings now have support for deprecated functions
   + Bugfixes for YCbCr JPEG TIFF files

* Wed Jan  6 2010 Adam Goode <adam@spicenitz.org> - 7.20.6-1
- New upstream release
   + About half of the VIPS library has been revised
   + Now using gtk-doc
   + Better image file support
   + MATLAB file read supported
   + New interpolation system
   + Support for Radiance files

* Fri Sep  4 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 7.18.2-1
- Update to 7.18.2 to sync with fixed nip2 FTBFS.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.16.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Adam Goode <adam@spicenitz.org> - 7.16.4-3
- Rebuild for ImageMagick soname change

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 28 2008 Adam Goode <adam@spicenitz.org> - 7.16.4-1
- New release

* Sun Dec 21 2008 Adam Goode <adam@spicenitz.org> - 7.16.3-1
- New release
- Update description

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 7.14.5-2
- Rebuild for Python 2.6

* Sat Aug 30 2008 Adam Goode <adam@spicenitz.org> - 7.14.5-1
- New release

* Fri Jun 20 2008 Adam Goode <adam@spicenitz.org> - 7.14.4-1
- New release

* Sat Mar 15 2008 Adam Goode <adam@spicenitz.org> - 7.14.1-1
- New release

* Mon Mar 10 2008 Adam Goode <adam@spicenitz.org> - 7.14.0-1
- New release
- Remove GCC 4.3 patch (upstream)

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 7.12.5-5
- Fix GCC 4.3 build

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 7.12.5-4
- GCC 4.3 mass rebuild

* Tue Oct 23 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-3
- Eliminate build differences in version.h to work on multiarch

* Mon Oct 15 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-2
- Rebuild for OpenEXR update

* Fri Sep 21 2007 Adam Goode <adam@spicenitz.org> - 7.12.5-1
- New upstream release

* Thu Aug 16 2007 Adam Goode <adam@spicenitz.org> - 7.12.4-2
- Add Conflicts for doc
- Update doc package description

* Thu Aug 16 2007 Adam Goode <adam@spicenitz.org> - 7.12.4-1
- New upstream release
- Update License tag

* Tue Jul 24 2007 Adam Goode <adam@spicenitz.org> - 7.12.2-1
- New stable release 7.12

* Sat May  5 2007 Adam Goode <adam@spicenitz.org> - 7.12.0-1
- New upstream release

* Thu Aug 31 2006 Adam Goode <adam@spicenitz.org> - 7.10.21-1
- New upstream release

* Fri Jul 28 2006 Adam Goode <adam@spicenitz.org> - 7.10.20-3
- Include results of running automake in the patch for undefined symbols
- No longer run automake or autoconf (autoconf was never actually necessary)

* Mon Jul 24 2006 Adam Goode <adam@spicenitz.org> - 7.10.20-2
- Eliminate undefined non-weak symbols in libvipsCC.so

* Fri Jul 21 2006 Adam Goode <adam@spicenitz.org> - 7.10.20-1
- New upstream release
- Updated for FC5

* Tue Dec 14 2004 John Cupitt <john.cupitt@ng-london.org.uk> 7.10.8
- updated for 7.10.8
- now updated from configure
- implicit deps and files

* Wed Jul 16 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.10
- updated for 7.8.10
- updated %%files
- copies formatted docs to install area

* Wed Mar 12 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.8
- updated for 7.8.8, adding libdrfftw

* Mon Feb 3 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.7-2
- hack to change default install prefix to /usr/local

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.7-1
- first stab at an rpm package for vips
