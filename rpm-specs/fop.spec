Name:           fop
Summary:        XSL-driven print formatter
Version:        2.4
Release:        1%{?dist}
# ASL 1.1:
# several files in fop-core/src/main/resources/org/apache/fop/render/awt/viewer/resources
# rest is ASL 2.0
License:        ASL 2.0 and ASL 1.1
URL:            https://xmlgraphics.apache.org/fop
Source0:        https://www.apache.org/dist/xmlgraphics/%{name}/source/%{name}-%{version}-src.tar.gz
Source1:        %{name}.script
Source2:        batik-pdf-MANIFEST.MF
Source3:        https://repo1.maven.org/maven2/org/apache/xmlgraphics/%{name}/%{version}/%{name}-%{version}.pom
Source4:        https://www.apache.org/licenses/LICENSE-1.1.txt
Patch1:         0001-Main.patch
Patch2:         0002-Use-sRGB.icc-color-profile-from-colord-package.patch
Patch3:         0003-Disable-javadoc-doclint.patch
Patch4:         0004-Port-to-QDox-2.0.patch
Patch5:         0005-Allow-javascript-in-javadoc.patch

BuildArch:      noarch

Requires:       apache-commons-io >= 1.2
Requires:       apache-commons-logging >= 1.0.4
Requires:       batik >= 1.7
Requires:       fontbox
Requires:       jakarta-commons-httpclient
Requires:       java
Requires:       xalan-j2 >= 2.7.0
Requires:       xml-commons-apis >= 1.3.04
Requires:       xmlgraphics-commons >= 1.5
# Explicit requires for javapackages-tools since fop script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-logging
BuildRequires:  batik
BuildRequires:  fontbox
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  qdox
BuildRequires:  servlet
BuildRequires:  xmlgraphics-commons >= 1.5
BuildRequires:  xmlunit

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%prep
%autosetup -p1

cp %{SOURCE4} LICENSE-1.1

rm -f fop/lib/*.jar fop/lib/build/*.jar

#upstream workaround -- many thanks to spepping@apache.org -- see https://issues.apache.org/bugzilla/show_bug.cgi?id=50575
ln -s %{_javadir}/qdox.jar fop/lib/build/qdox.jar

%build
#qdox intentionally left off classpath -- see https://issues.apache.org/bugzilla/show_bug.cgi?id=50575
export CLASSPATH=$(build-classpath apache-commons-logging apache-commons-io \
    fontbox xmlgraphics-commons batik-all avalon-framework-api \
    avalon-framework-impl servlet batik/batik-svg-dom xml-commons-apis \
    xml-commons-apis-ext objectweb-asm/asm-all xmlunit)
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
ant -f fop/build.xml jar-main transcoder-pkg javadocs

%install
# inject OSGi manifest
jar ufm fop/build/%{name}.jar %{SOURCE2}


# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 fop/build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 fop/build/%{name}-transcoder.jar %{buildroot}%{_javadir}/pdf-transcoder.jar

# script
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/fop

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
cp -rp fop/conf/* %{buildroot}%{_datadir}/%{name}/conf

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp fop/build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files -f .mfiles
%doc LICENSE LICENSE-1.1 README NOTICE
%{_datadir}/%{name}
%{_javadir}/pdf-transcoder.jar
%{_bindir}/fop

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE LICENSE-1.1


%changelog
* Fri Feb 21 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.4-1
- Ver. 2.4
- No nonger requires avalon framework

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.2-3
- Add explicit javapackages-tools requirement since fop script
  uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2-1
- Ver. 2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-8
- Elimitate race condition when injecting JAR manifest
- Resolves: rhbz#1495235

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-7
- Add fontbox to classpath
- Resolves: rhbz#1413340

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 2.0-4
- Fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Michael Simacek <msimacek@redhat.com> - 2.0-2
- Add fix for FOP-2461 (rhbz#1251173)

* Tue Jul 14 2015 Michael Simacek <msimacek@redhat.com> - 2.0-1
- Update to upstream version 2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-10
- Disable javadoc doclint

* Tue Mar 17 2015 Michael Simacek <msimacek@redhat.com> - 1.1-9
- Port to current QDox and xmlgraphics-commons

* Mon Jun 16 2014 Michal Srb <msrb@redhat.com> - 1.1-8
- Fix FTBFS

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 2 2014 Richard Hughes <rhughes@redhat.com> 1.1-6
- Drop the icc-profiles-openicc requirement and switch to using the colord sRGB
  profile filename.
- Resolves: #1042655

* Thu Nov 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1-5
- Fix the OSGi manifest.

* Wed Sep 18 2013 Michal Srb <msrb@redhat.com> - 1.1-4
- Fix license tag (Resolves: rhbz#979394)
- Add ASL 1.1 license text

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Michal Srb <msrb@redhat.com> - 1.1-2
- Build from clean tarball
- Spec file clean up

* Fri Apr 12 2013 Michal Srb <msrb@redhat.com> - 1.1-1
- Update to upstream version 1.1
- Replace proprietary color profile with free CP from icc-profiles-openicc package
- Resolves: rhbz#848659

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-20
- Add xml-commons-apis-ext to classpath

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-16
- Supply missing event-model.xml files

* Fri Jun 3 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-15
- Split avalon-framework into avalon-framework-api and avalon-framework-impl in classpath

* Thu Mar 10 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-14
- Reapply Fedora guidelines.
- Re-add pom.xml to unbreak Maven stack.
- Re-add OSGi manifest to unbreak Eclipse stack.
- Remove all bundled jars and classes and fix the build to work with our libs.

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-13
- reinstate updated manifest patch
- change define to global

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-12
- buildarch: noarch

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-11
- drop obsolete manifest patch

* Thu Mar 10 2011 Rüdiger Landmann <r.landmann@redhat.com> 1.0-10
- import 1.0 into Fedora, based on Mandriva package

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 4 2011 Rüdiger Landmann <r.landmann@redhat.com> - 1.0-8
- BR qdox

* Tue Jan 4 2011 Rüdiger Landmann <r.landmann@redhat.com> - 1.0-7
- set BR on xmlgraphics-commons >= 1.4
- Add qdox classpath

* Thu Dec 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-0.0.3mdv2011.0
- Revision: 617684
- Resubmit after moving

* Fri Dec 3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-6
- Add LICENSE to javadoc sub-package
- Few other tweaks according to new guidelines
- Make jars and javadoc versionless
- Add pom file (Resolves rhbz#655804)

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-5
- We need servlet not jsp.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-4
- BR jsp.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-3
- Add more BRs.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-2
- BR ant-nodeps.

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-1
- Update to 1.0.
- BR/R java 1.6.0 not openjdk (rhbz#620330).
- Remove jars in prep.

* Sat Sep 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.0.2mdv2011.0
- Revision: 576002
- rebuild for new xmlgraphics-commons

* Sun Aug 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.0.1mdv2011.0
- Revision: 574030
- update to new version 1.0
- disable patch 1
- disable gcj support

* Thu Apr 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.95-0.0.3mdv2010.1
- Revision: 540954
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.95-0.0.2mdv2010.0
- Revision: 437573
- rebuild

* Wed Dec 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.95-0.0.1mdv2009.1
- Revision: 315376
- update to new version 0.95
- drop patch0, not needed anymore
- spec file clean
- drop useles buildrequires
- use %%java_home

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0.94-0.2.1mdv2008.1
- Revision: 139372
- spec cleanup
- import fop


* Fri Dec  7 2007 Lillian Angel <langel at redhat.com> - 0.94-2
- Updated Release.

* Thu Dec  6 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Removed ppc/64 conditions since IcedTea is now available for ppc/64.

* Tue Nov 27 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Fixed to build with gcj on ppc/64.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0.94-1
- Fixed rpmlint errors.

* Tue Sep 18 2007 Joshua Sumali <jsumali at redhat.com> - 0:0.94-1
- Update to fop 0.94

* Thu Mar 30 2006 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-9jpp
- First build for JPP-1.7
- Replace avalon-framework, avalon-logkit with their new excalibur-*
  counterparts
- Drop non-free jimi and jai BRs

* Tue Oct 11 2005 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-8jpp
- Patch to Batik >= 1.5.1

* Fri Oct 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-7jpp
- Omit ant -d flag

* Mon Aug 23 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-6jpp
- Build with ant-1.6.2

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.20.5-5jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:0.20.5-4jpp
- Upgrade to Ant 1.6.X

* Thu Jan  8 2004 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-3jpp
- BuildRequires ant-optional.
- Crosslink with full J2SE javadocs instead of just JAXP/XML-commons.
- Add Main-Class back to manifest.

* Tue Sep 23 2003 Paul Nasrat <pauln at truemesh.com> - 0:0.20.5-2jpp
- Fix script and requires
- Remove class path in manifest
- New javadoc style

* Sat Jul 19 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-1jpp
- Update to 0.20.5.
- Crosslink with xml-commons-apis and batik javadocs.
- BuildRequires jai, jce and jimi.

* Sat Jun  7 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-0.rc3a.1jpp
- Update to 0.20.5rc3a.
- Include fop script.
- Non-versioned javadoc symlinks.

* Thu Apr 17 2003 Ville SkyttÃ¤ <ville.skytta at iki.fi> - 0:0.20.5-0.rc2.1jpp
- Update to 0.20.5rc2 and JPackage 1.5.

* Sun Mar 10 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.3-1jpp
- 0.20.3 final
- fixed missing symlink

* Mon Jan 21 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.3-0.rc.1jpp
- 0.20.3rc
- first unified release
- javadoc into javadoc package
- no dependencies for manual package
- s/jPackage/JPackage
- adaptation to new xalan-j2 package
- requires and buildrequires avalon-logkit

* Thu Aug 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 0.20.1-1mdk
- first release
