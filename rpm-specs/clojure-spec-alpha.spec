%global project     clojure
%global artifactId  spec.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}

Name:           clojure-spec-alpha
Epoch:          1
Version:        0.2.187
Release:        1%{?dist}
Summary:        Spec is a Clojure library to describe the structure of data and functions

Group:          Development/Languages
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}/
Source0:        https://github.com/%{project}/%{artifactId}/archive/%{artifactId}-%{full_version}.zip


BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)


%description 
Spec is a Clojure library to describe the structure of data and functions.
Specs can be used to validate data, conform (destructure) data, explain
invalid data, generate examples that conform to the specs, and automatically
use generative testing to test functions.

%prep
%setup -q -n %{archivename}-%{full_version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"

# Add builder helper to copy clojure source files so that
# compiler finds them.
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
%doc CHANGES.md README.md CONTRIBUTING.md
%changelog
* Sat Aug 01 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.2.187-1
- Update upstream to 0.2.187.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.176-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:0.2.176-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 02 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.2.176-2
- Use xmvn-builddep to generate BuildRequires and drop redundant Requires.

* Wed Apr 15 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.2.176-1
- Update upstream to 0.2.176, clojure dependency to 1.9.0

* Mon Apr 13 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.1.143-1
- Update upstream to 0.1.143, clojure dependency to 1.9.0-beta3
- Add builder helper to copy clojure source files

* Sun Apr 12 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.1.134-2
- Hook clojure-maven-plugin goals to maven goals

* Sun Apr 05 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:0.1.134-1
- Initial package
