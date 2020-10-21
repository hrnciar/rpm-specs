Name:           maven-license-plugin
Version:        1.8.0
Release:        30%{?dist}
Summary:        Maven plugin to update header licenses of source files

License:        ASL 2.0
URL:            http://code.google.com/p/maven-license-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-license-plugin.googlecode.com/svn/tags/maven-license-plugin-1.8.0 maven-license-plugin
# tar cfJ maven-license-plugin-1.8.0.tar.xz maven-license-plugin
Source0:        %{name}-%{version}.tar.xz
# remove testng dep (tests are skipped) and maven-license-plugin call
Patch0:         001-mavenlicenseplugin-fixbuild.patch
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-local
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-shared
BuildRequires:  plexus-utils
BuildRequires:  plexus-classworlds
BuildRequires:  xml-commons-apis
BuildRequires:  xmltool
BuildRequires:  maven-source-plugin

Requires:       jpackage-utils
Requires:       java-headless >= 1:1.6.0
Requires:       maven
Requires:       maven-shared
Requires:       xmltool

%description
maven-license-plugin is a Maven plugin that help you managing license
headers in source files. Basically, when you are developing a project
either in open source or in a company, you often need to add at the top
of your source files a license to protect your work.
This plugin lets you maintain the headers, including checking if the
header is present, generating a report and of course having the
possibility to update / reformat missing license headers.


%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1
# fix EOL
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

# Remove wagon-webdav extension which is not available
%pom_xpath_remove pom:build/pom:extensions

# Set sources/resources encoding
%pom_xpath_inject "pom:properties" "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE.txt
%doc NOTICE.txt

%files javadoc  -f .mfiles-javadoc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.0-29
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.0-28
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct  3 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.0-20
- Add missing BR: maven-source-plugin
- Adjust patch to current plexus-utils
- Resolves: rhbz#1307765

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Guido Grazioli <guido.grazioli@gmail.com> - 1.8.0-18
- Update to current guidelines and maven-local build macros
- Fix FTBFS

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.8.0-16
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Guido Grazioli <guido.grazioli@gmail.com> - 1.8.0-14
- Fix FTBFS

* Tue Feb 26 2013 Tomas Radej <tradej@redhat.com> - 1.8.0-13
- Reintroduced B/R on maven-shared

* Mon Feb 18 2013 Tomas Radej <tradej@redhat.com> - 1.8.0-12
- Removed BR on maven-shared (unnecessary + blocking maven-shared retirement)
- Remove wagon-webdav extension which is not available

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.0-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.0-8
- Remove maven-eclipse-plugin requirement to simplify build

* Tue Apr 17 2012 Tomas Radej <tradej@redhat.com> - 1.8.0-7
- Apache-resource-bundles BR
- Guidelines fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.8.0-5
- Adapt to current guidelines.

* Fri Jun 24 2011 Guido Grazioli <guido.grazioli@gmail.com> - 1.8.0-4
- Fix FTBFS
- Update to maven 3
- Adapt to current guidelines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 17 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.8.0-2
- Add missing Requires and update BuildRequires
- Fix macro usage

* Sat Oct 02 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.8.0-1
- Upstream version 1.8.0

* Sat May 08 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.6.1-1
- Initial packaging
