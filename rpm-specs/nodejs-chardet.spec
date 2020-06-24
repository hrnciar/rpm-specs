%global npmname chardet

Name:           nodejs-%{npmname}
Version:        0.8.0
Release:        2%{?dist}
Summary:        Character detection tool for NodeJS

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

# No tests on NPM. :(
Source0:        https://github.com/runk/node-chardet/archive/v%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  mocha

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Chardet is a character detection module for NodeJS written in pure Javascript.
Module is based on ICU project http://site.icu-project.org/, which uses
character occurency analysis to determine the most probable encoding.

%prep
%autosetup -n node-chardet-%{version}

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a match.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a encoding %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
mocha -R spec --recursive --bail

%files
%{nodejs_sitelib}/%{npmname}/
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.8.0-1
- Update to latest upstream release (rhbz#1741995).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.7.0-1
- Updated to latest upstream release.

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.6.0-1
- Initial package.
