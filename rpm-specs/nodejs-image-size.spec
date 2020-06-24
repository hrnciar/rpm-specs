%{?nodejs_find_provides_and_requires}

Name:           nodejs-image-size
Version:        0.6.3
Release:        4%{?dist}
Summary:        A Node module to get dimensions of any image file

License:        MIT
URL:            https://www.npmjs.com/package/image-size
Source0:        https://github.com/image-size/image-size/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(expect.js)
BuildRequires:  npm(sinon)


%description
%{summary}.


%prep
%autosetup -n image-size-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/image-size
cp -pr package.json bin lib %{buildroot}%{nodejs_sitelib}/image-size
mkdir -p %{buildroot}/%{_bindir}
ln -s %{nodejs_sitelib}/image-size/bin/image-size.js %{buildroot}/%{_bindir}/image-size
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha specs


%files
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/image-size
%{_bindir}/image-size


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Tom Hughes <tom@compton.nu> - 0.6.3-1
- Initial build of 0.6.3
