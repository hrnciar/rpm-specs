%global scalacheck_version 1.11.3
%global scala_version 2.10
%global SBT 0
%global ANT 1
%global build_style %{ANT}

Name:           scalacheck
Version:        %{scalacheck_version}
Release:        14%{?dist}
Summary:        property-based testing for Scala

License:        BSD
URL:            http://www.scalacheck.org
Source0:        https://github.com/rickynils/scalacheck/archive/%{scalacheck_version}.tar.gz

%if %{build_style} == %{SBT}
# remove cross-compilation (not supported for Fedora) and
# binary-compatibility testing (due to unsupported deps)
Patch0:        scalacheck-1.11.0-build.patch
%else
# We don't generate a POM from the ant build
Source1:       http://repo1.maven.org/maven2/org/scalacheck/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
# remove maven-ant-tasks
Patch0:        scalacheck-1.11.3-ant-build.patch
%endif

BuildArch:      noarch
BuildRequires:  scala
%if %{build_style} == %{SBT}
BuildRequires:  sbt
%else
BuildRequires:  ant
%endif
BuildRequires:  mvn(org.scala-sbt:test-interface)
BuildRequires:  javapackages-local


%description
ScalaCheck is a library written in Scala and used for automated
property-based testing of Scala or Java programs. ScalaCheck was
originally inspired by the Haskell library QuickCheck, but has also
ventured into its own.

ScalaCheck has no external dependencies other than the Scala runtime,
and works great with sbt, the Scala build tool. It is also fully
integrated in the test frameworks ScalaTest and specs2. You can of
course also use ScalaCheck completely standalone, with its built-in
test runner.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find . -name \*.class -delete
find . -name \*.jar -delete

%if %{build_style} == %{SBT}
cp -r /usr/share/java/sbt/ivy-local .
mkdir boot
%else

%endif

%patch0 -p1

%if %{build_style} == %{SBT}
sed -i -e 's/0[.]13[.]0/0.13.1/g' project/build.properties
%endif

%mvn_file org.%{name}:%{name}_%{scala_version} %{name}

%build

%if %{build_style} == %{SBT}
export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local
sbt package deliverLocal publishM2Configuration
%mvn_artifact target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar
%else
ant -Dversion=%{version} jar doc
%mvn_artifact %{SOURCE1} target/%{name}-%{version}.jar
%endif

%install

%if %{build_style} == %{SBT}

%mvn_install -J target/scala-%{scala_version}/api

%else
%mvn_install -J target/doc/main/api

# We only run %%check in an ant build at the moment
%check
ant test

%endif

%files -f .mfiles
%doc README.markdown RELEASE
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 gil cattaneo <puntogil@libero.it> 1.11.3-6
- Fix FTBFS RHBZ#1107280
- Introduce license macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 William Benton <willb@redhat.com> - 1.11.3-3
- rebuild

* Thu Jan 30 2014 William Benton <willb@redhat.com> - 1.11.3-2 
- rebuild now that all of our dependencies are in stable

* Wed Jan 29 2014 William Benton <willb@redhat.com> - 1.11.3-1 
- added optional but on-by-default Ant build (thanks to Gil Cattaneo for contributing this!)

* Mon Dec 23 2013 William Benton <willb@redhat.com> - 1.11.0-1 
- initial package
