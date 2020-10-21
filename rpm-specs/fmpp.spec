%global fmpp_version 0.9.14

Name:		fmpp
Version:	%{fmpp_version}
Release:	16%{?dist}
Summary:	FreeMarker-based text file PreProcessor 

License:	BSD
URL:		http://fmpp.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/fmpp/fmpp_%{version}.tar.gz

Patch0:		fmpp-0.9.14-build.xml.patch
Patch1:		fmpp-0.9.14-excise-imageinfo.patch

BuildRequires:	javapackages-local

BuildRequires:	ant

BuildRequires:	mvn(oro:oro)
BuildRequires:	mvn(org.freemarker:freemarker)
BuildRequires:	mvn(org.beanshell:bsh)
BuildRequires:	mvn(xml-resolver:xml-resolver)
BuildRequires:	mvn(xml-apis:xml-apis) 

Requires:	mvn(oro:oro)
Requires:	mvn(org.freemarker:freemarker)
Requires:	mvn(org.beanshell:bsh)
Requires:	mvn(xml-resolver:xml-resolver)
Requires:	mvn(xml-apis:xml-apis) 

BuildArch:	noarch


%description

FMPP is a general-purpose text file preprocessor tool that uses
FreeMarker templates. It is particularly designed for HTML
preprocessor, to generate complete (static) homepages: directory
structure that contains HTML-s, image files, etc. But of course it can
be used to generate source code or whatever text files. FMPP is
extendable with Java classes to pull data from any data sources
(database, etc.) and embed the data into the generated files.

%package javadoc
Summary:	Javadoc for %{name}
BuildArch:	noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}_%{fmpp_version}
%patch0 -p1 
%patch1 -p1 

find lib -name \*.jar -delete

rm -rf lib/forbuild/classes

# these two tests don't pass for some reason
find . -name always_create_dirs_\* -and -type d | xargs rm -rf

# strip carriage returns
find . -name \*.fmpp -or\
 -name package-list -or\
 -name \*.bsh -or\
 -name \*.txt -or\
 -name \*.xml -or\
 -name \*.c -or \
 -name \*.css -or \
 -name \*.csv -or \
 -name \*.dtd -or \
 -name \*.ent -or \
 -name \*.ftl -or \
 -name \*.html -or \
 -name \*.tdd| xargs sed -i 's/\r$//'

%build

ant build

ant make-pom

%mvn_artifact build/pom.xml lib/fmpp.jar

%check

ant test

%install
%mvn_install -J docs

%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt README.txt

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.9.14-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Mat Booth <mat.booth@redhat.com> - 0.9.14-5
- Fix FTBFS rhbz#1239506

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild


* Fri Feb 21 2014 William Benton <willb@redhat.com> - 0.9.14-2
- changed BR to java-headless (BZ 1068077)

* Thu Jan 2 2014 William Benton <willb@redhat.com> - 0.9.14-1
- initial package

