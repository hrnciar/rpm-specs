Name:           nodejs-function-bind
Version:        1.1.1
Release:        6%{?dist}
Summary:        Implementation of Function.prototype.bind

License:        MIT
URL:            https://github.com/Raynos/function-bind
Source0:        https://registry.npmjs.org/function-bind/-/function-bind-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/function-bind
cp -pr package.json index.js implementation.js %{buildroot}%{nodejs_sitelib}/function-bind
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test/index.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/function-bind


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Tom Hughes <tom@compton.nu> - 1.1.0-3
- Enable tests

* Sun Feb 14 2016 Tom Hughes <tom@compton.nu> - 1.1.0-2
- Add implementation.js to package

* Sun Feb 14 2016 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Initial build of 1.0.2
