Name:           nodejs-leaflet-formbuilder
Version:        0.2.3
Release:        8%{?dist}
Summary:        Helpers to build forms in Leaflet

License:        WTFPL
URL:            https://github.com/yohanboniface/Leaflet.FormBuilder
Source0:        http://registry.npmjs.org/leaflet-formbuilder/-/leaflet-formbuilder-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       js-leaflet-formbuilder = %{version}-%{release}

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel

%description
%{summary}.


%package -n js-leaflet-formbuilder
Summary:        Helpers to build forms in Leaflet
Requires:       web-assets-filesystem
Requires:       js-leaflet

%description -n js-leaflet-formbuilder
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{_jsdir}/leaflet
cp -pr Leaflet.FormBuilder.js %{buildroot}%{_jsdir}/leaflet
mkdir -p %{buildroot}%{nodejs_sitelib}/leaflet-formbuilder
cp -pr package.json %{buildroot}%{nodejs_sitelib}/leaflet-formbuilder
ln -s %{_jsdir}/leaflet/Leaflet.FormBuilder.js %{buildroot}%{nodejs_sitelib}/leaflet-formbuilder
%nodejs_symlink_deps


%files
%{nodejs_sitelib}/leaflet-formbuilder


%files -n js-leaflet-formbuilder
%{_jsdir}/leaflet/Leaflet.FormBuilder.js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Tom Hughes <tom@compton.nu> - 0.2.3-1
- Update to 0.2.3 upstream release

* Mon May 16 2016 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct  9 2015 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Initial build of 0.0.6
