Name:          growlight
Version:       1.2.16
Release:       1%{?dist}
Summary:       Disk manipulation and system setup tool
License:       GPLv3+
URL:           https://nick-black.com/dankwiki/index.php/Growlight
Source0:       https://github.com/dankamongmen/%{name}/archive/v%{version}.tar.gz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:       https://nick-black.com/dankamongmen.gpg

BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: readline-devel
BuildRequires: libpciaccess-devel
BuildRequires: cmake
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libatasmart)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(notcurses)
BuildRequires: device-mapper-devel
BuildRequires: cryptsetup-devel
BuildRequires: pandoc

%description
Growlight can manipulate both physical (NVMe, SATA, etc.) and virtual (mdadm,
device-mapper, etc.) block devices, help identify bottlenecks in a storage
topology, create and destroy filesystems, and prepare a machine for initial
boot when run in an installer context. Both full-screen and REPL readline UIs
are available.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -DUSE_LIBZFS=off .
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_bindir}/growlight
%{_bindir}/growlight-readline
%{_mandir}/man8/*.8*

%changelog
* Mon Oct 19 2020 Nick Black <dankamongmen@gmail.com> - 1.2.16-1
- New upstream release

* Thu Oct 15 2020 Nick Black <dankamongmen@gmail.com> - 1.2.15-1
- New upstream release

* Sat Oct 10 2020 Nick Black <dankamongmen@gmail.com> - 1.2.14-1
- New upstream release

* Tue Sep 29 2020 Nick Black <dankamongmen@gmail.com> - 1.2.13-1
- New upstream release, dep on notcurses 1.7.5+

* Sun Sep 20 2020 Nick Black <dankamongmen@gmail.com> - 1.2.12-1
- New upstream release, dep on notcurses 1.7.3+

* Wed Sep 02 2020 Nick Black <dankamongmen@gmail.com> - 1.2.11-1
- New upstream release

* Sun Aug 30 2020 Nick Black <dankamongmen@gmail.com> - 1.2.9-1
- New upstream release

* Tue Aug 11 2020 Nick Black <dankamongmen@gmail.com> - 1.2.8-4
- Use modern cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Nick Black <dankamongmen@gmail.com> - 1.2.8-1
- New upstream version

* Wed Jul 15 2020 Nick Black <dankamongmen@gmail.com> - 1.2.7-1
- New upstream version

* Sun Jun 21 2020 Nick Black <dankamongmen@gmail.com> - 1.2.6-1
- Initial packaging for Fedora 33
