%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-globule
Version:        1.3.0
Release:        2%{?dist}
Summary:        An easy-to-use wildcard globbing library for Node.js

License:        MIT
URL:            https://github.com/cowboy/node-globule
Source0:        https://github.com/cowboy/node-globule/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(glob)
BuildRequires:  npm(lodash)
%endif

%description
%{summary}.


%prep
%autosetup -p 1 -n node-globule-%{version}
%nodejs_fixdep glob "^6.0.3"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/globule
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/globule
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/nodeunit/bin/nodeunit test/globule_test.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/globule


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release
- Update npm(lodash) dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.2.0-5
- Update npm(glob) dependency
- Update npm(minimatch) dependency

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.2.0-4
- Update npm(lodash) dependency
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
