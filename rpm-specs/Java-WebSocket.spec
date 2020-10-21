%global forgeurl https://github.com/TooTallNate/Java-WebSocket

Name: Java-WebSocket
Version: 1.5.1
Release: 1%{?dist}
Summary: A barebones WebSocket client and server implementation written in 100% Java

%forgemeta

License: MIT
URL: %{forgeurl}
Source0: %{forgesource}
BuildArch: noarch

Requires: java-headless

BuildRequires: maven-local
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)

Provides: bundled(net.iharder:base64) = 2.3.8

%description
A barebones WebSocket server and client implementation written in 100% Java.
The underlying classes are implemented java.nio, which allows for a non-blocking
event-driven model (similar to the WebSocket API for web browsers).

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%forgesetup

%pom_remove_dep org.json:json

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
#missing dependencies
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.markdown
%doc CHANGELOG.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.markdown
%doc CHANGELOG.md
%license LICENSE

%changelog
* Tue Aug 04 2020 Jonny Heggheim <hegjon@gmail.com> - 1.5.1-1
- Updated to version 1.5.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.8-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

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
