Name:          concurrent-trees
Version:       2.6.1
Release:       6%{?dist}
Summary:       Concurrent Trees for Java
License:       ASL 2.0
URL:           https://github.com/npgall/%{name}/
Source0:       https://github.com/npgall/%{name}/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
# for version 2.6.0 add bnd-maven-plugin
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)

BuildArch:     noarch

%description
This library provides concurrent Radix Trees and
concurrent Suffix Trees for Java.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{version}
rm -r documentation/javadoc
rm -r documentation/documents
rm documentation/images/dfs-comic.png

# Unneeded tasks
%pom_remove_plugin :maven-release-plugin code
%pom_remove_plugin :maven-gpg-plugin code
%pom_remove_plugin :maven-javadoc-plugin code
%pom_remove_plugin :maven-source-plugin code

%mvn_file :%{name} %{name}

%build
# the following does not work in f28, probably a bug
#%%mvn_build -- -f code/pom.xml
cd code
%mvn_build

%install
cd code
%mvn_install

%files -f code/.mfiles
%doc README.md documentation/
%license LICENSE.txt

%files javadoc -f code/.mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Tomas Repik <trepik@redhat.com> - 2.6.1-1
- Update to 2.6.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Tomas Repik <trepik@redhat.com> - 2.6.0-1
- version update

* Tue Jun 21 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-2
- remove maven-source-plugin causing failure

* Thu Apr 21 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-1
- initial package

