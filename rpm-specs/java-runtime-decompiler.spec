Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 3.0
Release: 9%{?dist}
License: GPLv3
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/pmikova/%{name}/archive/%{name}-%{version}.tar.gz
Source1: java-runtime-decompiler
Source2: java-runtime-decompiler.1
Source3: jrd.desktop
Patch1: systemFernflower.patch
Patch2: systemProcyon.patch
Patch3: rsyntaxVersion.patch
BuildArch: noarch
BuildRequires: maven-local
BuildRequires: byteman
BuildRequires: rsyntaxtextarea
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
# depends on devel, not runtime (needs tools.jar)
BuildRequires: java-1.8.0-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
Requires: java-1.8.0-devel
Recommends: fernflower
Recommends: procyon-decompiler

%description
This application can access JVM memory at runtime,
extract byte code from the JVM and decompile it. 
%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
pushd runtime-decompiler
%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools
%pom_remove_plugin :maven-jar-plugin
popd
%mvn_build --xmvn-javadoc

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
cp -r %{_builddir}/%{name}-%{name}-%{version}/runtime-decompiler/src/plugins/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor="fedora"                     \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

%files -f .mfiles
%attr(755, root, -) %{_bindir}/java-runtime-decompiler
%{_mandir}/man1/java-runtime-decompiler.1*

# wrappers for decompilers
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%license LICENSE

%dir %{_datadir}/applications
%{_datadir}/applications/fedora-jrd.desktop

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-7
- aligned rsyntaxtextarea version, fixed javadoc generation

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-6
- changed jdk8 requirement

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-3
- all stdouts from customlauncher moved to stderr

* Mon Aug 26 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-0
- moved to usptream version 3.0
- adjusted configs, removed lambda patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-5
- improved Patch3, includeLambdas.patch to sort the lamdas t the bottom

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-4
- added depndence of procyon decompiler (currenlty under review
- added and applied Patch2, systemProcyon.patch to enable system procyon out of thebox
- added and applied Patch3, includeLambdas.patch to at least list lamdas untill fixed in upstream

* Thu Jan 10 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-3
- added depndence of fernflower decompiler
- added and applied Patch1, systemFernflower.patch to enable system fernflower

* Wed Nov 28 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-2
- fixed changelog

* Mon Nov 19 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-1
- fixed issues listed in review (rhbz#1636019)
- added installation of desktop file

* Wed Jun 06 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 1.1-1
- initial commit
