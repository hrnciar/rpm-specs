Name:           nodejs-har-validator
Version:        2.0.6
Release:        3%{?dist}
Summary:        Extremely fast HTTP Archive (HAR) validator using JSON Schema

License:        ISC
URL:            https://github.com/ahmadnassri/node-har-validator
Source0:        https://github.com/ahmadnassri/node-har-validator/archive/v%{version}/har-validator-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(require-directory)
BuildRequires:  npm(pinkie-promise)
BuildRequires:  npm(is-my-json-valid)
BuildRequires:  npm(should) >= 8.0.0

%description
%{summary}.


%prep
%autosetup -p 1 -n node-har-validator-%{version}
%nodejs_fixdep chalk
%nodejs_fixdep commander '2.x'
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/har-validator
cp -pr package.json lib bin %{buildroot}%{nodejs_sitelib}/har-validator
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/har-validator/bin/har-validator %{buildroot}%{_bindir}/har-validator
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
mocha


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/har-validator
%{_bindir}/har-validator


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 2.0.6-1
- Update to 2.0.6 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 2.0.3-2
- Patch tests to work with should 8.x

* Sun Dec 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Wed Nov 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.2-1
- Initial package
