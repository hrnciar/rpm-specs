%global project     clojure
%global artifactId  core.specs.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}

Name:           clojure-core-specs-alpha
Epoch:          1
Version:        0.2.44
Release:        4%{?dist}
Summary:        Clojure library containing specs to describe Clojure core macros and functions

Group:          Development/Languages
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}
Source0:        %{URL}/archive/%{artifactId}-%{full_version}.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
BuildRequires:  mvn(org.clojure:spec.alpha)


%description 
Core.specs.alpha is a Clojure library containing specs to describe Clojure
core macros and functions.

%prep
%setup -q -n %{archivename}-%{full_version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"

# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"
# Copy clojure source files so they are included in the jar
%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:1.12 . "
        <executions>
          <execution>
            <id>add-clojure-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-source</goal>
              <goal>add-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/main/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/main/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
          <execution>
            <id>add-clojure-test-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-test-source</goal>
              <goal>add-test-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/test/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/test/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
        </executions>"


%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license epl-v10.html
%doc epl-v10.html CHANGES.md README.md CONTRIBUTING.md

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:0.2.44-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 02 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.2.44-2
- Use xmvn-builddep to generate BuildRequires and drop redundant Requires.

* Wed Apr 15 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.2.44-1
- Update upstream to 0.2.44 and clojure dependency to 1.9.0.

* Sun Apr 12 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.1.24-2
- Add builder helper to copy clojure files

* Sun Apr 05 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.1.24-1
- Initial package
