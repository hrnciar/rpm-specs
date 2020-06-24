%global commit      708424d7b48f4772690b0e24574b9ab7b43b2f52
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191129

%global corename    gambatte

Name:           libretro-%{corename}
Version:        0
Release:        0.2.%{date}git%{shortcommit}%{?dist}
Summary:        Libretro implementation of libgambatte

License:        GPLv2
URL:            https://github.com/libretro/gambatte-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
Suggests:       gnome-games%{?_isa}
Suggests:       retroarch%{?_isa}

%description
Gambatte is an accuracy-focused, open-source, cross-platform Game Boy Color
emulator written in C++. It is based on hundreds of corner case hardware tests,
as well as previous documentation and reverse engineering efforts.

The core emulation code is contained in a separate library back-end
(libgambatte) written in platform-independent C++. There is currently a GUI
front-end (gambatte_qt) using Trolltech's Qt4 toolkit, and a simple command-line
SDL front-end (gambatte_sdl).

The GUI front-end contains platform-specific extensions for video, sound and
timers. It should work on MS Windows, Linux/BSD/UNIX-like OSes, and Mac OS X.

The SDL front-end should be usable on all platforms with a working SDL port. It
should also be quite trivial to create new (simple) front-ends (note that the
library API should in no way be considered stable).


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1
iconv -f iso8859-1 -t utf-8 README.md > README.md.conv && mv -f README.md.conv README.md


%build
%set_build_flags
%make_build


%install
%make_install core_installdir=%{_libdir}/libretro
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license COPYING
%doc README.md
%{_libdir}/libretro/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191129git708424d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191129git708424d
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Mon Oct 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190823git4d9ad7b
- Initial package
