#global commit d5b0d948fb737a9f1ef1e5bb261577f4f67e698c
%if %defined commit
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20160426
%endif

Summary: Stochastic reaction-diffusion simulator
Name: neurord
Version: 3.2.2
Release: 12%{?commit:.%{gitdate}git%{?shortcommit}}%{?dist}
License: GPLv2+

URL: https://github.com/neurord/stochdiff
%if %defined commit
Source0: %{url}/archive/%{commit}.tar.gz#/stochdiff-%{shortcommit}.tar.gz
%else
Source0: %{url}/archive/v%{version}.tar.gz#/stochdiff-%{version}.tar.gz
%endif
Patch1:        0001-Update-to-the-new-hdfview-2.13-interface.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.hdfgroup:jhdf5)
BuildRequires: mvn(org.hdfgroup:jhdfobj)
BuildRequires: mvn(org.jblas:jblas)
BuildRequires: mvn(org.testng:testng)

BuildRequires: /usr/bin/rst2html

# This is for jdfh5. Maybe it should be fixed there instead.
Requires:      mvn(org.slf4j:slf4j-api)
Requires:      mvn(org.slf4j:slf4j-simple)
# Explicit requires for javapackages-tools since neurord script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

%description
A simulator for biological reaction-diffusion systems.
Supports exact stochastic simulation, asynchronous leaping, fixed-τ leaping,
and stepped deterministic solutions. Output can be written as CSV text or HDF5
binary files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n stochdiff-%{?commit}%{?!commit:%{version}} -p1

%pom_remove_plugin :maven-shade-plugin
%pom_change_dep org.hdfgroup:hdf-java org.hdfgroup:jhdf5

%build
export LC_CTYPE=C.utf8
%mvn_build
rst2html README.rst README.html

%install
%mvn_install
%jpackage_script neurord.StochDiff "" "" neurord:jhdf5:jhdfobj:log4j/log4j-core:log4j/log4j-api:jblas:commons-cli:slf4j/slf4j-api:slf4j/slf4j-simple neurord true

%global _docdir_fmt %{name}

%files -f .mfiles
%{_bindir}/%{name}
%license LICENSE
%doc README.rst README.html stim-params{,2}.{svg,png}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.2-12
- Drop unnecessary BuildRequires maven-release-plugin.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.2.2-9
- Rebuild for hdf5 1.10.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 3.2.2-7
- Add explicit javapackages-tools requirement since neurord script
  uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.2-2
- Add patch and rebuild for new hdfview

* Mon Dec 12 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.2-1
- Update to latest release (#1403625)

* Sat Nov 12 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.1-1
- Update to latest release (#1389918)

* Sun Aug 21 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-1
- Update to latest release

* Wed Jul 20 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.1.2-1
- Update to latest release

* Tue Apr 26 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.0.0-7.20160426gitd5b0d94
- Update to latest upstream snapshot (fixes for a few bugs)

* Tue Apr 12 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-6.20160412git97a41ab
- Clarify licensing

* Mon Apr 11 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-5.20160317gitb17d063
- Use %%jpackage_script

* Fri Apr  1 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-4.20160317gitb17d063
- Remove more unnecessary deps

* Fri Apr  1 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-3.20160317gitb17d063
- Use proper maven deps for jhdf5

* Fri Mar 18 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-2.20160317gitb17d063
- Drop jpackage-utils dependency in javadoc subpackage

* Thu Mar 17 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-1.20160317gitb17d063
- Update to latest version, change name

* Wed Jan 30 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.10-2
- New logging setup.

* Wed Jan 30 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.10-1
- Initial build.
