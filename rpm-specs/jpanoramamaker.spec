%global majorv 5
%global minorv 6

Name:           jpanoramamaker
Version:        %{majorv}.%{minorv}
Release:        13%{?dist}
Summary:        Tool for stitching photos to panorama in linear curved space
BuildArch:      noarch

#Group:          Applications/Graphics
License:        BSD
URL:            http://jpanoramamaker.wz.cz
Source0:        http://jpanoramamaker.wz.cz/fedora/%{name}-%{version}.src.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         bumpJdkVersion.patch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  swing-layout
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Requires:       java
Requires:       swing-layout

%description
Tool for stitching photos to panorama in linear curved space

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.
This tool is unique in number of manual touches you can do to affect final result.
Sometimes simple changing of order of image or lying a bit on position where they meet can do miracles.


%prep
%setup -q -n %{name}-%{majorv}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch1 -p1

#add swing-layout to classpath
sed -i 's-javac.classpath=\\-javac.classpath=/usr/share/java/swing\-layout/swing\-layout.jar\:\\-g'  nbproject/project.properties
#remove copylibraries
sed -i 's/<taskdef/<!--<taskdef/g' nbproject/build-impl.xml
sed -i 's:</copylibs>:</copylibs>-->:g' nbproject/build-impl.xml

%build
ant

#pack manually
pushd  build/classes
jar -cvf ../../dist/%{name}.jar *
popd

%install
rm -rf $RPM_BUILD_ROOT

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  jpanoramamaker.desktop
cp -p ./jpanoramamaker.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/jpanoramamaker.png
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./jpanoramamaker $RPM_BUILD_ROOT%{_bindir}/jpanoramamaker
#end launcher



# we are in /BUILD/jpanoramamaker-5/
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp ./dist/javadoc/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


#####################################

%files
%{_datadir}/pixmaps/jpanoramamaker.png
%{_datadir}/applications/jpanoramamaker.desktop
%attr(755,root,root) %{_bindir}/jpanoramamaker
%{_datadir}/appdata/%{name}.appdata.xml


%defattr(-,root,root,-)
%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}


%changelog
* Wed Apr 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-13
- bumping source and target to dramatical 1.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 28 2014 Jiri Vanek <jvanek@redhat.com> - 5-6-3
- Added appdata.xml

* Fri Nov 29 2013 Jiri Vanek <jvanek@redhat.com> - 5.6-1
- updted to upstream 5.6
- removed versioned jar (resolves rhbz#1022124)
- adapted to new build script

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Jiri Vanek <jvanek@redhat.com> - 5.5-0
- folowing changes in jutils, version for classpath setup fixed
- unlimited number of arguments now supported
- removed ant-nodeps

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Jiri Vanek <jvanek@redhat.com> - 5.4-1
- rebuild with jdk7, corrected versioning, path in setup changed acordingly

* Tue Feb 7 2012 Jiri Vanek <jvanek@redhat.com> - 5-8
- updated sources to 5.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 3 2011 Jiri Vanek <jvanek@redhat.com> - 5-6
-updated sources to 5.3

* Sun Jul 3 2011 Jiri Vanek <jvanek@redhat.com> - 5-5
-updated sources to 5.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Jiri Vanek <jvanek@redhat.com> - 5-2
-added desktop integration
-launcher extracted to separated file


* Wed Sep 29 2010 Jiri Vanek <jvanek@redhat.com> - 5-1
-first release of version 5

