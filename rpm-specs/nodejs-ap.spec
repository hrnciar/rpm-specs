%{?nodejs_find_provides_and_requires}

Name:           nodejs-ap
Version:        0.2.0
Release:        9%{?dist}
Summary:        Currying in javascript

License:        MIT
URL:            https://www.npmjs.com/package/ap
Source0:        https://registry.npmjs.org/ap/-/ap-%{version}.tgz
# https://github.com/substack/node-ap/pull/6
Source1:        nodejs-ap-license.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)


%description
Currying in javascript. Like .bind() without also setting this.

Function.prototype.bind sets this which is super annoying if you
just want to do currying over arguments while passing this through.


%prep
%autosetup -n package
cp %{SOURCE1} LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ap
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/ap
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tap/bin/tap.js ./test


%files
%{!?_licensedir:%global license %doc}
%doc README.markdown examples
%license LICENSE
%{nodejs_sitelib}/ap


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Initial build of 0.2.0
