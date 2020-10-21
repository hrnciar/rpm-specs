Name:		slurp
Version:	1.3.0
Release:	2%{?dist}
Summary:	Select a region in Sway

License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/releases/download/v%{version}/slurp-%{version}.tar.gz
Source1:	%{url}/releases/download/v%{version}/slurp-%{version}.tar.gz.sig
Source2:	https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19

BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	scdoc
BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gnupg2

%description
Slurp is a command-line tool that allows the user to visually select a region
and prints it to the standard output.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/slurp
%{_mandir}/man1/slurp.1*

%changelog
* Fri Oct 16 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-2
- fix silly dependency error

* Fri Oct 16 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-1
- Slurp 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 8 2020 Benjamin Lowry <ben@ben.gmbh> 1.2.0-3
- Update description

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Benjamin Lowry <ben@ben.gmbh> 1.2.0-1
- Initial Fedora package
