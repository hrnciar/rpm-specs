%global srcname dirq
Name:		java-dirq
Version:	1.8
Release:	12%{?dist}
Summary:	Directory based queue
License:	ASL 2.0
URL:		https://github.com/cern-mig/%{name}
Source0:	https://github.com/cern-mig/%{name}/archive/%{srcname}-%{version}.tar.gz
Patch0:		java-dirq-1.8-no-checkstyle.patch
BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)

%description
The goal of this module is to offer a simple queue system using the underlying
file system for storage, security and to prevent race conditions via atomic
operations. It focuses on simplicity, robustness and scalability.

This module allows multiple concurrent readers and writers to interact with
the same queue.

A Perl implementation (Directory::Queue) and a Python implementation (dirq)
of the same algorithm are available so readers and writers can be written in
different programming languages.

%package javadoc
Summary:	Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{srcname}-%{version}
%patch0 -p1

%pom_remove_parent
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

# remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc CHANGES readme.md todo.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8-11
- Remove unnecessary dependency on maven-javadoc-plugin.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.8-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Lionel Cons <lionel.cons@cern.ch> - 1.8-8
- Disabled checkstyle since maven-checkstyle-plugin is now orphaned (#1735814)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Lionel Cons <lionel.cons@cern.ch> - 1.8-1
- Updated to upstream version (#1352493)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Lionel Cons <lionel.cons@cern.ch> - 1.7-1
- Updated to upstream version (#1286944)

* Tue Nov 24 2015 Lionel Cons <lionel.cons@cern.ch> - 1.6-4
- Applied upstream patch to fix permission problems

* Fri Nov 13 2015 Lionel Cons <lionel.cons@cern.ch> - 1.6-3
- Applied upstream patch to fix problems on ARM (#1270012)

* Wed Nov 11 2015 Lionel Cons <lionel.cons@cern.ch> - 1.6-2
- Reverted the package back to noarch

* Wed Nov 11 2015 Lionel Cons <lionel.cons@cern.ch> - 1.6-1
- Updated to latest version

* Fri Jul 03 2015 Mat Booth <mat.booth@redhat.com> - 1.4-7
- Fix FTBFS caused by strict javadoc linting

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Steve Traylen <steve.traylen@cern.ch> - 1.4-5
- Migrate from ant to mvn and latest fedora guidelines
- Be fussy about arch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.4-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.4-1
- Updating to latest version

* Thu May 30 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.3-3
- Spec file cleaning

* Fri May 24 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.3-2
- Spec file cleaning

* Fri May 10 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.3-1
- Updating to upstream version 1.3

* Thu Mar 14 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.2-1
- Updating to upstream version 1.2

* Tue Dec 04 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.0-1
- Initial packaging
