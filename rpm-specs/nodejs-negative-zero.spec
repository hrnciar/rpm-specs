%global npmname negative-zero

Name:           nodejs-%{npmname}
Version:        3.0.0
Release:        3%{?dist}
Summary:        Check if a number is negative zero

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Check if a number if negative zero.

%prep
%autosetup -n package

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a index.d.ts %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npmname}/
%license license
%doc readme.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Ben Rosser <rosser.bjr@gmail.com> - 3.0.0-1
- Update to latest upstream release (rhbz#1702221).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-1
- Initial package.
