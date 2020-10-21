%define patched_resolver_ver 1.2
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}

Name:    netbeans-resolver
Version: 6.7.1
Release: 23%{?dist}
Summary: Resolver subproject of xml-commons patched for NetBeans

License: ASL 1.1
URL:     http://xml.apache.org/commons/

Source0: http://archive.apache.org/dist/xml/commons/%{patched_resolver}.tar.gz

# see http://hg.netbeans._org/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0: %{name}-%{version}-nb.patch
Patch1: %{name}-%{version}-resolver.patch
Patch2: javadoc-source-version.patch

BuildArch: noarch

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: dos2unix

Requires: jpackage-utils
Requires: java-headless

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with 
a patch for NetBeans.

%package javadoc
Summary:    Javadocs for %{name}
Requires:   jpackage-utils

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf apidocs

%patch0 -p1 -b .sav
%patch1 -p1 -b .sav
%patch2 -p1 -b .sav

dos2unix -k KEYS
dos2unix -k LICENSE.resolver.txt

%build
ant -f resolver.xml jar docs

%install
mkdir -p %{buildroot}%{_javadir}
cp -p build/resolver.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/apidocs/resolver %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc LICENSE.resolver.txt KEYS

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.resolver.txt

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 6.7.1-21
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.7.1-16
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Omair Majid <omajid@redhat.com> - 6.7.1-9
- Require java-headless

* Fri Nov 15 2013 Omair Majid <omajid@redhat.com> - 6.7.1-8
- Add javadoc subpackage
- Install jar as %%{name}.jar, without version suffix
- Update package to comply with latest java package guidelines

* Fri Oct 04 2013 Omair Majid <omajid@redhat.com> - 6.7.1-7
- Fix upstream Source URL.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 6.7.1-2
- Use upstream gzipped tarball instead of zip.

* Wed Aug 12 2009 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.7.1-1
- Patching for the NetBeans 6.7.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.1-5
- The description is formatted
- The license viersion is fixed

* Fri Aug 22 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.1-4
- The dos2unix package is added as the build requirements

* Fri Aug 22 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.1-3
- Redundant distribution tag is removed
- Redundant user-defined macros are removed
- java-devel is specified in BuildRequires insead of java-1.6.0-openjdk
- An epoch of 1 is included in the requirements for the Java versions
- The %%{buildroot} is used everywhere instead of $RPM_BUILD_ROOT
- The canonical RPM macros are used instead of the commands ant and rm
- The -k option is used for the dos2unix commands
- More correct source URL is used, i.e not a mirror

* Fri Aug 15 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.1-2
- Docummentaion is added
- Appropriate value of the Group Tag are chosen from the official list

* Fri Jun 06 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 6.1-1
- Initial version

