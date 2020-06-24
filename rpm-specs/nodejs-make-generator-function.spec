%{?nodejs_find_provides_and_requires}

Name:           nodejs-make-generator-function
Version:        1.1.1
Release:        2%{?dist}
Summary:        Returns an arbitrary generator function

License:        MIT
URL:            https://github.com/ljharb/make-generator-function
Source0:        https://registry.npmjs.org/make-generator-function/-/make-generator-function-%{version}.tgz
# https://github.com/ljharb/make-generator-function/pull/1
Source1:        nodejs-make-generator-function-license.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
Returns an arbitrary generator function, or undefined if generator
syntax is unsupported. If both generator syntax and concise method
syntax are supported, the generator function returned will have
a "concise" property containing a concise generator method.


%prep
%setup -q -n package
cp %{SOURCE1} LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/make-generator-function
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/make-generator-function
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/make-generator-function


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Initial build of 1.1.0
