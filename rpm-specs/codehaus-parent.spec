Name:           codehaus-parent
Version:        4
Release:        17%{?dist}
Summary:        Parent pom file for codehaus projects
License:        ASL 2.0
URL:            http://codehaus.org/
BuildArch:      noarch

#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-enforcer.patch

BuildRequires:  maven-local

%description
This package contains the parent pom file for codehaus projects.

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
%patch0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-7
- Rebuild to regenerate Maven auto-requires

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-6
- Update to current packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-3
- Install LICENSE

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 Orion Poplawski <orion@cora.nwra.com> - 4-1
- Update to version 4

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-5
- Patch enforcer plugin out so it's not needed in all child packages

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 5 2011 Orion Poplawski <orion@cora.nwra.com> - 3-3
- Strip requires

* Wed May 4 2011 Orion Poplawski <orion@cora.nwra.com> - 3-2
- Drop build and defattr
- Better summary/description
- Upstream set license to ASL 2.0

* Fri Apr 29 2011 Orion Poplawski <orion@cora.nwra.com> - 3-1
- Initial package
