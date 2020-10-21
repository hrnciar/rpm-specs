# Disabled as ava module upstream not found
%global enable_tests 0
%global module_name require-uncached

Name:           nodejs-%{module_name}
Version:        3.2.1
Release:        1%{?dist}
Summary:        Require a module bypassing the cache

License:        MIT
URL:            https://github.com/sindresorhus/require-uncached
Source0:        http://registry.npmjs.org/%{module_name}/-/import-fresh-%{version}.tgz
# Please note upstream renamed this project to import-fresh module
Source1:        https://raw.githubusercontent.com/sindresorhus/import-fresh/v%{version}/license
Source2:        https://raw.githubusercontent.com/sindresorhus/import-fresh/v%{version}/test.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(caller-path)
BuildRequires:  npm(resolve-from)

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
%endif

%description
Useful for testing purposes when you need to freshly require a module.

%prep
%autosetup -n package
rm -rf node_modules
cp -p %{SOURCE1} %{SOURCE2} .
%nodejs_fixdep caller-path
%nodejs_fixdep resolve-from

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
node test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc readme.md 
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Aug 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.1-1
- Update to latest upstream release 3.2.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.0.3-5
- Update Source tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-1
- Update to 1.0.3 

* Mon Sep 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-6
- Relax fixdep for npm(caller-path)

* Mon Feb 15 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-5
- Relax dependency on npm(resolve-from)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- fix caller-path dependency

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

