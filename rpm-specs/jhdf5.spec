Name:           jhdf5
Version:        3.3.2
Release:        4%{?dist}
Summary:        Java HDF5 Package
License:        BSD with advertising
URL:            https://support.hdfgroup.org/products/java/
Source0:        https://support.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/hdfjni-%{version}/src/HDFJava-%{version}-Source.tar.gz

Patch1:         jhdf5-0001-add-a-generic-linux-host.patch
Patch3:         jhdf5-0003-use-system-linker-for-shared-library.patch
Patch4:         libdf.diff

BuildRequires:  autoconf
BuildRequires:  sed
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  libjpeg-devel
BuildRequires:  slf4j

BuildRequires:  junit
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils

Requires:       java-headless
Requires:       javapackages-tools
Requires:       slf4j
# hdf5 does not bump soname but check at runtime
Requires:       hdf5 = %{_hdf5_version}

%global _description %{expand:
HDF is a versatile data model that can represent very complex data objects
and a wide variety of meta-data. It is a completely portable file format
with no limit on the number or size of data objects in the collection.}

%description %_description

This Java package wraps the native HDF5 library.

%package devel
Summary:        JHDF5 development files
Requires:       %{name} = %{version}-%{release}
Requires:       hdf5-devel

%description devel
JHDF5 development headers and libraries.

%package -n jhdf
Summary:        Java HDF Package
Requires:       java-headless
Requires:       javapackages-tools
Requires:       slf4j

%description -n jhdf %_description

This Java package wraps the native HDF4 library.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -n hdfjava-%{version} -p1

# remove useless writability check
sed -r -i '/-d "\$JH45INST"/ {N; N; N; N; N; N; d;}' configure

# remove shipped jars
find -name '*.jar' -print -delete

# build jar repo
build-jar-repository -p lib/ junit slf4j-
ln -s slf4j-api.jar lib/slf4j-api-1.7.5.jar
ln -s slf4j-nop.jar lib/slf4j-nop-1.7.5.jar

# Prevent javadoc build failure
sed -i 's/$(JAVADOC_FLAGS)/$(JAVADOC_FLAGS) -Xdoclint:none/' Makefile*

# Add missing H4_ prefixes, also
# neuter H5_VERS_RELEASE check (the number has gone down in recent releases!)
find . -name \*.c -type f \( \
     -exec grep -q -P '\bMAX_(NC_NAME|VAR_DIMS)\b' {} \; -print \
     -exec sed -i -r 's/\bMAX_(NC_NAME|VAR_DIMS)\b/H4_&/g' {} \; \
     -o \
     -exec grep -q -P '\bH5_VERS_RELEASE\b' {} \; -print \
     -exec sed -i -r 's/H5_VERS_RELEASE >=? [^)]*/1/' {} \; \
     \)

# artifacts location
%mvn_package org.hdfgroup:jhdf5 jhdf5
%mvn_file org.hdfgroup:jhdf5 jhdf5
%mvn_package org.hdfgroup:jhdf jhdf
%mvn_file org.hdfgroup:jhdf jhdf

%global nowarn -Wno-maybe-uninitialized -Wno-unused-but-set-variable -Wno-unused-variable -Wno-unused-function
%global compat -DH5Fget_info_vers=1 -DH5Rdereference_vers=1

%build
export CPPFLAGS='-I%{java_home}/include/linux'
%configure --with-jdk=%{java_home}/include,%{java_home}/lib \
        --with-hdf5=%{_includedir},%{_libdir} \
        --with-hdf4=%{_includedir}/hdf,%{_libdir}/hdf \
        --with-libsz=%{_includedir},%{_libdir} \
        --with-libz=%{_includedir},%{_libdir} \
        --with-libjpeg=%{_includedir},%{_libdir}

make natives JPEGLIB=-ljpeg ZLIB=-lz HDF5LIB=-lhdf5 SZLIB=-lsz \
     CC='gcc -shared %{optflags} -fPIC %nowarn %compat' \
     LDOPT='%{?__global_ldflags} -shared'
make -C hdf
make packages javadocs

%check
make tests

%install

# jars and depmap
%mvn_artifact org.hdfgroup:jhdf5:%{version} lib/jhdf5.jar
%mvn_artifact org.hdfgroup:jhdf:%{version} lib/jhdf.jar
%mvn_install -J docs/javadocs

rm -r docs/javadocs

install -Dm744 -t%{buildroot}%{_libdir}/jhdf/ lib/*/libjhdf.so
install -Dm744 -t%{buildroot}%{_libdir}/jhdf5/ lib/*/libjhdf5.so

%global _docdir_fmt %{name}

%files -f .mfiles-jhdf5
%attr(755,root,root) %{_libdir}/jhdf5/libjhdf5.so
%doc Readme.txt
%license COPYING

%files -n jhdf -f .mfiles-jhdf
%attr(755,root,root) %{_libdir}/jhdf/libjhdf.so
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.2-3
- Add various workarounds to fix build with new HDF5 (#1735866)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-6
- Rebuild for hdf5 1.8.20
- Build with libsz support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.1-1
- Update to latest release
- jdfhobj* and hdfview have been split out, so those subpackages are
  dropped, and will have to be provided by a new source package.

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-9
- Rebuild for hdf5 1.8.18

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-8
- Rebuild for hdf5 1.8.17

* Mon Mar 28 2016 gil cattaneo <puntogil@libero.it> 2.11.0-7
- generate maven depmap and javadoc
- add javadoc sub package
- minor changes to adapt to current guideline
- fix some rpmlint problems
- introduce license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-5
- Rebuild for hdf5 1.8.16

* Sat Dec 12 2015 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-4
- BR hdf-static

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-2
- Rebuild for hdf5 1.8.15

* Wed Jan 7 2015 Orion Poplawski <orion@cora.nwra.com> - 2.11.0-1
- Update to 2.11.0

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.10.1-4
- hdfview: update mime scriptlet, fix icon scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Clément David <c.david86@gmail.com> - 2.10.1-2
- rebuilt

* Thu Jul 03 2014 Clément David <c.david86@gmail.com> - 2.10.1-1
- Update to jhdf5 1.10.1

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 2.10-3
- Rebuild for hdf 1.8.13

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Clément David <c.david86@gmail.com> - 2.10-1
- Update version
- Change R:java to R:java-headless (Bug 1068283).

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 2.9-4
- Rebuild for hdf5 1.8.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.9-2
- Rebuild for hdf5 1.8.11

* Thu Jan 24 2013 Clément David <c.david86@gmail.com> - 2.9-1
- Update to 2.9
- Upgrade to the Java packaging draft (JNI jar/so location)

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.8-10
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.8-9
- revbump after jnidir change

* Mon Dec 03 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8-8
- Rebuild for hdf5 1.8.10
- Add BR libjpeg-devel

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8-6
- Rebuild with hdf5 1.8.9

* Mon Feb 13 2012 Clément David <davidcl@fedoraproject.org> - 2.8-5
- bump version to depends on latest hdf5

* Tue Jan 31 2012 Clément David <davidcl@fedoraproject.org> - 2.8-4
- fix hdfview CLASSPATH

* Mon Jan 30 2012 Clément David <davidcl@fedoraproject.org> - 2.8-3
- split jhdfobj as an object oriented API of jhdf and jhdf5.

* Fri Jan 27 2012 Clément David <davidcl@fedoraproject.org> - 2.8-2
- use %%{_hdf5_version} for hdfview
- use same jhdf and jhdf5 versions for hdfview

* Wed Jan 25 2012 Clément David <davidcl@fedoraproject.org> - 2.8-1
- update to version 2.8

* Wed Jan 25 2012 Clément David <davidcl@fedoraproject.org> - 2.7-9
- move jars to more standard locations

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Orion Poplawski <orion@cora.nwra.com> - 2.7-7
- use %%{_hdf5_version}

* Thu Nov 17 2011 Clément David <c.david86@gmail.com> - 2.7-6
- use %%{hdf5ver} to avoid runtime crash

* Thu Nov 03 2011 Clément David <c.david86@gmail.com> - 2.7-5
- rebuilt
* Thu Nov  3 2011 Clément David <c.david86@gmail.com> - 2.7-4
- remove rpm-build BuildRequire

* Tue Oct 25 2011 Clément David <c.david86@gmail.com> - 2.7-3
- Fix executable permissions
- pass rpmlint

* Tue Aug 16 2011 Clément David <c.david86@gmail.com> - 2.7-2
- Update mime types to x-hdf and x-hdf5

* Tue Aug 16 2011 Clément David <c.david86@gmail.com> - 2.7-1
- Initial packaging

