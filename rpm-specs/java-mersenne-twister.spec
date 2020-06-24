Name:           java-mersenne-twister
Version:        22
Release:        10%{?dist}
Summary:        Mersenne Twister random number generator in Java

License:        BSD
URL:            http://www.cs.gmu.edu/~sean/research/
Source0:        http://www.cs.gmu.edu/~sean/research/mersenne/MersenneTwister.java
Source1:        http://www.cs.gmu.edu/~sean/research/mersenne/MersenneTwisterFast.java

BuildArch:      noarch

BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  javapackages-tools

Requires:       java-headless
Requires:       jpackage-utils

%description
The Mersenne Twister is an exceptionally high-quality, fast random number
generator.  This package contains two versions of it in Java, written by Sean
Luke.  MersenneTwister is a complete drop-in subclass replacement for
java.util.Random.  MersenneTwisterFast is algorithmically identical, except
that it isn't synchronized, and it's not a subclass of Random.  This, plus
other speed improvements, makes it over twice the speed.

%package javadoc
Summary:        Documentation for the Mersenne Twister in Java
Requires:       %{name} = %{version}-%{release}

%description javadoc
Javadoc documentation for the Mersenne Twister in Java.

%prep
%setup -c -T
mkdir -p ec/util
cp -p %{SOURCE0} ec/util
cp -p %{SOURCE1} ec/util

%build
# Build the JAR
javac -source 1.6 -target 1.6 ec/util/*.java
jar cf mersenne-twister.jar ec/util/*.class

# Build the documentation
mkdir doc
javadoc -d doc -source 1.6 ec/util/*.java

%install
# Install the JAR
mkdir -p %{buildroot}%{_javadir}
cp -p mersenne-twister.jar %{buildroot}%{_javadir}

# Install the documentation
mkdir -p %{buildroot}%{_javadocdir}
cp -a doc %{buildroot}%{_javadocdir}/mersenne-twister

%files
%{_javadir}/mersenne-twister.jar

%files javadoc
%{_javadocdir}/mersenne-twister

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  2 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 22-2
- More docstring updates from upstream, unfortunately without a
  version bump

* Wed Sep  2 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 22-1
- Update to version 22

* Wed Aug 26 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 20-4
- Remove Group tag from javadoc sub-package

* Tue Aug 25 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 20-3
- Add patch to fix javadoc generation

* Mon Aug 24 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 20-2
- Replace jpackage-utils Requires and BuildRequires with
  javapackages-tools

* Mon Dec 15 2014 Jerry James <loganjerry@gmail.com> - 20-1
- Initial RPM
