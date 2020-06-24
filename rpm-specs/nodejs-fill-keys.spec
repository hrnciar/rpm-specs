Name:           nodejs-fill-keys
Version:        1.0.2
Release:        9%{?dist}
Summary:        Fill keys in a destination that are defined on the source

License:        MIT
URL:            https://github.com/bendrucker/fill-keys
Source0:        https://github.com/bendrucker/fill-keys/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(is-object)
BuildRequires:  npm(merge-descriptors) >= 1.0.0

BuildRequires:  npm
BuildRequires:  npm(tape)


%description
Fill keys in a destination that are defined on the source. Copies
descriptors so properties like enumerable will persist.


%prep
%setup -q -n fill-keys-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fill-keys
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/fill-keys
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony %{nodejs_sitelib}/tape/bin/tape test.js


%files
%doc readme.md
%license license
%{nodejs_sitelib}/fill-keys


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

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release
- Use github as source to get tests
- Update tests to use tape as runner

* Wed May 20 2015 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
