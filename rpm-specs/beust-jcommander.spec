Name:           beust-jcommander
Version:        1.78
Release:        2%{?dist}
Summary:        Java framework for parsing command line parameters
License:        ASL 2.0
URL:            http://jcommander.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Adapted from earlier version that still shipped poms. It uses kobalt for building now
Source1:        %{name}.pom
# Cleaned up bundled jars whose licensing cannot be easily verified
Source2:        generate-tarball.sh

Patch0:         0001-ParseValues-NullPointerException-patch.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the %{summary}.

%prep
%setup -q
%patch0 -p1

chmod -x license.txt
cp -p %SOURCE1 pom.xml
sed -i 's/@VERSION@/%{version}/g' pom.xml

%build
%mvn_file : %{name}
%mvn_build -f --xmvn-javadoc

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Tue Jun 09 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-3
- skipped tests as they require user input with jdk11, changed way of javadoc generation

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.78-1
- Update to version 1.78.
- Remove unnecessary parent from POM file.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Michael Simacek <msimacek@redhat.com> - 1.71-5
- Repack the tarball without binaries

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Roman Vais <rvais@redhat.com> - 1.71-1
- Update to upstream version 1.71
- Add patch for issue https://github.com/cbeust/jcommander/issues/367

* Fri Mar 10 2017 Roman Vais <rvais@redhat.com> - 1.66-1
- Update to upstream version 1.66

* Fri Feb 17 2017 Roman Vais <rvais@redhat.com> - 1.65-1
- Update to upstream version 1.65

* Thu Jan 26 2017 Roman Vais <rvais@redhat.com> - 1.62-1
- Update to upstream version 1.62

* Wed Dec 14 2016 Michael Simacek <msimacek@redhat.com> - 1.60-1
- Update to upstream version 1.60

* Tue Nov 01 2016 Roman Vais <rvais@redhat.com> - 1.58-1
- Update to upstream version 1.58

* Fri Sep 30 2016 Roman Vais <rvais@redhat.com> - 1.57-1
- Update to upstream version 1.57
- Correct directory setup in prep section
- Change of tarball name in source url to correspond to upstream

* Tue Sep 27 2016 Roman Vais <rvais@redhat.com> - 1.56-1
- New version release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Michael Simacek <msimacek@redhat.com> - 1.47-1
- Update to upstream version 1.47
- Enable tests

* Mon Oct 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.45-1
- Update to upstream version 1.45

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.35-1
- Update to upstream version 1.35

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.30-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-2
- Replace BR: xmvn with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-1
- Update to upstream version 1.30
- Build with xmvn

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.17-6
- Install NOTICE files

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.17-3
- Use the new maven macro.

* Mon May 16 2011 Jaromir Capik <jcapik@redhat.com> - 1.17-2
- Unwanted comment removal
- Target javadoc:jar replaced with javadoc:aggregate

* Fri May 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.17-1
- Initial version of the package

