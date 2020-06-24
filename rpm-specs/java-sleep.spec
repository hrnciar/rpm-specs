Name:		java-sleep
Version:	2.1
Release:	19%{?dist}
Summary:	Multi-paradigm scripting language for Java

License:	LGPLv2+ and BSD
URL:		http://sleep.dashnine.org/
Source0:	http://sleep.dashnine.org/download/sleep21-bsd.zip
# Patch to allow bootstrapping sleep.jar without sleep-engine.jar
Patch0:		sleep-bootstrap.patch
# Bump target version to 1.6 for JDF 11 support
Patch1:         sleep-target.patch
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	java-devel
BuildRequires:	ant-contrib
Requires:	jpackage-utils
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:	java-headless
%else
Requires:	java
%endif

%description
Sleep ...

 - is a multi-paradigm scripting language for the Java Platform
 - easy to learn with Perl and Objective-C inspired syntax
 - executes scripts fast with a small package size (~250KB)
 - excels at data manipulation, component integration, and distributed
   communication
 - seamlessly uses Java objects and 3rd party libraries


%package javadoc
Summary:	Javadocs for %{name}
Requires:	jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n sleep-master
%patch0 -p1 -b .bootstrap
find -name \*.jar -delete
sed -i -e 's/\r//' *.txt
# Fix FSF address
sed -i -e 's/59 Temple Place, Suite 330/51 Franklin Street, Fifth Floor/' \
       -e 's/MA  02111-1307/MA  02110-1301/' license.txt


%build
# Build without sleep-engine components
ant -Dbootstrap=true
# Build sleep-engine.jar
ant -f jsr223/build.xml
# Build in the sleep-engine components
ant
# Build the test data jars
ant -f tests/data/build.xml
ant -f tests/data2/build.xml
ant -f tests/data3/build.xml
# Build docs
ant docs


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p sleep.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/sleep.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
mv docs/api docs_api
cp -rp docs_api $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api


%check
java -jar sleep.jar runtests.sl


%files
%doc *.txt docs
%{_javadir}/%{name}.jar
%{_javadir}/sleep.jar


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Fri May 01 2020 Orion Poplawski <orion@nwra.com> - 2.1-19
- Update to 2.1 update 5 tarball

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> 2.1-8
- Require java-headless (bug #1068190)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Orion Poplawski <orion@cora.nwra.com> 2.1-6
- Fully fix FSF address
- Remove javadoc api from main package docs

* Mon Apr 15 2013 Orion Poplawski <orion@cora.nwra.com> 2.1-5
- Rename to java-sleep

* Thu Apr 11 2013 Orion Poplawski <orion@cora.nwra.com> 2.1-4
- No buildroot cleanup in %%install
- Fix FSF address

* Wed Mar 14 2012 Orion Poplawski <orion@cora.nwra.com> 2.1-3
- Updated license source

* Wed Nov 23 2011 Orion Poplawski <orion@cora.nwra.com> 2.1-2
- Drop BuildRoot, clean, defattr
- Add BR/R on jpackage-utils
- Build docs

* Wed Nov 2 2011 Orion Poplawski <orion@cora.nwra.com> 2.1-1
- Initial package
