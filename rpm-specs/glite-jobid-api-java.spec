%global groupId     org.glite
%global artifactId  jobid-api-java
%{!?_mavenpomdir: %global _mavenpomdir %{_datadir}/maven2/poms}

Name:           glite-jobid-api-java
Version:        1.3.9
Release:        12%{?dist}
Summary:        JAVA implementation of handling gLite jobid

License:        ASL 2.0
URL:            http://glite.cern.ch
Source:         http://scientific.zcu.cz/emi/emi.jobid.api-java/%{name}-%{version}.tar.gz
# https://github.com/CESNET/glite-lb/commit/00da23f52e6e680f3dee067f545e5f35b07a751c
Patch0:         glite-jobid-api-java-javadoc.patch

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:  apache-commons-codec
BuildRequires:  maven-local
%else
BuildRequires:  jakarta-commons-codec
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
%endif
%if 0%{?rhel} >= 7 || 0%{?fedora}
Requires:       apache-commons-codec
%else
Requires:       jakarta-commons-codec
%endif
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 20
Requires:       java-headless
%else
Requires:       java
%endif
%if 0%{?rhel} <= 6 && ! 0%{?fedora}
Requires:       jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
%endif

%description
JAVA implementation of library handling gLite jobid.


%package        javadoc
Summary:        Java API documentation for %{name}
Requires:       %{name} = %{version}-%{release}
%if 0%{?rhel} <= 6 && ! 0%{?fedora}
Requires:       jpackage-utils
%endif

%description    javadoc
This package contains java API documentation for java implementation of gLite
jobid.


%prep
%setup -q
%patch0 -p2


%build
perl ./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_javadocdir}
mv %{buildroot}%{_docdir}/%{name}-%{version}/api %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_mavenpomdir}
install -m 0644 JPP-%{name}.pom %{buildroot}%{_mavenpomdir}
%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}
touch .mfiles
%endif


%if 0%{?rhel} <= 6 && ! 0%{?fedora}
%post
%update_maven_depmap
%endif


%if 0%{?rhel} <= 6 && ! 0%{?fedora}
%postun
%update_maven_depmap
%endif


%files -f .mfiles
%doc ChangeLog LICENSE
%if ! 0%{?add_maven_depmap:1}
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%endif

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 František Dvořák <valtri@civ.zcu.cz> - 1.3.9-4
- Patch to fix javadoc 8 errors

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.9-2
- Move from the old jakarta-commons-lang to apache-commons-lang in Requires

* Thu Jun 26 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.9-1
- New release 1.3.9 (L&B 4.1.2)
- Consistent style with buildroot macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.8-1
- New release 1.3.8 (L&B 4.1.1)
- Change jakarta-commons-codec BR/R in Fedora to apache-commons-codec
- Using .mfiles to build with javapackages 4.x

* Sun Feb 23 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.7-2
- EPEL 7 support
- Switch to java-headless (RB #1068106)

* Fri Nov 22 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.7-1
- New release 1.3.7 (L&B 4.0.12)
- Pom file patch not needed anymore

* Mon Aug 26 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.6-1
- Initial package
