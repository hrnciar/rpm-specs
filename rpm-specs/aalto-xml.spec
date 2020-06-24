Name:          aalto-xml
Version:       1.2.2
Release:       2%{?dist}
Summary:       Ultra-high performance non-blocking XML processor (Stax/Stax2, SAX/SAX2)
# Source files without license headers https://github.com/FasterXML/aalto-xml/issues/38
# See https://github.com/FasterXML/jackson-modules-base/issues/18, from main developer:
# "To whoever it concerns: policy of the Jackson project is to only include licensing information as project
# level metadata (in repo, pom.xml, artifact within source and binary jars), and not as headers in source files.
# Licensing is Apache License 2.0, for Jackson 2.x as indicated by various artifacts, and we have no plans to change this."
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/AaltoHome
Source0:       https://github.com/FasterXML/aalto-xml/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)

BuildArch:     noarch

%description
The Aalto XML processor is a StAX XML processor implementation. It
is not directly related to other existing mature implementations
(such as Woodstox or Sun Java Streaming XML Parser), although it
did come about as a prototype for evaluating implementation strategies
that differ from those traditionally used for Java-based parsers.

Two main goals (above and beyond stock StAX/SAX API implementation) are:

° Ultra-high performance parsing by making the Common Case Fast
  (similar to original RISC manifesto). This may mean limiting
  functionality, but never compromising correctness. XML 1.0
  compliance is not sacrificed for speed.

° Allowing non-block, asynchronous parsing: it should be possible to
  "feed" more input and incrementally get more XML events out, without
  forcing the current thread to block on I/O read operation.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
# Cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
sed -i 's/\r//' release-notes/asl/*
mv release-notes/asl/ASL2.0 LICENSE
mv release-notes/asl/LICENSE NOTICE

%mvn_file : %{name}

# Java 9 module support isn't needed
%pom_remove_plugin :moditect-maven-plugin

%build
%mvn_build -f --xmvn-javadoc

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-1
- Update to version 1.2.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Troy Dawson <tdawson@redhat.com> - 1.0.0-4
- Cleanup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 gil cattaneo <puntogil@libero.it> 1.0.0-1
- Update to 1.0.0

* Tue Jun 14 2016 gil cattaneo <puntogil@libero.it> 0.9.11-1
- initial rpm
