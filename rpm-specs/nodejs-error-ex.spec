# we have older version of coffee-script in fedora
%global enable_tests 0
%global module_name error-ex

Name:           nodejs-%{module_name}
Version:        1.3.1
Release:        8%{?dist}
Summary:        Easy error subclassing and stack customization

License:        MIT
URL:            https://github.com/Qix-/node-error-ex
Source0:        https://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/Qix-/node-error-ex/master/test/test.coffee

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(is-arrayish)
BuildRequires:  npm(istanbul)
BuildRequires:  npm(should)
%endif

%description
%{summary}.

%prep
%setup -q -n package
mkdir test
cp -p %{SOURCE1} .

%nodejs_fixdep is-arrayish

rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha --compilers coffee:coffee-script/register
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Parag Nemade <pnemade@fedoraproject.org> - 1.3.1-7
- Disable tests as nodejs-istanbul is retired in F31+ (rh#1736196)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-3
- Relax the npm(is-arrayish) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-1
- Update to 1.3.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-5
- Fix %%check section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Tom Hughes <tom@compton.nu> - 1.3.0-3
- Update npm(is-arraish) dependency
- Enable tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-1
- update to 1.3.0

* Fri Sep 25 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.1-1
- Initial packaging

