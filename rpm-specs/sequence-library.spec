Name:           sequence-library
Version:        1.0.3
Release:        5%{?dist}
Summary:        Textual diff and merge library

License:        Sequence     
URL:            http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/

# Tarball generated with:
#  svn export http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/tags/1.0.3/ sequence-library-1.0.3 && \
#      tar caf sequence-library-1.0.3.tar.gz sequence-library-1.0.3/
Source0:        %{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/de/regnis/q/sequence/sequence-library/%{version}/sequence-library-%{version}.pom
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)

%description
A textual diff and merge library.

%package javadoc
Summary: Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.jar' -o -name '*.class' -delete

cp -pr %{SOURCE1} pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Mat Booth <mat.booth@redhat.com> - 1.0.3-1
- Update to latest release
- Modernise spec file
- Fix failure to build from source

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Ismael Olea <ismael@olea.org> - 1.0.2-7
- fixing #1107293

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.2-5
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 9 2012 Ismael Olea <ismael@olea.org> - 1.0.2-2
- review changes: https://bugzilla.redhat.com/show_bug.cgi?id=873738#c7

* Thu Nov 8 2012 Ismael Olea <ismael@olea.org> - 1.0.2-1
- review changes: https://bugzilla.redhat.com/show_bug.cgi?id=873738#c2
- review changes: https://bugzilla.redhat.com/show_bug.cgi?id=873738#c3

* Tue Oct 9 2012 Ismael Olea <ismael@olea.org> - 1.0.2.20121003svn-2
- spec tuning

* Wed Oct 3 2012 Ismael Olea <ismael@olea.org> - 1.0.2.20121003svn-1
- first package
