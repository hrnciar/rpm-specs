%{?nodejs_find_provides_and_requires}

Name:           nodejs-is-callable
Version:        1.1.5
Release:        2%{?dist}
Summary:        Is this JS value callable?

License:        MIT
URL:            https://github.com/ljharb/is-callable
Source0:        https://registry.npmjs.org/is-callable/-/is-callable-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(foreach)
BuildRequires:  npm(make-arrow-function)
BuildRequires:  npm(make-generator-function)
BuildRequires:  npm(tape)


%description
Is this JS value callable? Works with Functions and
GeneratorFunctions, despite ES6 @@toStringTag.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-callable
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-callable
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --es-staging test


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-callable


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Hughes <tom@compton.nu> - 1.1.5-1
- Update to 1.1.5 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Tom Hughes <tom@compton.nu> - 1.1.4-1
- Update to 1.1.4 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Tom Hughes <tom@compton.nu> - 1.1.3-1
- Update to 1.1.3 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Initial build of 1.1.0
