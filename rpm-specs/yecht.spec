%global commitversion 157cf13
%global dlversion 0.0.2-0-g157cf13
%global cluster jruby

Name:     yecht
Version:  1.0
Release:  15%{?dist}
Summary:  A YAML processor based on Syck
License:  MIT
URL:      http://github.com/%{cluster}/%{name}
Source0:  https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.zip
Patch0:   disable-jruby-dep.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-local
Requires: java-headless
Requires: jpackage-utils

BuildArch:      noarch

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -n %{name}-%{name}-%{version}
%patch0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

# remove unnecessary dependency on parent POM
%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Sep 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0-15
- Actually remove BR: sonatype-oss-parent.

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0-14
- Remove unnecessary dependency on parent POM.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0-4
- Add missing BuildRequires for sonatype-oss-parent to fix FTBFS (BZ#1402485).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Mo Morsi <mmorsi@redhat.com> - 1.0-1
- Update to yecht 1.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.2-10
- Move to java-headless
- Resolves: rhbz#1068604

* Tue Jan 07 2014 Michael Simacek <msimacek@redhat.com> - 0.0.2-10
- Adapt to current packaging guidelines (rhbz#1022174)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  06 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-4
- sync'd tarball source w/ upstream
- added my name that was missing from changelog

* Wed May  05 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-3
- added Alexander Kurtakov's patch to generate javadocs
- added javadoc bits to the spec

* Tue Apr  27 2010  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-2
- removed deprecated gcj bits
- fixed source uri

* Thu Jan  21 2009  Mohammed Morsi <mmorsi@redhat.com> - 0.0.2-1
- Initial build.
