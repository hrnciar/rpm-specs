%{?nodejs_find_provides_and_requires}

Name:           nodejs-less-plugin-clean-css
Version:        1.5.1
Release:        5%{?dist}
Summary:        Compresses the css output from less using clean-css

License:        ASL 2.0
URL:            https://www.npmjs.com/package/less-plugin-clean-css
Source0:        http://registry.npmjs.org/less-plugin-clean-css/-/less-plugin-clean-css-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(clean-css)


%description
%{summary}.


%prep
%autosetup -n package
%nodejs_fixdep clean-css "^4.2.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/less-plugin-clean-css
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/less-plugin-clean-css
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/less-plugin-clean-css


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Tom Hughes <tom@compton.nu> - 1.5.1-4
- Update npm(clean-css) dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Tom Hughes <tom@compton.nu> - 1.5.1-1
- Initial build of 1.5.1
