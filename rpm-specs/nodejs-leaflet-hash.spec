Name:           nodejs-leaflet-hash
Version:        0.2.1
Release:        11%{?dist}
Summary:        Linkable location hashes for Leaflet

License:        MIT
URL:            https://github.com/mlevans/leaflet-hash
Source0:        http://registry.npmjs.org/leaflet-hash/-/leaflet-hash-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       js-leaflet-hash = %{version}-%{release}

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel

%description
Leaflet-hash lets you to add dynamic URL hashes to web pages with
Leaflet maps. You can easily link users to specific map views.


%package -n js-leaflet-hash
Summary:        Linkable location hashes for leaflet
Requires:       web-assets-filesystem
Requires:       js-leaflet

%description -n js-leaflet-hash
Leaflet-hash lets you to add dynamic URL hashes to web pages with
Leaflet maps. You can easily link users to specific map views.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep leaflet "^1.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{_jsdir}/leaflet
cp -pr leaflet-hash.js %{buildroot}%{_jsdir}/leaflet
mkdir -p %{buildroot}%{nodejs_sitelib}/leaflet-hash
cp -pr package.json %{buildroot}%{nodejs_sitelib}/leaflet-hash
ln -s %{_jsdir}/leaflet/leaflet-hash.js %{buildroot}%{nodejs_sitelib}/leaflet-hash
%nodejs_symlink_deps


%files
%{nodejs_sitelib}/leaflet-hash


%files -n js-leaflet-hash
%doc README.md
%license LICENSE.md
%{_jsdir}/leaflet/leaflet-hash.js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Tom Hughes <tom@compton.nu> - 0.2.1-4
- Update npm(leaflet) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Initial build of 0.2.1
