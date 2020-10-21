Name:           bpytop
Version:        1.0.44
Release:        1%{?dist}
Summary:        Linux/OSX/FreeBSD resource monitor 
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/aristocratos/bpytop
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       python3 >= 3.6
Requires:       python3-psutil

%description
Resource monitor that shows usage and stats for processor, memory, disks,
network and processes.

Python port of bashtop.

Features:

- Easy to use, with a game inspired menu system.
- Full mouse support, all buttons with a highlighted key is clickable and mouse
  scroll works in process list and menu boxes.
- Fast and responsive UI with UP, DOWN keys process selection.
- Function for showing detailed stats for selected process.
- Ability to filter processes, multiple filters can be entered.
- Easy switching between sorting options.
- Send SIGTERM, SIGKILL, SIGINT to selected process.
- UI menu for changing all config file options.
- Auto scaling graph for network usage.
- Shows message in menu if new version is available
- Shows current read and write speeds for disks


%prep
%autosetup -p1

# FIXME: this doesn't work
# * https://github.com/aristocratos/bpytop/issues/83#issuecomment-678773990
# - Disable new version check
sed -i 's|update_check: bool = True|update_check: bool = False|' bpytop.py


%build
%make_build


%install
%make_install PREFIX=%{_prefix}
rm %{buildroot}%{_datadir}/%{name}/doc/README.md


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/


%changelog
* Mon Oct 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.44-1
- build(update): 1.0.44

* Sun Oct 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.43-1
- build(update): 1.0.43

* Thu Oct  8 20:59:15 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.42-1
- build(update): 1.0.42

* Tue Sep 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.40-1
- Update to 1.0.40

* Thu Sep 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.37-1
- Update to 1.0.37

* Tue Sep 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.36-1
- Update to 1.0.36

* Sun Sep 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.35-1
- Update to 1.0.35

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.33-1
- Update to 1.0.33

* Sun Sep 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.31-1
- Update to 1.0.31

* Sat Sep 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.27-1
- Update to 1.0.27

* Wed Sep  9 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.26-1
- Update to 1.0.26

* Mon Sep  7 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.25-1
- Update to 1.0.25

* Sun Sep  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.24-1
- Update to 1.0.24

* Wed Sep  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.22-1
- Update to 1.0.22

* Tue Aug 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.21-1
- Update to 1.0.21

* Sun Aug 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.20-1
- Update to 1.0.20

* Sun Aug 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.17-1
- Update to 1.0.17

* Sun Aug 16 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.16-1
- Update to 1.0.16

* Sat Aug 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.15-1
- Update to 1.0.15

* Fri Aug 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.14-1
- Update to 1.0.14

* Thu Aug 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.13-2
- Disable new version check

* Wed Aug 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Tue Aug 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.10-1
- Update to 1.0.10

* Mon Aug 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Wed Aug 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-2
- Initial package
