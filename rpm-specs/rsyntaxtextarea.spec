%global upname RSyntaxTextArea

Name:           rsyntaxtextarea
Version:        3.1.1
Release:        2%{?dist}
Summary:        A syntax highlighting, code folding text editor for Java Swing applications

License:        BSD
URL:            https://github.com/bobbylight/%{upname}
Source0:        https://github.com/bobbylight/%{upname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        pom.xml

BuildRequires:  java-devel
BuildRequires:  maven-local

Requires:       java-headless

# Apply workaround until gradle doesn't exists in repos
Provides:       mvn(com.fifesoft:rsyntaxtextarea)
Provides:       osgi(com.fifesoft.rsyntaxtextarea)

BuildArch:      noarch

%description
%{upname} is a customizable, syntax highlighting text component for Java
Swing applications. Out of the box, it supports syntax highlighting for 40+
programming languages, code folding, search and replace, and has add-on
libraries for code completion and spell checking. Syntax highlighting for
additional languages can be added via tools such as JFlex.

%package        javadoc
Summary:        Javadoc for %{upname}

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -n %{upname}-%{version} -p1

# Drop included jars
find . -name "*.jar" -delete

pushd %{upname}
for file in src/main/dist/%{upname}.License.txt src/main/dist/readme.txt; do
    sed "s|\r||g" $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd


%build
d=`mktemp -d`
f=`find %{upname}/src/main/java -type f | grep \.java$`
javac -d $d $f
cp -rv %{upname}/src/main/resources/* $d
l=`pwd`
pushd $d
jar -cf $l/%{name}.jar *
popd
%mvn_artifact %{SOURCE1} %{name}.jar

%install
%mvn_install




%files -f .mfiles
%license %{upname}/src/main/dist/%{upname}.License.txt
%doc %{upname}/src/main/dist/readme.txt
%{_datadir}/java/%{name}/%{name}.jar



%changelog
* Tue Jun 09 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.1-2
- made indexable for maven, so it can be used as maven depndence

* Tue Apr 28 2020 ElXreno <elxreno@gmail.com> - 3.1.1-1
- Updated to version 3.1.1

* Mon Apr 27 2020 ElXreno <elxreno@gmail.com> - 2.6.1-10
- Apply workaround until gradle doesn't exists in repos

* Mon Apr 27 2020 ElXreno <elxreno@gmail.com> - 2.6.1-9
- Set proper BuildRequires

* Mon Apr 27 2020 Jri Vanek <jvanek@redhat.com> - 2.6.1-8
- moved to gradle-less build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Gianluca Sforna <giallu@gmail.com> - 2.6.1-1
- new upstream release
- rebase patches

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 20 2016 Dennis Chen <barracks510@gmail.com> - 2.5.8-2
- Fix License file installed when any subpackage combination is installed.

* Mon Jul 11 2016 Dennis Chen <barracks510@gmail.com> - 2.5.8-1
- First Fedora Packaging.
