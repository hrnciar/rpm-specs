Name:           jnr-enxio
Version:        0.19
Release:        7%{?dist}
Summary:        Unix sockets for Java
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        ASL 2.0 and LGPLv3
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

# Avoid split-package situation, this patch submitted upstream here: https://github.com/jnr/jnr-enxio/pull/26
Patch0: 0001-Add-enxio-classes-from-jnr-unixsocket.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 0.19-7
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.19-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Mat Booth <mat.booth@redhat.com> - 0.19-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Mat Booth <mat.booth@redhat.com> - 0.16-3
- Avoid OSGi split-package problems

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 0.16-1
- Update to latest release and regenerate BRs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.14-1
- Update to upstream 0.14.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.12-2
- Add missing BuildRequires to fix FTBFS (BZ#1405579).

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 0.12-1
- Update to upstream 0.12 that ships osgi metadata too.

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 0.10-1
- Update to upstream 0.10 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Jeff Johnston <jjohnstn@redhat.com> - 0.9-3
- Add proper MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.9-1
- Update to upstream 0.9.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8-1
- Update to upstream 0.8.

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-7
- Fix FTBFS due to XMvn changes in F21 (#1106957)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.3-5
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-3
- Document the multiple licensing scenario.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-2
- The license is in fact ASL 2.0 and LGPLv3.
- Properly use the dist tag.

* Wed Feb 06 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-1
- Initial package.
