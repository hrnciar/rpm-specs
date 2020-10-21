Name: ttyd
Summary: Share your terminal over the web
Version: 1.6.1
Release: 1%{?dist}
License: MIT
URL: https://tsl0922.github.io/ttyd/
Source0: https://github.com/tsl0922/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: json-c-devel
BuildRequires: vim-common
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: libwebsockets-devel
Buildrequires: gcc-c++
Buildrequires: zlib-devel
Patch0:       ws_ping_pong_interval.patch

%description
ttyd is a simple command-line tool for sharing terminal over the web,
inspired by GoTTY.

%prep
%autosetup -p2

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*

%changelog
* Sat Sep 12 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.1-1
- new version 1.6.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.0-1
- new version 1.6.0
- use autosetup macro

* Tue Dec 03 2019 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.2-1
- new version 1.5.2

* Sun Mar 10 2019 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.2-1
- new version 1.4.2

* Thu Sep 28 2017 Huaren Zhong <huaren.zhong@gmail.com> 1.3.3
- Rebuild for Fedora
