%global forgeurl    https://github.com/mariusor/mpris-scrobbler

Name:           mpris-scrobbler
Version:        0.4.0
Release:        1%{?dist}
Summary:        User daemon to submit currently playing song to LastFM, LibreFM, ListenBrainz

%forgemeta

# https://bugzilla.redhat.com/show_bug.cgi?id=1846774
ExcludeArch:    s390x

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  /usr/bin/m4

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif

%if 0%{?fedora}
BuildRequires:  /usr/bin/scdoc
%endif

Requires:       /usr/bin/xdg-open


%description
mpris-scrobbler is a minimalist user daemon that submits the currently playing
song to LastFM, LibreFM, ListenBrainz, and compatible services. To retrieve
song information, it uses the MPRIS DBus interface, so it works with any media
player that exposes this interface.


%prep
%forgesetup
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-signon
%{_userunitdir}/%{name}.service

%if 0%{?fedora}
%{_mandir}/man1/mpris-scrobbler{,-signon}.1*
%{_mandir}/man5/mpris-scrobbler-{config,credentials}.5*
%endif


%changelog
* Mon Jun 01 2020 Justin W. Flory <jflory7@fedoraproject.org> - 0.4.0-1
- Update to latest upstream stable release
- Temporary ExcludeArch for s390x architecture build failures

* Wed May 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.93-1
- Update to latest pre-release tag
- Fixing bug when the scrobbler would hang randomly
- Added hard dependency on DBus version 1.9 or higher
- Improved logic of now_playing/queue events in case tracks cannot fully load

* Tue May 26 2020 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.92-1
- Push update for official repositories

* Mon May 25 2020 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.92-1.copr
- Update to latest pre-release tag

* Sat May 16 2020 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.91-1.copr
- Update to latest pre-release tag

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.3.5-4
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.5-2
- Remove Fedora CI gating (broken for reasons I do not have time to debug)

* Sun Sep 08 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.5-1
- Update package to latest upstream release

* Tue Aug 20 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.4-1
- Update package to latest upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.3.2-2
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.2-1
- Update package to latest upstream release

* Sat Feb 16 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-2
- Add systemd scriptlets

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-1
- First release: mpris-scrobbler
- With guidance and help from  Igor Gnatenko

