%global base_name       dbcp
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.4
Release:          29%{?dist}
Summary:          Apache Commons DataBase Pooling Package
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
BuildArch:        noarch

Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

Patch0:           jdbc41.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-pool:commons-pool)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

%description
Many Apache projects support interaction with a relational database. Creating a
new connection for each user can be time consuming (often requiring multiple
seconds of clock time), in order to perform a database transaction that might
take milliseconds. Opening a connection per user can be unfeasible in a
publicly-hosted Internet application where the number of simultaneous users can
be very large. Accordingly, developers often wish to share a "pool" of open
connections between all of the application's current users. The number of users
actually performing a request at any given time is usually a very small
percentage of the total number of active users, and during request processing
is the only time that a database connection is required. The application itself
logs into the DBMS, and handles any user account issues internally.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
iconv -f iso8859-1 -t utf-8 RELEASE-NOTES.txt > RELEASE-NOTES.txt.conv && mv -f RELEASE-NOTES.txt.conv RELEASE-NOTES.txt

%patch0

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{short_name} %{name}

%build
# Skip tests, tomcat:naming-java and tomcat:naming-common not available
%mvn_build -f -- -Dcommons.osgi.symbolicName=org.apache.commons.dbcp -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Mat Booth <mat.booth@redhat.com> - 1.4-28
- Set compiler source and target to fix FTBFS

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 1.4-26
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-18
- Remove unused depmap
- Mavenize build-requires

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-15
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug  8 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-14
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Pavel Tisnovsky <ptisnovs@redhat.com> - 1.4-9
- Make this package independent of OpenJDK6 (it's buildable on OpenJDK7)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-7
- Build with maven 3
- Fixes according to latest guidelines

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 1.4-5
- Removed maven* BRs in favour of apache-commons-parent
- Added deprecated groupId to depmap for compatibility reasons
- Removed commons-pool from custom depmap

* Wed Oct 27 2010 Chris Spike <chris.spike@arcor.de> 1.4-4
- Added depmap entry to find commons-pool.jar

* Wed Oct 27 2010 Chris Spike <chris.spike@arcor.de> 1.4-3
- Added BR apache-commons-pool

* Mon Oct 18 2010 Chris Spike <chris.spike@arcor.de> 1.4-2
- Removed Epoch

* Mon Oct 4 2010 Chris Spike <chris.spike@arcor.de> 1.4-1
- Rename and rebase from jakarta-commons-dbcp
