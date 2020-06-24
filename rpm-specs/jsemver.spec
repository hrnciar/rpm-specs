Name:           jsemver
Version:        0.9.0
Release:        11%{?dist}
Summary:        A Java implementation of the Semantic Versioning Specification

License:        MIT
URL:            https://github.com/zafarkhaja/jsemver
Source0:        https://github.com/zafarkhaja/jsemver/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin >= 3.2
BuildRequires:  maven-javadoc-plugin >= 2.10.2
BuildRequires:  junit >= 4.12
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
JSemVer (formerly Java SemVer) is a Java implementation of
version 2.0.0 of the Semantic Versioning Specification

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q
find -name \*.jar -delete
find -name \*.class -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc CHANGELOG.md
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 28 2017 Neal Gompa <ngompa13@gmail.com> - 0.9.0-5
- Add missing BuildRequires, thanks to Nicolas Lécureuil from Mageia

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Neal Gompa <ngompa13@gmail.com> - 0.9.0-1
- Update to upstream version 0.9.0

* Wed Apr  8 2015 Neal Gompa <ngompa13@gmail.com> - 0.8.0-1
- Added extra prep step to delete *.class/*.jar files
- Added statement to own maven pom dir
- Removed duplicate doc files from -javadoc
- Removed license file going into doc
- Removed unnecessary epoch
- Initial Packaging
