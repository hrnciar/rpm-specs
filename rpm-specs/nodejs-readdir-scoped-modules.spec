%{?nodejs_find_provides_and_requires}

Name:           nodejs-readdir-scoped-modules
Version:        1.0.2
Release:        9%{?dist}
Summary:        Like fs.readdir but handling @org/module dirs as if they were a single entry

License:        ISC
URL:            https://www.npmjs.com/package/readdir-scoped-modules
Source0:        https://registry.npmjs.org/readdir-scoped-modules/-/readdir-scoped-modules-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(debuglog)
BuildRequires:  npm(dezalgo)
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(once)


%description
%{summary}.


%prep
%autosetup -n package
%nodejs_fixdep once "^1.1.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/readdir-scoped-modules
cp -pr package.json readdir.js %{buildroot}%{nodejs_sitelib}/readdir-scoped-modules
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test/*.js


%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/readdir-scoped-modules


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Initial build of 1.0.2
