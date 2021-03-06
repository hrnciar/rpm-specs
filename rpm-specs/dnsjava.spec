# Test of properly function library need DNS querys. It work perfectly on my machine and pass all tests.
# But internet access is not allowed from mock chroot. So, I need disable it by default. Yo may enable it if you want.
%global do_not_test 1

Name:          dnsjava
Version:       2.1.3
Release:       21%{?dist}
Summary:       Java DNS implementation
License:       BSD and MIT
URL:           http://www.dnsjava.org/
Source0:       http://www.dnsjava.org/download/%{name}-%{version}.tar.gz
Source1:       %{name}-%{version}.pom
# bz#842582
Patch0:        dnsjava-2.0.6-java1.5.target.patch

BuildRequires: ant
BuildRequires: aqute-bnd
# see https://fedorahosted.org/released/javapackages/doc/#_add_maven_depmap_macro_2
BuildRequires: javapackages-local
# For tests
BuildRequires: ant-junit
BuildArch:     noarch

%description
dnsjava is an implementation of DNS in Java. It supports all of the common
record types and the DNSSEC types. It can be used for queries, zone transfers,
and dynamic updates. It includes a cache which can be used by clients, and a
minimal implementation of a server. It supports TSIG authenticated messages,
partial DNSSEC verification, and EDNS0.

dnsjava provides functionality above and beyond that of the InetAddress class.
Since it is written in pure Java, dnsjava is fully threadable, and in many
cases is faster than using InetAddress.

dnsjava provides both high and low level access to DNS. The high level
functions perform queries for records of a given name, type, and class, and
return an array of records. There is also a clone of InetAddress, which is
even simpler. A cache is used to reduce the number of DNS queries sent. The
low level functions allow direct manipulation of dns messages and records, as
well as allowing additional resolver properties to be set.

A 'dig' clone and a dynamic update program are included, as well as a
primary-only server.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
rm -rf doc/
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%patch0 -p0 -b .java1.5

iconv -f iso8859-1 -t utf8 Changelog > Changelog.tmp
touch -r Changelog Changelog.tmp
mv -f Changelog.tmp Changelog
# install in _javadir
%mvn_file %{name}:%{name} %{name}

%build

export CLASSPATH=%(build-classpath jce aqute-bnd)
ant -Dj2se.javadoc=%{_javadocdir}/java clean docsclean bundle docs

%mvn_artifact %{SOURCE1} org.xbill.dns_%{version}.jar

%install
%mvn_install -J doc

%if ! 0%{?do_not_test}
%check
export CLASSPATH='%(build-classpath junit):%{name}-%{version}.jar'
ant -Dj2se.javadoc=%{_javadocdir}/java compile_tests
ant -Dj2se.javadoc=%{_javadocdir}/java run_tests
%endif

%files -f .mfiles
%license LICENSE
%doc Changelog README USAGE examples.html *.java

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.1.3-19
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Mat Booth <mat.booth@redhat.com> - 2.1.3-11
- Build with OSGi metadata
- Include license
- Disable java 8 doclinting

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 gil cattaneo <puntogil@libero.it> - 2.1.3-8
- FTBFS in rawhide rhbz#1106150
- Adapt to current guideline:
        o Remove Javadoc scriptlets (no more required)
        o Remove Requires (automatically generated by xmvn)
        o Remove BuildRequires: jpackage-utils (provided by javapackages package)
        o Remove Group (no more required)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 3 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 2.1.3-6
- Switch to java-headless. Bz#1068028.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 1 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 2.1.3-3
- For changes and patch thanks to Gil Cattaneo <puntogil@libero.it>
- Added maven pom
- Fixes according to new guidelines (versionless jars, javadocs)

* Sun Aug 12 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 2.1.3-2
- Update to 2.1.3.
- Add Patch0: dnsjava-2.0.6-java1.5.target.patch to compile with 1.5 java target (bz#842582).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-6
- Fix test condition logick for %%check

* Wed Apr 15 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-5
- Continue review.
- As it can't be build by gcj, delete back this stuff from spec.
- Tests made now by conditional. As internet access is not allowed in default mock chroot, it is disabled now.
- Changelog recoded form iso8859-1 (charset is guessed by Orcan 'oget' Ogetbil)

* Wed Apr 15 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-4
- Continue review.
- Delete explicit installation in %%install *.java files.
- License from BSD changed to "BSD and MIT"
- Delete unneeded BR: jce, java-javadoc
- Fix mistake: Add Requires: jpackage-utils and delete listed twice BuildRequires: jpackage-utils
- BR: java-devel >= 1.7, R: java >= 1.7

* Tue Apr 14 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-3
- Review in progress. Thanks to Orcan 'oget' Ogetbil.
- Add *.java examplees into documentation (it is mentioned in USAGE)
- Add testing:
	o Add BuildRequires: ant-junit
	o Add %%check section.
- Group from "Development/Libraries" changed to "System Environment/Libraries" by Orcan 'oget' Ogetbil suggestion.
- rm -rf doc/ in %%prep section.
- Removee listed twice Requires: jpackage-utils

* Mon Apr 13 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-2
- Issues from review:
	o Add
		. BuildRequires:	java-devel
		. BuildRequires:	jpackage-utils
		. Requires:		java >= specific_version
		. Requires:		jpackage-utils
	o Delete "%%define section free"
	o "%%defattr(0644,root,root,0755)" replaced by "%%defattr(-,root,root,-)" in both packages.
	o Add gcj-related stuff.
	o Remove Javadoc scriptlets

* Sun Apr 12 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.0.6-1
- Import src.rpm from JPackage - http://ftp.heanet.ie/pub/jpackage/1.6/generic/free/SRPMS/dnsjava-1.5.1-2jpp.src.rpm
- Step to last version 2.0.6
- Reformat spec with tabs.
- In Source0 tag inject %%{name} and %%{version} macroses.
- $RPM_BUILD_ROOT replaced by %%{buildroot}
- Delete (comment out) tags:
	o Epoch:		0
	o Vendor:		JPackage Project
	o Distribution:	JPackage
- Add %%{?dist} into relese instead of "jpp"
- Introduced by rpmlint:
	o Group Development/Libraries/Java changed to simple Development/Libraries
	o Licence changed to BSD
	o javadoc ackage group changed form Development/Documentation to simple Documentation

* Fri Aug 20 2004 Ralph Apel <r.ape at r-apel.de> 0:1.5.1-2jpp
- Build with ant-1.6.2

* Thu Jan 22 2004 David Walluck <david@anti-microsoft.org> 0:1.5.1-1jpp
- 1.5.1
- remove crosslink patch (merged upstream)

* Fri Oct 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4.3-1jpp
- Update to 1.4.3.
- Crosslink with local J2SE javadocs.
- Spec cleanups, save in UTF-8.

* Tue May 06 2003 David Walluck <david@anti-microsoft.org> 0:1.3.2-2jpp
- update for JPackage 1.5

* Wed Mar 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.3.2-1jpp
- Update to 1.3.2.
- Use ant instead of make for building.
- Drop patches, and include DNSSEC/JCE code.
- Use sed instead of bash 2 extension when symlinking jars during build.

* Sat May 11 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2.4-1jpp
- updated by Ville Skyttä <ville.skytta@iki.fi>
 - Updated to 1.2.4.
 - Fixed Vendor, Distribution and Group tags.
 - Updated description.
 - Versioned javadocs.
 - Added -no-debug and -no-jce patches.
 - Doesn't BuildRequire ant.

* Fri Dec 7 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2.3-2jpp
- javadoc into javadoc package

* Fri Nov 2 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2.3-1jpp
- first JPackage release
