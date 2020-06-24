# -*-Mode: rpm-spec -*-

Name: wlogout
Version: 1.1.1
Release: 5%{?dist}
Summary: Wayland based logout menu
License: MIT
URL:     https://github.com/ArtsyMacaw/wlogout
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# appears to be from https://github.com/zserge/jsmn at git tag
# cdcfaafa49ffe5661978292a55cec7fd459571e4 and MIT license:
Provides: bundled(jsmn) = cdcfaafa49ffe5661978292a55cec7fd459571e4

BuildRequires: gcc
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: gnupg2

%description
A wayland based logout menu.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/zsh/
%{_datadir}/fish/
%{_datadir}/bash-completion/
%dir %{_sysconfdir}/%{name}

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.5.*

%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Tue Apr 21 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-5
- fix issues from RHBZ#1821120

* Mon Apr 20 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-4
- fix issues from RHBZ#1821120

* Sun Apr 19 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-3
- fix issues from RHBZ#1821120

* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-2
- fix issues from fedora-review

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-1
- version 1.1.1
