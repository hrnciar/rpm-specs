%global npmname discord.js

Name:           nodejs-discord-js
Version:        11.5.1
Release:        2%{?dist}
Summary:        Powerful JavaScript library for interacting with the Discord API

# The "typings" directory seems to be under MIT.
# I'm not sure if it is policy to ship that or not; I chose to here though.
License:        ASL 2.0 and MIT

URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://github.com/discordjs/discord.js/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-long
BuildRequires:  nodejs-prism-media
BuildRequires:  nodejs-snekfetch
BuildRequires:  nodejs-tweetnacl
BuildRequires:  nodejs-ws

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
discord.js is a powerful Node.js module that allows you to interact with
the Discord API very easily.

%prep
%autosetup -n %{npmname}-%{version}

# We almost certainly need to do this.
%nodejs_fixdep ws
%nodejs_fixdep snekfetch

# I bet that this will not work and we need 0.0.3.
%nodejs_fixdep prism-media

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a src/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a typings/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 11.5.1-1
- Updated to latest upstream release (rhbz#1708961).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 11.4.2-1
- Initial package.
