%global enable_tests 0
%global module_name caller-path

Name:           nodejs-%{module_name}
Version:        2.0.0
Release:        10%{?dist}
Summary:        Get the path of the caller module

License:        MIT
URL:            https://github.com/sindresorhus/caller-path
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/sindresorhus/caller-path/master/test.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(fixture)
BuildRequires:  npm(mocha)
%endif

%description
Get the path of the caller module. You can't use module.parent as modules are 
cached and it will return the first caller module, not necessarily the current
one.

%prep
%setup -q -n package
rm -rf node_modules

cp -p %{SOURCE1} .

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 2.0.0-6
- Remove duplicate license source file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-2
- Remove fixdep for npm(callsites)

* Fri Sep 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- update to 2.0.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- update to 1.0.0 release

* Mon Dec 08 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.0-1
- Initial packaging

