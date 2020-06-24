Name:          jfontchooser
Version:       1.0.5
Release:       10%{?dist}
Summary:       Swing-based java component for font selection
URL:           http://jfontchooser.sourceforge.jp/site/jfontchooser/index.html
Source0:       http://iij.dl.osdn.jp/jfontchooser/31074/jfontchooser-%{version}-src.zip
License:       MIT
BuildRequires: maven-local
BuildArch:     noarch

%description
JFontChooser is a swing-based java component for font selection.


%package javadoc
Summary:       API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q
%pom_remove_parent
find -name '*.jar' -delete


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.txt
%license LICENSE.txt


%files javadoc -f .mfiles-javadoc
%license LICENSE.txt


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.5-2
- Review from Michael Simacek (#1286002):
- Drop POM parent with a macro
- Include license text in javadoc subpackage

* Fri Nov 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.5-1
- Initial packaging
