# https://github.com/JasonLG1979/gnome-shell-extensions-mediaplayer/commit/65867e7447dd3f4e3f118c0c76922f7d729f87dd
%global commit  65867e7447dd3f4e3f118c0c76922f7d729f87dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20190419

# Minimum GNOME Shell version supported
%global min_gs_version 3.20

%global uuid mediaplayer@patapon.info
%global _gsextdir %{_datadir}/gnome-shell/extensions

Name:           gnome-shell-extension-media-player-indicator
Version:        0
Release:        0.26.%{gitdate}git%{shortcommit}%{?dist}
Summary:        Control MPRIS2 capable media players: Rhythmbox, Banshee, Clementine and more

License:        GPLv2+
URL:            https://extensions.gnome.org/extension/55/media-player-indicator/
Source0:        https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer/archive/%{commit}/mediaplayer-indicator-%{shortcommit}.tar.gz

BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  meson
Requires:       gnome-shell-extension-common >= %{min_gs_version}
BuildArch:      noarch

%description
This GNOME Shell extension controls any MPRIS v2.1 capable media player.

This extension will monitor D-Bus for active players and automatically display
them in the GNOME Shell's volume menu by default.

%prep
%setup -q -c -n mediaplayer-indicator-%{shortcommit}

%build
pushd gnome*
%meson
%meson_build
popd


%install
pushd gnome*
%meson_install
install -d %{buildroot}/%{_gsextdir}/%{uuid}
popd

%find_lang gnome-shell-extensions-mediaplayer

%files -f gnome-shell-extensions-mediaplayer.lang
%doc gnome*/README.md
%license gnome*/LICENSE
%dir %{_gsextdir}/%{uuid}
%{_gsextdir}/*/metadata.json
%{_gsextdir}/*/stylesheet.css
%{_gsextdir}/mediaplayer@patapon.info/mpi-symbolic.svg
%{_gsextdir}/mediaplayer@patapon.info/schemas/org.gnome.shell.extensions.mediaplayer.gschema.xml
%{_gsextdir}/*/*.js

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20190419git65867e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20190419git65867e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 0-0.24.20190419git65867e7
- Update to new git snapshot 0-0.24.20190419git65867e7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20181105git813c05a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 0-0.22.20181105git813c05a
- Update to new git snapshot 0-0.22.20181105git813c05a

* Fri Sep 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 0-0.21.20180918gitd3201ea
- Update to new git snapshot 0-0.21.20180918gitd3201ea
- Remove scriptlet glib-compile-schemas: This scriptlet SHOULD NOT be used in Fedora 24 or later.

* Wed Sep 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 0-0.20.20180902git0795671
- Update to new git snapshot 0-0.20.20180902git0795671

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20171119gite5ac200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20171119gite5ac200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.17.20171119gite5ac200
- Update to new git snapshot 0-0.17.20171119gite5ac200

* Wed Aug 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.16.20170809git4e69776
- Update to new git snapshot 0-0.16.20170809git4e69776
- Switched to meson build system
- Add BR meson

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20170725gitba389fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.14.20170629git74bc4bd
- Update to new git snapshot 0-0.14.20170725git74bc4bd

* Thu Jul 13 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.13.20170713gitba389fa
- Update to new git snapshot 0-0.13.20170713gitba389fa

* Thu Jun 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.12.20170629git7bc47fd
- Update to new git snapshot 0-0.12.20170629git7bc47fd

* Sat May 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.11.20170520git065ea3b
- Update to new git snapshot 0-0.11.20170520git065ea3b

* Sat Apr 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.10.20170417git09749bb
- Update to new git snapshot 0-0.10.20170417git09749bb

* Sun Apr 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.9.20170401git2be196b
- Update to new git snapshot 0-0.9.20170401git2be196b

* Tue Mar 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.8.20170314git61d9118
- Update to new git snapshot 0-0.8.20170314git61d9118
- Remove RR glib2

* Sat Mar 11 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.7.20170311git0810df8
- Update to new git snapshot 0-0.7.20170311git0810df8
- Clanup specfile
- Add pushd/popd
- Update license field to GPLv2+

* Thu Mar 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.6.20170308git67e54ae
- Use Version 0 until upstream formally designates an actual version

* Wed Mar 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.5.20170308git67e54ae
- Update to new git snapshot 0-0.5.20170308git67e54ae
- Add INSTALL="install -p"

* Fri Feb 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 0-0.4.20170201gite7ed852
- Update to new git snapshot 0-0.4.20170201gite7ed852

* Tue Nov 15 2016 Martin Gansser <martinkg@fedoraproject.org> - 0-0.3.20161103gitb20fa7f
- Update to new git snapshot 0-0.3.20161103gitb20fa7f
- Used wildcard instead of manually enumerate files in section files

* Wed Nov 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 0-0.2.20161103gitb20fa7f
- Update to new git snapshot 0-0.2.20161103gitb20fa7f

* Wed Oct 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0-0.1.20161010gite2cc6d4
- initial build for Fedora
