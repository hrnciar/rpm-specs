%global plugin_dir %{_datadir}/findbugs/plugin
%global eclipse_plugin_vers 3.0.1
%global eclipse_plugin_date 20150306
%global eclipse_plugin_rev  5afe4d1
%global eclipse_plugins_dir %{_datadir}/eclipse/droplets/findbugs/plugins
%global eclipse_plugin_dir  %{eclipse_plugins_dir}/edu.umd.cs.findbugs.plugin.eclipse_%{eclipse_plugin_vers}.%{eclipse_plugin_date}-%{eclipse_plugin_rev}

Name:           findbugs-contrib
Version:        7.4.7
Release:        3%{?dist}
Summary:        Extra findbugs detectors

License:        LGPLv2+
URL:            http://fb-contrib.sourceforge.net/
Source0:        http://repo1.maven.org/maven2/com/mebigfatguy/fb-contrib/fb-contrib/%{version}/fb-contrib-%{version}-sources.jar

# This patch has not been submitted upstream, as it contains Fedora-specific
# changes.  It looks in /usr/share/java for jar files at both compile time and
# run time, instead of using the jars in lib/.
Patch0:         findbugs-contrib-build.patch

# Add flags for skipping compilation of test/sample code
Patch1:         findbugs-contrib-add-no-compile-options.patch

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64-bit architectures
ExcludeArch:    s390 %{arm} %{ix86}

BuildRequires:  ant, findbugs, java-devel >= 1:1.6.0, jpackage-utils

Requires:       findbugs, java >= 1:1.6.0, jpackage-utils

%description
This is an extra detector plugin to be used with the static bug finder
FindBugs.  See the documentation for descriptions of the detectors.

%package javadoc
Summary:        Javadoc documentation for %{name}

%description javadoc
Javadoc documentation for %{name}.

%package samples
Summary:        Sample input files illustrating the detectors
Requires:       %{name} = %{version}-%{release}

%description samples
This package contains sample input files that illustrate the various findbugs
detectors.

%package -n eclipse-findbugs-contrib
Summary:        Eclipse plugin for findbugs-contrib
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-findbugs = %{eclipse_plugin_vers}

%description -n eclipse-findbugs-contrib
This package integrates the findbugs-contrib detectors into Eclipse, in
addition to the base findbugs detectors.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
ant build   -Dno.yank=1 -Dno.compile_test=1 -Dno.compile_samples=1 -Dno.test=1
ant javadoc -Dno.yank=1

%install
# Install the plugin
mkdir -p $RPM_BUILD_ROOT%{plugin_dir}
cp -p target/fb-contrib-%{version}.jar $RPM_BUILD_ROOT%{plugin_dir}

# Install the documentation
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/fb-contrib
cp -a target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/fb-contrib

# Make a soft link for eclipse
mkdir -p $RPM_BUILD_ROOT%{eclipse_plugin_dir}/plugin
ln -s %{plugin_dir}/fb-contrib-%{version}.jar \
  $RPM_BUILD_ROOT%{eclipse_plugin_dir}/plugin/fb-contrib-%{version}.jar

%pretrans javadoc -p <lua>
path = "%{_javadocdir}/fb-contrib"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files
%license license.txt
%{plugin_dir}/fb-contrib-%{version}.jar

%files javadoc
%{_javadocdir}/*

%files samples
%doc src/samples/java/*

%files -n eclipse-findbugs-contrib
%{eclipse_plugin_dir}/plugin/fb-contrib-%{version}.jar

%changelog
* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 7.4.7-3
- Use %%license

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Richard Fearn <richardfearn@gmail.com> - 7.4.7-1
- Update to 7.4.7 (bug #1763541)

* Sun Sep 08 2019 Richard Fearn <richardfearn@gmail.com> - 7.4.6-4
- Do not compile test/sample code, to fix FTBFS (bug #1735211)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Richard Fearn <richardfearn@gmail.com> - 7.4.6-2
- Restrict build to architectures that support Eclipse

* Mon Jun 24 2019 Richard Fearn <richardfearn@gmail.com> - 7.4.6-1
- Update to 7.4.6 (bug #1720937)

* Sun May 05 2019 Richard Fearn <richardfearn@gmail.com> - 7.4.5-1
- Update to 7.4.5 (bug #1706470)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.3-3
- Drop OPM_Sample patch (Mockito has been updated)

* Fri Nov 02 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.3-2
- Fix Eclipse plugin directory (bug #1644935)

* Mon Jul 23 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.3-1
- Update to 7.4.3 (bug #1607098)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.2-1
- Update to 7.4.2 (bug #1580171)

* Sat Jun 02 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.1-1
- Update to 7.4.1 (bug #1580171)

* Sun May 13 2018 Richard Fearn <richardfearn@gmail.com> - 7.4.0-1
- Update to 7.4.0 (bug #1577489)

* Fri May 4 2018 Alexander Kurtakov <akurtako@redhat.com> 7.2.1-3
- Adjust for servlet 4.

* Sat Apr 28 2018 Richard Fearn <richardfearn@gmail.com> - 7.2.1-2
- Update to build with ASM 6.1.1

* Sat Mar 10 2018 Richard Fearn <richardfearn@gmail.com> - 7.2.1-1
- Update to 7.2.1 (bug #1529276)

* Sun Mar 04 2018 Richard Fearn <richardfearn@gmail.com> - 7.2.0-1
- Update to 7.2.0 (bug #1529276)

* Tue Feb 13 2018 Richard Fearn <richardfearn@gmail.com> - 7.0.5-3
- Fix build after guava.jar moved down into guava subdirectory

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.5-1
- Update to 7.0.5 (bug #1488265)

* Tue Oct 10 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.4-1
- Update to 7.0.4

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.3-2
- Remove unnecessary Group: tags

* Fri Jul 28 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.3-1
- Update to 7.0.3 (bug #1473048)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.2-1
- Update to 7.0.2 (bug #1456618)

* Fri May 05 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.1-1
- Update to 7.0.1 (bug #1442499)

* Fri May 05 2017 Richard Fearn <richardfearn@gmail.com> - 7.0.0-1
- Update to 7.0.0 (bug #1442499)

* Tue Mar 28 2017 Richard Fearn <richardfearn@gmail.com> - 6.8.4-1
- Update to 6.8.4 (bug #1431470)

* Sun Mar 12 2017 Richard Fearn <richardfearn@gmail.com> - 6.8.3-1
- Update to 6.8.3 (bug #1421516)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Richard Fearn <richardfearn@gmail.com> - 6.8.2-1
- Update to 6.8.2 (bug #1398044)

* Sat Nov 19 2016 Richard Fearn <richardfearn@gmail.com> - 6.8.1-1
- Update to 6.8.1 (bug #1396311)

* Sat Oct 15 2016 Richard Fearn <richardfearn@gmail.com> - 6.8.0-1
- Update to 6.8.0 (bug #1383534)

* Thu Sep 29 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.3-2
- Don't validate pmd-rules.xml during build, as this can't be done offline

* Thu Sep 29 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.3-1
- Update to 6.6.3 (bug #1379056)

* Sat Aug 27 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.2-1
- Update to 6.6.2 (bug #1370690)

* Thu Jul 14 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.1-2
- Update to reflect FindBugs plugin being installed in droplets instead of dropins

* Sun May 01 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.1-1
- Update to 6.6.1 (bug #1328962)

* Tue Mar 01 2016 Richard Fearn <richardfearn@gmail.com> - 6.6.0-1
- Update to 6.6.0 (bug #1301782)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Richard Fearn <richardfearn@gmail.com> - 6.4.3-1
- Update to 6.4.3 (bug #1291027)
- Drop findbugs-contrib-encoding.patch as the problem has been fixed upstream
  (see upstream commits 5771866 and dcb015d)

* Sun Nov 29 2015 Richard Fearn <richardfearn@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Sun Nov 01 2015 Richard Fearn <richardfearn@gmail.com> - 6.2.3-2
- Force use of Tomcat (not Glassfish) Servlet/JSP API JARs

* Tue Aug 25 2015 Richard Fearn <richardfearn@gmail.com> - 6.2.3-1
- Update to 6.2.3
- Put sample classes into JAR file
- findbugs-contrib-javadoc no longer depends on findbugs-contrib

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Richard Fearn <richardfearn@gmail.com> - 6.0.0-3
- Update to build against FindBugs 3.0.1

* Wed Mar 4 2015 Alexander Kurtakov <akurtako@redhat.com> 6.0.0-2
- Bump to jsp 2.3 and servlet 3.1.

* Fri Jan 09 2015 Richard Fearn <richardfearn@gmail.com> - 6.0.0-1
- Update to 6.0.0
- Add extra dependencies to -samples package

* Thu Jan 08 2015 Richard Fearn <richardfearn@gmail.com> - 5.2.1-4
- Install Javadoc into unversioned directory (bug #1068945)

* Mon Jul 07 2014 Richard Fearn <richardfearn@gmail.com> - 5.2.1-3
- Update to build against FindBugs 3.0.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Richard Fearn <richardfearn@gmail.com> - 5.2.1-1
- Update to 5.2.1

* Fri May 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.2.0-2
- Fix requires on junit

* Mon May 05 2014 Richard Fearn <richardfearn@gmail.com> - 5.2.0-1
- Update to 5.2.0

* Mon Dec 30 2013 Richard Fearn <richardfearn@gmail.com> - 4.6.1-6
- Rebuild against eclipse-findbugs 2.0.3

* Sat Oct 26 2013 Richard Fearn <richardfearn@gmail.com> - 4.6.1-5
- Rebuild against eclipse-findbugs 2.0.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Richard Fearn <richardfearn@gmail.com> - 4.6.1-2
- Fix location of symlink added to FindBugs Eclipse plugin

* Tue Aug 14 2012 Richard Fearn <richardfearn@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Tue Aug 14 2012 Richard Fearn <richardfearn@gmail.com> - 4.2.0-8
- Include asm-tree.jar in compilation classpath

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Richard Fearn <richardfearn@gmail.com> - 4.2.0-6
- Update to Tomcat 7: depend on servlet3 & jsp22

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Alexander Kurtakov <akurtako@redhat.com> 4.2.0-4
- Adapt for building/running with openjdk 7.
- Remove not needed parts.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Richard Fearn <richardfearn@gmail.com> - 4.2.0-2
- rhbz#652019 - migrate from Tomcat 5 to Tomcat 6

* Mon Jan 18 2010 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Mon Oct  5 2009 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Wed Aug 26 2009 Jerry James <loganjerry@gmail.com> - 3.8.1-4
- Rebuilt for findbugs 1.3.9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Jerry James <loganjerry@gmail.com> - 3.8.1-2
- Add eclipse-findbugs-contrib package as suggested by Alexander Kurtakov

* Tue Apr  7 2009 Jerry James <loganjerry@gmail.com> - 3.8.1-1
- Initial RPM
