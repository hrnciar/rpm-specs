Name:          plexus-pom
Version:       6.4
Release:       1%{?dist}
Summary:       Root Plexus Projects POM
License:       ASL 2.0

URL:           https://github.com/codehaus-plexus/plexus-pom
Source0:       %{url}/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :taglist-maven-plugin

cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Sun Aug 16 2020 Fabio Valentini <decathorpe@gmail.com> - 6.4-1
- Update to version 6.4.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Fabio Valentini <decathorpe@gmail.com> - 6.3-1
- Update to version 6.3.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 6.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 6.2-1
- Update to version 6.2.

* Thu Feb 13 2020 Fabio Valentini <decathorpe@gmail.com> - 6.1-1
- Update to version 6.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1-1
- Update to version 5.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Marian Koncek <mkoncek@redhat.com> - 5.0-4
- Remove Group tag

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.0-1
- Update to upstream version 5.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.3-1
- Update to upstream version 3.3.3

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-10
- Update upstream URL

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 3.3.1-9
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-7
- Rebuild to regenerate Maven auto-requires

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-6
- Rebuild to regenerate provides

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.3.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Dec 08 2012 gil cattaneo <puntogil@libero.it> 3.3.1-1
- Update to 3.3.1

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-3
- Install LICENSE file
- Resolves: rhbz#878825

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 gil cattaneo <puntogil@libero.it> 3.0.1-1
- initial rpm
