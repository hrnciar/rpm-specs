Name:          replacer
Version:       1.6
Release:       17%{?dist}
Summary:       Replacer Maven Mojo
License:       MIT
URL:           https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:       https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(xerces:xercesImpl)

BuildArch:     noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-replacer-plugin-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

# remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

%pom_xpath_inject pom:build/pom:plugins "<plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration><source>\${maven.compiler.source}</source><detectJavaApiLink>false</detectJavaApiLink></configuration>
</plugin>"

# trivial port to commons-lang3
%pom_change_dep :commons-lang org.apache.commons:commons-lang3:3.8.1

for i in $(find -name "*.java"); do
    sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" $i;
done

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jul 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6-17
- Port to commons-lang3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.6-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Mat Booth <mat.booth@redhat.com> - 1.6-14
- Allow building against Java 11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.6-12
- Remove unnecessary dependency on parent POM.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Mat Booth <mat.booth@redhat.com> - 1.6-10
- Disable tests to reduce dependency tree

* Wed Feb 13 2019 Mat Booth <mat.booth@redhat.com> - 1.6-9
- Fix build against mockito 2.x

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 gil cattaneo <puntogil@libero.it> 1.6-1
- update to 1.6
- fix Url tag and Source0 tag

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.5.3-2
- introduce license macro

* Thu Jul 03 2014 gil cattaneo <puntogil@libero.it> 1.5.3-1
- update to 1.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.5.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.5.2-2
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.5.2-1
- initial rpm
