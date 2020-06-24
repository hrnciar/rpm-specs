%{?scl:%scl_package jgraphx}
%{!?scl:%global pkg_name %{name}}

%if 0%{?rhel} && 0%{?rhel} <= 7
# Use java common's requires/provides generator
%{?java_common_find_provides_and_requires}
%endif

Name:           %{?scl_prefix}jgraphx
Version:        3.6.0.0
Release:        10%{?dist}
Summary:        Java Graph Drawing Component

License:        BSD
URL:            http://www.jgraph.com/jgraph.html
Source0:        http://www.jgraph.com/downloads/jgraphx/archive/%{pkg_name}-%(echo %{version} |sed 's/\./_/g').zip
Source1:        bnd.properties

Patch1:         CVE-2017-18197-XXE-fix.patch

BuildRequires:  %{?scl_prefix_java_common}javapackages-local
BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  %{?scl_prefix_maven}aqute-bnd
%{!?scl:
Requires:       java-headless
Requires:       jpackage-utils
}
%{?scl:Requires: %scl_runtime}

BuildArch:      noarch

%description
JGraphX is the a powerful, easy-to-use and feature-rich graph drawing
component for Java. It is a rewrite of JGraph, also known as JGraph 6.

%package javadoc
Summary:        API Documentation for %{name}
%{!?scl:
Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
}
%{?scl:Requires: %scl_runtime}

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n %{pkg_name}
find -name '*.jar' -delete
rm -rf docs/api
%patch1 -p2

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
ant build maven-jar

#Convert to OSGi bundle
pushd lib
%if 0%{?fedora} >= 23 || 0%{?rhel} > 7
  bnd wrap --output %{pkg_name}.bar --properties %{SOURCE1} \
           --version %{version} %{pkg_name}.jar
%else
  java -jar $(build-classpath aqute-bnd) wrap -output jgraphx.bar -properties %{SOURCE1} %{pkg_name}.jar
%endif
mv %{pkg_name}.bar %{pkg_name}.jar
popd
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_artifact pom.xml lib/%{pkg_name}.jar
%mvn_install -J docs/api/
%{?scl:EOF}

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%if 0%{?rhel} <= 6 || 0%{?rhel} > 7
  %doc license.txt
%else
  %license license.txt
%endif

%files javadoc -f .mfiles-javadoc
%if 0%{?rhel} <= 6 || 0%{?rhel} > 7
  %doc license.txt
%else
  %license license.txt
%endif

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Severin Gehwolf <sgehwolf@redhat.com> - 3.6.0.0-6
- Add patch for CVE-2017-18197.
  Resolves RHBZ#1550354

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Merlin Mathesius <mmathesi@redhat.com> - 3.6.0.0-4
- Cleanup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Severin Gehwolf <sgehwolf@redhat.com> - 3.6.0.0-1
- Update to latest upstream release. Resolves RHBZ#1325575.

* Tue Mar 22 2016 Severin Gehwolf <sgehwolf@redhat.com> - 3.5.0.0-1
- Update to latest upstream release. Resolves RHBZ#1179202.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Severin Gehwolf <sgehwolf@redhat.com> - 3.1.2.0-6
- Make latest spec file buildable on F22 too.

* Thu Jul 23 2015 Severin Gehwolf <sgehwolf@redhat.com> - 3.1.2.0-5
- SCL-ize package.

* Fri Jul 17 2015 Severin Gehwolf <sgehwolf@redhat.com> - 3.1.2.0-4
- Wrap jar using aqute-bnd so as to provide OSGi metadata.
- Resolves: RHBZ#1240777

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Clément David <c.david86@gmail.com> - 3.1.2.0-2
- Provide maven pom.xml

* Tue Dec 09 2014 Clément David <c.david86@gmail.com> - 3.1.2.0-1
- Update version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Clément David <c.david86@gmail.com> - 2.5.0.2-1
- Update version

* Wed Oct 23 2013 Clément David <c.david86@gmail.com> - 2.1.0.7-2
- Remove versioned jars

* Fri Aug 02 2013 Clément David <c.david86@gmail.com> - 2.1.0.7-1
- Update version

* Fri Jul 26 2013 Clément David <c.david86@gmail.com> - 2.1.0.4-1
- Update version

* Tue Dec 04 2012 Clément David <c.david86@gmail.com> - 1.10.4.0-1
- Update version

* Thu Apr 05 2012 Clément David <c.david86@gmail.com> - 1.9.2.5-1
- Bump version

* Mon Apr 02 2012 Clément David <c.david86@gmail.com> - 1.9.2.4-2
- Update version

* Wed Sep 29 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.4.1.0-2
- Drop files in %%prep, fix URL (Markus Mayer)

* Mon Sep 20 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.4.1.0-1
- Bump version
- Fix URL (Markus Mayer)
- Add required dependencies (Markus Mayer)

* Thu Apr 29 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1.6-1
- Initial packaging
