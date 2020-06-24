%global commit be8c976fd2a8c4fb0a50c764e97d7f3bf8619a13

Name:           nodejs-deep-eql
Version:        0.1.3
Release:        13%{?dist}
Summary:        Improved deep equality testing for Node.js and the browser

License:        MIT
URL:            https://github.com/chaijs/deep-eql
Source0:        https://github.com/chaijs/deep-eql/archive/%{commit}/deep-eql-%{commit}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(simple-assert)
BuildRequires:  npm(type-detect)

%description
Improved deep equality testing for Node.js and the browser.


%prep
%setup -q -n deep-eql-%{commit}
%nodejs_fixdep type-detect "^2.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/deep-eql
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/deep-eql
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --require test/bootstrap --reporter list test/*.js


%files
%doc README.md History.md 
%{nodejs_sitelib}/deep-eql



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Tom Hughes <tom@compton.nu> - 0.1.3-6
- Update npm(type-detect) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr  6 2015 Tom Hughes <tom@compton.nu> - 0.1.3-3
- Update type-detect dependency
- Switch to using github as source so we get tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Tom Hughes <tom@compton.nu> - 0.1.3-1
- Initial build of 0.1.3
