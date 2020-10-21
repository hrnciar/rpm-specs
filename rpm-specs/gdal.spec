#TODO: Create script to make clean tarball
#TODO: msg needs to have PublicDecompWT.zip from EUMETSAT, which is not free;
#      Building without msg therefore
#TODO: e00compr bundled?
#TODO: There are tests for bindings -- at least for Perl
#TODO: Java has a directory with test data and a build target called test
#      It uses %%{JAVA_RUN}; make test seems to work in the build directory
#TODO: e00compr source is the same in the package and bundled in GDAL
#TODO: Consider doxy patch from Suse, setting EXTRACT_LOCAL_CLASSES  = NO

# Tests can be of a different version
%global testversion 3.1.3
%global run_tests 1

%global bashcompletiondir %(pkg-config --variable=compatdir bash-completion)

%if 0%{?bootstrap}
%global with_mysql 0
%global mysql --without-mysql
%global with_poppler 0
%global poppler --without-poppler
%global with_spatialite 0
%global spatialite --without-spatialite
%else
# https://bugzilla.redhat.com/show_bug.cgi?id=1490492
%global with_mysql 1
%global mysql --with-mysql
# https://bugzilla.redhat.com/show_bug.cgi?id=1490492
%global with_poppler 1
%global poppler --with-poppler
%global with_spatialite 1
%global spatialite "--with-spatialite"
%endif

%bcond_with python2
%bcond_without python3

# No ppc64 build for spatialite in EL6
# https://bugzilla.redhat.com/show_bug.cgi?id=663938
%if 0%{?rhel} == 6
%ifnarch ppc64
%global with_spatialite 0
%global spatialite --without-spatialite
%endif
%endif

Name:          gdal
Version:       3.1.3
Release:       2%{?dist}%{?bootstrap:.%{bootstrap}.bootstrap}
Summary:       GIS file format library
License:       MIT
URL:           http://www.gdal.org
# Source0:   http://download.osgeo.org/gdal/%%{version}/gdal-%%{version}.tar.xz
# See PROVENANCE.TXT-fedora and the cleaner script for details!

Source0:       %{name}-%{version}-fedora.tar.xz
Source1:       http://download.osgeo.org/%{name}/%{testversion}/%{name}autotest-%{testversion}.tar.gz

# Cleaner script for the tarball
Source3:       %{name}-cleaner.sh

Source4:       PROVENANCE.TXT-fedora

# Fedora uses Alternatives for Java
Patch2:        %{name}-1.9.0-java.patch
# Ensure rpc/types.h is found by dods driver (indirectly required by libdap/XDRUtils.h)
Patch3:        gdal_tirpcinc.patch
# Use libtool to create libiso8211.a, otherwise broken static lib is created since object files are compiled through libtool
Patch4:        gdal_iso8211.patch
# Don't pass -W to sphinx, it causes it to error out on warnings
# Don't do parallel build, currently fails with "Sphinx parallel build error: NotImplementedError"
Patch5:        gdal_sphinx.patch
# Fix makefiles installing libtool wrappers instead of actual executables
Patch6:        gdal_installapps.patch
# Don't refer to PDF manual which is not built
Patch7:        gdal_nopdf.patch
# Adapt to jasper 2.0.21
# See https://github.com/OSGeo/gdal/commit/9ef8e16e27c5fc4c491debe50bf2b7f3e94ed334
Patch8:        gdal_jasper.patch


BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: ant
# No armadillo in EL5
BuildRequires: armadillo-devel
BuildRequires: bash-completion
BuildRequires: cfitsio-devel
# No CharLS in EL5
#BuildRequires: CharLS-devel
BuildRequires: chrpath
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
# No freexl in EL5
BuildRequires: freexl-devel
BuildRequires: geos-devel >= 3.7.1
BuildRequires: ghostscript
BuildRequires: hdf-devel
BuildRequires: hdf-static
BuildRequires: hdf5-devel
# No complete java yet in EL8
%if 0%{?rhel} < 8
BuildRequires: java-devel >= 1:1.6.0
%endif
BuildRequires: jasper-devel
BuildRequires: jpackage-utils
# No complete java yet in EL8
%if 0%{?rhel} < 8
# For 'mvn_artifact' and 'mvn_install'
BuildRequires: javapackages-local
%endif
BuildRequires: json-c-devel
BuildRequires: libgeotiff-devel
# No libgta in EL5
BuildRequires: libgta-devel

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
# No libkml in EL
BuildRequires: libkml-devel

%if %{with_spatialite}
BuildRequires: libspatialite-devel
%endif

BuildRequires: libtiff-devel
# No libwebp in EL 5 and 6
BuildRequires: libwebp-devel
BuildRequires: libtool
BuildRequires: giflib-devel
BuildRequires: netcdf-devel
BuildRequires: libdap-devel
BuildRequires: librx-devel
%if 0%{?with_mysql}
BuildRequires: mariadb-connector-c-devel
%endif
BuildRequires: pcre-devel
BuildRequires: ogdi-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: openjpeg2-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: %{_bindir}/pkg-config
%if 0%{?with_poppler}
BuildRequires: poppler-devel
%endif
BuildRequires: libpq-devel
BuildRequires: proj-devel >= 5.2.0
%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-numpy
%endif
%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-setuptools
%endif
BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: unixODBC-devel
BuildRequires: xerces-c-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: libtirpc-devel

BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-breathe

# Run time dependency for gpsbabel driver
Requires:      gpsbabel

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

# We have multilib triage
%if "%{_lib}" == "lib"
  %global cpuarch 32
%else
  %global cpuarch 64
%endif

#TODO: Description on the lib?
%description
Geospatial Data Abstraction Library (GDAL/OGR) is a cross platform
C++ translator library for raster and vector geospatial data formats.
As a library, it presents a single abstract data model to the calling
application for all supported formats. It also comes with a variety of
useful commandline utilities for data translation and processing.

It provides the primary data access engine for many applications.
GDAL/OGR is the most widely used geospatial data access library.


%package devel
Summary:       Development files for the GDAL file format library
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for GDAL.


%package libs
Summary:       GDAL file format library
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14

%description libs
This package contains the GDAL file format library.


# No complete java yet in EL8
%if 0%{?rhel} < 8
%package java
Summary:        Java modules for the GDAL file format library
Requires:       jpackage-utils
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description java
The GDAL Java modules provide support to handle multiple GIS file formats.


%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.
%endif


%package perl
Summary:        Perl modules for the GDAL file format library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description perl
The GDAL Perl modules provide support to handle multiple GIS file formats.

%if %{with python2}
%package -n python2-gdal
%{?python_provide:%python_provide python2-gdal}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        Python modules for the GDAL file format library
Requires:       numpy
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python2-gdal
The GDAL Python modules provide support to handle multiple GIS file formats.
The package also includes a couple of useful utilities in Python.
%endif


%if %{with python3}
%package -n python3-gdal
%{?python_provide:%python_provide python3-gdal}
Summary:        Python modules for the GDAL file format library
Requires:       python3-numpy
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      gdal-python3 < 2.3.1
Provides:       gdal-python3 = %version-%release

%description -n python3-gdal
The GDAL Python 3 modules provide support to handle multiple GIS file formats.
%endif


%if %{with python2} || %{with python3}
%package python-tools
Summary:        Python tools for the GDAL file format library
Requires:       %{?with_python3:python3-gdal}%{?!with_python3:python2-gdal}

%description python-tools
The GDAL Python package provides number of tools for programming and
manipulating GDAL file format library
%endif


%package doc
Summary:        Documentation for GDAL
BuildArch:      noarch

%description doc
This package contains documentation for GDAL.

# We don't want to provide private Python extension libs
%if %{with python2} && %{with python3}
%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\.so$
%elif %{with python2}
%global __provides_exclude_from ^%{python2_sitearch}/.*\.so$
%elif %{with_python3}
%global __provides_exclude_from ^%{python3_sitearch}/.*\.so$
%endif



%prep
%autosetup -p1 -n %{name}-%{version}-fedora -a 1

# Delete bundled libraries
rm -rf frmts/zlib
rm -rf frmts/png/libpng
rm -rf frmts/gif/giflib
rm -rf frmts/jpeg/libjpeg
rm -rf frmts/jpeg/libjpeg12
rm -rf frmts/gtiff/libgeotiff
rm -rf frmts/gtiff/libtiff

# Copy in PROVENANCE.TXT-fedora
cp -p %SOURCE4 .

# Sanitize permissions
chmod 644 apps/gnmanalyse.cpp apps/gnmmanage.cpp

# Adjust check for LibDAP version
# http://trac.osgeo.org/gdal/ticket/4545
%if %cpuarch == 64
  sed -i 's|with_dods_root/lib|with_dods_root/lib64|' configure.ac
%endif

# Fix mandir
sed -i "s|^mandir=.*|mandir='\${prefix}/share/man'|" configure.ac

# Delete .doxygen_up_to_date, otherwise doxygen isn't run
rm -f doc/.doxygen_up_to_date


%build
# For future reference:
# epsilon: Stalled review -- https://bugzilla.redhat.com/show_bug.cgi?id=660024
# Building without pgeo driver, because it drags in Java
autoreconf -ifv

%configure \
	--with-autoload=%{_libdir}/%{name}plugins \
	--includedir=%{_includedir}/%{name}/ \
	--prefix=%{_prefix}         \
	--with-bash-completion      \
	--with-armadillo            \
	--with-curl                 \
	--with-cfitsio              \
	--with-dods-root=%{_prefix} \
	--with-expat                \
	--with-freexl               \
	--with-geos                 \
	--with-geotiff              \
	--with-gif                  \
	--with-gta                  \
	--with-hdf4                 \
	--with-hdf5                 \
	--with-jasper               \
%if 0%{?rhel} < 8
	--with-java                 \
%endif
	--with-jpeg                 \
	--with-libjson-c            \
	--without-jpeg12            \
	--with-liblzma              \
	--with-libtiff              \
	--with-libz                 \
	--without-mdb               \
	--without-msg               \
	%{mysql}                    \
	--with-netcdf               \
	--with-odbc                 \
	--with-ogdi                 \
	--with-openjpeg             \
	--with-pcraster             \
	--with-pg                   \
	--with-png                  \
	%{poppler}                  \
	--with-proj                 \
	%{spatialite}               \
	--with-sqlite3              \
	--with-threads              \
	--with-webp                 \
	--with-xerces               \
	--enable-shared             \
	--with-libkml

%make_build

# Build some utilities, as requested in BZ #1271906
make -C ogr/ogrsf_frmts/s57 all
make -C frmts/iso8211 all

# Documentation
make man
make docs

# No complete java yet in EL8
%if 0%{?rhel} < 8

# Make Java module and documentation
pushd swig/java
  make
  ant maven
popd
%mvn_artifact swig/java/build/maven/gdal-%version.pom swig/java/build/maven/gdal-%version.jar
%endif

# Make Python modules
pushd swig/python
  %{?with_python2:%py2_build}
  %{?with_python3:%py3_build}
popd

# Make Perl modules
pushd swig/perl
  perl Makefile.PL INSTALLDIRS=vendor
  %make_build
popd


%install
pushd swig/python
  %{?with_python2:%py2_install}
  %{?with_python3:%py3_install}
popd

%make_install -C swig/perl

%make_install install-man

# Drop gdal.pdf symlink, as we don't build the pdf documentation
rm doc/build/html/gdal.pdf

install -pm 755 ogr/ogrsf_frmts/s57/s57dump %{buildroot}%{_bindir}
install -pm 755 frmts/iso8211/8211createfromxml %{buildroot}%{_bindir}
install -pm 755 frmts/iso8211/8211dump %{buildroot}%{_bindir}
install -pm 755 frmts/iso8211/8211view %{buildroot}%{_bindir}
# Rename for %%files doc below
mv frmts/iso8211/html frmts/iso8211/iso8211_html

# Directory for auto-loading plugins
mkdir -p %{buildroot}%{_libdir}/%{name}plugins

#TODO: Don't do that?
rm %{buildroot}%{perl_archlib}/perllocal.pod

%if %{without python} && %{without python3}
rm %buildroot%_mandir/man1/{pct2rgb,rgb2pct}.1
%endif

# Correct permissions
#TODO and potential ticket: Why are the permissions not correct?
find %{buildroot}%{perl_vendorarch} -name "*.so" -exec chmod 755 '{}' \;
find %{buildroot}%{perl_vendorarch} -name "*.pm" -exec chmod 644 '{}' \;

# No complete java yet in EL8
%if 0%{?rhel} < 8
# install Java plugin
%mvn_install -J swig/java/java

# 775 on the .so?
# copy JNI libraries and links, non versioned link needed by JNI
# What is linked here?
mkdir -p %{buildroot}%{_jnidir}/%{name}
cp -pl swig/java/.libs/*.so*  \
    %{buildroot}%{_jnidir}/%{name}/
chrpath --delete %{buildroot}%{_jnidir}/%{name}/*jni.so*

# Install Java API documentation in the designated place
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr swig/java/java/org %{buildroot}%{_javadocdir}/%{name}
%endif

#TODO: Header date lost during installation
# Install multilib cpl_config.h bz#430894
install -p -D -m 644 port/cpl_config.h %{buildroot}%{_includedir}/%{name}/cpl_config-%{cpuarch}.h
# Create universal multilib cpl_config.h bz#341231
# The problem is still there in 1.9.
#TODO: Ticket?

#>>>>>>>>>>>>>
cat > %{buildroot}%{_includedir}/%{name}/cpl_config.h <<EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "gdal/cpl_config-32.h"
#else
#if __WORDSIZE == 64
#include "gdal/cpl_config-64.h"
#else
#error "Unknown word size"
#endif
#endif
EOF
#<<<<<<<<<<<<<
touch -r NEWS port/cpl_config.h


# Multilib gdal-config
# Rename the original script to gdal-config-$arch (stores arch-specific information)
# and create a script to call one or the other -- depending on detected architecture
# TODO: The extra script will direct you to 64 bit libs on
# 64 bit systems -- whether you like that or not
mv %{buildroot}%{_bindir}/%{name}-config %{buildroot}%{_bindir}/%{name}-config-%{cpuarch}
#>>>>>>>>>>>>>
cat > %{buildroot}%{_bindir}/%{name}-config <<EOF
#!/bin/bash

ARCH=\$(uname -m)
case \$ARCH in
x86_64 | ppc64 | ppc64le | ia64 | s390x | sparc64 | alpha | alphaev6 | aarch64 )
%{name}-config-64 \${*}
;;
*)
%{name}-config-32 \${*}
;;
esac
EOF
#<<<<<<<<<<<<<
touch -r NEWS %{buildroot}%{_bindir}/%{name}-config
chmod 755 %{buildroot}%{_bindir}/%{name}-config

#jni-libs and libgdal are also built static (*.a)
#.exists and .packlist stem from Perl
for junk in {*.a,*.la,*.bs,.exists,.packlist} ; do
  find %{buildroot} -name "$junk" -delete
done

# Don't duplicate license files
rm %{buildroot}%{_datadir}/%{name}/LICENSE.TXT


# No complete java yet in EL8
%if 0%{?rhel} < 8
%check
%if %{run_tests}
for i in -I/usr/lib/jvm/java/include{,/linux}; do
    java_inc="$java_inc $i"
done
%endif

pushd %{name}autotest-%{testversion}
	# Export test enviroment
	export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python2_sitearch}
	#TODO: Nötig?
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
	# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%%{buildroot}%%{_libdir}:$java_inc

	export GDAL_DATA=%{buildroot}%{_datadir}/%{name}/

	# Enable these tests on demand
	#export GDAL_RUN_SLOW_TESTS=1
	#export GDAL_DOWNLOAD_TEST_DATA=1

	# Remove some test cases that would require special preparation
	rm -rf ogr/ogr_pg.py # No database available
	rm -rf ogr/ogr_mysql.py # No database available
	rm -rf osr/osr_esri.py # ESRI datum absent
	rm -rf osr/osr_erm.py # File from ECW absent

	# Run tests but force normal exit in the end
	./run_all.py || true
popd
%endif
#%%{run_tests}


%ldconfig_scriptlets libs


%files
%{_bindir}/gdallocationinfo
%{_bindir}/gdal_contour
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdaladdo
%{_bindir}/gdalinfo
%{_bindir}/gdaldem
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaltindex
%{_bindir}/gdalwarp
%{_bindir}/gdal_grid
%{_bindir}/gdalenhance
%{_bindir}/gdalmanage
%{_bindir}/gdalserver
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltransform
%{_bindir}/nearblack
%{_bindir}/gdal_viewshed
%{_bindir}/gdalmdiminfo
%{_bindir}/gdalmdimtranslate
%{_bindir}/ogr*
%{_bindir}/8211*
%{_bindir}/s57*
%{_bindir}/testepsg
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/gdal*.1*
%exclude %{_mandir}/man1/gdal-config.1*
%exclude %{_mandir}/man1/gdal2tiles.1*
%exclude %{_mandir}/man1/gdal_fillnodata.1*
%exclude %{_mandir}/man1/gdal_merge.1*
%exclude %{_mandir}/man1/gdal_retile.1*
%exclude %{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr*.1*
%{_mandir}/man1/gnm*.1.*


%files libs
%doc LICENSE.TXT NEWS PROVENANCE.TXT COMMITTERS PROVENANCE.TXT-fedora
%{_libdir}/libgdal.so.27
%{_libdir}/libgdal.so.27.*
%{_datadir}/%{name}
#TODO: Possibly remove files like .dxf, .dgn, ...
%dir %{_libdir}/%{name}plugins

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-config-%{cpuarch}
%{_mandir}/man1/gdal-config.1*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

# No complete java yet in EL8
%if 0%{?rhel} < 8
# Can I even have a separate Java package anymore?
%files java -f .mfiles
%doc swig/java/apps
%{_jnidir}/%{name}/libgdalalljni.so*

%files javadoc -f .mfiles-javadoc
%endif

%files perl
%doc swig/perl/README
%{perl_vendorarch}/*
%{_mandir}/man3/*.3pm*

%if %{with python2}
%files -n python2-gdal
%doc swig/python/README.rst
%doc swig/python/samples
%{python2_sitearch}/osgeo
%{python2_sitearch}/GDAL-%{version}-py*.egg-info
%{python2_sitearch}/osr.py*
%{python2_sitearch}/ogr.py*
%{python2_sitearch}/gdal*.py*
%endif

%if %{with python3}
%files -n python3-gdal
%doc swig/python/README.rst
%doc swig/python/samples
%{python3_sitearch}/osgeo
%{python3_sitearch}/GDAL-%{version}-py*.egg-info
%{python3_sitearch}/osr.py
%{python3_sitearch}/__pycache__/osr.*.py*
%{python3_sitearch}/ogr.py
%{python3_sitearch}/__pycache__/ogr.*.py*
%{python3_sitearch}/gdal*.py
%{python3_sitearch}/__pycache__/gdal*.*.py*
%endif

%if %{with python2} || %{with python3}
%files python-tools
%_bindir/*.py
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%endif

%files doc
%doc doc/build/html frmts/iso8211/iso8211_html

#TODO: jvm
#Should be managed by the Alternatives system and not via ldconfig
#The MDB driver is said to require:
#Download jackcess-1.2.2.jar, commons-lang-2.4.jar and
#commons-logging-1.1.1.jar (other versions might work)
#If you didn't specify --with-jvm-lib-add-rpath at
#Or as before, using ldconfig

%changelog
* Fri Oct 16 21:25:24 CEST 2020 Sandro Mani <manisandro@gmail.com> - 3.1.3-2
- Rebuild (jasper)

* Mon Sep 07 2020 Sandro Mani <manisandro@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 09:48:50 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.1.2-5
- Rebuild (poppler)

* Thu Jul 16 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.2-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jul 15 15:55:55 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.1.2-3
- Rebuild (poppler)

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jul 07 2020 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.0-5
- Perl 5.32 re-rebuild updated packages

* Fri Jun 26 2020 Orion Poplawski <orion@nwra.com> - 3.1.0-4
- Rebuild for hdf5 1.10.6

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.0-3
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Sat May 09 2020 Markus Neteler <neteler@mundialis.de> - 3.0.4-5
* disabled JAVA and LaTeX support for EPEL8, due to (yet) missing dependencies

* Wed Apr 22 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.4-4
- Re-enable annobin

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.4-3
- Rebuild (json-c)
- Temporarily disable annobin, as it is broken

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.0.4-2
- Fix libtool wrappers installed for gdal utilities instead of actual binaries

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rich Mattes <richmattes@gmail.com> - 2.3.2-15
- Patch out include that was removed in newer poppler
- Remove comment following an endif in the specfile

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.2-15
- F-32: rebuild against new poppler

* Tue Sep 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.2-14
- Fix linkage against Proj

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 2.3.2-13
- Bump proj_somaj for proj 6

* Wed Sep 4 2019 Devrim Gündüz <devrim@gunduzorg> - 2.3.2-12
- Rebuild for new Proj

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.2-9
- Perl 5.30 rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Tue Feb 05 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-7
- Drop Python 2 subpackage for mass Python 2 packages removal

* Mon Feb 04 2019 Pavel Raiskup <praiskup@redhat.com> - 2.3.2-6
- modernize java packaging (PR#9)

* Mon Feb 04 2019 Devrim Gündüz <devrim@gunduzorg> - 2.3.2-6
- Rebuild for new GeOS and Proj

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Marek Kasik <mkasik@redhat.com> - 2.3.2-4
- Additional fixes for the rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 2.3.2-3
- Rebuild for poppler-0.73.0

* Thu Oct 04 2018 Pavel Raiskup <praiskup@redhat.com> - 2.3.2-2
- Python 3 is the default Python now

* Mon Oct  1 2018 Volker Fröhlich <volker27@gmx.at> - 2.3.2-1
- New upstream release

* Mon Aug 27 2018 José Abílio Matos <jamatos@fc.up.pt> - 2.3.1-3
- rebuild for armadillo soname bump (take 2)

* Fri Aug 17 2018 José Abílio Matos <jamatos@fc.up.pt> - 2.3.1-2
- rebuild for armadillo soname bump

* Tue Aug 14 2018 Volker Fröhlich <volker27@gmx.at> - 2.3.1-1
- New upstream release

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 2.2.4-10
- Rebuild for poppler-0.67.0

* Wed Jul 25 2018 Devrim Gündüz <devrim@gunduz.org> - 2.2.4-9
- Fix #1606875

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 2.2.4-7
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.4-6
- Perl 5.28 rebuild

* Fri Jun 22 2018 Orion Poplawski <orion@nwra.com> - 2.2.4-5
- Rebuild for libdap 3.19.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-4
- Rebuilt for Python 3.7

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.2.4-3
- rebuilt for cfitsio 3.450

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.4-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Mon Mar 26 2018 Volker Fröhlich <volker27@gmx.at> - 2.2.4-1
- New upstream release

* Fri Mar 23 2018 Adam Williamson <awilliam@redhat.com> - 2.2.3-14
- Rebuild for poppler 0.63.0

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.3-13
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.2.3-12
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 2.2.3-11
- rebuild for poppler 0.62.0

* Wed Feb 14 2018 Volker Fröhlich <volker27@gmx.at> - 2.2.3-10
- Don't own /etc/bash_completion.d (BZ#1545012)

* Tue Feb 13 2018 Pavel Raiskup <praiskup@redhat.com> - 2.2.3-9
- silence some rpmlint warnings

* Tue Feb 13 2018 Tom Hughes <tom@compton.nu> - 2.2.3-8
- Add patch for bug by node-gdal tests and fixed upstream

* Tue Feb 13 2018 Tom Hughes <tom@compton.nu> - 2.2.3-7
- Use libtirpc for RPC routines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Than Ngo <than@redhat.com> - - 2.2.3-6
- cleanup condition

* Thu Dec 14 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.2.3-5
- Cleanup spec file conditionals

* Thu Dec 14 2017 Pavel Raiskup <praiskup@redhat.com> - 2.2.3-4
- drop bootstrap mode
- build-require mariadb-connector-c-devel (rhbz#1494096)

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.3-3.1.bootstrap
- Add patch to cleanly build against json-c v0.13

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.3-2.1.bootstrap
- Rebuilt for libjson-c.so.3

* Mon Dec 04 2017 Volker Froehlich <volker27@gmx.at> - 2.2.3-1
- New upstream release

* Wed Nov 29 2017 Volker Froehlich <volker27@gmx.at> - 2.2.2-2
- Re-enable bsb format (BZ#1432330)

* Fri Sep 22 2017 Volker Froehlich <volker27@gmx.at> - 2.2.2-1
- New upstream release
- Add new entries to the files sections

* Sun Sep 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.4-11
- rebuild (armadillo)

* Mon Sep 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.4-10
- support %%bootstrap mode, enable for rawhide (#1490492)
- segment POPPLER_OPTS, makes buildable on f25

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 2.1.4-9
- rebuild for poppler 0.59.0

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.4-8
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Orion Poplawski <orion@cora.nwra.com> - 2.1.4-7
- Handle new g2clib name in Fedora 27+

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.4-6
- Python 2 binary package renamed to python2-gdal
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 2.1.4-5
- rebuild for poppler 0.57.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Adam Williamson <awilliam@redhat.com> - 2.1.4-2
- Rebuild against MariaDB 10.2
- BuildRequires: javapackages-local, for a macro that got moved there

* Sat Jul 01 2017 Volker Froehlich <volker27@gmx.at> - 2.1.4-1
- New upstream release

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-4
- Perl 5.26 rebuild

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 2.1.3-3
- rebuild for poppler 0.53.0

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.1.3-2
- Rebuild (libwebp)

* Fri Jan 27 2017 Volker Froehlich <volker27@gmx.at> - 2.1.3-1
- New upstream release
- Don't run tests by default (BZ #1260151)

* Tue Jan 24 2017 Devrim Gündüz <devrim@gunduz.org> - 2.1.2-6
- Rebuilt for proj 4.9.3
- Fix many rpmlint warnings/errors.
- Add a workaround for the pkg-config change in rawhide.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuild for Python 3.6

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 2.1.2-4
- rebuild for poppler 0.50.0

* Thu Dec 01 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.2-3
- Rebuild for jasper 2.0
- Add patch to fix build with jasper 2.0

* Wed Nov 23 2016 David Tardon <dtardon@redhat.com> - 2.1.2-2
- rebuild for poppler 0.49.0

* Sun Oct 30 2016 Volker Froehlich <volker27@gmx.at> - 2.1.2-1
- New upstream release

* Sat Oct 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-2
- Use system libjson-c

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 2.1.1-2
- Rebuild for poppler-0.48.0

* Fri Aug 12 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-1
- Update to 2.1.1
- Add patch to fix bash-completion installation and install it (bug #1337143)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 2.1.0-7
- Rebuild for poppler-0.45.0

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.0-6
- Perl 5.24 rebuild

* Mon May 09 2016 Volker Froehlich <volker27@gmx.at> - 2.1.0-5
- Add missing BR for libkml

* Fri May 06 2016 Sandro Mani <manisandro@gmail.com>- 2.1.0-4
- Enable libKML support
  Resolves: #1332008

* Tue May 03 2016 Adam Williamson <awilliam@redhat.com> - 2.1.0-3
- rebuild for updated poppler

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 2.1.0-2
- Rebuild for poppler-0.43.0

* Mon May 02 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 2.1.0-1
- New upstream release

* Mon Apr 18 2016 Tom Hughes <tom@compton.nu> - 2.0.2-5
- Rebuild for libdap change Resoloves: #1328104

* Tue Feb 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-4
- Add Python 3 support

* Sun Feb 14 2016 Volker Froehlich <volker27@gmx.at> - 2.0.2-3
- Add patch for GDAL issue #6360

* Mon Feb 08 2016 Volker Froehlich <volker27@gmx.at> - 2.0.2-2
- Rebuild for armadillo 6

* Thu Feb 04 2016 Volker Froehlich <volker27@gmx.at> - 2.0.2-1
- New upstream release
- Fix geos support (BZ #1284714)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> 2.0.1-5
- Rebuild for poppler-0.40.0

* Fri Jan 15 2016 Adam Jackson <ajax@redhat.com> 2.0.1-4
- Rebuild for libdap soname bump

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.1-3
- Rebuilt for libwebp soname bump

* Sun Oct 18 2015 Volker Froehlich <volker27@gmx.at> - 2.0.1-2
- Solve BZ #1271906 (Build iso8211 and s57 utilities)

* Thu Sep 24 2015 Volker Froehlich <volker27@gmx.at> - 2.0.1-1
- Updated for 2.0.1; Add Perl module manpage

* Wed Sep 23 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-5
- Rebuild for libdap 3.15.1

* Sun Sep 20 2015 Volker Froehlich <volker27@gmx.at> - 2.0.0-4
- Support openjpeg2

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-3
- Rebuilt for Boost 1.59

* Sun Aug 09 2015 Jonathan Wakely <jwakely@redhat.com> 2.0.0-2
- Patch to set _XOPEN_SOURCE correctly (bug #1249703)

* Sun Jul 26 2015 Volker Froehlich <volker27@gmx.at> - 2.0.0-1
- Disable charls support due to build issues
- Solve a string formatting and comment errors in the Perl swig template

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> - 1.11.2-12
- Rebuild (poppler-0.34.0)

* Fri Jul  3 2015 José Matos <jamatos@fedoraproject.org> - 1.11.2-11
- Rebuild for armadillo 5(.xxx.y)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Volker Fröhlich <volker27@gmx.at> - 1.11.2-9
- Rebuild for Perl's dropped module_compat_5.20.*

* Tue Jun 09 2015 Dan Horák <dan[at]danny.cz> - 1.11.2-8
- add upstream patch for poppler >= 31

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.2-7
- Perl 5.22 rebuild

* Thu May 21 2015 Devrim Gündüz <devrim@gunduz.org> - 1.11.2-6
- Fix proj soname in ogr/ogrct.cpp. Patch from Sandro Mani
  <manisandro @ gmail.com>  Fixes #1212215.

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.11.2-5
- Rebuild for hdf5 1.8.15

* Sat Apr 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.11.2-4
- Rebuild for gcc-5.0.1 ABI changes.

* Tue Mar 31 2015 Orion Poplawski <orion@cora.nwra.com> - 1.11.2-3
- Rebuild for g2clib fix

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> - 1.11.2-2
- Rebuilt for proj 4.9.1

* Tue Feb 17 2015 Volker Fröhlich <volker27@gmx.at> - 1.11.2-1
- New release
- Remove obsolete sqlite patch

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> - 1.11.1-6
- Rebuild (poppler-0.30.0)

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.11.1-5
- Rebuild for hdf5 1.8.4

* Sat Dec  6 2014 Volker Fröhlich <volker27@gmx.at> - 1.11.1-4
- Apply upstream changeset 27949 to prevent a crash when using sqlite 3.8.7

* Tue Dec  2 2014 Jerry James <loganjerry@gmail.com> - 1.11.1-3
- Don't try to install perllocal.pod (bz 1161231)

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> - 1.11.1-3
- Rebuild (poppler-0.28.1)

* Fri Nov 14 2014 Dan Horák <dan[at]danny.cz> - 1.11.1-2
- update gdal-config for ppc64le

* Thu Oct  2 2014 Volker Fröhlich <volker27@gmx.at> - 1.11.1-1
- New release
- Correct test suite source URL

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.0-9
- Perl 5.20 rebuild

* Mon Aug 25 2014 Devrim Gündüz <devrim@gunduz.org> - 1.11.0-7
- Rebuilt for libgeotiff

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Volker Fröhlich <volker27@gmx.at> - 1.11.0-6
- Add aarch64 to gdal-config script (BZ#1129295)

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.0-5
- rebuild (libspatialite)

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 1.11.0-4
- Rebuild for libgeotiff 1.4.0

* Fri Jul 11 2014 Orion Poplawski <orion@cora.nwra.com> - 1.11.0-3
- Rebuild for libdap 3.13.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Volker Fröhlich <volker27@gmx.at> - 1.11.0-1
- New upstream release
- Remove libgcj as BR, as it no longer exists in F21
- Re-enable ogdi and spatialite where possible
- Adapt Python-BR to python2-devel
- Obsolete Ruby bindings, due to the suggestion of Even Rouault
- Preserve timestamp of Fedora README file
- Explicitly create HTML documentation with Doxygen
- Make test execution conditional
- Truncate changelog

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.10.1-6
- Use Requires: java-headless rebuild (#1067528)

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-5
- Rebuild for armadillo soname bump

* Wed Jan 08 2014 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-4
- Rebuild for cfitsio 3.360

* Thu Jan 02 2014 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-3
- Rebuild for libwebp soname bump

* Sat Sep 21 2013 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-2
- Rebuild to pick up atlas 3.10 changes

* Sun Sep  8 2013 Volker Fröhlich <volker27@gmx.at> - 1.10.1-1
- New upstream release

* Fri Aug 23 2013 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-1
- Update to 1.10.0
- Enable PCRE support
- Drop man patch applied upstream
- Drop dods patch fixed upstream
- Add more tex BRs to handle changes in texlive packaging
- Fix man page install location

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 1.9.2-12
- Rebuild (poppler-0.24.0)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.9.2-10
- Perl 5.18 rebuild

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.2-9
- Rebuild for cfitsio 3.350

* Mon Jun 24 2013 Volker Fröhlich <volker27@gmx.at> - 1.9.2-8
- Rebuild for poppler 0.22.5

* Wed Jun 12 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.2-7
- Update Java/JNI for new guidelines, also fixes bug #908065

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.2-6
- Rebuild for hdf5 1.8.11

* Mon Apr 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.2-5
- Rebuild for ARM libspatialite issue

* Tue Mar 26 2013 Volker Fröhlich <volker27@gmx.at> - 1.9.2-4
- Rebuild for cfitsio 3.340

* Sun Mar 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.2-3
- rebuild (libcfitsio)

* Wed Mar 13 2013 Vít Ondruch <vondruch@redhat.com> - 1.9.2-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sun Mar 10 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.2-1
- Update to 1.9.2
- Drop poppler and java-swig patches applied upstream

* Fri Jan 25 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.9.1-18
- Rebuild with geos 3.3.7.

* Mon Jan 21 2013 Volker Fröhlich <volker27@gmx.at> - 1.9.1-17
- Rebuild due to libpoppler 0.22

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.9.1-16
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 28 2012 Richard W.M. Jones <rjones@redhat.com> - 1.9.1-15
- Rebuild, see
  http://lists.fedoraproject.org/pipermail/devel/2012-December/175685.html

* Thu Dec 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.1-14
- Tweak -fpic CFLAGS to fix FTBFS on ARM

* Mon Dec  3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.1-13
- Rebuild for hdf5 1.8.10

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> - 1.9.1-12
- Rebuild for libspatialite soname bump

* Thu Aug  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-11
- Correct and extend conditionals for ppc andd ppc64, considering libspatialite
  Related to BZ #846301

* Sun Jul 29 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-10
- Use the correct shell idiom "if true" instead of "if 1"

* Sun Jul 29 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-9
- Ignore for the moment the test for armadillo (to be removed after gcc 4.7.2 release)

* Fri Jul 27 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-8
- Rebuild for new armadillo

* Fri Jul 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.1-7
- Build with PIC

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.9.1-5
- Perl 5.16 rebuild

* Sat Jul  7 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-4
- Delete unnecessary manpage, that seems to be created with
  new Doxygen (1.8.1 or 1.8.1.1)

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 1.9.1-3
- Rebuild (poppler-0.20.1)

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.9.1-2
- Perl 5.16 rebuild

* Wed May 23 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-1
- New upstream release
- Update poppler patch
- Add cleaner script

* Sun May 20 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-5
- Patches for libpoppler 0.20, libdap 3.11.3 and swig 2.0.6

* Thu May 10 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-4
- Correct provides-filtering as of https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Usage
- Support webp
- Remove bogus libjpeg-turbo conditional
- Update Ruby ABI version to 1.9.1
- Install Ruby bindings to vendorarchdir on F17 and later
- Conditionals for Ruby specific elements for versions prior F17 and for EPEL
- Correct quotes for CFLAGS and Ruby
- Disable ogdi, until BZ#816282 is resolved

* Wed Apr 25 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-2
- Rebuild for cfitsio 3.300

* Sun Feb 26 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-1
- Completely re-work the original spec-file
  The major changes are:
- Add a libs sub-package
- Move Python scripts to python sub-package
- Install the documentation in a better way and with less slack
- jar's filename is versionless
- Update the version in the Maven pom automatically
- Add a plugins directory
- Add javadoc package and make the man sub-package noarch
- Support many additional formats
- Drop static sub-package as no other package uses it as BR
- Delete included libs before building
- Drop all patches, switch to a patch for the manpages, patch for JAVA path
- Harmonize the use of buildroot and RPM_BUILD_ROOT
- Introduce testversion macro

* Sun Feb 19 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-14
- Require Ruby abi
- Add patch for Ruby 1.9 include dir, back-ported from GDAL 1.9
- Change version string for gdal-config from <version>-fedora to
  <version>
- Revert installation path for Ruby modules, as it proofed wrong
- Use libjpeg-turbo

* Thu Feb  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-13
- Rebuild for Ruby 1.9
  http://lists.fedoraproject.org/pipermail/ruby-sig/2012-January/000805.html

* Tue Jan 10 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-12
- Remove FC10 specific patch0
- Versioned MODULE_COMPAT_ Requires for Perl (BZ 768265)
- Add isa macro to base package Requires
- Remove conditional for xerces_c in EL6, as EL6 has xerces_c
  even for ppc64 via EPEL
- Remove EL4 conditionals
- Replace the python_lib macro definition and install Python bindings
  to sitearch directory, where they belong
- Use correct dap library names for linking
- Correct Ruby installation path in the Makefile instead of moving it later
- Use libdir variable in ppc64 Python path
- Delete obsolete chmod for Python libraries
- Move correction for Doxygen footer to prep section
- Delete bundled libraries before building
- Build without bsb and remove it from the tarball
- Use mavenpomdir macro and be a bit more precise on manpages in
  the files section
- Remove elements for grass support --> Will be replaced by plug-in
- Remove unnecessary defattr
- Correct version number in POM
- Allow for libpng 1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.3-11
- Rebuild for new libpng

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-10
- Rebuild for hdf5 1.8.7

* Fri Apr 22 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-9
- Patched spaces problem for Mapinfo files (mif)
  (http://trac.osgeo.org/gdal/ticket/3694)
- Replaced all define macros with global
- Corrected ruby_sitelib to ruby_sitearch
- Use python_lib and ruby_sitearch instead of generating lists
- Added man-pages for binaries
- Replaced mkdir and install macros
- Removed Python files from main package files section, that
  effectively already belonged to the Python sub-package

* Mon Apr 11 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-8
- Solved image path problem with Latex
- Removed with-tiff and updated with-sqlite to with-sqlite3
- Add more refman documents
- Adapted refman loop to actual directories
- Harmonized buildroot macro use

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-7
- Rebuild for netcdf 4.1.2

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.7.3-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Sun Mar 20 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-5
- Dropped unnecessary encoding conversion for Russian refman
- Install Russian refman
- Don't try to install refman for sdts and dgn, as they fail to compile
- Added -p to post and postun
- Remove private-shared-object-provides for Python and Perl
- Remove installdox scripts
- gcc 4.6 doesn't accept -Xcompiler

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.7.3-4
- Rebuilt with xerces-c 3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.7.3-2
- Install all the generated pdf documentation.
- Build documentation as a separate package.
- Spec cleanup

* Fri Nov 19 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.7.3-1
- Update to latest upstream version
- Added jnis
- Patches updated with proper version info
- Added suggestions from Ralph Apel <r.apel@r-apel.de>
	+ Versionless symlink for gdal.jar
	+ Maven2 pom
	+ JPP-style depmap
	+ Use -f XX.files for ruby and python
