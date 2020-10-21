Name:          reflections
Version:       0.9.12
Release:       4%{?dist}
Summary:       Java run-time meta-data analysis
License:       WTFPL
URL:           https://github.com/ronmamo/reflections
Source0:       https://github.com/ronmamo/reflections/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.dom4j:dom4j)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jsr-305:ri)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  java-atk-wrapper

BuildArch:     noarch

%description
A Java run-time meta-data analysis, in the spirit of Scannotations

Reflections scans your class-path, indexes the meta-data, allows you
to query it on run-time and may save and collect that information
for many modules within your project.

Using Reflections you can query your meta-data such as:
* get all sub types of some type
* get all types/methods/fields annotated with some annotation,
  w/o annotation parameters matching
* get all resources matching matching a regular expression

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

# Unwanted
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin
# Use system maven default conf
%pom_remove_plugin :maven-javadoc-plugin

# Force servlet 3.1 apis
%pom_change_dep :servlet-api :javax.servlet-api:3.1.0

# Cannot find symbol package javax.annotation
%pom_add_dep org.jsr-305:ri

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license COPYING.txt

%files javadoc -f .mfiles-javadoc
%license COPYING.txt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.9.12-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Apr 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.9.12-2
- Clean up BuildRequires with xmvn-builddep.

* Fri Feb 07 2020 Ben Rosser <rosser.bjr@gmail.com> - 0.9.12-1
- Update to latest upstream release, 0.9.12.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Mat Booth <mat.booth@redhat.com> - 0.9.10-6
- Fix failure to build from source

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 gil cattaneo <puntogil@libero.it> 0.9.10-1
- update to 0.9.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 gil cattaneo <puntogil@libero.it> 0.9.9-3
- fix url taraball

* Mon Mar 02 2015 gil cattaneo <puntogil@libero.it> 0.9.9-2
- remove bundled jar (used only for testing)

* Sat Feb 21 2015 gil cattaneo <puntogil@libero.it> 0.9.9-1
- update to 0.9.9

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 0.9.9-0.2.RC1
- fix license tag

* Tue Jun 04 2013 gil cattaneo <puntogil@libero.it> 0.9.9-0.1.RC1
- update to 0.9.9-RC1

* Fri Jun 22 2012 gil cattaneo <puntogil@libero.it> 0.9.8-1
- initial rpm
