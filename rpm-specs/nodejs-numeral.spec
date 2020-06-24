Name:           nodejs-numeral
Version:        2.0.6
Release:        7%{?dist}
Summary:        A javascript library for formatting and manipulating numbers

License:        MIT
URL:            https://github.com/adamwdraper/Numeral-js
Source0:        https://registry.npmjs.org/numeral/-/numeral-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)


%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/numeral
cp -pr package.json numeral.js locales.js %{buildroot}%{nodejs_sitelib}/numeral
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha tests/**/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/numeral


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Tom Hughes <tom@compton.nu> - 2.0.6-1
- Update to 2.0.6 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 2.0.4-1
- Update to 2.0.4 upstream release

* Sun Dec 18 2016 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Update to 2.0.3 upstream release

* Sat Dec 17 2016 Tom Hughes <tom@compton.nu> - 2.0.2-1
- Update to 2.0.2 upstream release

* Wed Dec  7 2016 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Thu Nov 24 2016 Tom Hughes <tom@compton.nu> - 1.5.6-1
- Update to 1.5.6 upstream release

* Mon Nov 21 2016 Tom Hughes <tom@compton.nu> - 1.5.5-1
- Update to 1.5.5 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 1.5.3-1
- Initial build of 1.5.3
