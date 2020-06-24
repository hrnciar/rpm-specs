# we have older version of coffee-script in fedora
%global enable_tests 0
%global module_name is-arrayish

Name:           nodejs-%{module_name}
Version:        1.3.1
Release:        9%{?dist}
Summary:        Check if an object can be used like an Array

License:        MIT
URL:            https://github.com/Qix-/node-is-arrayish
Source0:        https://github.com/Qix-/node-%{module_name}/archive/%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires: coffee-script
BuildRequires: nodejs-istanbul
BuildRequires: mocha
BuildRequires: npm(should)
%endif

%description
%{summary}.

%prep
%setup -q -n node-%{module_name}-%{version}
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-8
- Disable tests as we lost nodejs-istanbul package in Fedora

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-1
- Update to 1.3.1 release

* Thu Feb 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.3.0-1
- Update to 0.3.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.2.1-2
- Enable tests as we have new coffee-script in rawhide

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.2.1-1
- Initial packaging

