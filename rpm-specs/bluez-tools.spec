# No proper release-tags, yet.  :(
%global commit 7cb788c9c43facfd2d14ff50e16d6a19f033a6a7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170912
%global git_ver -git%{gitdate}.%{shortcommit}
%global git_rel .git%{gitdate}.%{shortcommit}


Name:		bluez-tools
Version:	0.2.0
Release:	0.13%{?git_rel}%{?dist}
Summary:	A set of tools to manage Bluetooth devices for Linux

License:	GPLv2+
URL:		https://github.com/khvzak/%{name}
Source0:	%{url}/archive/%{commit}/%{name}-%{version}%{?git_ver}.tar.gz
Patch0:		%{url}/pull/34.patch#/fix_gcc-10_compile.patch

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	readline-devel

Requires:	bluez%{?_isa}

%description
This was a GSoC'10 project to implement a new command line tools for
bluez (Bluetooth stack for Linux).  It is currently an active open
source project.

The project is implemented in C and uses the D-Bus interface of bluez.

The project is still a work in progress, and not all APIs from Bluez
have been implemented as a part of bluez-tools.  The APIs which have
been implemented in bluez-tools are adapter, agent, device, network
and obex.  Other APIs, such as interfaces for medical devices,
pedometers and other specific APIs have not been ported to bluez-tools.


%prep
%autosetup -n %{name}-%{commit} -p 1
%{_bindir}/autoreconf -fiv


%build
%configure
%make_build


%install
%make_install


%files
%license AUTHORS COPYING
%doc ChangeLog README
%{_bindir}/bt-*
%{_mandir}/man1/bt-*


%changelog
* Fri Jan 31 2020 Leigh Scott <leigh123linux@googlemail.com> - 0.2.0-0.13.git20170912.7cb788c
- Fix gcc-10 compile

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.12.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.11.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-0.10.git20170912.7cb788c
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.9.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.8.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.7.git20170912.7cb788c
- New snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.6.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.5.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.4.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.3.git20161212.97efd29
- Append %%{?git_rel} to Release-tag

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.2
- Initial import (rhbz#1424772)

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.1
- Initial rpm-release (rhbz#1424772)
