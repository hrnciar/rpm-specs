Name:           os-maven-plugin
Version:        1.6.2
Release:        2%{?dist}
Summary:        Maven plugin for generating platform-dependent properties
License:        ASL 2.0
URL:            https://github.com/trustin/os-maven-plugin/
BuildArch:      noarch

Source0:        https://github.com/trustin/%{name}/archive/%{name}-%{version}.tar.gz

Patch0:         0001-Don-t-fail-on-unknown-arch.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove Eclipse plugin (not needed in Fedora)
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.2-2
- Mass rebuild for javapackages-tools 201902

* Thu Jun 27 2019 Marian Koncek <mkoncek@redhat.com> - 1.6.2-1
- Update to upstream version 1.6.2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-10
- Mass rebuild for javapackages-tools 201901

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-6
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-4
- Don't fail on unknown arch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 1.2.3-2
- Port to current plexus-utils

* Tue Jul  8 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-1
- Initial pagkaging
