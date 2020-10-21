Name:           apache-commons-collections4
Summary:        Extension of the Java Collections Framework
Version:        4.4
Release:        4%{?dist}
License:        ASL 2.0

URL:            http://commons.apache.org/proper/commons-collections/
Source0:        http://archive.apache.org/dist/commons/collections/source/commons-collections4-%{version}-src.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)

%description
Commons-Collections seek to build upon the JDK classes by providing
new interfaces, implementations and utilities.


%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.


%prep
%setup -q -n commons-collections4-%{version}-src
%mvn_file : commons-collections4 %{name}


%build
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.collections4


%install
%mvn_install


%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.4-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.4-1
- Update to version 4.4.

* Fri Feb 08 2019 Mat Booth <mat.booth@redhat.com> - 4.1-5
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Mat Booth <mat.booth@redhat.com> - 4.1-1
- Update to latest upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 4.0-7
- Regenerate buildrequires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 4.0-4
- Fix parent POM BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0-1
- Initial packaging

