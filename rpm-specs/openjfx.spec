%global openjfxdir %{_jvmdir}/%{name}

Name:           openjfx
Version:        11.0.3
Release:        0%{?dist}
Summary:        Rich client application platform for Java

License:        GPL v2 with exceptions and BSD
URL:            http://openjdk.java.net/projects/openjfx/

Source0:        hg.openjdk.java.net/openjfx/11/rt/archive/rt-11.0.3+1.tar.bz2
Source1:        pom-base.xml
Source2:        pom-controls.xml
Source3:        pom-fxml.xml
Source4:        pom-graphics.xml
Source5:        pom-graphics_antlr.xml
Source6:        pom-graphics_decora.xml
Source7:        pom-graphics_compileJava.xml
Source8:        pom-graphics_compileJava-decora.xml
Source9:        pom-graphics_compileJava-java.xml
Source10:       pom-graphics_compileJava-prism.xml
Source11:       pom-graphics_graphics.xml
Source12:       pom-graphics_libdecora.xml
Source13:       pom-graphics_libglass.xml
Source14:       pom-graphics_libglassgtk2.xml
Source15:       pom-graphics_libglassgtk3.xml
Source16:       pom-graphics_libjavafx_font.xml
Source17:       pom-graphics_libjavafx_font_freetype.xml
Source18:       pom-graphics_libjavafx_font_pango.xml
Source19:       pom-graphics_libjavafx_iio.xml
Source20:       pom-graphics_libprism_common.xml
Source21:       pom-graphics_libprism_es2.xml
Source22:       pom-graphics_libprism_sw.xml
Source23:       pom-graphics_prism.xml
Source24:       pom-media.xml
Source25:       pom-openjfx.xml
Source26:       pom-swing.xml
Source27:       pom-swt.xml
Source28:       pom-web.xml
Source29:       build.xml

ExclusiveArch:  x86_64

Requires:       java-11-openjdk	
Requires:       javapackages-tools

BuildRequires:  java-11-openjdk-devel
BuildRequires:  maven-local
BuildRequires:	ant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  mvn(org.eclipse.swt:swt)
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.mojo:native-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)

BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(gl)

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media and web module have been removed due to missing dependencies.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-devel
Summary: OpenJFX development tools and libraries

%description devel
%{summary}.

%global debug_package %{nil}

%prep
%setup -q -n rt-11.0.3+1

#Drop *src/test folders
rm -rf modules/javafx.{base,controls,fxml,graphics,media,swing,swt,web}/src/test/
rm -rf modules/jdk.packager/src/test/

#prep for javafx.graphics
cp -a modules/javafx.graphics/src/jslc/antlr modules/javafx.graphics/src/main/antlr3
cp -a modules/javafx.graphics/src/main/resources/com/sun/javafx/tk/quantum/*.properties modules/javafx.graphics/src/main/java/com/sun/javafx/tk/quantum

find -name '*.class' -delete
find -name '*.jar' -delete

#copy maven files
cp -a %{_sourcedir}/pom-*.xml .
mv pom-openjfx.xml pom.xml

for MODULE in base controls fxml graphics media swing swt web
do
	mv pom-$MODULE.xml ./modules/javafx.$MODULE/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-{antlr,decora,compileJava,graphics,libdecora,libglass,libglassgtk2,libglassgtk3,libjavafx_font,libjavafx_font_freetype,libjavafx_font_pango,libjavafx_iio,libprism_common,libprism_es2,libprism_sw,prism}
for GRAPHMOD in antlr decora compileJava graphics libdecora libglass libglassgtk2 libglassgtk3 libjavafx_font libjavafx_font_freetype libjavafx_font_pango libjavafx_iio libprism_common libprism_es2 libprism_sw prism
do
	mv pom-graphics_$GRAPHMOD.xml ./modules/javafx.graphics/mvn-$GRAPHMOD/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-compileJava/mvn-{decora,java,prism}
for SUBMOD in decora java prism
do
	mv pom-graphics_compileJava-$SUBMOD.xml ./modules/javafx.graphics/mvn-compileJava/mvn-$SUBMOD/pom.xml
done

#set VersionInfo
cp -a %{_sourcedir}/build.xml .
ant -f build.xml

cp -a ./modules/javafx.swing/src/main/module-info/module-info.java ./modules/javafx.swing/src/main/java

%build

#set openjdk11 for build
export JAVA_HOME=%{_jvmdir}/java-11-openjdk
export CFLAGS="${RPM_OPT_FLAGS}"
export CXXFLAGS="${RPM_OPT_FLAGS}" 

%mvn_build --skip-javadoc

%install

install -d -m 755 %{buildroot}%{openjfxdir}
cp -a modules/javafx.{base,controls,fxml,media,swing,swt,web}/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/javafx.graphics/mvn-compileJava/mvn-java/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/javafx.graphics/mvn-lib{decora,javafx_font,javafx_font_freetype,javafx_font_pango,glass,glassgtk2,glassgtk3,javafx_iio,prism_common,prism_es2,prism_sw}/target/*.so %{buildroot}%{openjfxdir}

%files
%dir %{openjfxdir}
%{openjfxdir}/
%license LICENSE
%license ADDITIONAL_LICENSE_INFO
%license ASSEMBLY_EXCEPTION
%doc README

%files devel
%{openjfxdir}/
%license LICENSE
%license ADDITIONAL_LICENSE_INFO
%license ASSEMBLY_EXCEPTION
%doc README

%changelog
* Wed Aug 14 2019 Nicolas De Amicis - 11.0.3-0
- Initial packaging
