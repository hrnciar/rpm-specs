Name:           hdfview
Version:        2.14
Release:        5%{?dist}
Summary:        Java HDF5 Object viewer

License:        BSD with advertising
URL:            https://support.hdfgroup.org/products/java/
#Source0:       https://support.hdfgroup.org/ftp/HDF5/hdf-java/current/src/hdfview-%{version}.tar.gz
Source0:        hdfview-%{version}-nolibs.tar.xz
Source1:        hdfview
Source2:        hdfview.xml
Source3:        hdfview.desktop
Source4:        hdfview.appdata.xml

# ./getsources.sh will download Source0 and remove bundled libs
Source9:        getsources.sh

# Upstream creates a single jar with both the jhdfobj interface and
# the HDFView parts. Split that into separate jars.
Patch0:         hdfview-jars.patch

%global jhdf_version 3.3.2

BuildRequires:  maven-local
BuildRequires:  ant
BuildRequires:  mvn(org.hdfgroup:jhdf) >= %{jhdf_version}
BuildRequires:  mvn(org.hdfgroup:jhdf5) >= %{jhdf_version}
BuildRequires:  mvn(gov.nasa.gsfc.heasarc:nom-tam-fits)
BuildRequires:  mvn(edu.ucar:cdm)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       java
Requires:       javapackages-tools
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(org.slf4j:slf4j-simple)
Requires:       mvn(org.hdfgroup:jhdf) >= %{jhdf_version}
Requires:       mvn(org.hdfgroup:jhdf5) >= %{jhdf_version}
Requires:       mvn(gov.nasa.gsfc.heasarc:nom-tam-fits)
Requires:       mvn(edu.ucar:cdm)
Requires:       jhdfobj = %{version}-%{release}
Requires:       hicolor-icon-theme

BuildArch:      noarch

%description
HDF is a versatile data model that can represent very complex data objects
and a wide variety of meta-data. It is a completely portable file format
with no limit on the number or size of data objects in the collection.

This package provides a HDF4/HDF5 viewer.

%package -n jhdfobj
Summary:        Java HDF/HDF5 Object Package
Requires:       javapackages-tools
Requires:       mvn(org.hdfgroup:jhdf)
Requires:       mvn(org.hdfgroup:jhdf5)
Requires:       mvn(org.slf4j:slf4j-api)

%description -n jhdfobj
HDF is a versatile data model that can represent very complex data objects
and a wide variety of meta-data. It is a completely portable file format
with no limit on the number or size of data objects in the collection.

This Java package implements HDF4/HDF5 data objects in an
object-oriented form. It provides a common Java API for accessing HDF files.

%package doc
Summary:        Sample files and example code for %{name}
Enhances:       %{name}
Requires:       %{name}-javadoc

%description doc
%{summary}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%autosetup

# build jar repo
mkdir -p lib/extra
build-jar-repository -p lib/ junit slf4j- jhdf jhdf5 nom-tam-fits thredds/cdm
ln -s slf4j-api.jar lib/slf4j-api-1.7.5.jar
ln -s slf4j-nop.jar lib/slf4j-nop-1.7.5.jar
ln -s nom-tam-fits.jar lib/fits.jar
ln -s jhdf.jar lib/jarhdf.jar
ln -s jhdf5.jar lib/jarhdf5.jar
ln -s thredds_cdm.jar lib/netcdf.jar

# simulate the settings files
echo 'HDF4 Version: %_hdf5_version' >lib/libhdf4.settings
echo 'HDF5 Version: %_hdf5_version' >lib/libhdf5.settings

# artifacts location
%mvn_package org.hdfgroup:jhdfobj jhdfobj
%mvn_file org.hdfgroup:jhdfobj jhdfobj
%mvn_package org.hdfgroup:jhdfview jhdfview
%mvn_file org.hdfgroup:jhdfview jhdfview

echo hdf.lib.dir=$(pwd)/lib >> build.properties

%build
ant jar
ant javadoc

%install
# jars and depmap
%mvn_artifact org.hdfgroup:jhdfobj:%{version} build/jar/jhdfobj.jar
%mvn_artifact org.hdfgroup:jhdfview:%{version} build/jar/HDFView.jar
%mvn_install -J build/javadocs

install -Dpm0755 %{SOURCE1} -t %{buildroot}%{_bindir}/

# Create and install hicolor icons.
for i in 16 22 32 48 ; do
  mkdir -p icons/${i}x${i}/apps
  convert -resize ${i}x${i} src/hdf/view/icons/hdf_large.gif \
    icons/${i}x${i}/apps/hdfview.png

  install -Dpm 0644 icons/${i}x${i}/apps/hdfview.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/hdfview.png

  install -Dpm 0644 icons/${i}x${i}/apps/hdfview.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/application-x-hdf.png

done

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                                    \
        --dir %{buildroot}%{_datadir}/applications      \
        %{SOURCE3}

# mime types
install -Dpm644 -t %{buildroot}%{_datadir}/mime/packages/ %{SOURCE2}

# appdata
install -Dpm644 -t %{buildroot}%{_datadir}/appdata/ %{SOURCE4}

rm src/examples/testfiles/*.txt

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%global _docdir_fmt %{name}

%files -f .mfiles-jhdfview
%_bindir/hdfview
%{_datadir}/applications/hdfview.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/mime/packages/hdfview.xml
%{_datadir}/appdata/hdfview.appdata.xml

%files -n jhdfobj -f .mfiles-jhdfobj
%doc Readme.txt docs/RELEASE.txt
# other docs are very outdated, stuff that's on the web seems better
%license COPYING

%files doc
%doc samples/
%doc src/examples/
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.14-3
- Remove obsolete requirements for %%post/%%postun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.13.0-4
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.13.0-1
- Also add /usr/share/mime, /usr/share/mime/packages to %%files

* Tue Dec 13 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.13.0-1
- Add versioned requirement on jhdf5 in hdfview binary package
- New javadoc subpackage
- Fix ownership issues in icons directory
- Exclude text files in examples/testfiles

* Sat Dec 10 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.13.0-1
- Fix BuildRequires

* Thu Dec  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.13.0-1
- Initial split from jhdf5
