%global module_name ip

Name:           nodejs-%{module_name}
Version:        1.1.5
Release:        7%{?dist}
Summary:        IP address utilities for node.js

License:        MIT
URL:            https://github.com/indutny/node-%{module_name}
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(mocha)

%description
%{summary}.

%prep
%autosetup -n package
rm -rf node_modules

%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha --reporter spec test/*-test.js

%files
%doc README.md
%{nodejs_sitelib}/%{module_name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.1.5-1
- Update to 1.1.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.1.4-1
- Update to 1.1.4

* Tue Aug 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.1.3-1
- Update to 1.1.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.3.2-1
- Initial packaging

