%global url     https://github.com/tdunning/%{name}

Name:           t-digest
Version:        3.0
Release:        12%{?dist}
Summary:        A new data structure for on-line accumulation of statistics
License:        ASL 2.0
URL:            %{url}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
#grep -ir -e "<p/>"
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TreeDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/ArrayDigest.java
Patch0:         jdk8-javadoc.patch

BuildArch:      noarch

BuildRequires:  maven-local

Requires:       java

%description
A new data structure for accurate on-line accumulation of rank-based statistics
eg. quantiles and trimmed means. The t-digest algorithm is also very parallel
friendly making it useful in map-reduce and parallel streaming applications.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
# Useless tasks
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

%build
#skipping tests, they requires currently unpacked depndences
%mvn_build  --force -- -Dmaven.javadoc.skip=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICES

%files javadoc 
%license LICENSE NOTICES

%changelog
* Mon May 04 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- dropping javadoc to build with jdk11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 gil cattaneo <puntogil@libero.it> 3.0-4
- remove useless plugin
- remove duplicate files
- introduce license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Jiri Vanek <jvanek@redhat.com> - 3.0-2
- added  patch0, jdk8-javadoc.patch (will be upstreamed)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jul 20 2014 Jiri Vanek <jvanek@redhat.com> - 3.0-1
- Initial packaging
