Name:           moconti
Version:        102609
Release:        18%{?dist}
Summary:        Web Application Server for Sleep

License:        LGPLv2
URL:            http://hick.org/~raffi/moconti.html
Source0:        http://www.polishmywriting.com/download/moconti102609.tgz
# Add javadoc target
Patch0:         moconti-javadoc.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  java-sleep

Requires:       jpackage-utils
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       java-headless
%else
Requires:       java
%endif
Requires:       java-sleep

%description
Moconti is a light-weight application server that lets you create web sites
using the Sleep Scripting Language. It supports multiple websites and is very
easy to setup.


%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .javadoc
find -name '*.jar' -delete
# Fix java source/target
sed -i -e 's/1.4/1.6/' build.xml
build-jar-repository -s -p lib sleep


%build
ant
ant javadoc


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p moconti.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%{_javadir}/*
%doc docs

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 102609-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 102609-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 02 2020 Orion Poplawski <orion@nwra.com> - 102609-16
- Bump java source/target to 1.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 102609-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 102609-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 102609-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 102609-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 102609-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 102609-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 102609-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 102609-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 102609-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 102609-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> - 102609-5
- Require java-headless (bug #1068420)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 102609-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 102609-3
- Fix java target/source to 1.5
- Add javadoc

* Wed Apr 17 2013 Orion Poplawski <orion@cora.nwra.com> - 102609-2
- Update URL
- BR/R java-sleep

* Wed Nov 2 2011 Orion Poplawski <orion@cora.nwra.com> - 102609-1
- Initial package
