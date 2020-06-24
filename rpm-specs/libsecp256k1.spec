%global _hardened_build 1

Name:    libsecp256k1
Version: 0.20.9
Release: 2%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

License: MIT
URL:     https://github.com/Bitcoin-ABC/secp256k1
Source0: https://github.com/Bitcoin-ABC/secp256k1/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake autoconf libtool

%description
%{summary}.

Includes support for Schnorr signature.

Uses the implementation maintained by Bitcoin-ABC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n secp256k1-%{version}


%build
./autogen.sh
%configure --disable-static

%make_build

%install
%make_install

%check
./tests


%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.0*

%files devel
%license COPYING
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Jonny Heggheim <hegjon@gmail.com> - 0.20.9-1
- Using the implementation by Bitcoin-ABC, includes support for Schnorr

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190222git949e85b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190221git949e85b
- Updated to 20190221git949e85b
- Added configure flags for schnorrsig

* Thu May 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190210gita34bcaa
- Updated to 20190210gita34bcaa
- Included support for Schnorr module

* Fri Jan 11 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20181126gite34ceb3
- Inital packaging
