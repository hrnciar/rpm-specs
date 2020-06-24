Name:    termy-server
Summary: TermySequence terminal multiplexer server
Version: 1.1.4
Release: 5%{?dist}

License: GPLv2
URL:     https://termysequence.io
Source:  https://termysequence.io/releases/termysequence-server-%{version}.tar.xz

Patch1: setup-fix-session-check.patch

BuildRequires: cmake >= 3.9.0
BuildRequires: gcc-c++
BuildRequires: libcmocka-devel
BuildRequires: libgit2-devel >= 0.26
BuildRequires: libuuid-devel
BuildRequires: systemd-devel >= 235
BuildRequires: utf8cpp-devel >= 2.3.4

%{?systemd_requires}
Recommends: libgit2
Obsoletes: termy-shell-integration-bash

%description
A multiplexing terminal emulator server implementing
the TermySequence protocol.

%prep
%autosetup -p1 -n termysequence-%{version}
# Avoid the bundled copy of UTF8-CPP
rm -rf vendor/utf8cpp

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=ON .
%make_build

%install
%make_install

%check
ctest -V

%post
%systemd_user_post termy-server.socket

%preun
%systemd_user_preun termy-server.service termy-server.socket

%files
%license COPYING.txt
%{_bindir}/termy*
%{_datadir}/termy-server
%{_userunitdir}/termy-server.*
%{_mandir}/man1/termy*.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Eamon Walsh <ewalsh@termysequence.com> - 1.1.4-2
- setup: Move up the systemd session check and make it mandatory

* Mon Oct 08 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.1.4-1
- Update to 1.1.4
- Drop termy-shell-integration-bash subpackage

* Sat Sep 01 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.1.0-2
- Set CMAKE_BUILD_TYPE back to Release (#1582983)

* Thu Aug 09 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.1.0-1
- Update to 1.1.0

* Tue Jun 05 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.0.3-1
- Update to 1.0.3
- Set CMAKE_BUILD_TYPE to None

* Sat Jun 02 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.0.2-2
- Set CMAKE_BUILD_TYPE to Release

* Mon May 28 2018 Eamon Walsh <ewalsh@termysequence.com> - 1.0.2-1
- Initial package for Fedora
