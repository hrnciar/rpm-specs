Name:		rgbds
Version:	0.4.1
Release:	2%{?dist}
Summary:	A development package for the Game Boy, including an assembler

# See LICENSE for details
License:	DWPL and ISC and MIT and BSD
URL:		https://github.com/rednex/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	pkgconfig(libpng)

%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker package
for the Game Boy and Game Boy Color.

It consists of:

* rgbasm (assembler)
* rgblink (linker)
* rgbfix (checksum/header fixer)
* rgbgfx (PNG‐to‐2bpp graphics converter)

%prep
%autosetup

%build
%make_build Q="" CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} STRIP="-p" MANMODE="644 -p" Q=""

%files
%{_bindir}/rgbasm
%{_bindir}/rgblink
%{_bindir}/rgbfix
%{_bindir}/rgbgfx
%{_mandir}/man1/rgbasm.1.*
%{_mandir}/man1/rgblink.1.*
%{_mandir}/man1/rgbfix.1.*
%{_mandir}/man1/rgbgfx.1.*
%{_mandir}/man5/rgbds.5.*
%{_mandir}/man5/rgbasm.5.*
%{_mandir}/man5/rgblink.5.*
%{_mandir}/man7/rgbds.7.*
%{_mandir}/man7/gbz80.7.*
%license LICENSE
%doc README.rst

%changelog
* Sun Aug 02 2020 Benjamin Lowry <ben@ben.gmbh> - 0.4.1-2
- Change source url
- Change BuildRequires
- Use make_install macro
- Preserve timestamps when running install

* Sat Aug 01 2020 Benjamin Lowry <ben@ben.gmbh> - 0.4.1-1
- Update to latest version
- Fix FTBFS

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Sanqui <gsanky@gmail.com> - 0.3.2-1
- Update to 0.3.2
- Add flex as a dependency
- Temporarily add a `make clean` step
- Fix `make` parameters to work with Makefile changes
- README -> README.md
- Add new manpages

* Sun Mar 26 2017 Sanqui <gsanky@gmail.com> - 0.2.5-2
- Add newlines between changelog entries in the specfile

* Sat Mar 25 2017 Sanqui <gsanky@gmail.com> - 0.2.5-1
- Patch the Makefie to prevent stripping symbols
- Enable debuginfo build

* Fri Mar  3 2017 Sanqui <gsanky@gmail.com> - 0.2.4-2
- Correct license (added BSD)
- Remove commented out Requires:
- Change Q= to Q=""
- Honor optflags

* Wed Mar  1 2017 Sanqui <gsanky@gmail.com> - 0.2.4-1
- Initial package
