Name:		sump-analyzer
Version:	0.8
Release:	5%{?dist}
Summary:	SUMP Logic Analyzer Client

License:	GPLv2+
URL:		https://www.sump.org/projects/analyzer/client/
Source0:	https://www.sump.org/projects/analyzer/downloads/la-src-%{version}.tar.bz2

BuildRequires:	java-devel
BuildRequires:	javapackages-tools
BuildRequires:	rxtx
Requires:	javapackages-filesystem
Requires:	java >= 1:1.8
Requires:	rxtx
BuildArch:	noarch

%description
The client application for SUMP Logic Analyzer. It allows to configure the
device, read and display captured data and to perform file operations on
captured data.


%prep
%setup -q -n LogicAnalyzer


%build
cd client

javac -classpath $(build-classpath RXTXcomm) \
	-encoding UTF-8 -source 1.7 -target 1.8 \
	org/sump/analyzer/*.java \
	org/sump/analyzer/tools/*.java \
	org/sump/util/*.java

jar cf org.sump.analyzer-%{version}.jar \
	org/sump/analyzer/*.class \
	org/sump/analyzer/tools/*.class \
	org/sump/analyzer/icons/*.png \
	org/sump/util/*.class


%install
mkdir -p %{buildroot}%{_javadir}
install -pm644 client/org.sump.analyzer-%{version}.jar \
	%{buildroot}%{_javadir}/org.sump.analyzer-%{version}.jar
%jpackage_script org.sump.analyzer.Loader "" "" RXTXcomm:org.sump.analyzer-%{version}.jar sump-analyzer true


%files
%{_bindir}/sump-analyzer
%{_javadir}/org.sump.analyzer-%{version}.jar
%doc client/doc/*
%license client/license.txt


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.8-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.8-2
- Add rxtx dependency

* Fri Aug 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.8-1
- Initial packaging
