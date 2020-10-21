%global upstream    talios
%global groupId     com.theoryinpractise
%global artifactId  clojure-maven-plugin

Name:           %{artifactId}
Version:        1.8.4
Release:        2%{?dist}
Summary:        Clojure plugin for Maven

License:        EPL-1.0
URL:            https://github.com/%{upstream}/%{name}
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{URL}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
This plugin has been designed to make working with clojure as easy as
possible, when working in a mixed language, enterprise project.


%prep
%setup -q -n %{artifactId}-%{artifactId}-%{version}

# release plugin is not required for RPM builds
%pom_remove_plugin :maven-release-plugin

# trivial port to commons-lang3
%pom_remove_dep :commons-lang
%pom_add_dep org.apache.commons:commons-lang3

sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/com/theoryinpractise/clojure/AbstractClojureCompilerMojo.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/com/theoryinpractise/clojure/ClojureNReplMojo.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/com/theoryinpractise/clojure/ClojureSwankMojo.java


%build
# test1.clj does not get discovered if LANG=C
# also, using 'package' instead of 'install' to avoid
# running integration tests - they do installation tests
# for a lot of packages*versions we do not currently have
export LANG=en_US.utf8
# Do not run tests cause we miss dependencies fest-assert
# and maven-surefire-provider-junit5
%mvn_build -f -j


%install
%mvn_install

%files -f .mfiles
%license epl-v10.html 
%doc README.markdown


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.4-1
- Update to 1.8.4 release.

* Fri Jul 24 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-8
- Port to commons-lang3.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.1-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-6
- Regenerate BuildRequires with xmvn-builddep and drop redundant Requires.

* Sat Apr 04 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-5
- Rebuilt for Fedora 33 rawhide

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-3
- Fix license short name to EPL-1.0
- Update BuildRequires to use mvn(org.apache.maven:maven-toolchain)

* Sun Feb 10 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-2
- Remove jpackage-utils from (Build)Requires
- Use license macro for file epl-v10.html 
- Remove unnecessary Epoch

* Sat Jan 05 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-1
- Update to upstream 1.8.1
- Update to Xmvn macros
- Remove maven-surefire-provider-junit4 and fest-assert build requirement

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.10-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.10-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Michel Salim <salimma@fedoraproject.org> - 1.3.10-1
- Initial package
