Name:           openid-selector
Version:        1.3
Release:        12%{?dist}
Summary:        A user-friendly way to select an OpenID

License:        BSD
URL:            http://code.google.com/p/openid-selector/
Source0:        http://openid-selector.googlecode.com/files/%{name}-%{version}.zip
Patch0:         0001-add-fedora.patch

BuildArch:      noarch

%description
A user-friendly way to select an OpenID

%prep
%setup -q -n %{name}
%patch0 -p1

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pR css images images.large images.small js generate-sprite.js generate-sprite.rb generate-sprite.sh %{buildroot}%{_datadir}/%{name}

%files
%doc README.txt demo.html demo-mootools.html demo-prototype.html demo-ru.html demo-uk.html
%{_datadir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 13 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.3-2
- Added Fedora provider

* Tue Oct 01 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.3-1
- Initial packaging

