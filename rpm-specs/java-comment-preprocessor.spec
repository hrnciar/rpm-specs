%if 0%{?fedora}
%bcond_with tests
%else
%bcond_with tests
%endif

%global section		devel

Summary:	The Most Powerful Multi-Pass Java Preprocessor
Name:		java-comment-preprocessor
Version:	6.1.4
Release:	6%{?dist}
License:	ASL 2.0

URL:		https://github.com/raydac/java-comment-preprocessor
Source0:	https://github.com/raydac/%name/archive/%version/%name-%version.tar.gz

Patch0:		java-comment-preprocessor-6.1.4-revert-junit5.patch

BuildArch:		noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-jar)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.powermock:powermock-api-mockito)
BuildRequires:  mvn(org.powermock:powermock-module-junit4)
%endif

%description
It is the most powerful multi-pass preprocessor for Java
but also it can be used everywhere for text processing
if the destination technology supports Java like comment definitions.

%package javadoc
Summary:	API docs for %{name}

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%autosetup -p1

# remove unpackaged and dangerous deps
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml
%pom_remove_plugin :maven-shade-plugin pom.xml

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%build
%if %{with tests}
%mvn_build    -- -P'!metacheck'
%else
%mvn_build -f -- -P'!metacheck'
%endif

%install
%mvn_install

%files -f .mfiles
%license texts/LICENSE-2.0.txt
%doc texts/readme.txt

%files javadoc -f .mfiles-javadoc
%license texts/LICENSE-2.0.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Pavel Raiskup <praiskup@redhat.com> - 6.1.4-4
- disable testsuite as a workaround for too new mockito (rhbz#1675171)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Pavel Raiskup <praiskup@redhat.com> - 6.1.4-1
- new upstream release

* Wed May 30 2018 Pavel Raiskup <praiskup@redhat.com> - 6.0.1-9
- use better upstream tarball name

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.0.1-9
- Disable tests and regenerate BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Merlin Mathesius <mmathesi@redhat.com> - 6.0.1-7
- Add missing BuildRequires to fix FTBFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 6.0.1-4
- Add missing BuildRequires to fix FTBFS (BZ#1405633).

* Fri Apr 15 2016 Pavel Kajaba <pkajaba@redhat.com> - 6.0.1-3
- Deleted unused and dangerous dependencies (review rhbz#1297347)

* Thu Apr 14 2016 Pavel Raiskup <praiskup@redhat.com> - 6.0.1-2
- don't require jpackage-utils (review rhbz#1297347)

* Tue Jan 5 2016 Pavel Kajaba <pkajaba@redhat.com> - 6.0.1-1
- Initial creation of java-comment-preprocessor package
