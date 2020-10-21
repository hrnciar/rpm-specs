%global  git_commit d0ec879
%global  cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           bytelist
Version:        1.0.8
Release:        22%{?dist}
Summary:        A java library for lists of bytes

License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

Patch0:         00-set-javac-1.8-source-target.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  jcodings
BuildRequires:  jpackage-utils
BuildRequires:  javapackages-local
BuildRequires:  junit

Requires:       java-headless
Requires:       jcodings
Requires:       jpackage-utils


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
%patch0 -p1

find -name '*.class' -delete
find -name '*.jar' -delete


%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
mkdir -p lib
%ant


%install
mkdir -p %{buildroot}%{_javadir}

cp -p lib/%{name}-1.0.2.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%check
export CLASSPATH=$(build-classpath junit jcodings)
%ant test

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml
%doc README.txt

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.8-21
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.8-20
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Troy Dawson <tdawson@redhat.com> - 1.0.8-14
- As of F27, pom_* macros are now located in javapackages-local.
  Added BuildRequires javapackages-local to provide needed POM editor macros.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 27 2014 Mo Morsi <mmorsi@redhat.com> - 1.0.8-9
- Updates to fix build against rawhide

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.8-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.0.8-4
- add maven pom
- adapt to current guideline

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.8-1
- Bumped version to latest upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 25 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.0.5-1
- Bumped version to latest upstream release

* Tue Feb 09 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.3-2
- Fix the clean up code in the prep section
- Fix typo
- Save changelog

* Thu Jan 28 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.3-1
- 1.0.3
- Remove gcj bits
- New URL
- Use macros in all sections of the spec
- Add README.txt generated on the fly

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.svn9177
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.1-0.1.svn9177
- Bump to SVN HEAD.

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Bump to 1.0 release.

* Tue Apr 22 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-0.2.svn6558
- Do not include version in jar filename.
- Run tests in check section.

* Tue Apr 22 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-0.1.svn6558
- Initial RPM.
