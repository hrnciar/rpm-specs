%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-el-3.0-api
Version:          1.0.13
Release:          2%{dist}
Summary:          JSR-341 Expression Language 3.0 API
License:          (CDDL or GPLv2 with exceptions) and ASL 2.0
Url:              https://github.com/jboss/jboss-el-api_spec
Source0:          %{url}/archive/jboss-el-api_3.0_spec-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:          cddl.txt

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.glassfish:javax.el-impl)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

BuildArch:        noarch

%description
The JSR-341 Expression Language 3.0 API classes.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-el-api_spec-jboss-el-api_3.0_spec-%{namedversion}

cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin :maven-source-plugin

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE cddl.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE cddl.txt LICENSE-2.0.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.13-1
- Update to version 1.0.13.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 gil cattaneo <puntogil@libero.it> 1.0.5-1
- update to 1.0.5.Final
- fix BR list and use BR mvn()-like
- introduce license macro
- remove some rpmlint problems
- remove duplicate files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Alpha1
- Initial packaging


