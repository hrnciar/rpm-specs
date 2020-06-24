Name: ttyd
Summary: Share your terminal over the web
Version: 1.6.0
Release: 1%{?dist}
License: MIT
URL: https://tsl0922.github.io/ttyd/
Source0: https://github.com/tsl0922/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: ttyd-ignore-libwebsockets-extensions.patch

BuildRequires: json-c-devel
BuildRequires: vim-common
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: libwebsockets-devel
Buildrequires: gcc-c++
Buildrequires: zlib-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web,
inspired by GoTTY.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*

%changelog
* Fri May 08 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.0-1
- new version 1.6.0
- use autosetup macro

* Tue Dec 03 2019 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.2-1
- new version 1.5.2

* Sun Mar 10 2019 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.2-1
- new version 1.4.2

* Thu Sep 28 2017 Huaren Zhong <huaren.zhong@gmail.com> 1.3.3
- Rebuild for Fedora
