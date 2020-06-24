%{?nodejs_find_provides_and_requires}

Name:           nodejs-okay
Version:        1.0.0
Release:        6%{?dist}
Summary:        Bubble errors back up your big ol' nested callback chain

License:        MIT
URL:            https://www.npmjs.com/package/okay
Source0:        https://registry.npmjs.org/okay/-/okay-%{version}.tgz
# https://github.com/brianc/node-okay/pull/6
Source1:        nodejs-okay-license.txt
# Drop test that tests behaviour of Node without okay
Patch0:         nodejs-okay-without-okay.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(bcrypt)
BuildRequires:  npm(sliced)


%description
%{summary}.


%prep
%autosetup -p 1 -n package
cp %{SOURCE1} LICENSE
%nodejs_fixdep sliced "^1.0.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/okay
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/okay
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/okay


%changelog
* Fri Feb  7 2020 Tom Hughes <tom@compton.nu> - 1.0.0-6
- Drop test that tests behaviour of Node without okay

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar  8 2018 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0.
