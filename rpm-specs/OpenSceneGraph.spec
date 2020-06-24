#
# Copyright (c) 2005 - 2017 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%global apivers 3.4.1
%global srcvers 3.4.1

# GStreamer support: Default on
%bcond_without  gstreamer

# GDal support: Default on
%bcond_without  gdal

# Inventor support: Default to Coin3
# These are mutually exclusive
%bcond_with     Inventor
%bcond_without  Coin4

# Jasper support: Default on
%bcond_without  jasper

# OpenEXR support: Default on
%bcond_without  OpenEXR

# Collada support: Default on
%bcond_without  Collada

Name:           OpenSceneGraph
Version:        %{srcvers}
Release:        18%{?dist}
Summary:        High performance real-time graphics toolkit

# The OSGPL is just the wxWidgets license.
License:        wxWidgets
URL:            http://www.openscenegraph.org/
Source0:	https://github.com/openscenegraph/%{name}/archive/%{name}-%{srcvers}.tar.gz

Patch1:         0001-Cmake-fixes.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch2:         0002-Activate-osgviewerWX.patch
# Unset DOT_FONTNAME
Patch3:         0003-Unset-DOT_FONTNAME.patch
# Re-add osgframerenderer
Patch4:         0004-Re-add-osgframerenderer.patch
# Building breaks with unsigned char (arm, c11)
Patch5:         0005-c-11-narrowing-hacks-Work-around-c-11-erroring-out-n.patch
# Hack to build against collada-dom-2.5
Patch6:		0006-Add-collada-dom-2.5.patch
# Force osgviewerWX to always use X11 backend (wxGLCanvas is broken on Wayland)
Patch7:         force-x11-backend.patch
# Work around for wx_gtk3_gl library not being linked with.
Patch8:         0008-Fix_wxWidgets_gl.patch
Patch9:         osg-freeglut.patch
# Fix build against recent asio
Patch10:        OpenSceneGraph_asio.patch

BuildRequires:  boost-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
%{?with_Inventor:BuildRequires:  Inventor-devel}
%{?with_Coin4:BuildRequires:  Coin4-devel}
BuildRequires:  freeglut-devel
BuildRequires:  libjpeg-devel
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  doxygen graphviz
BuildRequires:  cmake
BuildRequires:  wxGTK3-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  openal-soft-devel

BuildRequires:  qt-devel
BuildRequires:  qtwebkit-devel
BuildRequires:  asio-devel

# Optional
%{?with_OpenEXR:BuildRequires: OpenEXR-devel}

# Optional
%{?with_Collada:BuildRequires: pkgconfig(collada-dom)}

# Optional
%{?with_jasper:BuildRequires:  jasper-devel}

# Used by osgmovie
BuildRequires:  SDL2-devel
# Used by SDL-examples
BuildRequires:  SDL-devel

# Optional
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-base-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-app-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-audio-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-fft-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-video-1.0)}

BuildRequires:  fltk-devel fltk-fluid

BuildRequires:  gnuplot

BuildRequires:  libvncserver-devel

BuildRequires: pkgconfig(cairo)
%{?with_gdal:BuildRequires:  gdal-devel}
BuildRequires: pkgconfig(gta)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtkglext-x11-1.0)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(librsvg-2.0) >= 2.35
BuildRequires: pkgconfig(xrandr)

# According to the FPG, this should be defined, but it's not.
%global _fontdir /usr/share/fonts

%description
The OpenSceneGraph is an OpenSource, cross platform graphics toolkit for the
development of high performance graphics applications such as flight
simulators, games, virtual reality and scientific visualization.
Based around the concept of a SceneGraph, it provides an object oriented
framework on top of OpenGL freeing the developer from implementing and
optimizing low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%prep
%setup -q -n OpenSceneGraph-OpenSceneGraph-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1

sed -i -e 's,\.:/usr/share/fonts/ttf:,.:%{_fontdir}:/usr/share/fonts/ttf:,' \
src/osgText/Font.cpp

iconv -f ISO-8859-1 -t utf-8 AUTHORS.txt > AUTHORS.txt~
mv AUTHORS.txt~ AUTHORS.txt

# Update doxygen
doxygen -u doc/Doxyfiles/doxyfile.cmake
doxygen -u doc/Doxyfiles/openthreads.doxyfile.cmake

# HACK: Make CMakeModules/FindInventor.cmake multilib-aware
sed -i -e 's,/lib,/%{_lib},' CMakeModules/FindInventor.cmake

# HACK: Make CMakeModules/FindFLTK.cmake multilib-aware
sed -i -e 's,/lib,/%{_lib},' CMakeModules/FindFLTK.cmake

# Adjust path to Coin4 includes
%{?with_Coin4:sed -i -e 's,/include,/include/Coin4,' CMakeModules/FindInventor.cmake}

# CMakeLists.txt is playing silly games with CXXFLAGS
# Kick out -pedantic
sed -i -e 's, -pedantic,,' CMakeLists.txt

%build
mkdir -p BUILD
pushd BUILD
CFLAGS="${RPM_OPT_FLAGS} -pthread"
CXXFLAGS="${RPM_OPT_FLAGS} -pthread"
LDFLAGS="$LDFLAGS -lglut" %cmake -DBUILD_OSG_EXAMPLES=ON -DBUILD_DOCUMENTATION=ON \
  .. \
  -Wno-dev
LDFLAGS="$LDFLAGS -lglut" make VERBOSE=1 %{?_smp_mflags}

make doc_openscenegraph doc_openthreads
popd

%install
pushd BUILD
make install DESTDIR=${RPM_BUILD_ROOT}

# Supposed to take OpenSceneGraph data
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/OpenSceneGraph
popd


%files
%doc AUTHORS.txt NEWS.txt README.txt
%license LICENSE.txt
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/osgfilecache
%{_bindir}/present3D

%package libs
Summary:        Runtime libraries for OpenSceneGraph

%description libs
Runtime libraries files for OpenSceneGraph.

%ldconfig_scriptlets libs

%files libs
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_3dc.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_3ds.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_ac.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_bmp.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_bsp.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_bvh.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_cfg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_curl.so
%{?with_Collada:%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_dae.so}
%{_libdir}/osgPlugins-%{apivers}/osgdb_dds.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osganimation.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgfx.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgparticle.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgshadow.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgsim.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgterrain.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgtext.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgviewer.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgvolume.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_deprecated_osgwidget.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_dot.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_dw.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_dxf.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_freetype.so
%{?with_OpenEXR:%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_exr.so}
%{?with_gdal:%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_gdal.so}
%{_libdir}/osgPlugins-%{apivers}/osgdb_gif.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_gles.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_glsl.so
%{?with_gstreamer:%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_gstreamer.so}
%{_libdir}/osgPlugins-%{apivers}/osgdb_gta.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_gz.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_hdr.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_iv.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_ive.so
%{?with_jasper:%{_libdir}/osgPlugins-%{apivers}/osgdb_jp2.so}
%{_libdir}/osgPlugins-%{apivers}/osgdb_jpeg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_ktx.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_logo.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_lua.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_lwo.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_lws.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_md2.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_mdl.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_normals.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_obj.so
%{?with_gdal:%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_ogr.so}
%{_libdir}/osgPlugins-%{apivers}/osgdb_openflight.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osc.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osga.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osgjs.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osgshadow.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osgterrain.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osgtgz.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_osgviewer.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_p3d.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_pdf.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_pic.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_ply.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_png.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_pnm.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_pov.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_pvr.so
%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_qfont.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_resthttp.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_revisions.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_rgb.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_rot.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_scale.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_sdl.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osganimation.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgfx.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgga.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgmanipulator.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgparticle.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgshadow.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgsim.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgterrain.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgtext.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgui.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgutil.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgviewer.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_serializers_osgvolume.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_shp.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_stl.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_svg.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_tf.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_tga.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_tgz.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_tiff.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_trans.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_trk.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_txf.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_txp.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_vnc.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_vtf.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_x.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_zip.so
%{_libdir}/libosgAnimation.so.*
%{_libdir}/libosgDB.so.*
%{_libdir}/libosgFX.so.*
%{_libdir}/libosgGA.so.*
%{_libdir}/libosgManipulator.so.*
%{_libdir}/libosgParticle.so.*
%{_libdir}/libosgPresentation.so.*
%{_libdir}/libosgShadow.so.*
%{_libdir}/libosgSim.so.*
%{_libdir}/libosg.so.*
%{_libdir}/libosgTerrain.so.*
%{_libdir}/libosgText.so.*
%{_libdir}/libosgUI.so.*
%{_libdir}/libosgUtil.so.*
%{_libdir}/libosgViewer.so.*
%{_libdir}/libosgVolume.so.*
%{_libdir}/libosgWidget.so.*

%package devel
Summary:        Development files for OpenSceneGraph
Requires:       OpenSceneGraph-libs = %{version}-%{release}
Requires:       OpenThreads-devel

%description devel
Development files for OpenSceneGraph.

%files devel
%doc BUILD/doc/OpenSceneGraphReferenceDocs
%{_includedir}/osg
%{_includedir}/osgAnimation
%{_includedir}/osgDB
%{_includedir}/osgFX
%{_includedir}/osgGA
%{_includedir}/osgManipulator
%{_includedir}/osgParticle
%{_includedir}/osgPresentation
%{_includedir}/osgShadow
%{_includedir}/osgSim
%{_includedir}/osgTerrain
%{_includedir}/osgText
%{_includedir}/osgUI
%{_includedir}/osgUtil
%{_includedir}/osgViewer
%{_includedir}/osgVolume
%{_includedir}/osgWidget
%{_libdir}/libosgAnimation.so
%{_libdir}/libosgDB.so
%{_libdir}/libosgFX.so
%{_libdir}/libosgGA.so
%{_libdir}/libosgManipulator.so
%{_libdir}/libosgParticle.so
%{_libdir}/libosgPresentation.so
%{_libdir}/libosgShadow.so
%{_libdir}/libosgSim.so
%{_libdir}/libosg.so
%{_libdir}/libosgTerrain.so
%{_libdir}/libosgText.so
%{_libdir}/libosgUI.so
%{_libdir}/libosgUtil.so
%{_libdir}/libosgViewer.so
%{_libdir}/libosgVolume.so
%{_libdir}/libosgWidget.so
%{_libdir}/pkgconfig/openscenegraph-osgAnimation.pc
%{_libdir}/pkgconfig/openscenegraph-osgDB.pc
%{_libdir}/pkgconfig/openscenegraph-osgFX.pc
%{_libdir}/pkgconfig/openscenegraph-osgGA.pc
%{_libdir}/pkgconfig/openscenegraph-osgManipulator.pc
%{_libdir}/pkgconfig/openscenegraph-osgParticle.pc
%{_libdir}/pkgconfig/openscenegraph-osg.pc
%{_libdir}/pkgconfig/openscenegraph-osgShadow.pc
%{_libdir}/pkgconfig/openscenegraph-osgSim.pc
%{_libdir}/pkgconfig/openscenegraph-osgTerrain.pc
%{_libdir}/pkgconfig/openscenegraph-osgText.pc
%{_libdir}/pkgconfig/openscenegraph-osgUtil.pc
%{_libdir}/pkgconfig/openscenegraph-osgViewer.pc
%{_libdir}/pkgconfig/openscenegraph-osgVolume.pc
%{_libdir}/pkgconfig/openscenegraph-osgWidget.pc
%{_libdir}/pkgconfig/openscenegraph.pc


%package examples-SDL
Summary:        OSG sample applications using SDL

%description examples-SDL
OSG sample applications using SDL.

%files examples-SDL
%{_bindir}/osgviewerSDL

%package examples-fltk
Summary:        OSG sample applications using FLTK

%description examples-fltk
OSG sample applications using FLTK.

%files examples-fltk
%{_bindir}/osgviewerFLTK

%package examples-gtk
Summary:        OSG sample applications using gtk

%description examples-gtk
OSG sample applications using gtk

%files examples-gtk
%{_bindir}/osgviewerGTK

%if %{with gdal}
%package gdal
Summary:        OSG Gdal plugin

%description gdal
OSG Gdal plugin.

%files gdal
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_gdal.so
%{_libdir}/osgPlugins-%{apivers}/osgdb_ogr.so
%endif /* gdal */

%if %{with Collada}
%package Collada
Summary:        OSG Collada plugin

%description Collada
OSG Collada plugin.

%files Collada
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_dae.so
%endif /* Collada */

%if %{with OpenEXR}
%package OpenEXR
Summary:        OSG OpenEXR plugin

%description OpenEXR
OSG OpenEXR plugin.

%files OpenEXR
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_exr.so
%endif /* OpenEXR */

%if %{with gstreamer}
%package gstreamer
Summary:        OSG gstreamer plugin

%description gstreamer
OSG gstreamer plugin.

%files gstreamer
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_gstreamer.so
%endif /* gstreamer */

%package qt
Summary:        OSG Qt bindings

%description qt
OSG Qt bindings.

%files qt
%{_libdir}/libosgQt.so.*
%dir %{_libdir}/osgPlugins-%{apivers}
%{_libdir}/osgPlugins-%{apivers}/osgdb_qfont.so

%ldconfig_scriptlets qt

%package qt-devel
Summary:        OSG Qt development files
Requires:       OpenSceneGraph-qt = %{version}-%{release}
Requires:       OpenSceneGraph-devel = %{version}-%{release}
Requires:       qt-devel

%description qt-devel
Development files for OSG Qt bindings.

%files qt-devel
%{_includedir}/osgQt
%{_libdir}/libosgQt.so
%{_libdir}/pkgconfig/openscenegraph-osgQt.pc


%package examples-qt
Summary:        OSG sample applications using qt

%description examples-qt
OSG sample applications using qt

%files examples-qt
%{_bindir}/osgqfont
%{_bindir}/osgviewerQt
%{_bindir}/osgQtBrowser
%{_bindir}/osgQtWidgets

# OpenSceneGraph-examples
%package examples
Summary:        Sample applications for OpenSceneGraph

%description examples
Sample applications for OpenSceneGraph

%files examples
%{_bindir}/osg2cpp
%{_bindir}/osganalysis
%{_bindir}/osganimate
%{_bindir}/osganimationeasemotion
%{_bindir}/osganimationhardware
%{_bindir}/osganimationmakepath
%{_bindir}/osganimationmorph
%{_bindir}/osganimationnode
%{_bindir}/osganimationskinning
%{_bindir}/osganimationsolid
%{_bindir}/osganimationtimeline
%{_bindir}/osganimationviewer
%{_bindir}/osgatomiccounter
%{_bindir}/osgautocapture
%{_bindir}/osgautotransform
%{_bindir}/osgbillboard
%{_bindir}/osgblenddrawbuffers
%{_bindir}/osgblendequation
%{_bindir}/osgcallback
%{_bindir}/osgcamera
%{_bindir}/osgcatch
%{_bindir}/osgclip
%{_bindir}/osgcluster
%{_bindir}/osgcompositeviewer
%{_bindir}/osgcomputeshaders
%{_bindir}/osgcopy
%{_bindir}/osgcubemap
%{_bindir}/osgdatabaserevisions
%{_bindir}/osgdelaunay
%{_bindir}/osgdepthpartition
%{_bindir}/osgdepthpeeling
%{_bindir}/osgdistortion
%{_bindir}/osgdrawinstanced
%{_bindir}/osgfadetext
%{_bindir}/osgfont
%{_bindir}/osgforest
%{_bindir}/osgfpdepth
%{_bindir}/osgframerenderer
%{_bindir}/osgfxbrowser
%{_bindir}/osggameoflife
%{_bindir}/osggeometry
%{_bindir}/osggeometryshaders
%{_bindir}/osggpucull
%{_bindir}/osggpx
%{_bindir}/osggraphicscost
%{_bindir}/osghangglide
%{_bindir}/osghud
%{_bindir}/osgimagesequence
%{_bindir}/osgimpostor
%{_bindir}/osgintersection
%{_bindir}/osgkdtree
%{_bindir}/osgkeyboard
%{_bindir}/osgkeyboardmouse
%{_bindir}/osgkeystone
%{_bindir}/osglauncher
%{_bindir}/osglight
%{_bindir}/osglightpoint
%{_bindir}/osglogicop
%{_bindir}/osglogo
%{_bindir}/osgmanipulator
%{_bindir}/osgmemorytest
%{_bindir}/osgmotionblur
%{_bindir}/osgmovie
%{_bindir}/osgmultiplemovies
%{_bindir}/osgmultiplerendertargets
%{_bindir}/osgmultitexture
%{_bindir}/osgmultitexturecontrol
%{_bindir}/osgmultitouch
%{_bindir}/osgmultiviewpaging
%{_bindir}/osgoccluder
%{_bindir}/osgocclusionquery
%{_bindir}/osgoit
%{_bindir}/osgoscdevice
%{_bindir}/osgoutline
%{_bindir}/osgpackeddepthstencil
%{_bindir}/osgpagedlod
%{_bindir}/osgparametric
%{_bindir}/osgparticle
%{_bindir}/osgparticleeffects
%{_bindir}/osgparticleshader
%{_bindir}/osgpdf
%{_bindir}/osgphotoalbum
%{_bindir}/osgpick
%{_bindir}/osgplanets
%{_bindir}/osgpoints
%{_bindir}/osgpointsprite
%{_bindir}/osgposter
%{_bindir}/osgprecipitation
%{_bindir}/osgprerender
%{_bindir}/osgprerendercubemap
%{_bindir}/osgreflect
%{_bindir}/osgrobot
%{_bindir}/osgSSBO
%{_bindir}/osgscalarbar
%{_bindir}/osgscreencapture
%{_bindir}/osgscribe
%{_bindir}/osgsequence
%{_bindir}/osgshadercomposition
%{_bindir}/osgshadergen
%{_bindir}/osgshaders
%{_bindir}/osgshaderterrain
%{_bindir}/osgshadow
%{_bindir}/osgshape
%{_bindir}/osgsharedarray
%{_bindir}/osgsidebyside
%{_bindir}/osgsimpleshaders
%{_bindir}/osgsimplegl3
%{_bindir}/osgsimplifier
%{_bindir}/osgsimulation
%{_bindir}/osgslice
%{_bindir}/osgspacewarp
%{_bindir}/osgspheresegment
%{_bindir}/osgspotlight
%{_bindir}/osgstereoimage
%{_bindir}/osgstereomatch
%{_bindir}/osgteapot
%{_bindir}/osgterrain
%{_bindir}/osgtessellate
%{_bindir}/osgtessellationshaders
%{_bindir}/osgtext
%{_bindir}/osgtext3D
%{_bindir}/osgtexture1D
%{_bindir}/osgtexture2D
%{_bindir}/osgtexture3D
%{_bindir}/osgtexture2DArray
%{_bindir}/osgtexturecompression
%{_bindir}/osgtexturerectangle
%{_bindir}/osgthirdpersonview
%{_bindir}/osgthreadedterrain
%{_bindir}/osgtransferfunction
%{_bindir}/osgtransformfeedback
%{_bindir}/osguniformbuffer
%{_bindir}/osgunittests
%{_bindir}/osguserdata
%{_bindir}/osguserstats
%{_bindir}/osgvertexattributes
%{_bindir}/osgvertexprogram
%{_bindir}/osgviewerGLUT
%{_bindir}/osgviewerWX
%{_bindir}/osgvirtualprogram
%{_bindir}/osgvnc
%{_bindir}/osgvolume
%{_bindir}/osgwidgetaddremove
%{_bindir}/osgwidgetbox
%{_bindir}/osgwidgetcanvas
%{_bindir}/osgwidgetframe
%{_bindir}/osgwidgetinput
%{_bindir}/osgwidgetlabel
%{_bindir}/osgwidgetmenu
%{_bindir}/osgwidgetmessagebox
%{_bindir}/osgwidgetnotebook
%{_bindir}/osgwidgetperformance
%{_bindir}/osgwidgetscrolled
%{_bindir}/osgwidgetshader
%{_bindir}/osgwidgetstyled
%{_bindir}/osgwidgettable
%{_bindir}/osgwidgetwindow
%{_bindir}/osgwindows

%{_datadir}/OpenSceneGraph

# OpenThreads
%package -n OpenThreads
Summary:        OpenThreads
License:        wxWidgets

%description -n OpenThreads
OpenThreads is intended to provide a minimal & complete Object-Oriented (OO)
thread interface for C++ programmers.  It is loosely modeled on the Java
thread API, and the POSIX Threads standards.  The architecture of the
library is designed around "swappable" thread models which are defined at
compile-time in a shared object library.

%ldconfig_scriptlets -n OpenThreads

%files -n OpenThreads
%doc AUTHORS.txt NEWS.txt README.txt
%license LICENSE.txt
%{_libdir}/libOpenThreads.so.*

# OpenThreads-devel
%package -n OpenThreads-devel
Summary:        Devel files for OpenThreads
License:        wxWidgets
Requires:       OpenThreads = %{version}-%{release}
Requires:       pkgconfig

%description -n OpenThreads-devel
Development files for OpenThreads.

%files -n OpenThreads-devel
%doc BUILD/doc/OpenThreadsReferenceDocs
%{_libdir}/pkgconfig/openthreads.pc
%{_libdir}/libOpenThreads.so
%{_includedir}/OpenThreads

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-18
- Rebuilt for Boost 1.73

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.4.1-17
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.4.1-16
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.4.1-14
- Rebuild for poppler-0.84.0

* Sat Oct  9 2019 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-13
- Rebuild with Coin4.

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.4.1-12
- Rebuilt for new freeglut

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-10
- Rebuild for OpenEXR 2.3.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-8
- Rebuilt for Boost 1.69

* Sat Aug 04 2018 Scott Talbert <swt@techie.net> - 3.4.1-7
- Rebuild against wxWidgets 3.0 and patch to always use GTK X11 backend

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 3.4.1-5
- Rebuild (giflib)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-3
- Rebuilt for Boost 1.66

* Wed Oct 25 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.1-2
- Add 0006-Add-collada-dom-2.5.patch.
- Rebuild against collada-dom-2.5.

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.1-1
- Upgrade to 3.4.1.
- Rebase patches.
- Reflect Source0:-URL having changed.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-11
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-10
- Rebuilt for Boost 1.64

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.4.0-9
- rebuild (libvncserver)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-7
- Get rid of additional OpenSceneGraph-%%version directory.
- Tidy-up %%changelog.

* Thu Dec 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-6
- Add Collada plugin subpackage.
- Add OpenEXR plugin subpackage.
- Cleanup conditionals.
- BR: libcurl-devel instead of curl-devel.

* Sun Dec 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-5
- Rebuild for jasper-2.0.0.

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-4
- Add 0005-c-11-narrowing-hacks.patch (F24FTBFS on arm).
- Remove -pedantic from CMakeLists.txt.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-2
- Eliminate %%define.

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-1
- Upstream update to 3.4.0.
- Rebase patches.
- Rework package deps.

* Tue Aug 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-3
- Move osgqfonts into *-qt.
- Make CMakeModules/FindFLTK multilib-aware.
- Add BR: pkgconfig(*) for those packages, cmake checks for.
- Explicitly list all plugins.
- Spec file cosmetics.

* Mon Aug 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-2
- Reflect upstream having changed Source0:-URL.

* Sun Aug 16 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3.
- Rebase patches.

* Wed Aug 12 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-3
- Set %%Version to %%srcvers.
- BR: boost-devel.
- Add support for Coin3 and Inventor.

* Mon Aug 10 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-2
- Add 0004-Unset-DOT_FONTNAME.patch.

* Sat Aug 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2.
- Rebase patches.

* Wed Jun 24 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-7
- Add 0005-From-Jannik-Heller-Fix-for-Qt4-multi-threaded-crash..patch
  (Address RHBZ#1235030)
- Run doxygen -u on doxygen source-files.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-5
- Rebuild (gcc-5.0.1).
- Modernize spec.
- Add %%license.

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-4
- rebuild (fltk,gcc5)

* Thu Oct 30 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-3
- Add 0004-Applied-fix-to-Node-remove-Callback-NodeCallback-ins.patch
  (RHBZ #1158669).
- Rebase patches.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-1
- Upgrade to 3.2.1.
- Rebase patches.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-2
- Modernize spec.
- Preps for 3.2.1.

* Wed Aug 14 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-1
- Upstream update.
- Rebase patches.

* Tue Aug 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-18
- Fix %%changelog dates.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.1-15
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.0.1-14
- rebuild against new libjpeg

* Mon Sep 03 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-13
- BR: libvncserver-devel, ship osgvnc (RHBZ 853755).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Marek Kasik <mkasik@redhat.com> - 3.0.1-11
- Rebuild (poppler-0.20.0)

* Mon May 07 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-10
- Append -pthread to CXXFLAGS (Fix FTBFS).

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.0.1-7
- Rebuild for new libpng

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-6
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 3.0.1-5
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-3
- Add BR: qtwebkit-devel.
- Add osgQtBrowser, osgQtWidgets to OpenSceneGraph-examples-qt.

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3.0.1-2
- Rebuild (poppler-0.17.3)

* Wed Aug 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-1
- Upstream update.
- Remove OpenSceneGraph2* tags.
- Split out OpenSceneGraph-qt, OpenSceneGraph-qt-devel.
- Pass -Wno-dev to cmake.
- Append -pthread to CFLAGS.

* Sun Jul 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.5-3
- Reflect curl having silently broken their API.

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 2.8.5-2
- Rebuild (poppler-0.17.0)

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.5-1
- Upstream update.

* Mon May 30 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.4-2
- Reflect fltk-include paths having changed incompatibly.

* Wed Apr 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.4-1
- Upstream update.
- Rebase OpenSceneGraph-*.diff.
- Spec file cleanup.

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 2.8.3-10
- Rebuild (poppler-0.16.3)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-8
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-7
- rebuild (poppler)

* Wed Dec 15 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-6
- Add %%{_fontdir} to OSG's font file search path.

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-5
- rebuilt (poppler)

* Thu Sep 30 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-4
- rebuild (libpoppler-glib.so.6).

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-3
- rebuild (poppler)

* Mon Jul 12 2010 Dan Horák <dan@danny.cz> - 2.8.3-2
- rebuilt against wxGTK-2.8.11-2

* Fri Jul 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-1
- Upstream update.
- Add osg-examples-gtk.

* Wed Aug 26 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-3
- Change Source0 URL (Upstream moved it once again).

* Tue Aug 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-2
- Spec file cleanup.

* Mon Aug 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-1
- Upstream update.
- Reflect upstream having changes Source0-URL.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.1-2
- Remove /usr/bin/osgfilecache from *-examples.
- Further spec cleanup.

* Wed Jun 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.1-1
- Upstream update.
- Reflect upstream having consolidated their Source0:-URL.
- Stop supporting OSG < 2.6.0.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Ralf Corsépius <rc040203@freenet.de> - 2.8.0-1
- Upgrade to OSG-2.8.0.
- Remove Obsolete: Producer hacks.

* Thu Aug 14 2008 Ralf Corsépius <rc040203@freenet.de> - 2.6.0-1
- Upgrade to OSG-2.6.0.

* Wed Aug 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-4
- Preps for 2.6.0.
- Reflect the Source0-URL having changed.
- Major spec-file overhaul.

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.0-3
- fix license tag

* Tue May 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-2
- Add Orion Poplawski's patch to fix building with cmake-2.6.0.

* Mon May 12 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-1
- Upstream update.
- Adjust patches to 2.4.0.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-5
- Add *-examples-SDL package.
- Add osgviewerSDL.
- Add *-examples-fltk package.
- Add osgviewerFLTK.
- Add *-examples-qt package.
- Move osgviewerQT to *-examples-qt package.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-4
- Rebuild for gcc43.
- OpenSceneGraph-2.2.0.diff: Add gcc43 hacks.

* Wed Nov 28 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-3
- Re-add apivers.
- Rebuild against doxygen-1.5.3-1 (BZ 343591).

* Fri Nov 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-2
- Add qt.

* Thu Nov 01 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-1
- Upstream upgrade.
- Reflect Source0-URL having changed once again.
- Reflect upstream packaging changes to spec.

* Sat Oct 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-8
- Reflect Source0-URL having changed.

* Thu Sep 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-7
- Let OpenSceneGraph-libs Obsoletes: Producer
- Let OpenSceneGraph-devel Obsoletes: Producer-devel.

* Wed Sep 26 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-6
- By public demand, add upstream's *.pcs.
- Add hacks to work around the worst bugs in *.pcs.
- Add OpenSceneGraph2-devel.
- Move ldconfig to *-libs.
- Abandon OpenThreads2.
- Remove obsolete applications.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-5
- Prepare renaming package into OpenSceneGraph2.
- Split out run-time libs into *-libs subpackage.
- Rename pkgconfig files into *-2.pc.
- Reactivate ppc64.
- Mass rebuild.

* Sat Jun 30 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-4
- Cleanup CVS.
- Add OSG1_Producer define.

* Fri Jun 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-3
- Re-add (but don't ship) *.pc.
- Let OpenSceneGraph "Obsolete: Producer".
- Let OpenSceneGraph-devel "Obsolete: Producer-devel".

* Wed Jun 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-2
- Build docs.

* Fri Jun 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-1
- Upgrade to 2.0.

* Thu Oct 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2-1
- Upstream update.

* Thu Aug 24 2006 Ralf Corsépius <rc040203@freenet.de> - 1.1-1
- Upstream update.

* Sat Dec 10 2005 Ralf Corsépius <rc040203@freenet.de> - 1.0-1
- Upstream update.

* Tue Aug 02 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-1
- FE submission.

* Thu Jul 21 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-0
- Initial spec.
