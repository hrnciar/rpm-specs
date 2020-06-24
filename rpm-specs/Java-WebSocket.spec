Name: Java-WebSocket
Version: 1.3.8
Release: 5%{?dist}
Summary: A barebones WebSocket client and server implementation written in 100% Java

License: MIT
URL: http://java-websocket.org/
Source0: https://github.com/TooTallNate/%{name}/archive/v%{version}.tar.gz
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(net.iharder:base64)
BuildRequires: mvn(org.json:json)

%description
A barebones WebSocket server and client implementation written in 100% Java.
The underlying classes are implemented java.nio, which allows for a non-blocking
event-driven model (similar to the WebSocket API for web browsers).

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

rm -f src/main/java/org/java_websocket/util/Base64.java
find -name '*.java' -exec sed -i 's/org.java_websocket.util.Base64/net.iharder.Base64/g' {} +
%pom_add_dep net.iharder:base64:2.3.8

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

%build
#unknown compile errors in tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.markdown
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.markdown
%license LICENSE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Jonny Heggheim <hegjon@gmail.com> - 1.3.8-1
- Updated to version 1.3.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-0.5.git58d1778
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-0.4.git58d1778
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-0.3.git58d1778
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-0.2.git58d1778
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Jonny Heggheim <hegjon@gmail.com> - 1.3.1-0.1.git58d1778
- Updated to latest snapshot. It is more stable than the 1.3.0 release

* Sun Jun 14 2015 Jonny Heggheim <hegjon@gmail.com> - 1.3.0-1
- Inital packaging
