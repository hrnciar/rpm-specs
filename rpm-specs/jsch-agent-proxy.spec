Name:           jsch-agent-proxy
Version:        0.0.8
Release:        13%{?dist}
Summary:        Proxy to ssh-agent and Pageant in Java
License:        BSD
URL:            http://www.jcraft.com/jsch-agent-proxy/
BuildArch:      noarch

Source0:        https://github.com/ymnk/jsch-agent-proxy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:platform)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

# SSHj is not longer available in Fedora
Obsoletes: %{name}-sshj <= 0.0.8-11

%description
jsch-agent-proxy is a proxy program to OpenSSH ssh-agent and Pageant
included Putty.  It will be easily integrated into JSch, and users
will be allowed to use those programs in authentications.  This
software has been developed for JSch, but it will be easily applicable
to other ssh2 implementations in Java.  This software is licensed
under BSD style license.

%package connector-factory
Summary:        Connector factory for jsch-agent-proxy

%description connector-factory
%{summary}.

%package core
Summary:        jsch-agent-proxy core module

%description core
%{summary}.

%package jsch
Summary:        JSch connector for jsch-agent-proxy

%description jsch
%{summary}.

%package pageant
Summary:        Pageant connector for jsch-agent-proxy

%description pageant
%{summary}.

%package sshagent
Summary:        ssh-agent connector for jsch-agent-proxy

%description sshagent
%{summary}.

%package trilead-ssh2
Summary:        trilead-ssh2 connector for jsch-agent-proxy

%description trilead-ssh2
%{summary}.

%package usocket-jna
Summary:        USocketFactory implementation using JNA

%description usocket-jna
%{summary}.

%package usocket-nc
Summary:        USocketFactory implementation using Netcat

%description usocket-nc
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Put parent POM together with core module
%mvn_package :jsch.agentproxy jsch.agentproxy.core

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"
%pom_remove_plugin ":maven-source-plugin"
%pom_xpath_remove pom:build/pom:extensions

# Remove hard-coded compiler configuration
%pom_remove_plugin ":maven-compiler-plugin"

# SSHj not available in Fedora
%pom_disable_module jsch-agent-proxy-sshj

%build
%mvn_build -s -- -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files core -f .mfiles-jsch.agentproxy.core
%doc README README.md
%license LICENSE.txt

%files connector-factory -f .mfiles-jsch.agentproxy.connector-factory
%files jsch -f .mfiles-jsch.agentproxy.jsch
%files pageant -f .mfiles-jsch.agentproxy.pageant
%files sshagent -f .mfiles-jsch.agentproxy.sshagent
%files trilead-ssh2 -f .mfiles-jsch.agentproxy.svnkit-trilead-ssh2
%files usocket-jna -f .mfiles-jsch.agentproxy.usocket-jna
%files usocket-nc -f .mfiles-jsch.agentproxy.usocket-nc

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 0.0.8-13
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 0.0.8-11
- Allow building against JDK 11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Mat Booth <mat.booth@redhat.com> - 0.0.8-8
- Use license macro
- Enable minimal build without extra dependencies

* Wed Apr 11 2018 Mat Booth <mat.booth@redhat.com> - 0.0.8-7
- Drop BRs on unnecessary build plugins

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.8-1
- Update to upstream version 0.0.8

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 0.0.7-7
- Fix parent POM BR

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-5
- Use Requires: java-headless rebuild (#1067528)

* Tue Jan  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-4
- Enable trilead-ssh2 module

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-3
- Fix directory ownership

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-2
- Fix a typo in javadoc pkg description
- Install README files

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-1
- Initial packaging

