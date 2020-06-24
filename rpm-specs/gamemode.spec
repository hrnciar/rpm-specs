Name:		gamemode
Version:	1.5.1
Release:	1%{?dist}
Summary:	Optimize system performance for games on demand
License:	BSD
URL:		https://github.com/FeralInteractive/gamemode
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(inih) >= 49
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimizations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU "powersave" or "ondemand" governors, but is
now host to a range of optimisation features and configurations, like
tweaking various settings: the CPU govenor, the I/O priority, the
kernel scheduler, the GPU performance mode and gpu overclocking
(NVIDIA). It can also excute custom scripts when launching games.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc	 README.md
%{_bindir}/gamemoded
%{_bindir}/gamemoderun
%{_libexecdir}/cpugovctl
%{_libexecdir}/gpuclockctl
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_libdir}/libgamemode*.so.*
%{_libdir}/libgamemode*.so
%{_userunitdir}/gamemoded.service
%{_mandir}/man8/gamemoded.8*

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/pkgconfig/gamemode*.pc

%changelog
* Thu Jun  4 2020 Christian Kellner <ckellner@redhat.com> - 1.5.1-1
- New upstream release (1.5.1)
- Require inih package because gamemode now uses the system installed one.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Christian Kellner <ckellner@redhat.com> - 1.5-1
- New upstream release (1.5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Christian Kellner <christian@kellner.me> - 1.4-1
- New upstream release (1.4)
- Add dbus-1 dependency, required by the client library.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.3.1-3
- Rebuild with Meson fix for #1699099

* Mon Apr  8 2019 Christian Kellner <christian@kellner.me> - 1.3.1-2
- Ship unversioned .so in main package, because old games require that one.
  Resolves: rhbz#1694938

* Mon Apr  1 2019 Christian Kellner <christian@kellner.me> - 1.3.1-1
- New upstream release (1.3.1)
  Resloves: rhbz#1694254
- Drop the patch(es) (all upstreamed).

* Thu Mar 28 2019 Christian Kellner <christian@kellner.me> - 1.3-1
- New upstream Release (1.3)
  Resolves: rhbz#1689371
- Includes a new gamemoderun script to easily invoce gamemode.
- Add patch that ensures all strncpy calls leave strings properly null
  terminated and other code cleanups (all but one are upstreamed already).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Christian Kellner <christian@kellner.me> - 1.2-1
- New upstream release
  Resolves: #1607099
- Drop all patches (all upstreamed)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Christian Kellner <christian@kellner.me>  - 1.1-1
- Initial package
  Resolves: #1596293
- Patch to move manpage to section 8
  Upstream commit 28fcb09413bbf95507788024b98b675cbf656f6c
- Patch for dbus auto-activation
  Merged PR https://github.com/FeralInteractive/gamemode/pull/62
- Patch for proper library versioning
  Merged PR https://github.com/FeralInteractive/gamemode/pull/63

