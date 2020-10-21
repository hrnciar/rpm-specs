Name:       saxpath
Version:    1.0
Release:    22%{?dist}
Summary:    Simple API for XPath
License:    Saxpath
URL:        http://sourceforge.net/projects/saxpath/
Source0:    http://downloads.sourceforge.net/saxpath/saxpath-1.0.tar.gz
Source1:    %{name}-%{version}.pom
Source2:    LICENSE
BuildArch:  noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
Requires:       jpackage-utils

%description
The SAXPath project is a Simple API for XPath. SAXPath is analogous to SAX
in that the API abstracts away the details of parsing and provides a simple
event based callback interface.

%package javadoc
Summary:    API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{version}-FCS

find -name \*.jar -delete

cp %{SOURCE2} .

%build
mkdir src/conf
touch src/conf/MANIFEST.MF

ant

# fix rpmlint warings: saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding /usr/share/javadoc/saxpath/**/*.css
for file in `find build/doc -type f | grep .css`; do
    sed -i 's/\r//g' $file
done

%install
install -d -m 755 %{buildroot}/%{_javadir}
install -d -m 755 %{buildroot}/%{_mavenpomdir}
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}

install -p -m 644 build/%{name}.jar %{buildroot}/%{_javadir}/
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
cp -a build/doc/* %{buildroot}/%{_javadocdir}/%{name}/

%check
ant test

%files -f .mfiles
%doc LICENSE

%files javadoc
%doc LICENSE
%{_javadocdir}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-21
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-13
- Add missing BR on javapackages-local
- Resolves: rhbz#1406919

* Wed Dec 21 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0-12
- Add missing BuildRequires to fix FTBFS (BZ#1406919).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-7
- Add separate LICENSE text to rpms

* Tue Jul 23 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-6
- Enable testsuite

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-5.10
- Update to current packaging guidelines

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-5.9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-5.8
- Don't own /usr/share/maven-fragments
- Resolves: rhbz#850001

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 10 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0-1.7
- Added missing Requires: jpackage-utils (%%{_javadir} and %%{_javadocdir})

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0-1.6
- Fix GROUPS.
- Wrap changelog.

* Mon Jun 8 2009 Yong Yang <yyang@redhat.com> 1.0-1.5
- Fix "saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding
  /usr/share/javadoc/saxpath/**/*.css"
- Fix "saxpath.src: W: mixed-use-of-spaces-and-tabs
  (spaces: line 1, tab: line 6)"

* Wed May 13 2009 Fernando Nasser <fnasser@redhat.com> 1.0-1.4
- Fix license

* Tue Mar 10 2009 Yong Yang <yyang@redhat.com> 1.0-1.3
- rebuild with maven2 2.0.8 built in bootstrap mode

* Tue Jan 06 2009 Yong Yang <yyang@redhat.com> 1.0-1.2
- Import from dbhole's maven 2.0.8 packages

* Wed Dec 03 2008 Deepak Bhole <dbhole@redhat.com> 1.0-1.1
- Initial build.
