%global enable_tests 0

Name:           nodejs-leaflet
Version:        1.0.3
Release:        8%{?dist}
Summary:        An open source JavaScript Library for Interactive Maps

License:        BSD
URL:            http://leafletjs.com/
Source0:        http://registry.npmjs.org/leaflet/-/leaflet-%{version}.tgz
# Patch out use of git-rev
Patch0:         nodejs-leaflet-git-rev.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       js-leaflet = %{version}-%{release}

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel

BuildRequires:  npm(jake)
BuildRequires:  npm(uglify-js)

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(happen)
BuildRequires:  npm(jshint)
BuildRequires:  npm(karma)
BuildRequires:  npm(karma-mocha)
BuildRequires:  npm(karma-chrome-launcher)
BuildRequires:  npm(karma-phantomjs-launcher)
%endif


%description
An open source JavaScript library for mobile-friendly
interactive maps.


%package -n js-leaflet
Summary:        An open source JavaScript Library for Interactive Maps
Requires:       web-assets-filesystem

%description -n js-leaflet
An open source JavaScript library for mobile-friendly
interactive maps.


%prep
%autosetup -p 1 -n package
rm -rf node_modules dist/*.js


%build
%nodejs_symlink_deps --build
jake build[,,true]


%install
mkdir -p %{buildroot}%{_jsdir}/leaflet
cp -pr dist/* %{buildroot}%{_jsdir}/leaflet
mkdir -p %{buildroot}%{nodejs_sitelib}/leaflet
cp -pr package.json %{buildroot}%{nodejs_sitelib}/leaflet
ln -s %{_jsdir}/leaflet %{buildroot}%{nodejs_sitelib}/leaflet/dist
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
jake test
%endif


%files
%{nodejs_sitelib}/leaflet


%files -n js-leaflet
%doc README.md CHANGELOG.md CONTRIBUTING.md FAQ.md PLUGIN-GUIDE.md
%license LICENSE
%{_jsdir}/leaflet


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release

* Mon Nov 21 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Sun Oct  2 2016 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Wed Sep 28 2016 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Tom Hughes <tom@compton.nu> - 0.7.7-1
- Update to 0.7.7 upstream release

* Wed Sep  2 2015 Tom Hughes <tom@compton.nu> - 0.7.5-1
- Update to 0.7.5 upstream release

* Tue Sep  1 2015 Tom Hughes <tom@compton.nu> - 0.7.4-1
- Update to 0.7.4 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Tom Hughes <tom@compton.nu> - 0.7.3-2
- Add (disabled) support for running tests

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.7.3-1
- Initial build of 0.7.3
