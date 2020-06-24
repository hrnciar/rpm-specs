%{?nodejs_find_provides_and_requires}

Name:           nodejs-rewire
Version:        2.5.2
Release:        8%{?dist}
Summary:        Easy dependency injection for node.js unit testing

License:        MIT
URL:            https://www.npmjs.com/package/rewire
Source0:        https://github.com/jhnns/rewire/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(expect.js)


%description
Rewire adds a special setter and getter to modules so you can
modify their behavior for better unit testing. You may:

* Inject mocks for other modules or globals like process
* Leak private variables
* Override variables within the module.

Rewire does not load the file and eval the contents to emulate
node's require mechanism. In fact it uses node's own require to
load the module. Thus your module behaves exactly the same in
your test environment as under regular circumstances (except
your modifications).


%prep
%autosetup -n rewire-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rewire
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/rewire
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec --check-leaks


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/rewire


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Tom Hughes <tom@compton.nu> - 2.5.2-1
- Update to 2.5.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 2.5.1-1
- Initial build of 2.5.1
