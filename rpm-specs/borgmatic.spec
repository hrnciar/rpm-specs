Name:           borgmatic
Version:        1.5.10
Release:        1%{?dist}
Summary:        Simple Python wrapper script for borgbackup

License:        GPLv3
URL:            https://torsion.org/borgmatic
Source0:        https://projects.torsion.org/witten/borgmatic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?fedora} < 30 || 0%{?rhel} < 8
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%endif

Requires:       borgbackup
Requires:       python%{python3_pkgversion}-colorama
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-ruamel-yaml
Requires:       python%{python3_pkgversion}-pykwalify


%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for
the Borg backup software that initiates a backup, prunes any old backups
according to a retention policy, and validates backups for consistency.


%prep
%autosetup -n %{name}


%build
%py3_build


%install
%py3_install

install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic
install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic.d

sed -i 's#^ExecStart=.*#ExecStart=%{_bindir}/%{name}#' sample/systemd/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.timer %{buildroot}%{_unitdir}/%{name}.timer


%files
%doc AUTHORS NEWS README.md
%license LICENSE
%attr(0750, root, root) %{_sysconfdir}/borgmatic
%attr(0750, root, root) %{_sysconfdir}/borgmatic.d
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_bindir}/borgmatic
%{_bindir}/generate-borgmatic-config
%{_bindir}/upgrade-borgmatic-config
%{_bindir}/validate-borgmatic-config
%{_unitdir}/borgmatic.service
%{_unitdir}/borgmatic.timer


%post
%systemd_post borgmatic.timer


%preun
%systemd_preun borgmatic.timer


%postun
%systemd_postun borgmatic.timer


%changelog
* Fri Sep 04 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.10-1
- update to 1.5.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.9-1
- update to 1.5.9

* Sun Jul 12 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.8-1
- update to 1.5.8

* Wed Jun 24 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.7-1
- update to 1.5.7
- add python3-setuptools BuildRequires

* Sun Jun 07 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.6-1
- update to 1.5.6

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.5-2
- Rebuilt for Python 3.9

* Wed May 27 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.5-1
- update to 1.5.5

* Sat May 16 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.4-1
- update to 1.5.4

* Thu May 14 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.3-1
- update to 1.5.3

* Sat Apr 25 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.2-1
- update to 1.5.2

* Mon Feb 03 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.1-1
- update to 1.5.1

* Tue Jan 28 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.4.22-1
- update to 1.4.22

* Sat Dec 21 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.21-1
- update to 1.4.21

* Fri Dec 13 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.20-1
- update to 1.4.20
- added missing Requires for python-requests

* Mon Dec 09 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.18-1
- update to 1.4.18

* Sat Dec 07 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.17-1
- update to 1.4.17

* Tue Dec 03 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.16-1
- update to 1.4.16

* Tue Nov 26 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.15-1
- update to 1.4.15

* Tue Nov 26 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.14-1
- update to 1.4.14

* Wed Nov 20 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.13-1
- update to 1.4.13

* Mon Nov 18 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.12-1
- update to 1.4.12

* Mon Nov 18 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.11-1
- update to 1.4.11

* Wed Nov 13 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.10-1
- update to 1.4.10

* Tue Nov 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.9-1
- update to 1.4.9

* Tue Nov 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.8-1
- update to 1.4.8

* Mon Nov 04 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.6-1
- update to 1.4.6

* Wed Oct 23 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Oct 21 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.26-1
- update to 1.3.26

* Sat Oct 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.23-2
- insert conditionals for F29 and EL7
- bring back python3_version variable for EL7 compatibility

* Fri Oct 11 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.23-1
- update to 1.3.23
- fix dependencies
- build for noarch
- use release tarball directly from upstream
- include docs and license from release tarball
- use included unit and timer files
- remove tests, they require internet access
- cleanups and modernizations

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.2.0-1
- upstream release 1.2.0
- added missing deps ruamel.yaml and pykwalify

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.15-3
- Rebuilt for Python 3.7

* Thu Apr 12 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.15-2
- add empty /etc/borgmatic.d as described in documentation
- add empty /etc/borgmatic as described in documentation

* Thu Apr 12 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.15-1
- Initial packaging for the borgmatic project

