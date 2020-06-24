Name:           nodejs-has
Version:        1.0.3
Release:        3%{?dist}
Summary:        Object.prototype.hasOwnProperty.call shortcut

License:        MIT
URL:            https://github.com/tarruda/has
Source0:        https://registry.npmjs.org/has/-/has-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(function-bind)


%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/has
cp -pr package.json src %{buildroot}%{nodejs_sitelib}/has
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test


%files
%doc README.md
%license LICENSE-MIT
%{nodejs_sitelib}/has


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun  3 2018 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build of 1.0.1
