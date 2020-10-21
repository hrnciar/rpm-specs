Name:          zxing
Version:       3.2.1
Release:       14%{?dist}
Summary:       Java multi-format 1D/2D bar-code image processing library
License:       ASL 2.0
URL:           https://github.com/zxing/zxing/
# remove unused files (126MB)
# sh zxing-repack.sh <VERSION>
Source0:       %{name}-%{version}.tar.xz
Source1:       zxing-repack.sh
# FTBFS fix manually cherry picked from upstream commit
#   https://github.com/zxing/zxing/commit/e2afb336e2f7afaa9d0895c4d16e9e85013c2f3d
Patch0:        zxing-3.2.1-deprecated-JCommander-usage.patch

BuildRequires: maven-local
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(junit:junit)

# https://fedorahosted.org/fpc/ticket/574
Provides: bundled(barcode4j)

BuildArch:     noarch

%description
ZXing ("zebra crossing") is an open-source,
multi-format 1D/2D bar-code image processing library
implemented in Java, with ports to other languages.

%package javase
Summary:       ZXing Java SE extensions

%description javase
Java SE-specific extensions to core ZXing library.

%package parent
Summary:       ZXing Parent POM

%description parent
This package provides ZXing Parent POM.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0

%pom_remove_dep com.google.android:
%pom_remove_dep :android-core
%pom_remove_dep :android-integration

%pom_disable_module android-core
%pom_disable_module android-integration
# use com.google.gwt:gwt-{servlet,user}:2.6.1,org.codehaus.mojo:gwt-maven-plugin
%pom_disable_module zxing.appspot.com
%pom_disable_module zxingorg

# Unwanted/unneeded tasks
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-release-plugin
# Break build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :apache-rat-plugin
# Unavailble plugin
%pom_remove_plugin -r :clirr-maven-plugin

# Unavailable test resources
rm -r core/src/test/java/com/google/zxing/qrcode/QRCodeWriterTestCase.java \
 core/src/test/java/com/google/zxing/qrcode/QRCodeBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/datamatrix/DataMatrixBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/pdf417/PDF417BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/EAN13BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code39BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCEANExtensionBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCABlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code93BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCEBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code128BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/CodabarBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/ITFBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/negative \
 core/src/test/java/com/google/zxing/oned/EAN8BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code39ExtendedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/RSS14BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedStackedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/aztec/AztecBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedInternalTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedStackedInternalTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2stringTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2binaryTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2resultTestCase.java

sed -i '/DataMatrixBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code39BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/EAN13BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCABlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCABlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCEBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/PDF417BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/QRCodeBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code128BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/ITFBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/EAN8BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code39ExtendedBlackBox2TestCase/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-core
%doc AUTHORS CHANGES README.md
%license COPYING NOTICE

%files javase -f .mfiles-javase
%license COPYING NOTICE

%files parent -f .mfiles-zxing-parent
%license COPYING NOTICE

%files javadoc -f .mfiles-javadoc
%license COPYING NOTICE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.1-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Merlin Mathesius <mmathesi@redhat.com> - 3.2.1-6
- Fix FTBFS error resulting from deprecated JCommander usage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Jonny Heggheim <hegjon@gmail.com> - 3.2.1-2
- Added Provides: bundled(barcode4j) (FPC-574)

* Sun Aug 30 2015 gil cattaneo <puntogil@libero.it> 3.2.1-1
- update to 3.2.1

* Sun Feb 08 2015 gil cattaneo <puntogil@libero.it> 3.1.0-1
- initial rpm
