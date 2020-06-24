Name:          ebay-cors-filter
Version:       1.0.1
Release:       12%{?dist}
Summary:       eBay CORS filter
License:       ASL 2.0
URL:           https://github.com/eBay/cors-filter
Source0:       https://github.com/eBay/cors-filter/archive/cors-filter-%{version}.tar.gz
Patch0:        %{name}-1.0.1-servlet.patch

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
CORS (Cross Origin Resource Sharing) is a mechanism supported by W3C to
enable cross origin requests in web-browsers. CORS requires support from
both browser and server to work. This is a Java servlet filter
implementation of server-side CORS for web containers such as Apache
Tomcat.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n cors-filter-cors-filter-%{version}
%patch0 -p1

%build
sed -i 's/\r//' LICENSE NOTICE README.md
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md cors-flowchart.png
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-3
- Fixed unowned directories
- Fixed DOS newlines in license and doc files

* Sat Apr  4 2015 Gil Cattaneo <puntogil@libero.it> - 1.0.1-2
- Added NOTICE to licenses
- Added servlet 3.1 apis support

* Fri Apr  3 2015 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-1
- Initial packaging.
