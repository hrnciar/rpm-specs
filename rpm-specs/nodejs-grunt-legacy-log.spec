%{?nodejs_find_provides_and_requires}

Name:           nodejs-grunt-legacy-log
Version:        2.0.0
Release:        2%{?dist}
Summary:        The Grunt 0.4.x logger

License:        MIT
URL:            https://github.com/gruntjs/grunt-legacy-log
Source0:        https://registry.npmjs.org/grunt-legacy-log/-/grunt-legacy-log-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(nodeunit)
BuildRequires:  npm(async)
BuildRequires:  npm(colors)
BuildRequires:  npm(grunt-legacy-log-utils)
BuildRequires:  npm(hooker)
BuildRequires:  npm(lodash)
BuildRequires:  npm(underscore.string)


%description
%{summary}.


%prep
%setup -q -n package
%nodejs_fixdep colors "^1.1.2"
%nodejs_fixdep underscore.string "^2.3.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-legacy-log
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/grunt-legacy-log
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
FORCE_COLOR=1 %{nodejs_sitelib}/nodeunit/bin/nodeunit test/index.js


%files
%{!?_licensedir:%global license %doc}
%doc README.md CHANGELOG
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-legacy-log


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 27 2018 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Fri Mar  2 2018 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-1
- Update to 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Tom Hughes <tom@compton.nu> - 0.1.3-1
- Update to 0.1.3 upstream release

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.1.2-3
- Update npm(lodash) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.1.2-2
- Update npm(colors) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.1.2-1
- Initial build of 0.1.2
