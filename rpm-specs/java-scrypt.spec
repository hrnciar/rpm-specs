Name: java-scrypt
Version: 1.4.0
Release: 10%{?dist}
Summary: Java implementation of scrypt

License: ASL 2.0
URL: http://github.com/wg/scrypt
Source0: https://github.com/wg/scrypt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: no-jni.patch
BuildArch: noarch

BuildRequires: maven-local

%description
A pure Java implementation of the scrypt key derivation function.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n scrypt-%{version}

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.jar' -print -delete

%build
#Disble tests, since many of them are releated to JNI
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-2
- Minor refactor of spec file

* Sat Aug 08 2015 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-1
- Inital packaging
