Name:           jaxb-fi
Version:        1.2.18
Release:        1%{?dist}
Summary:        Implementation of the Fast Infoset Standard for Binary XML
# jaxb-fi is licensed ASL 2.0 and EDL-1.0 (BSD)
# bundled org.apache.xerces.util.XMLChar.java is licensed ASL 1.1
License:        ASL 2.0 and BSD and ASL 1.1

URL:            https://github.com/eclipse-ee4j/jaxb-fi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:xsom)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-fastinfoset = %{version}-%{release}
Obsoletes:      glassfish-fastinfoset < 1.2.15-5

# javadoc subpackage is currently not built
Obsoletes:      glassfish-fastinfoset-javadoc < 1.2.15-5

%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.


%prep
%setup -q

pushd code
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and not required
%pom_remove_parent

# disable unnecessary submodules
%pom_disable_module roundtrip-tests
%pom_disable_module samples

# disable unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
popd


%build
pushd code
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -DbuildNumber=unknown
popd


%install
pushd code
%mvn_install
popd


%files -f code/.mfiles
%license LICENSE NOTICE.md
%doc README.md


%changelog
* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.18-1
- Initial package renamed from glassfish-fastinfoset.

