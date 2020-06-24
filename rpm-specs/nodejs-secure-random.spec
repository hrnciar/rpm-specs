%{?nodejs_find_provides_and_requires}

Name:           nodejs-secure-random
Version:        1.1.2
Release:        3%{?dist}
Summary:        Normalize the creation of cryptographically strong random values

License:        MIT
URL:            https://www.npmjs.com/package/secure-random
Source0:        https://github.com/jprichardson/secure-random/archive/%{version}/secure-random-%{version}.tar.gz
# https://github.com/jprichardson/secure-random/issues/3
Source1:        nodejs-secure-random-license.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(terst)


%description
%{summary}.


%prep
%autosetup -n secure-random-%{version}
cp %{SOURCE1} LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/secure-random
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/secure-random
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --ui bdd


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/secure-random


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 24 2016 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Initial build of 1.1.1
