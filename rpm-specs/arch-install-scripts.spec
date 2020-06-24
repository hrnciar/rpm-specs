Name:           arch-install-scripts
Version:        23
Release:        1%{?dist}
Summary:        Scripts to bootstrap Arch Linux distribution
License:        GPLv2
URL:            https://projects.archlinux.org/arch-install-scripts.git
Source0:        https://projects.archlinux.org/arch-install-scripts.git/snapshot/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  m4
BuildRequires:  asciidoc
Requires:       archlinux-keyring
Requires:       pacman

%description
A small suite of scripts aimed at automating some menial tasks when
installing Arch Linux, most notably including actually performing the
installation.

To install and launch Arch in a container:
  pacman-key --init
  pacman-key --populate archlinux
  mkdir -p /var/lib/machines/arch
  pacstrap -G -M -i -c /var/lib/machines/arch base
  systemd-nspawn -bD /var/lib/machines/arch

%prep
%setup -q

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%{_bindir}/arch-chroot
%{_bindir}/genfstab
%{_bindir}/pacstrap
%{_datadir}/bash-completion/completions/arch-chroot
%{_datadir}/bash-completion/completions/genfstab
%{_datadir}/bash-completion/completions/pacstrap
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_archinstallscripts
%{_mandir}/man8/arch-chroot.8*
%{_mandir}/man8/genfstab.8*
%{_mandir}/man8/pacstrap.8*

%changelog
* Tue Mar 31 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 23-1
- Update to latest version (#1717676)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 21-1
- Update to latest version (#1622287)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 18-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Christopher Meng <rpm@cicku.me> - 15-1
- Update to v15

* Tue Jan 06 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 14-1
- Update to v14. (#1175134).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 13-2
- Update installation instructions.

* Thu Feb 06 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 13-1
- Update to v13. (#1062168).

* Thu Aug 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 11-2
- Remove "+" from license.
- Replace path with macro.
- Package accepted (#998125).

* Fri Aug 16 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 11-1
- Initial packaging.
