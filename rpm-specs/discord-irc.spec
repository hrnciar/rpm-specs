%global npmname discord-irc

Name:           %{npmname}
Version:        2.7.2
Release:        4%{?dist}
Summary:        Connects Discord and IRC channels by sending messages back and forth

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

# Script to run discord-irc.
Source1:        discord-irc

# Default config file, taken from upstream README.
Source2:        config.json

# Systemd service file.
Source3:        discord-irc.service

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-check-env
BuildRequires:  nodejs-commander
BuildRequires:  nodejs-discord-js
BuildRequires:  nodejs-irc-colors
BuildRequires:  nodejs-irc-formatting
BuildRequires:  nodejs-irc-upd
BuildRequires:  nodejs-lodash
BuildRequires:  nodejs-simple-markdown
BuildRequires:  nodejs-strip-json-comments
BuildRequires:  nodejs-winston

%{?systemd_requires}
BuildRequires:  systemd

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Connects Discord and IRC channels by sending messages back and forth.

%prep
%autosetup -n package

# There is no point even pretending any of these packages will ever
# be the right versions.
%nodejs_fixdep check-env
%nodejs_fixdep commander
%nodejs_fixdep discord.js
%nodejs_fixdep irc-colors
%nodejs_fixdep irc-formatting
%nodejs_fixdep irc-upd
%nodejs_fixdep lodash
%nodejs_fixdep simple-markdown
%nodejs_fixdep strip-json-comments
%nodejs_fixdep winston

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a dist %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

# We need to land a script in /usr/bin to do something.
mkdir -p %{buildroot}%{_bindir}
cp -p %SOURCE1 %{buildroot}%{_bindir}

# We should install template configuration file.
mkdir -p %{buildroot}%{_sysconfdir}/discord-irc
cp -p %SOURCE2 %{buildroot}%{_sysconfdir}/discord-irc/

# We need to install a systemd service file too.
mkdir -p %{buildroot}%{_unitdir}
cp -p %SOURCE3 %{buildroot}%{_unitdir}

# Remove the shbang after installation from cli.js
sed '/env node/d' -i %{buildroot}%{nodejs_sitelib}/%{npmname}/dist/cli.js

%check
%nodejs_symlink_deps --check

%post
%systemd_post discord-irc.service

%preun
%systemd_preun discord-irc.service

%postun
%systemd_postun_with_restart discord-irc.service

%files
%{_bindir}/discord-irc
%{_unitdir}/discord-irc.service
%{nodejs_sitelib}/%{npmname}/
%config(noreplace) %{_sysconfdir}/discord-irc
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.7.2-1
- Updated to latest upstream release (rhbz#1702377).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.6.1-2
- Add missing systemd scriplets.
- Own the entire /etc/discord-irc/ directory as config(noreplace).
- Strip shbang from dist/cli.js in the module install directory.

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.6.1-1
- Initial package.
