%global npmname irc-colors

Name:           nodejs-%{npmname}
Version:        1.5.0
Release:        3%{?dist}
Summary:        Color and formatting for irc made easy

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

# Tests not included on NPM.
Source0:        https://github.com/fent/irc-colors.js/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-vows

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Easily use colored output and formatting in your irc bots.

%prep
%autosetup -n irc-colors.js-%{version}

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a lib/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

# Istanbul was retired from Fedora. It's also deprecated upstream.
# So we can no longer run tests.
# istanbul-js cover vows -- --spec test/*-test.js

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md example/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.5.0-1
- Updated to latest upstream release, 1.5.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.4.3-1
- Updated to latest upstream release (rhbz#1607137).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.4.2-1
- Updated to latest upstream release (#1549109).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1508189)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.3.3-1
- Initial package.
