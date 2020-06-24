%global npmname int64-buffer

Name:           nodejs-%{npmname}
Version:        0.99.1007
Release:        1%{?dist}
Summary:        64bit Long Integer on Buffer/Array/ArrayBuffer in Pure JavaScript

License:        MIT
URL:            https://www.npmjs.com/package/int64-buffer
Source0:        https://registry.npmjs.org/int64-buffer/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildRequires:  mocha

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
JavaScript's number based on IEEE-754 could only handle 53 bits precision. This
module provides a couple of classes: Int64BE and Uint64BE which could hold 64
bits long integer and loose no bit.

%prep
%autosetup -n package

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a int64-buffer.d.ts int64-buffer.js dist/ package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

mocha -R spec *.json ./test/*.js

%files
%{nodejs_sitelib}/%{npmname}
%license LICENSE
%doc README.md


%changelog
* Tue Jun 16 2020 Ben Rosser <rosser.bjr@gmail.com> - 0.99.1007-1
- Updated to latest upstream release (rhbz#1834050).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.1.10-1
- Updated to latest upstream release.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep  9 2016 Ben Rosser <rosser.bjr@gmail.com> 0.1.9-1
- Update to latest version.

* Wed Jun 29 2016 Ben Rosser <rosser.bjr@gmail.com> 0.1.7-1
- Initial package.
