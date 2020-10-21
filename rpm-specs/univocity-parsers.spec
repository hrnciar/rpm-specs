%bcond_without tests

Name:           univocity-parsers
Version:        2.9.0
Release:        1%{?dist}
Summary:        Collection of parsers for Java
License:        ASL 2.0

URL:            https://github.com/uniVocity/univocity-parsers
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
%if %{with tests}
BuildRequires:  mvn(com.univocity:univocity-output-tester)
BuildRequires:  mvn(org.hsqldb:hsqldb)
BuildRequires:  mvn(org.testng:testng)
%endif

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%if %{with tests}
%mvn_build
%else
%mvn_build -f
%endif

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.html

%changelog
* Fri Aug 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.9.0-1
- Update to version 2.9.0.

* Thu Aug 13 2020 Mat Booth <mat.booth@redhat.com> - 2.8.4-5
- Make OSGi requirement on com.googlecode.openbeans optional

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Mat Booth <mat.booth@redhat.com> - 2.8.4-3
- Allow building without tests

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.8.4-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Feb 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.8.4-1
- Update to version 2.8.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.3-1
- Update to version 2.8.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Mat Booth <mat.booth@redhat.com> - 2.5.5-4
- Remove unnecessary javadoc invocation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.5-1
- Initial packaging
