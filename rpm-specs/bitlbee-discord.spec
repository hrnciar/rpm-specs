Name:           bitlbee-discord
Version:        0.4.3
Release:        3%{?dist}
Summary:        Bitlbee plugin for Discord

License:        GPLv2+
URL:            https://github.com/sm00th/bitlbee-discord

Source0:        https://github.com/sm00th/bitlbee-discord/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bitlbee-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libtool

# This is a bitlbee plugin, rpm won't automatically see the needed dep.
Requires:       bitlbee

%description
Discord protocol plugin for bitlbee.

%prep
%autosetup -p1 -n %{name}-%{version}
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

# Remove libtool archive.
rm -f %{buildroot}%{_libdir}/bitlbee/discord.la

%files
%{_libdir}/bitlbee/discord.so
%{_datadir}/bitlbee/discord-help.txt
%license LICENSE
%doc README

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Ben Rosser <rosser.bjr@gmail.com> - 0.4.3-1
- Update to latest upstream release (rhbz#1819635).

* Tue Feb 11 2020 Ben Rosser <rosser.bjr@gmail.com> - 0.4.2-5.20200211git69e16be
- Update to git snapshot to resolve connection issues.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.4.2-1
- Updated to 0.4.2, latest upstream release.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.4.1-2
- Add missing requires on bitlbee.
- Add patch to remove obsolete M4 macro.

* Tue Feb 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.4.1-1
- Initial package.
