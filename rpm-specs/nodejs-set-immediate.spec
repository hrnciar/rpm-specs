Name:           nodejs-set-immediate
Version:        0.1.1
Release:        10%{?dist}
Summary:        A shim for the setImmediate API

License:        MIT
URL:            https://github.com/jussi-kalliokoski/setImmediate.js
Source0:        http://registry.npmjs.org/set-immediate/-/set-immediate-%{version}.tgz
# https://github.com/jussi-kalliokoski/setImmediate.js/pull/5
Source1:        nodejs-set-immediate-license.txt
# https://github.com/jussi-kalliokoski/setImmediate.js/pull/4
Patch0:         nodejs-set-immediate-test.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
A simple and lightweight shim for the setImmediate W3C Draft API, for
use in any browsers and NodeJS.


%prep
%setup -q -n package
%patch0 -p1
cp %{SOURCE1} LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/set-immediate
cp -pr package.json setImmediate.js %{buildroot}%{nodejs_sitelib}/set-immediate
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs tests/test.js


%files
%doc README.md LICENSE
%{nodejs_sitelib}/set-immediate


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Tom Hughes <tom@compton.nu> - 0.1.1-1
- Initial build of 0.1.1
