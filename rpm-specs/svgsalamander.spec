%global gittag v1.1.2
%global gitname svgSalamander
# spec file for package svgsalamander

Name:           svgsalamander
Version:        1.1.2
Release:        5%{?dist}
Summary:        An SVG engine for Java

License:        LGPLv2+ or BSD
URL:            https://github.com/blackears/svgSalamander/
Source0:        https://github.com/blackears/%{gitname}/archive/%{gittag}/%{gitname}-%{version}.tar.gz
# Pulled from version 1.1.1
Source1:        pom.xml
# The interesting code changes from release to the commit 658fd1a
# https://github.com/blackears/svgSalamander/compare/v1.1.2...658fd1a
Patch1:         svgsalamander-master.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils 
BuildRequires:  maven-local
BuildRequires:  java-devel
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  sonatype-oss-parent
BuildRequires:  dos2unix
BuildRequires:  ant

Provides:       %{gitname}


%description
SVG Salamander is an SVG engine for Java that's designed to be small, fast, 
and allow programmers to use it with a minimum of fuss. It's in particular 
targeted for making it easy to integrate SVG into Java games and making it 
much easier for artists to design 2D game content - from rich interactive 
menus to charts and graphcs to complex animations.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{gitname}-%{version}
# To apply patches, we need normal line endings
find . -name '*.java' -exec dos2unix '{}' \;
%patch1 -p1

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

# Remove DOS line endings
for file in www/docs/*.html www/docs/exampleCode/*.html; do
  sed 's|\r||g' $file >$file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
pushd svg-core
cp %SOURCE1 pom.xml
%mvn_file : %{name} svgSalamander svg-salamander
%mvn_alias : com.kitfox.svg:svg-salamander
%mvn_build
popd

%install
pushd svg-core
%mvn_install
popd

%files -f svg-core/.mfiles
%doc www/docs/{exampleCode/,use.html}
%doc www/license/*

%files javadoc -f svg-core/.mfiles-javadoc
%doc www/license/*

%changelog
* Mon Feb 10 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.2-5
- Unbreak build by adding missing dependency (#1800173)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.2-3
- Backport upstream patches since release. The release introduced several
  regressions, which were slowly breaking JOSM (#1730554).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.2-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Cédric OLIVIER <cedric.olivier@free.fr> 1.1.1-1
- Update to release 1.1.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.39-1
- Update to release 0.1.39

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.33-1
- Update to release 0.1.33

* Tue Aug 12 2014 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.29-1
- Update to release 0.1.29

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 17 2013 Mat Booth <fedora@matbooth.co.uk> - 0.1.19-2
- Update for latest guidelines, rhbz #993389

* Tue Aug 06 2013 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.19-1
- Update to release 0.1.19

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.1.10-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Oct 18 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.10-1
- Update to release 0.1.10

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 02 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.1.1-1
- Update to release 0.1.1

* Sun Mar 11 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.1-1
- Update to release 0.1

* Tue Jan 17 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-6.106svn
- Update to last svn snapshot - new method needed by another package : josm
- Build with maven (it was ant before)
- Remove docs rights fix (updated in upstream)

* Wed Oct 05 2011 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-5
- Add ant.jar in classpath

* Wed Oct 05 2011 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-4
- Fix stange permissions on svgsalamander-generate-tarball.sh

* Thu Sep 08 2011 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-3
- Method to set classpath changed

* Sun Aug 14 2011 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-2
- Add to maven
- Remove DOS end lines

* Sun Aug 14 2011 Cédric OLIVIER <cedric.olivier@free.fr> 0.0-1
- First release

