Name:           options
Version:        1.2
Release:        17%{?dist}
Summary:        Library for managing sets of JVM properties to configure an app or library
License:        ASL 2.0
URL:            https://github.com/headius/%{name}
Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  maven-local

%description
Provides a simple mechanism for defining JVM property-based
configuration for an application or library.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .

# remove unnecessary dependency on parent POM
%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files  -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2-17
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.2-7
- Add missing BuildRequires to fix FTBFS (BZ#1406488).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-4
- Remove Group from javadoc package, add license to
  both packages

* Wed Dec 03 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-3
- Moved LICENSE-2.0.txt file to main pkg, marked as doc

* Tue Oct 14 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-2
- Include license text, remove group tag
- Update to comply with Fedora guidelines

* Mon Oct 13 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-1
- Initial package
