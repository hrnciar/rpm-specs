Name:           jaxb-istack-commons
Version:        3.0.11
Release:        2%{?dist}
Summary:        iStack Common Utility Code
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(org.testng:testng)

%global obs_vr 3.0.11-2

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons = %{version}-%{release}
Obsoletes:      istack-commons < %{obs_vr}

# javadoc subpackage is currently not built
Obsoletes:      istack-commons-javadoc < %{obs_vr}

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.


%package -n istack-commons-maven-plugin
Summary:        istack-commons Maven Mojo

# package renamed in fedora 33, remove in fedora 35
Provides:       maven-istack-commons-plugin = %{version}-%{release}
Obsoletes:      maven-istack-commons-plugin < %{obs_vr}

%description -n istack-commons-maven-plugin
This package contains the istack-commons Maven Mojo.


%package -n import-properties-plugin
Summary:        istack-commons import properties plugin

%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.


%package buildtools
Summary:        istack-commons buildtools

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons-buildtools = %{version}-%{release}
Obsoletes:      istack-commons-buildtools < %{obs_vr}

%description buildtools
This package contains istack-commons buildtools.


%package runtime
Summary:        istack-commons runtime

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons-runtime = %{version}-%{release}
Obsoletes:      istack-commons-runtime < %{obs_vr}

%description runtime
This package contains istack-commons runtime.


%package soimp
Summary:        istack-commons soimp

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons-soimp = %{version}-%{release}
Obsoletes:      istack-commons-soimp < %{obs_vr}

%description soimp
This package contains istack-commons soimp.


%package test
Summary:        istack-commons test

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons-test = %{version}-%{release}
Obsoletes:      istack-commons-test < %{obs_vr}

%description test
This package contains istack-commons test.


%package tools
Summary:        istack-commons tools

# package renamed in fedora 33, remove in fedora 35
Provides:       istack-commons-tools = %{version}-%{release}
Obsoletes:      istack-commons-tools < %{obs_vr}

%description tools
This package contains istack-commons tools.


%prep
%setup -q

pushd istack-commons
# disable very verbose warnings
sed -i -e '/Xlint:all/d' pom.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin
popd


%build
pushd istack-commons
# - skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
# - ignore test failures due to faulty JVM version detection
%mvn_build -j -s -- -DscmBranch=%{version} -DbuildNumber=unknown -Dmaven.test.failure.ignore=true
popd


%install
pushd istack-commons
%mvn_install
popd


%files -f istack-commons/.mfiles-istack-commons
%license LICENSE.md NOTICE.md
%doc README.md

%files -n istack-commons-maven-plugin -f istack-commons/.mfiles-istack-commons-maven-plugin
%license LICENSE.md NOTICE.md

%files -n import-properties-plugin -f istack-commons/.mfiles-import-properties-plugin
%license LICENSE.md NOTICE.md

%files buildtools -f istack-commons/.mfiles-istack-commons-buildtools
%license LICENSE.md NOTICE.md

%files runtime -f istack-commons/.mfiles-istack-commons-runtime
%license LICENSE.md NOTICE.md

%files soimp -f istack-commons/.mfiles-istack-commons-soimp
%license LICENSE.md NOTICE.md

%files test -f istack-commons/.mfiles-istack-commons-test
%license LICENSE.md NOTICE.md

%files tools -f istack-commons/.mfiles-istack-commons-tools
%license LICENSE.md NOTICE.md


%changelog
* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0.11-2
- Initial package renamed from istack-commons.

