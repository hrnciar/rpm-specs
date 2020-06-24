# Current upstream requires few packages for
# running tests which are not in Fedora yet
%global enable_tests 0
%global module_name object-assign

Name:           nodejs-%{module_name}
Version:        4.1.1
Release:        9%{?dist}
Summary:        ES6 Object.assign() ponyfill

License:        MIT
URL:            https://github.com/sindresorhus/object-assign
Source0:        https://github.com/sindresorhus/%{module_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
BuildRequires:  npm(xo)
BuildRequires:  npm(matcha)
BuildRequires:  npm(lodash)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

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
xo && ava
match bench.js
%endif

%files
%doc readme.md 
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1-3
- Disable tests are required packages not in Fedora yet

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1-1
- Update to 4.1.1 release

* Tue May 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 4.1.0-1
- Update to 4.1.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 4.0.1-1
- Update to 4.0.1

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-2
- Add test.js from upstream and enable tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- Initial packaging

