%global majorversion 2
Name:          metadata-extractor2
Version:       2.10.1
Release:       11%{?dist}
Summary:       Extracts EXIF, IPTC, XMP, ICC and other metadata from image files
License:       ASL 2.0
URL:           http://drewnoakes.com/code/exif/
Source0:       https://github.com/drewnoakes/metadata-extractor/archive/%{version}/metadata-extractor-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.adobe.xmp:xmpcore)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
# Explicit requires for javapackages-tools since metadata-extractor2 script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

Provides:      mvn(com.drewnoakes:metadata-extractor) = %{version}-%{release}

BuildArch:     noarch

%description
Metadata Extractor is a straightforward Java library
for reading metadata from image files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metadata-extractor-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

# remove unnecessary dependency on parent POM
%pom_remove_parent
# Unavailable plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
# Unwanted plugins
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# Unneeded task
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
# Fix manifest entries
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest/pom:addClasspath" false
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest" "<mainClass>com.drew.imaging.ImageMetadataReader</mainClass>"
# Use standard maven output directory
%pom_xpath_remove "pom:build/pom:directory"
%pom_xpath_remove "pom:build/pom:outputDirectory"

# javascript not allowed in javadoc
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:bottom"

# Add OSGi support
%pom_xpath_set "pom:project/pom:packaging" bundle 
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

sed -i 's/\r//' LICENSE-2.0.txt README.md Resources/javadoc-stylesheet.css

%mvn_file :metadata-extractor %{name}
%mvn_alias :metadata-extractor "drew:metadata-extractor"
%mvn_compat_version ":metadata-extractor" %{majorversion}

%build

%mvn_build

%install
%mvn_install

%jpackage_script com.drew.imaging.ImageMetadataReader "" "" %{name}-%{majorversion}:xmpcore %{name} true

%files -f .mfiles
%{_bindir}/*
%doc README.md
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.1-11
- Remove unnecessary dependency on parent POM.
- Drop native2ascii invocations (no longer necessary?).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.10.1-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.10.1-4
- Add explicit requirement on javapackages-tools since launcher script
  uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.10.1-1
- update to 2.10.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 gil cattaneo <puntogil@libero.it> 2.9.1-2
- fix FTBFS

* Sat Dec 31 2016 gil cattaneo <puntogil@libero.it> 2.9.1-1
- update to 2.9.1

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 2.8.1-4
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 gil cattaneo <puntogil@libero.it> 2.8.1-1
- update to 2.8.1

* Mon Feb 23 2015 gil cattaneo <puntogil@libero.it> 2.7.2-1
- update to 2.7.2

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 2.6.4-5
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 gil cattaneo <puntogil@libero.it> 2.6.4-3
- fix rhbz#1068933

* Mon Oct 21 2013 gil cattaneo <puntogil@libero.it> 2.6.4-2
- fix script

* Mon Jan 21 2013 gil cattaneo <puntogil@libero.it> 2.6.4-1
- initial rpm
