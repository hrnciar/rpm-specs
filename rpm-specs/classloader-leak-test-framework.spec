%bcond_without tests

Name:		classloader-leak-test-framework
Version:	1.1.1
Release:	11%{?dist}
Summary:	Detection and verification of Java ClassLoader leaks
License:	ASL 2.0
URL:		https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:	https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.bcel:bcel)
%if %{with tests}
BuildRequires: mvn(javax.el:el-api)
%endif

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{name}-%{version}

rm -r classloader-leak-prevention
cp -r %{name}/* .

%pom_remove_dep com.sun.faces:jsf-api
%pom_remove_dep com.sun.faces:jsf-impl

%build
%if %{with tests}
%mvn_build --xmvn-javadoc
%else
%mvn_build -f --xmvn-javadoc
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri May 15 2020 Ondrej Dubaj <odubaj@redhat.com> - 1.1.1-11
- fixed javadoc build problem

* Thu May 14 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.1-10
- removed javadoc, as it is broken as tooling is not ready for jdk11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-5
- Disable tests and remove dependency on mojarra

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Tomas Repik <trepik@redhat.com> - 1.1.1-1
- initial package

