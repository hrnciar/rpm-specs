%global commit aa1930a

Summary: A rendering system for photo-realistic image synthesis
Name: sunflow
Version: 0.07.4
Release: 12%{?dist}
URL: https://github.com/sparkoo/sunflow
Source0: https://github.com/sparkoo/sunflow/archive/v%{version}/%{name}-%{version}.tar.gz
# based on sunflow_logo.png from http://sunflow.sourceforge.net/logo2007.zip
Source1: sunflow_icon_128.png
Source2: sunflow.desktop
License: MIT
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: maven-local
BuildRequires: janino
# Explicit requires for javapackages-tools since sunflow script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

%description
Sunflow is an open source rendering system for photo-realistic image synthesis.
It is written in Java and built around a flexible ray tracing core and an
extensible object-oriented design.

%package javadoc
Summary: Javadoc for sunflow

%description javadoc
API documentation for sunflow.

%prep
%setup -q -n %{name}-%{version}
dos2unix -k CHANGELOG LICENSE README
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%jpackage_script org.sunflow.SunflowGUI "" "" "janino:sunflow" sunflow true

install -Dpm644 %{SOURCE1} \
                %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/sunflow.png

desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
 --mode=644 \
 --vendor="" \
 %{SOURCE2}

%check
java -server -Xmx1g -classpath $(build-classpath janino):target/%{name}-%{version}.jar org.sunflow.Benchmark -bench 0 128

%files -f .mfiles
%doc CHANGELOG README
%license LICENSE
%{_bindir}/sunflow
%{_datadir}/icons/hicolor/128x128/apps/sunflow.png
%{_datadir}/applications/sunflow.desktop

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 0.07.4-11
- Remove unnecessary dependency on maven-javadoc-plugin.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.07.4-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 0.07.4-6
- Add explicit javapackages-tools requirement for sunflow script.
  See RHBZ#1600426.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.07.4-3
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 2 2017 Michal Vala <mvala@redhat.com 0.07.4-1
- new version to fix bad versioning

* Thu Feb 23 2017 Michal Vala <mvala@redhat.com> 0.07.3-aa1930a
- fixed RH1424525
- removed assemble plugin from maven

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.3-8097f6d.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Michal Vala <mvala@redhat.com> 0.07.3-8097f6d
- forked https://github.com/sparkoo/sunflow
- build with maven
- license headers in source files
- applied no jvm warn patch
- updated janino dependency to match with fedora one
- removed javadoc.jar

* Tue Aug 12 2014 Dominik Mierzejewski <rpm@greysector.net> 0.07.3-0.1.20140412git4f5017f
- switch to new upstream https://github.com/skrat/sunflow
- use pom file

* Sat Aug 09 2014 Dominik Mierzejewski <rpm@greysector.net> 0.07.2-2
- merge ant calls
- fix jpackage_script call parameters
- separate porting to newer janino patch from build fixes
- don't warn about running non-Sun JVM

* Sat Aug 09 2014 Dominik Mierzejewski <rpm@greysector.net> 0.07.2-1
- initial build
