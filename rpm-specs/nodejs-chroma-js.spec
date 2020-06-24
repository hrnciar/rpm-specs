%{?nodejs_find_provides_and_requires}

Name:           nodejs-chroma-js
Version:        2.1.0
Release:        2%{?dist}
Summary:        JavaScript library for color conversions

# BSD except for src/colors/colorbrewer.coffee which is ASL 2.0
License:        BSD and ASL 2.0
URL:            https://www.npmjs.com/package/chroma-js
Source0:        https://registry.npmjs.org/chroma-js/-/chroma-js-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(vows)
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(es6-shim)


%description
%{summary}.


%prep
%autosetup -p1 -n package
%nodejs_fixdep -r cross-env
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/chroma-js
cp -pr package.json chroma.js %{buildroot}%{nodejs_sitelib}/chroma-js
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/vows/bin/vows --spec


%files
%doc readme.md CHANGELOG.md docs/index.html
%license LICENSE
%{nodejs_sitelib}/chroma-js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Tom Hughes <tom@compton.nu> - 2.1,0-1
- Update to 2.1.0 upstream release

* Thu Aug 29 2019 Tom Hughes <tom@compton.nu> - 2.0.6-1
- Update to 2.0.6 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Tom Hughes <tom@compton.nu> - 2.0.4-1
- Update to 2.0.4 upstream release

* Sun Feb 17 2019 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Update to 2.0.3 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Sun Jul 15 2018 Tom Hughes <tom@compton.nu> - 1.3.7-1
- Update to 1.3.7 upstream release
- Add patch for node 10 compatibility

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Tom Hughes <tom@compton.nu> - 1.3.4-2
- Correct license tag

* Fri Aug 11 2017 Tom Hughes <tom@compton.nu> - 1.3.4-1
- Initial build of 1.3.4
