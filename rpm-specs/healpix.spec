%global release_date 2018Dec10

%global majornum 0

Name:           healpix
Version:        3.50
Release:        6%{?dist}
Summary:        Hierarchical Equal Area isoLatitude Pixelization of a sphere

License:        GPLv2+
URL:            http://healpix.jpl.nasa.gov/
Source0:        http://downloads.sourceforge.net/project/healpix/Healpix_%{version}/Healpix_%{version}_%{release_date}.tar.gz
Source1:        Makefile_f

Patch0:         healpix-3.31-java-use-system-libraries.patch
Patch1:         javadoc.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfitsio-devel
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libtool

# Java
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  nom-tam-fits

%description
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains Fortran binaries and libraries.

NB. Due to some generic names, the binaries have been renamed to start with
hp_, e.g. anafast is now hp_anafast.


%package devel
Summary:        Healpix Fortran headers
Requires:       %{name} = %{version}-%{release}
Requires:	gcc-gfortran

%description devel
This package contains the Fortran module files needed to compile against
the HEALPix Fortran libraries.


%package c++
Summary:        Healpix C++ binaries and libraries

%description c++
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains HEALPix binaries and libraries that are written in C++.

NB. Due to some generic names, the binaries have been renamed to start with
hp_, e.g. anafast is now hp_anafast.


%package c++-devel
Summary:        Healpix C++ headers
Requires:       %{name}-c++ = %{version}-%{release}

%description c++-devel
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains development headers for the C++ part of HEALPix.


%package -n c%{name}
Summary:        HEALPix C Bindings Library

%description -n c%{name}
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the library for tools that use HEALPix C bindings.


%package -n c%{name}-devel
Summary:        HEALPix C Bindings Library development files
Requires:       c%{name} = %{version}-%{release}

%description -n c%{name}-devel
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the C include file for development with HEALPix.


%package java
Summary:        Java version of HEALPix
BuildArch:      noarch
Requires:       java
Requires:       jpackage-utils
Requires:       nom-tam-fits

%description java
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the Java version of HEALPix.


%package javadoc
Summary:        Javadocs for %{name}
BuildArch:      noarch
Requires:       jpackage-utils

%description javadoc
This package contains the Java API documentation for %{name}.



%prep
%setup -q -n Healpix_%{version}
%patch0 -p1
%patch1 -p0
cp %{SOURCE1} Makefile
mkdir binf libf includef
pushd libf
%__ln_s libhealpix.so.%{majornum} libhealpix.so
%__ln_s libhpxgif.so.%{majornum} libhpxgif.so
%__ln_s libsharp_healpix_f.so.%{majornum} libsharp_healpix_f.so
popd

%build
### Fortran build
make F90_FFLAGS="%{optflags} -DGFORTRAN  \
      -fopenmp -fPIC " SHLIB_SUFFIX=".so.%{majornum}" \
      F90_CFLAGS="%{optflags} -std=c99 -DgFortran -fopenmp -fPIC"

### C bindings
pushd src/C/autotools
autoreconf -fi
%configure --enable-static=no
make
popd

### C++ bindings
pushd src/cxx/autotools
autoreconf -fi
%configure --enable-static=no
make
popd

### Java build
pushd src/java
# We don't want to have prebuilt bundled jars!
rm lib/*.jar
ant
popd

%install
pushd src/C/autotools
%make_install
popd

pushd src/cxx/autotools
%make_install
popd

# Rename binaries to have prefix hp_
pushd %{buildroot}%{_bindir}
for exec in *; do
        mv $exec hp_$exec
done
popd

#Fortran
pushd binf
install -d %{buildroot}%{_bindir}
install -D -m 755 alteralm %{buildroot}%{_bindir}/hp_alteralm
install -D -m 755 anafast %{buildroot}%{_bindir}/hp_anafast
install -D -m 755 hotspot %{buildroot}%{_bindir}/hp_hotspot
install -D -m 755 map2gif %{buildroot}%{_bindir}/hp_map2gif
install -D -m 755 median_filter %{buildroot}%{_bindir}/hp_median_filter
install -D -m 755 plmgen %{buildroot}%{_bindir}/hp_plmgen
install -D -m 755 process_mask %{buildroot}%{_bindir}/hp_process_mask
install -D -m 755 sky_ng_sim %{buildroot}%{_bindir}/hp_sky_ng_sim
install -D -m 755 sky_ng_sim_bin %{buildroot}%{_bindir}/hp_sky_ng_sim_bin
install -D -m 755 smoothing %{buildroot}%{_bindir}/hp_smoothing
install -D -m 755 synfast %{buildroot}%{_bindir}/hp_synfast
install -D -m 755 ud_grade %{buildroot}%{_bindir}/hp_ud_grade
popd

pushd libf
install -d %{buildroot}%{_libdir}
install -D -m 755 libhealpix.so.%{majornum} %{buildroot}%{_libdir}
install -D -m 755 libhpxgif.so.%{majornum} %{buildroot}%{_libdir}
install -D -m 755 libsharp_healpix_f.so.%{majornum} %{buildroot}%{_libdir}
popd
pushd %{buildroot}%{_libdir}
ln -s libhealpix.so.%{majornum} libhealpix.so
ln -s libhpxgif.so.%{majornum} libhpxgif.so
ln -s libsharp_healpix_f.so.%{majornum} libsharp_healpix_f.so
popd

pushd includef
install -d %{buildroot}/%{_fmoddir}/healpix
install -D -m 644 *.mod %{buildroot}/%{_fmoddir}/healpix
popd

# remove unwanted files
rm -f %{buildroot}%{_includedir}/healpix_cxx/sharp_geomhelpers.c
rm -f %{buildroot}%{_libdir}/*.la

# remove rpath from binaries
chrpath -d %{buildroot}%{_bindir}/*


### Java install
pushd src/java
mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/jhealpix.jar %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}
cp -rp doc %{buildroot}%{_javadocdir}/%{name}
popd

%ldconfig_scriptlets


%ldconfig_scriptlets c++


%ldconfig_scriptlets -n c%{name}


%files
%license COPYING READ_Copyrights_Licenses.txt
%{_bindir}/hp_alteralm
%{_bindir}/hp_anafast
%{_bindir}/hp_hotspot
%{_bindir}/hp_map2gif
%{_bindir}/hp_median_filter
%{_bindir}/hp_plmgen
%{_bindir}/hp_sky_ng_sim
%{_bindir}/hp_sky_ng_sim_bin
%{_bindir}/hp_smoothing
%{_bindir}/hp_synfast
%{_bindir}/hp_ud_grade
%{_bindir}/hp_compute_weights
%{_bindir}/hp_needlet_tool
%{_libdir}/libhealpix.so.*
%{_libdir}/libhpxgif.so.*
%{_libdir}/libsharp_healpix_f.so.*


%files devel
%{_libdir}/libhealpix.so
%{_libdir}/libhpxgif.so
%{_libdir}/libsharp_healpix_f.so
%{_fmoddir}/healpix/


%files c++
%license COPYING READ_Copyrights_Licenses.txt
%{_bindir}/hp_alm2map_cxx
%{_bindir}/hp_anafast_cxx
%{_bindir}/hp_calc_powspec
%{_bindir}/hp_hotspots_cxx
%{_bindir}/hp_map2tga
%{_bindir}/hp_median_filter_cxx
%{_bindir}/hp_mult_alm
%{_bindir}/hp_process_mask
%{_bindir}/hp_rotalm_cxx
%{_bindir}/hp_smoothing_cxx
%{_bindir}/hp_syn_alm_cxx
%{_bindir}/hp_udgrade_cxx
%{_bindir}/hp_udgrade_harmonic_cxx
%{_libdir}/libhealpix_cxx.so.*


%files c++-devel
%{_libdir}/libhealpix_cxx.so
%dir %{_includedir}/healpix_cxx
%{_includedir}/healpix_cxx/*.h
%{_libdir}/pkgconfig/healpix_cxx.pc


%files -n chealpix
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/libchealpix.so.*


%files -n chealpix-devel
%{_libdir}/libchealpix.so
%{_includedir}/chealpix.h
%{_libdir}/pkgconfig/chealpix.pc

%files java
%license COPYING READ_Copyrights_Licenses.txt
%{_javadir}/jhealpix.jar

%files javadoc
%license COPYING READ_Copyrights_Licenses.txt
%{_javadocdir}/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.50-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.50-4
- Disable javadoc for jdk11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.50-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 3.31-11
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 3.31-10
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Christian Dersch <lupinix@mailbox.org> - 3.31-8
- rebuilt for GCC 8.x (gfortran soname bump)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Apr 15 2017 Christian Dersch <lupinix@mailbox.org> - 3.31-4
- enabled java build

* Fri Apr 07 2017 Christian Dersch <lupinix@mailbox.org> - 3.31-3
- disabled parallel build
- have ppc64 in again, no more ExcludeArch

* Wed Apr 05 2017 Christian Dersch <lupinix@mailbox.org> - 3.31-2
- fix: delete rpath from binaries

* Wed Apr 05 2017 Christian Dersch <lupinix@mailbox.org> - 3.31-1
- new version
- modernized spec (removed obsolete group tags, use license macro)

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.13a-20
- Rebuilt for libgfortran soname bump

* Thu Mar 03 2016 Jon Ciesla <limburgher@gmail.com> - 2.13a-19
- Fix FTBFS, BZ 1307613.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.13a-16
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Jon Ciesla <limburgher@gmail.com> - 2.13a-13
- cfitsio rebuild.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Jon Ciesla <limburgher@gmail.com> - 2.13a-11
- cfitsio rebuild.

* Fri Mar 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.13a-10
- cfitsio rebuild.

* Wed Mar 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.13a-9
- cfitsio rebuild.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.13a-7
- Fix build to pass as-needed to the linker, as it should

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 2.13a-2
- Fix build

* Sun Dec 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.13a-1
- Update to upstream 2.13a.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.12a-1
- Update to upstream 2.12a.

* Mon Jul 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.11c-7
- Move modules to %%{_fmoddir}.
- Add missing documentation to -c++ package.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 2.11c-5
- Minor style adjustments
- Don't override sane gcc flags
- Moved tests to -devel packages
- C++ -devel doesn't depend on fortran ones anymore
- mkdir with -p to allow short-circuit builds
- Fix build with GCC 4.4

* Sat Apr 04 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.11c-4
- Review fixes.
- Add C++ bindings, rename C++ and Fortran binaries (general names!).

* Fri Apr 03 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 2.11c-3
- Build Fortran library as DSO

* Thu Mar 26 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.11c-2
- Add Fortran bindings.

* Wed Mar 25 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 2.11c-1
- Initial packaging of the C bindings
