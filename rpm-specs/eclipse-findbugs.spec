%global pkg_date     20150306
%global pkg_git_rev  5afe4d1

Name:           eclipse-findbugs
Version:        3.0.1
Release:        20%{?dist}
Summary:        Eclipse plugin for FindBugs

License:        LGPLv2+
URL:            http://findbugs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/findbugs/edu.umd.cs.findbugs.plugin.eclipse_%{version}.%{pkg_date}-%{pkg_git_rev}-source.zip
Source1:        fragment.info

# This patch is Fedora-specific, so it has not been submitted upstream.  The
# patch makes the build infrastructure use installed JARs for the build, rather
# than downloading JARs.
Patch0:         eclipsePlugin-build.patch

BuildRequires:  ant, ant-findbugs, eclipse-pde, findbugs = %{version}
BuildRequires:  java-devel >= 1:1.6.0, javapackages-tools
BuildRequires:  dom4j
Requires:       ant, ant-findbugs, eclipse-jdt, findbugs = %{version}
Requires:       java >= 1:1.6.0, javapackages-tools
Requires:       dom4j

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

%global droplets_dir %{_datadir}/eclipse/droplets
%global droplet_dir %{droplets_dir}/findbugs
%global plugins_dir %{droplet_dir}/plugins
%global plugin_dir  %{plugins_dir}/edu.umd.cs.findbugs.plugin.eclipse_%{version}.%{pkg_date}-%{pkg_git_rev}

%description
An Eclipse plugin for the FindBugs Java bug detector.

%prep
%setup -q -c edu.umd.cs.findbugs.plugin.eclipse_%{version}.%{pkg_date}-%{pkg_git_rev}
%patch0 -p1

%build
# Eclipse is always in /usr/lib on all arches
ECLIPSE_BASE=/usr/lib/eclipse

# Set up the eclipse path
sed -i -e "s|@SWT_JAR@|${ECLIPSE_BASE}/swt.jar|" build.xml

ant -DeclipsePlugin.dir=${ECLIPSE_BASE}/plugins \
    -DeclipseJdtPlugin.dir=%{droplets_dir}/eclipse-jdt/plugins \
    -DeclipseSdkPlugin.dir=%{droplets_dir}/eclipse-pde/plugins \
    -Djavadir=%{_javadir} \
    -Dplugin.date=%{pkg_date} \
    -Drelease.base=%{version} \
    -Dfindbugs.git.revision=%{pkg_git_rev} \
    dist

%install
mkdir -p $RPM_BUILD_ROOT%{plugins_dir}
unzip -q -d $RPM_BUILD_ROOT%{plugins_dir} \
  zips/edu.umd.cs.findbugs.plugin.eclipse_%{version}.%{pkg_date}-%{pkg_git_rev}.zip

# Symlink to the external jars we need
mkdir $RPM_BUILD_ROOT%{plugin_dir}/lib
for i in findbugs jsr-305 findbugs-annotations findbugs-bcel dom4j jaxen \
  jFormatString apache-commons-lang objectweb-asm/asm-all; do
    ln -s ../../../../../../java/$i.jar $RPM_BUILD_ROOT%{plugin_dir}/lib
done

# Remove unnecessary files (used at build-time only)
rm -f $RPM_BUILD_ROOT%{plugin_dir}/.options
rm -fr $RPM_BUILD_ROOT%{plugin_dir}/doc

cp %{SOURCE1} $RPM_BUILD_ROOT%{droplet_dir}/

%files
%doc RELEASENOTES
%{droplet_dir}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Mat Booth <mat.booth@redhat.com> - 3.0.1-18
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Richard Fearn <richardfearn@gmail.com> - 3.0.1-16
- Fix installation of fragment.info, and lib symlinks (bug #1645854)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Richard Fearn <richardfearn@gmail.com> - 3.0.1-14
- Update to build with ASM 6.1.1

* Thu May 17 2018 Mat Booth <mat.booth@redhat.com> - 3.0.1-13
- Remove extra eclipse dir from install location and always find eclipse in
  /usr/lib

* Wed May 9 2018 Alexander Kurtakov <akurtako@redhat.com> 3.0.1-12
- Adjust for the removed extra eclipse dir in droplets.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> 3.0.1-10
- Remove unnecessary Group: tag

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Richard Fearn <richardfearn@gmail.com> 3.0.1-7
- Install plugin into droplets instead of dropins

* Wed Apr 27 2016 Alexander Kurtakov <akurtako@redhat.com> 3.0.1-6
- Update to packaging changes for Neon.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Richard Fearn <richardfearn@gmail.com> - 3.0.1-4
- Remove %%define from spec

* Wed Jul 01 2015 Richard Fearn <richardfearn@gmail.com> - 3.0.1-3
- Add dom4j dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Richard Fearn <richardfearn@gmail.com> - 3.0.1-1
- Update to 3.0.1 (bug #1199681)

* Mon Jul 07 2014 Richard Fearn <richardfearn@gmail.com> - 3.0.0-1
- Update to 3.0.0 (bug #1116843)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> 2.0.3-2
- Ensure build succeeds on 32-bit and 64-bit builders

* Sat Dec 28 2013 Richard Fearn <richardfearn@gmail.com> 2.0.3-1
- Update to 2.0.3

* Sun Dec 08 2013 Richard Fearn <richardfearn@gmail.com> 2.0.2-2
- Update following introduction of objectweb-asm3 package

* Sat Oct 26 2013 Richard Fearn <richardfearn@gmail.com> 2.0.2-1
- Update to 2.0.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Richard Fearn <richardfearn@gmail.com> 1.3.9-7
- Package should own /usr/share/eclipse/dropins/findbugs and
  /usr/share/eclipse/dropins/findbugs/plugins (#814964)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1.3.9-4
- Fix BR/R to handle openjdk 7.
- Remove not needed anymore elements like BuildRoot, clean section and etc.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 23 2009 Jerry James <loganjerry@gmail.com> - 1.3.9-2
- Remove explicit versions from the manifest to match the symlinks (bz 530512)

* Tue Aug 25 2009 Jerry James <loganjerry@gmail.com> - 1.3.9-1
- Update to 1.3.9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Jerry James <loganjerry@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Wed Mar 11 2009 Jerry James <loganjerry@gmail.com> - 1.3.7-4
- Require OpenJDK to compile due to use of Sun-specific classes.
- Require eclipse-jdt

* Fri Mar  6 2009 Jerry James <loganjerry@gmail.com> - 1.3.7-3
- Fix spec file problems discovered in review

* Tue Feb 10 2009 Jerry James <loganjerry@gmail.com> - 1.3.7-2
- Adapt to latest Eclipse plugin guidelines

* Fri Jan  2 2009 Jerry James <loganjerry@gmail.com> - 1.3.7-1
- Update to 1.3.7

* Wed Dec 10 2008 Jerry James <loganjerry@gmail.com> - 1.3.6-1
- Update to 1.3.6

* Thu Sep 25 2008 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- Initial RPM
