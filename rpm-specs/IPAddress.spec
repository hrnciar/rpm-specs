Name:           IPAddress
Version:        5.2.1
Release:        5%{?dist}
Summary:        Library for handling IP addresses and subnets, both IPv4 and IPv6
License:        ASL 2.0
URL:            https://github.com/seancfoley/IPAddress
Source0:        https://github.com/seancfoley/IPAddress/archive/v%{version}.tar.gz
Patch1:         removeNonAsciChars.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  ant
# the package builds in jdk8 friendly, but in jdk9+ usable jar/module
BuildRequires:  java-11-openjdk-devel

Requires: java-headless

%description
Library for handling IP addresses and subnets, both IPv4 and IPv6

%prep
%setup -q
%patch1 -p1

%build
pushd IPAddress
rm dist/IPAddress.jar
mkdir bin #for classes
#while jdk8 is main, we need both jdks, and prefer the upper one
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# be aware, the build do not fail in compilation faiure, and you can end with empty, or full of sources jar, as I did first time!
ant "create dist jar" #yah, funny name, as the whole ant-maven-less-with-pom build system
mv dist/IPAddress*.jar dist/IPAddress.jar
#%%mvn_build it looks like pom is useles, and is enough as it is

%install
%mvn_artifact IPAddress/pom.xml IPAddress/dist/IPAddress.jar
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-3
- hack with LANG did not worked, pathcing out non asci chars

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-2
- Fixed build, so the final jar contains also classes and not just sources

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-1
- Initial packaging
